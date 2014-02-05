"""
    scatter.async.gevent
    ~~~~~~~~~~~~~~~~~~~~

    ....
"""
from __future__ import absolute_import

__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('GeventService', 'GeventWorker', 'Event',
           'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Queue', 'Signal')


from gevent import monkey; monkey.patch_all()
from gevent import queue, lock, event, pool, spawn, spawn_later, sleep, reinit, signal, getcurrent, Timeout
from scatter.async import Worker, WorkerPool
from scatter.async.greenlet import GreenletService
from scatter.exceptions import ScatterTimeout, ScatterExit


Event = event.Event
#Condition = event.Event
Lock = lock.RLock
RLock = lock.RLock
Semaphore = lock.Semaphore
BoundedSemaphore = lock.BoundedSemaphore
Queue = queue.Queue
Signal = signal


class GeventWorker(Worker):
    """

    """

    def done(self):
        """

        """
        return self._worker.ready()

    def running(self):
        """
        """
        return not self.done()

    def stop(self, timeout=None):
        """
        """
        self._worker.kill(ScatterExit, timeout=timeout)
        return self.done()

    def join(self, timeout=None):
        """
        """
        return self._worker.join(timeout)

    def cancel(self, timeout=None):
        """
        """
        if self.done() or self.running():
            return False
        return self.stop(timeout)

    def get_result(self, timeout=None):
        """
        """
        try:
            return self._worker.get(timeout=timeout)
        except Timeout:
            raise ScatterTimeout('[{0}] Failed to get result after {1} seconds.'.format(self.name, timeout))

    def add_callback(self, func):
        """
        """
        self._worker.link(self.callback(func))

    def remove_callback(self, func):
        """
        """
        self._worker.unlink(self.callback(func))


class GeventWorkerPool(WorkerPool):
    """

    """

    @property
    def size(self):
        """
        """
        return self.pool.size

    def spawn(self, func, *args, **kwargs):
        """
        """
        return self.pool.spawn(func, *args, **kwargs)

    def spawn_later(self, seconds, func, *args, **kwargs):
        """
        """
        worker = self.pool.greenlet_class(func, *args, **kwargs)
        self.pool.add(worker)
        worker.start_later(seconds)
        return worker

    def flush(self, timeout=None):
        """
        """
        try:
            self.pool.kill(ScatterExit, block=True, timeout=timeout)
        except Timeout:
            raise ScatterTimeout('[{0}] Failed to flush all workers after {1} seconds.'.format(self.name, timeout))

    def resize(self, size):
        self.pool._semaphore.counter = size
        self.pool.size = size


class GeventService(GreenletService):
    """

    """

    def spawn(self, func, *args, **kwargs):
        """
        """
        worker = self.workers.spawn(func, *args, **kwargs)
        worker.name = 'Scatter-Worker-Gevent-'.format(len(self.workers))
        return GeventWorker(worker)

    def spawn_later(self, seconds, func, *args, **kwargs):
        """
        """
        worker = self.workers.spawn_later(seconds, func, *args, **kwargs)
        worker.name = 'Scatter-Worker-Gevent-'.format(len(self.workers))
        return GeventWorker(worker)

    def sleep(self, seconds):
        """
        """
        return sleep(seconds)

    def queue(self, *args, **kwargs):
        """
        """
        return queue.Queue(*args, **kwargs)

    def pool(self, *args, **kwargs):
        """
        """
        return pool.Pool(*args, **kwargs)

    def worker_pool(self, size):
        """
        """
        return GeventWorkerPool(pool.Pool, size)

    def group(self, *args, **kwargs):
        """
        """
        return pool.Group(*args, **kwargs)

    def event(self, *args, **kwargs):
        """
        """
        return event.Event(*args, **kwargs)

    def lock(self, *args, **kwargs):
        """
        """
        return lock.RLock(*args, **kwargs)

    def signal(self, *args, **kwargs):
        """
        """
        return signal(*args, **kwargs)

    def on_initialized(self):
        """
        """
        self.config.setdefault('WORKER_POOL_SIZE', 1000)
        self.config.setdefault('WORKER_STOP_TIMEOUT', 5)

    def on_started(self):
        """
        """
        self.workers = self.worker_pool(self.worker_pool_size)

    def on_stopped(self):
        """

        """
        #Ensure we're not a member of worker pool we're flushing.
        if getcurrent() in self.workers:
            return spawn(self.on_stopping).join()

        try:
            self.log.info('Flushing {0} workers.'.format(len(self.workers)))
            self.workers.flush(self.worker_stop_timeout)
        except ScatterTimeout:
            self.log.warning('Failed to stop all workers after {0} seconds.'.format(self.worker_stop_timeout))


