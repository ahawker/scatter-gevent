"""

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('GeventPool', 'GeventPoolService')


from gevent import pool, Timeout
from scatter.exceptions import ScatterExit, ScatterTimeout
from scatter.ext.async.pool import Pool, GreenletPoolService
from scatter_gevent.worker import GeventWorkerService


class GeventPool(Pool):
    """

    """

    pool_cls = pool.Pool

    # def __init__(self, pool_cls=pool.Pool, *args, **kwargs):
    #     super(GeventPool, self).__init__(pool_cls, *args, **kwargs)

    @property
    def size(self):
        """
        """
        print 'gevent pool size'
        return self._pool.size

    def spawn(self, func, *args, **kwargs):
        """
        """
        print 'gevent pool spawn'
        return self._pool.spawn(func, *args, **kwargs)

    def spawn_later(self, seconds, func, *args, **kwargs):
        """
        """
        worker = self._pool.greenlet_class(func, *args, **kwargs)
        self._pool.add(worker)
        worker.start_later(seconds)
        return worker

    def flush(self, timeout=None):
        """
        """
        try:
            self._pool.kill(ScatterExit, block=True, timeout=timeout)
        except Timeout:
            raise ScatterTimeout('[{0}] Failed to flush all workers after {1} seconds.'.format(self.name, timeout))

    def resize(self, size):
        self._pool._semaphore.counter = size
        self._pool.size = size


class GeventPoolService(GreenletPoolService):
    """

    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.pool_class = GeventPool
        self.pool_runner_class = GeventWorkerService
        self.pool_worker_class = GeventWorkerService
        self.pool_max_size = 100