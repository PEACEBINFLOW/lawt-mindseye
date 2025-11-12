from datetime import datetime
from dateutil import tz


BW_TZ = tz.gettz("Africa/Gaborone")


def time_label(ts: datetime) -> str:
"""Return a stable time label like "YYYY-MM-DD HH:MM | phase:XXm".
Phase buckets are 10-minute bins for MindsEye rhythm.
"""
local = ts.astimezone(BW_TZ)
bucket = local.strftime("%Y-%m-%d %H:%M")
phase = (local.minute // 10) * 10
return f"{bucket} | phase:{phase:02d}m"
