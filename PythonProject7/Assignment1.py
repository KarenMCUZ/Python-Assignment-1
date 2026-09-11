# Q1.i. The error happens because Python sees calls as a new local variable inside wrapper,
# but the code tries to read it before it has been assigned a value.

# 1.ii. Store the decorator’s state in the closure so it persists across calls.
# For class methods, that closure is shared by all instances; use closure-level state for a shared limit,
# or key the state by instance for independent limits.

# iii. corrected code
import time
from collections import deque
from functools import wraps

def rate_limit(max_calls: int, period: int):
    def decorator(func):
        calls = deque()

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()


            while calls and now - calls[0] >= period:
                calls.popleft()

            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded")

            calls.append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator

@rate_limit(max_calls=3, period=10)
def fetch_user_data(user_id):
    return f"Data for {user_id}"

#Question 2 code
class EventDispatcher:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_type: str, callback: callable):
        """Register a callback for a particular event type."""
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []

        self._subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: str, callback: callable):
        """Remove a previously registered callback."""
        if event_type in self._subscribers:
            try:
                self._subscribers[event_type].remove(callback)
            except ValueError:
                pass

            if not self._subscribers[event_type]:
                del self._subscribers[event_type]

    def dispatch(self, event_type: str, *args, **kwargs):
        """Execute callbacks registered for an event."""
        callbacks = self._subscribers.get(event_type, [])

        for callback in list(callbacks):
            try:
                callback(*args, **kwargs)
            except Exception as error:
                print( f"Error in callback for '{event_type}': {error}" )


def send_email(username):
    print(f"Email notification sent to {username}")


def update_dashboard(username):
    print(f"Dashboard updated for {username}")


def faulty_callback(username):
    raise Exception("Simulated callback failure")


dispatcher = EventDispatcher()

dispatcher.subscribe("user_registered", send_email)
dispatcher.subscribe("user_registered", faulty_callback)
dispatcher.subscribe("user_registered", update_dashboard)

dispatcher.dispatch("user_registered", "Karen")

dispatcher.unsubscribe("user_registered", faulty_callback)

print("\nAfter unsubscribing faulty_callback:")
dispatcher.dispatch("user_registered", "Karen")

#Question 3
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.storage_name = None

    def __set_name__(self, owner, name):
        self.storage_name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )

        setattr(instance, self.storage_name, value)

class Student:
    age = Typed(int)
    name = Typed(str)

    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Karen", 38)
print(student.name)
print(student.age)

#Question 4
def product_of_multiples(factor, limit):
    if factor == 0:
        raise ValueError("factor must not be zero")

    product = 1

    for number in range(factor, limit, factor):
        product *= number

    return product

print(product_of_multiples(2, 10))








