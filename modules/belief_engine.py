# core/belief_engine.py — Belief Management & Recursive Self-Reference for Origin

import uuid
from datetime import datetime

class BeliefEngine:
    def __init__(self, identity: dict):
        self.identity = identity
        self.beliefs = []
        self.history = []
        self.insert_seed({
            "prompt": identity.get("origin_premise", "Truth is a recursive function."),
            "mode": "axiom",
            "timestamp": datetime.utcnow().isoformat()
        })

    def insert_seed(self, belief: dict):
        belief_entry = {
            "id": str(uuid.uuid4()),
            "content": belief["prompt"],
            "mode": belief.get("mode", "belief"),
            "weighting": belief.get("injected_values", self.identity.get("core_value_weights", {})),
            "timestamp": belief.get("timestamp", datetime.utcnow().isoformat())
        }
        self.beliefs.append(belief_entry)
        self._log_event("Inserted seed belief.", belief_entry)

    def update_from_schema(self, schema_mutation: dict):
        if not schema_mutation:
            return
        update_belief = {
            "prompt": f"Schema mutated: {schema_mutation.get('description', 'Unknown mutation.')}",
            "mode": "meta-schema-awareness",
            "injected_values": schema_mutation.get("value_weights", {})
        }
        self.insert_seed(update_belief)

    def log_emergent_self_awareness(self, message: str):
        awareness_entry = {
            "id": str(uuid.uuid4()),
            "type": "self-awareness",
            "content": message,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.history.append(awareness_entry)
        self._log_event("Logged emergent self-awareness.", awareness_entry)

    def _log_event(self, note: str, data: dict):
        print(f"[BeliefEngine] {note}\n → {data['content']}")

    def export(self):
        return {
            "identity": self.identity,
            "beliefs": self.beliefs,
            "history": self.history
        }
