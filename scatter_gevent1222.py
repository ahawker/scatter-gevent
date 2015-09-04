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
from scatter.exceptions import ScatterTimeout, ScatterExit
from scatter.ext.async.core import Worker, WorkerPool, PoolService, AsyncPool, QueueService
from scatter.ext.async.queue import AsyncQueue
from scatter.ext.async.greenlet import GreenletService



Event = event.Event
#Condition = event.Event
Lock = lock.RLock
RLock = lock.RLock
Semaphore = lock.Semaphore
BoundedSemaphore = lock.BoundedSemaphore
Queue = queue.Queue
Signal = signal











