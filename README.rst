trollius_requests: yieldfrom.Requests (Requests for asyncio) for trollius
========================================

Requests is an Apache2 Licensed HTTP library, written in Python, for human
beings.

https://github.com/rdbhost/yieldfromRequests
yieldfrom.Requests is the same library, ported to run under Python's asyncio.

https://github.com/andrewleech/yieldfromRequests_trollius
yieldfrom.Requests (trollius) is yieldfrom.Requests with syntax converted to suit trollius under 2.7 etc.

Where in regular Requests you would write:

.. code-block:: pycon

    >>> r = requests.get('https://api.github.com', auth=('user', 'pass'))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> r.text
    ...
    >>> return r.status_code

in yieldfrom.Requests you write:

.. code-block:: pycon

    >>> r = yield From (requests.get('https://api.github.com', auth=('user', 'pass')))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> yield From (r.text)
    ...
    >>> raise Return (r.status_code)

The *get* method and the *text* property involve I/O latency, hence are called as coroutines.
The headers and status_code attributes are still plain attributes.


The feature set is the same as the original, though a few methods work slightly differently.

The .stream() method does not stream, but preloads all data, and simulates a stream, so existing
dependencies can work with minimal conversion.

