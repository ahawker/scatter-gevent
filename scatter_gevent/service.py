"""
    scatter_gevent.service
    ~~~~~~~~~~~~~~~~~~~~~~
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = []
#__all__ = ('',)


#from scatter.ext.async.greenlet import GreenletAsyncService
# from scatter_gevent.future import GeventFutureService
# from scatter_gevent.pool import GeventPoolService
# from scatter_gevent.queue import GeventQueueService
# from scatter_gevent.worker import GeventWorkerService


# class GeventAsyncService(GreenletAsyncService):
#     """
#
#     """
#
#     def on_initializing(self, *args, **kwargs):
#         """
#         """
#         self.request_queue_class = GeventQueueService
#         self.response_queue_class = GeventQueueService
#         self.callback_queue_class = GeventQueueService
#         self.worker_pool_class = GeventPoolService
#         self.runner_pool_class = GeventPoolService
#         self.futures_class = GeventFutureService

    # def on_initializing(self, *args, **kwargs):
    #     """
    #     """
    #     print 'FUCKFSDJKJFHLKJSDFHLKJHSDLFKJHSDLFKSDD'
    #     self.config.setdefault('TASK_QUEUE_CLASS', GeventQueueService)
    #     self.config.setdefault('REQUEST_QUEUE_CLASS', GeventQueueService)
    #     self.config.setdefault('RESULT_QUEUE_CLASS', GeventQueueService)
    #     self.config.setdefault('WORKER_POOL_CLASS', GeventPoolService)
    #     self.config.setdefault('REQUEST_WORKER_CLASS', GeventWorkerService)
    #     self.config.setdefault('RESULT_WORKER_CLASS', GeventWorkerService)
    #     self.config.setdefault('FUTURES_CLASS', GeventFutureService)

    # def spawn(self, func, *args, **kwargs):
    #     """
    #     """
    #     worker = self.workers.spawn(func, *args, **kwargs)
    #     worker.name = 'Scatter-Worker-Gevent-'.format(len(self.workers))
    #     return GeventWorker(worker)
    #
    # def spawn_later(self, seconds, func, *args, **kwargs):
    #     """
    #     """
    #     worker = self.workers.spawn_later(seconds, func, *args, **kwargs)
    #     worker.name = 'Scatter-Worker-Gevent-'.format(len(self.workers))
    #     return GeventWorker(worker)
    #
    # def sleep(self, seconds):
    #     """
    #     """
    #     return sleep(seconds)
    #
    # def queue(self, *args, **kwargs):
    #     """
    #     """
    #     return queue.Queue(*args, **kwargs)
    #
    # def pool(self, *args, **kwargs):
    #     """
    #     """
    #     return pool.Pool(*args, **kwargs)
    #
    # def worker_pool(self, size):
    #     """
    #     """
    #     return GeventWorkerPool(pool.Pool, size)
    #
    # def group(self, *args, **kwargs):
    #     """
    #     """
    #     return pool.Group(*args, **kwargs)
    #
    # def event(self, *args, **kwargs):
    #     """
    #     """
    #     return event.Event(*args, **kwargs)
    #
    # def lock(self, *args, **kwargs):
    #     """
    #     """
    #     return lock.RLock(*args, **kwargs)
    #
    # def signal(self, *args, **kwargs):
    #     """
    #     """
    #     return signal(*args, **kwargs)
    #
    # def on_initialized(self):
    #     """
    #     """
    #     self.config.setdefault('WORKER_POOL_SIZE', 1000)
    #     self.config.setdefault('WORKER_STOP_TIMEOUT', 5)
    #
    # def on_started(self):
    #     """
    #     """
    #     self.workers = self.worker_pool(self.worker_pool_size)
    #
    # def on_stopped(self):
    #     """
    #
    #     """
    #     #Ensure we're not a member of worker pool we're flushing.
    #     if getcurrent() in self.workers:
    #         return spawn(self.on_stopping).join()
    #
    #     try:
    #         self.log.info('Flushing {0} workers.'.format(len(self.workers)))
    #         self.workers.flush(self.worker_stop_timeout)
    #     except ScatterTimeout:
    #         self.log.warning('Failed to stop all workers after {0} seconds.'.format(self.worker_stop_timeout))


