"""
    scatter_gevent
    ~~~~~~~~~~~~~~

"""

ENABLED = True

try:
    import gevent
    from gevent import monkey
    monkey.patch_all()
except ImportError:
    ENABLED = False
else:
    import itertools

    from scatter_gevent import core
    from scatter_gevent.core import *
    from scatter_gevent import future
    from scatter_gevent.future import *
    from scatter_gevent import pool
    from scatter_gevent.pool import *
    from scatter_gevent import queue
    from scatter_gevent.queue import *
    from scatter_gevent import service
    from scatter_gevent.service import *
    from scatter_gevent import worker
    from scatter_gevent.worker import *

    __all__ = list(itertools.chain(core.__all__,
                                   future.__all__,
                                   pool.__all__,
                                   queue.__all__,
                                   service.__all__,
                                   worker.__all__))
