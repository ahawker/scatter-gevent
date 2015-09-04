"""
    scatter_gevent.core
    ~~~~~~~~~~~~~~~~~~~

    Asynchronous primitives for gevent.
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('Event', 'Condition', 'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Queue', 'Signal')


from gevent import event, lock, queue, signal, thread, threading, threadpool, hub



# class Condition(object):
#     """
#     """
#
#     def __init__(self, lock=None, verbose=None):
#         self._links = set()
#         self._todo = set()
#         self._hub = hub.get_hub()
#         self._notifier = None
#
#     def


# class Condition(object):
#     """
#
#     """
#
#     def __init__(self, lock=None):
#         self._lock = lock or lock.RLock()
#         self.acquire = self._lock.acquire
#         self.release = self._lock.release
#         self._release_save = self._lock._release_save
#         self._acquire_restore = self._lock._acquire_restore
#         self._is_owned = self._lock._is_owned
#         self._links = set()
#         self._todo = set()
#
#     def __enter__(self):
#         return self._lock.__enter__()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return self._lock.__exit__(exc_type, exc_val, exc_tb)
#
#     def __repr__(self):
#         return '<Condition({0}, {1})>'.format(self._lock, len(self._links))
#
#
#     def wait(self, timeout=None):
#         """
#
#         """
#         if not self._is_owned():
#             raise RuntimeError('cannot wait on un-acquired lock')
#         waiter = thread.allocate_lock()
#         pass
#
#     def notify(self, n=1):
#         """
#         """
#
#
#     def notify_all(self):
#         """
#         """
#         return self.notify(len(self._links))




Event = event.Event
Condition = None
Lock = lock.RLock
RLock = lock.RLock
Semaphore = lock.Semaphore
BoundedSemaphore = lock.BoundedSemaphore
Queue = queue.JoinableQueue
Signal = signal