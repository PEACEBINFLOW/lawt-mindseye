future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict, Any, Optional
from ..core.event import Event


@dataclass
class LawResult:
passed: bool
score: float = 0.0
reason: str = ""


class Law:
"""Composable predicate with scoring. Think: a small, testable law."""
def __init__(self, name: str, fn: Callable[[Event, Dict[str, Any]], LawResult]):
self.name = name
self.fn = fn


def __call__(self, event: Event, ctx: Optional[Dict[str, Any]] = None) -> LawResult:
return self.fn(event, ctx or {})


# Example baseline laws


def law_type_in(allowed: set[str]) -> Law:
def _fn(e: Event, _: Dict[str, Any]) -> LawResult:
ok = e.type in allowed
return LawResult(ok, 1.0 if ok else 0.0, f"type={e.type}")
return Law("type_in", _fn)


def law_payload_has(keys: set[str]) -> Law:
def _fn(e: Event, _: Dict[str, Any]) -> LawResult:
missing = [k for k in keys if k not in e.payload]
ok = len(missing) == 0
return LawResult(ok, 1.0 if ok else 0.0, "missing="+",".join(missing))
return Law("payload_has", _fn)
