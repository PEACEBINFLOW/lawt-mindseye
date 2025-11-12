from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, List
from datetime import datetime, timezone


from lawt.core.event import Event
from lawt.engine.mindseye import MindsEye


app = FastAPI(title="LAW-T API", version="0.1")
engine = MindsEye()


class EventIn(BaseModel):
source: str
type: str
payload: Dict[str, Any]
labels: List[str] = []


@app.get("/health")
def health():
return {"status": "ok"}


@app.post("/ingest")
def ingest(evt: EventIn):
e = Event(source=evt.source, type=evt.type, payload=evt.payload, labels=evt.labels)
e, outcome = engine.ingest(e)
return {
"event": {
"source": e.source,
"type": e.type,
"labels": e.labels,
"t_label": e.t_label,
"ts": e.ts.isoformat()
},
"decision": {
"decision": outcome.decision,
"score": outcome.score,
"reasons": outcome.reasons
}
}
