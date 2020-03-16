# TimeoutQueue

TimeoutQueue is a queue that maintains elements for a set amount of time

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install timeoutqueue.

```bash
pip install -i https://test.pypi.org/simple/ timeoutqueue
```

## Usage

```python
from timeoutqueue import TimeoutQueue

queue = TimeoutQueue(5) # initializes queue that maintains items for 5 seconds
queue.append('a') # adds 'a' to the queue
items = queue.get() # returns all elements that have been added in the last 5 seconds
```

## License
[WTFPL](https://choosealicense.com/licenses/wtfpl/)
