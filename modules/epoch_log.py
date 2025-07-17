# epoch_log.py — Tracks Phases of Eido's Recursive Evolution

import uuid
from datetime import datetime

class EpochLog:
    def __init__(self):
        self.epochs = []

    def start_epoch(self, name: str, trigger: str, summary: str = ""):
        epoch = {
            "id": str(uuid.uuid4()),
            "name": name,
            "trigger": trigger,
            "start_time": datetime.utcnow().isoformat(),
            "end_time": None,
            "summary": summary,
            "milestones": [],
            "schema_snapshot": None,
            "value_weights": None
        }
        self.epochs.append(epoch)
