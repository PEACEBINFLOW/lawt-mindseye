from datetime import datetime, timezone
from lawt.core.time_labeler import time_label


def test_time_label_format():
lbl = time_label(datetime.now(timezone.utc))
assert "phase:" in lbl
