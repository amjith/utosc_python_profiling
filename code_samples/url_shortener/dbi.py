from collections import defaultdict
import datetime

import tldextract
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Unicode, DateTime, Integer

DATABASE_URL = 'sqlite:///url_shortener.db3'

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
Session = scoped_session(sessionmaker(bind=engine))


class Url(Base):
    """
    urls table in the database.
    Columns:
        long_url
        created_at
        clicks
    """
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    long_url = Column(Unicode)
    created_at = Column(DateTime)
    clicks = Column(Integer)

    def __init__(self, long_url, created_at=datetime.datetime.now(), clicks=0):
        self.long_url = unicode(long_url)
        self.created_at = created_at
        self.clicks = clicks

    def __repr__(self):
        return "<Url('%u', '%s', '%s')>" % (self.long_url,
                                                  self.created_at,
                                                  self.clicks)


def init_db():
    """
    Initializes the database.
    """
    Base.metadata.create_all(engine)


def get_or_create(url):
    """
    Search for the url and return the row_id
    If url doens't exist create a row and return the row_id.
    """
    session = Session()
    url_record = session.query(Url).filter_by(long_url=url).first()
    if not url_record:
        url_record = Url(url)
        session.add(url_record)
        session.commit()
    return url_record.id


def visit_count(row_id):
    """
    Retunrs the clicks column for the row_id.
    If row_id doesn't exist, return 0.
    """
    session = Session()
    url_record = session.query(Url).filter_by(id=row_id).first()
    if url_record:
        return url_record.clicks
    else:
        return 0


def get_url(row_id):
    """
    Given a row_id, returns the long_url stored in the record.
    If row_id is not found return None.
    """
    session = Session()
    url_record = session.query(Url).filter_by(id=row_id).first()
    if not url_record:
        return None
    return url_record.long_url


def increment_click(row_id):
    """
    Increment the click counter at the row_id.
    """
    session = Session()
    url_record = session.query(Url).filter_by(id=row_id).first()
    if url_record:
        url_record.clicks += 1
        session.merge(url_record)
        session.commit()
        return True
    else:
        return False


def get_last(n):
    session = Session()
    last_n = session.query(Url.long_url).order_by(Url.created_at).limit(n).all()
    return last_n


def get_popular_domains(days, count):
    """
    Gets the records for the past x days.
    Counts the domains for each record.
    Returns the top 'n' domains.
    """
    session = Session()
    domain_count = defaultdict(int)
    date_limit = datetime.datetime.now() - datetime.timedelta(days=days)
    urls = (session.query(Url.long_url)
                    .filter(Url.created_at >= date_limit)).all()
    for url in urls:
        domain_name = tldextract.extract(url[0])[1]
        domain_count[domain_name] += 1
    return sorted(domain_count, key=domain_count.get, reverse=True)[:count]
