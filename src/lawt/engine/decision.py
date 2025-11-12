from dataclasses import dataclass
from typing import List, Dict, Any
from ..core.event import Event
from .rules import Law, LawResult


@dataclass
class DecisionOutcome:
decision: str
score: float
reasons: List[str]


class DecisionNode:
"""Evaluate a set of Laws and produce a decision label.
Strategy: if all pass → ACCEPT; if any critical fails → REJECT; else → REVIEW.
"""
def __init__(self, laws: List[Law]):
self.laws = laws


def evaluate(self, e: Event, ctx: Dict[str, Any] | None = None) -> DecisionOutcome:
results: List[LawResult] = [law(e, ctx or {}) for law in self.laws]
passed = all(r.passed for r in results)
score = sum(r.score for r in results) / max(1, len(results))
reasons = [r.reason for r in results if r.reason]
if passed:
return DecisionOutcome("ACCEPT", score, reasons)
if any(not r.passed for r in results) and score < 0.5:
return DecisionOutcome("REJECT", score, reasons)
return DecisionOutcome("REVIEW", score, reasons)
