import dbi
from prof_func import profile_func

BASE_URL = u'http://disq.us/'
ALPHABET = u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


def get_last_shortened(n=100):
    return [x[0] for x in dbi.get_last(n)]


def visited_count(short_url):
    """
    Return the number of times a shortened url has been visited.
    """
    row_id = convert_url_to_id(short_url)
    return dbi.visit_count(row_id)


def get_popular_domains(days=30, count=10):
    """
    Returns the top domains that were shortened in the past x days.
    """
    return dbi.get_popular_domains(days, count)


@profile_func()
def convert_id_to_code(row_id):
    """
    Takes row_id as a base 10 int and converts it to a base 62 int.
    Builds the short_url_code using the base 62 int using the ALPHABETs.
    """
    digits = []
    base = len(ALPHABET)
    while row_id > 0:
        digits.append(row_id % base)
        row_id = row_id / base
    digits.reverse()
    short_code = ''.join([ALPHABET[i] for i in digits])
    return short_code


def convert_url_to_id(short_id):
    """
    Convert the short_url to the row_id.
    """
    short_code = [ALPHABET.index(c) for c in short_id]
    row_id = 0
    base = len(ALPHABET)
    for idx, digit in enumerate(reversed(short_code)):
        row_id += digit * (base ** idx)
    return row_id


def visit(short_url):
    """
    Increment the click count.
    Return the long_url for the given short_url.
    """
    short_id = short_url.split('/')[-1]
    row_id = convert_url_to_id(short_id)
    dbi.increment_click(row_id)
    return dbi.get_url(row_id)


def shorten(long_url):
    """
    Take a regular long_url and returns the shortened url.
    """
    row_id = dbi.get_or_create(unicode(long_url))
    short_code = convert_id_to_code(row_id)
    return BASE_URL + short_code


if __name__ == '__main__':
    dbi.init_db()
    with open('test_urls.txt') as f:
        for url in f:
            short_url = shorten(url.strip())
            long_url = visit(short_url)
            print 'short_url:', short_url
            print 'long_url:', long_url
    print 'Last 10 shortened urls:', get_last_shortened(10)
    short_url = u'http://disq.us/B'
    #print 'Visit count for %s:%d' % (short_url, visited_count(short_url))
    print 'Popular shortened domains:', get_popular_domains()
