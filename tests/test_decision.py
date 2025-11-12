from lawt.core.event import Event
from lawt.engine.mindseye import MindsEye


def test_decision_accept():
e = Event(source="web", type="click", payload={"path": "/"})
_, out = MindsEye().ingest(e)
assert out.decision in {"ACCEPT", "REVIEW", "REJECT"}
