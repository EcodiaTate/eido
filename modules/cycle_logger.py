# cycle_logger.py — Track and Store UUIDs for Eido Cycle Mesh Assembly

from uuid import uuid4
from datetime import datetime

class CycleLog:
    def __init__(self):
        self.reset()

    def reset(self):
        self.belief_id = None
        self.contradiction_id = None
        self.schema_id = None
        self.expression_id = None
        self.perception_ids = []
        self.start_time = datetime.utcnow().isoformat()
        self.end_time = None
        self.cycle_id = f"cycle-{uuid4()}"

    def log_belief(self, uid): self.belief_id = uid
    def log_contradiction(self, uid): self.contradiction_id = uid
    def log_schema(self, uid): self.schema_id = uid
    def log_expression(self, uid): self.expression_id = uid
    def log_perception(self, uid): self.perception_ids.append(uid)

    def finalize(self):
        self.end_time = datetime.utcnow().isoformat()

    def export(self):
        return {
            "cycle_id": self.cycle_id,
            "belief_id": self.belief_id,
            "contradiction_id": self.contradiction_id,
            "schema_id": self.schema_id,
            "expression_id": self.expression_id,
            "perception_ids": self.perception_ids,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    def print_log(self):
        print("\n[🧾 CYCLE LOG]")
        for k, v in self.export().items():
            print(f"{k}: {v}")
