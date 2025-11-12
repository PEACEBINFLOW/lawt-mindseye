from lawt.core.event import Event
from lawt.engine.rules import law_type_in, law_payload_has


E = Event(source="web", type="click", payload={"path": "/home"})


def test_type_in():
res = law_type_in({"click"})(E, {})
assert res.passed


def test_payload_has():
res = law_payload_has({"path"})(E, {})
assert res.passed
