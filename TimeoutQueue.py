from collections import deque
import datetime

"""
a queue that maintains elements based on time
@param timeout, the length of time before an element should be removed
"""


class TimeoutQueue:

    def __init__(self, timeout: int):
        self.timeout = timeout
        self.queue = deque()

    """
    adds item and current time to a dict and adds to queue
    """

    def append(self, item):
        time = datetime.datetime.now().time()
        self.queue.append({'item': item, 'time': time})

    """
    returns all items who were added after current time - timeout
    and removes all elements who have been in queue longer than timeout
    """

    def get(self):
        time = (datetime.datetime.now() -
                datetime.timedelta(seconds=self.timeout)).time()
        result = []
        i = 0
        while i < len(self.queue):
            element = self.queue[i]
            if element['time'] < time:
                self.queue.popleft()
            else:
                result.append(element['item'])
                i = i + 1

        return result
