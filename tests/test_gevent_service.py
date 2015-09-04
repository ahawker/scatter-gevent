"""

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'


from scatter.tests import ServiceTestCase
from scatter_gevent.pool import GeventPoolService
from scatter_gevent.queue import GeventQueueService
from scatter_gevent.service import GeventService
from scatter_gevent.worker import GeventWorkerService


class TestGeventService(ServiceTestCase):
    """

    """

    #:
    #:
    service_class = GeventService

    # @classmethod
    # def setUpClass(cls):
    #     print 'setup'

    def test_config_defaults(self):
        """

        """
        self.assert_equal(self.service.task_queue_class, GeventQueueService)
        self.assert_equal(self.service.request_queue_class, GeventQueueService)
        self.assert_equal(self.service.result_queue_class, GeventQueueService)
        self.assert_equal(self.service.worker_pool_class, GeventPoolService)
        self.assert_equal(self.service.request_worker_class, GeventWorkerService)
        self.assert_equal(self.service.result_worker_class, GeventWorkerService)


if __name__ == '__main__':
    import unittest
    unittest.main()