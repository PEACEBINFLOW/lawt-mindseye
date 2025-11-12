from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass(slots=True)
class Event:
source: str
type: str
payload: Dict[str, Any]
labels: List[str] = field(default_factory=list)
ts: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
t_label: Optional[str] = None # set by time_label
