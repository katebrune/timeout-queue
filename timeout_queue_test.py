import unittest
from TimeoutQueue import TimeoutQueue
import time


class TimeOutQueueTest(unittest.TestCase):
    """
    set up a queue that maintains items for 5 seconds
    """

    def setUp(self):
        self.queue = TimeoutQueue(5)

    """
    tests that items are added to queue
    """

    def test_adds_items(self):
        self.queue.append('a')
        self.queue.append('b')
        result = self.queue.get()
        self.assertEqual(len(result), 2)

    """
    tests that items are removed after time
    and not returned
    """

    def test_removes_after_time(self):
        self.queue.append('a')
        self.queue.append('b')
        time.sleep(6)
        self.queue.append('c')
        result = self.queue.get()
        self.assertEqual(len(result), 1)
