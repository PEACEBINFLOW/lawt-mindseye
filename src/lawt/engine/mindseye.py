from ..core.event import Event
from ..core.time_labeler import time_label
from ..core.memory import Memory
from .decision import DecisionNode, DecisionOutcome
from .rules import law_type_in, law_payload_has


class MindsEye:
"""Thin orchestrator: label time → apply laws → store → return decision."""
def __init__(self, memory: Memory | None = None):
self.memory = memory or Memory()
self.node = DecisionNode([
law_type_in({"click", "metric", "log"}),
law_payload_has({"path"})
])


def ingest(self, e: Event) -> tuple[Event, DecisionOutcome]:
e.t_label = time_label(e.ts)
outcome = self.node.evaluate(e, ctx={})
self.memory.add(e)
return e, outcome
