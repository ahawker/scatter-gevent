"""
    scatter_gevent.worker
    ~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = ('GeventWorkerService',)


import sys
import gevent
from gevent import greenlet

from scatter.exceptions import ScatterExit
from scatter.ext.async import Worker, WorkerService, AsyncResult
from scatter_gevent.core import Event


class ScatterGreenlet(gevent.Greenlet):
    """

    """

    def __init__(self, func, *args, **kwargs):
        super(ScatterGreenlet, self).__init__(func, *args, **kwargs)
        self._started = Event()
        self._cancelled = Event()

    @property
    def id(self):
        return id(self)

    def started(self):
        """
        """
        return self._started.is_set()

    def running(self):
        """
        """
        return not self.ready()

    def cancelled(self):
        """
        """
        return self._cancelled.is_set()

    def completed(self):
        """
        """
        return self.ready()

    def wait_for_start(self, timeout=None):
        """
        """
        return self._started.wait(timeout)

    def wait_for_completion(self, timeout=None):
        """
        """
        return self.join(timeout)

    def run(self):
        """
        """
        if self._cancelled.is_set():
            return

        self._started.set()
        super(ScatterGreenlet, self).run()
        return self.get()

    def cancel(self):
        """
        """
        if self.started():
            return False
        self._cancelled.set()
        self.stop()
        return not self.started()

    def stop(self, exception=ScatterExit, block=True, timeout=None):
        """
        """
        self.kill(exception, block, timeout)
        return not self.running()

    def join(self, timeout=None):
        """
        """
        super(ScatterGreenlet, self).join(timeout)
        return not self.running()

    def is_current(self):
        """
        """
        return gevent.getcurrent() is self


class GeventWorker(Worker):
    """

    """

    worker_cls = ScatterGreenlet


class GeventWorkerService(WorkerService):
    """

    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.worker_class = GeventWorker