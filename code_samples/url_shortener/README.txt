Scripts:
    * shorten.py
        - This is the main script that has all the APIs.
    * dbi.py 
        - This is the database interface apis used by shorten.
    * memoized.py 
        - Memoization decorator that adds caching to functions. (ref: http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize)


Requirements:
    * SQLAlchemy==0.7.6
        - ORM for talking to the databse.
    * tldextract==1.1 
        - python library for extracting domain name from urls.


APIs:
    * IMPORTANT: dbi.init_db() must be called to create the databse before calling any APIs.
    * shorten(long_url)
        - Returns the shortened url for the long_url.
    * visit(short_url)
        - Returns the long url corresponding to the short_url.
    * get_last_shortened(n)
        - Return the last 'n' shortened urls.
    * visited_count(short_url)
        - Return the number of times a short_url was visited.
    * get_popular_domains(x_days, n_count)
        - Return the 'n' most popular domains that were shortened in the past
          'x' days.

Features:
    * Supports unicode urls.
    * Accurately determines the domain name. 
    * Functions without side-effects are memoized (caching technique).
        - This saves a trip to the database when same urls are requested for
          shortening. Fast.
    * Keeps track of number of visits to a short url.

Known Issues:
    * No sanity checks for url format.
    * Short_urls are expected in this format 'http://disq.us/XXX' otherwise the
      script will break. Adding sanity checks with regex shouldn't be too
      difficult.
    * http://google.com and http://www.google.com are treated as different urls.
    * dbi.init_db() must be called to create the databse before calling any APIs.
    * The current implementation of Memoization does not limit the size of the
      cache. This can be limited by using a limited size dictionary.
    * Calling the APIs before calling dbi.init_db results in a error. Error
      handling can be added later to catch this.
