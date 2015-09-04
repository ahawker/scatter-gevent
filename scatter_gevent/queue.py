"""
    scatter_gevent.queue
    ~~~~~~~~~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('GeventQueue', 'GeventQueueService')


from gevent.queue import JoinableQueue, Empty, Full
from scatter.ext.async.queue import Queue, QueueService


class GeventQueue(Queue):
    """

    """

    queue_cls = JoinableQueue

    def join(self, timeout=None):
        """
        """
        return self._queue._cond.wait(timeout)


class GeventQueueService(QueueService):
    """

    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.queue_class = GeventQueue
        self.queue_max_size = None
        self.queue_empty_exception = Empty
        self.queue_full_exception = Full
        #self.config.setdefault('QUEUE_CLASS', GeventQueue)
        #self.config.setdefault('QUEUE_MAX_SIZE', None)
        #self.config.setdefault('QUEUE_EMPTY_EXCEPTION', Empty)
        #self.config.setdefault('QUEUE_FULL_EXCEPTION', Full)
