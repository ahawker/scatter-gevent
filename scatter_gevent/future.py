"""
    scatter_gevent.future
    ~~~~~~~~~~~~~~~~~~~~~


"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('GeventFuture', 'GeventFutureService')


from gevent.event import AsyncResult
from scatter.ext.async.future import Future, FutureService


class ScatterAsyncResult(AsyncResult):
    """

    """

    def completed(self):
        """
        """
        return self.ready()

    def set_result(self, result):
        """
        """
        return self.set(result)


class GeventFuture(Future):
    """

    """

    future_cls = ScatterAsyncResult


class GeventFutureService(FutureService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """

        """
        self.future_class = GeventFuture