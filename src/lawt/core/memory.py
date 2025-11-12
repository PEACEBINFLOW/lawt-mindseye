from typing import List
from .event import Event


class Memory:
"""In-memory store; swap with real TS backend later."""
def __init__(self):
self._events: List[Event] = []


def add(self, e: Event) -> None:
self._events.append(e)


def latest(self, n: int = 50) -> List[Event]:
return self._events[-n:]
