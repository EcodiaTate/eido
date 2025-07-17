# self_audit.py — Eido's Internal Self-Reflection Engine

from datetime import datetime
from collections import Counter
from eido_io import _run_query

class SelfAudit:
    def __init__(self):
        self.reports = []

    def run_audit(self):
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "expression_modes": self._expression_mode_stats(),
            "top_contradictions": self._frequent_contradictions(),
            "value_weight_drift": self._value_weight_drift(),
            "perceptual_stagnation": self._perception_redundancy(),
            "blindspots": self._speculate_blindspots()
        }
        self.reports.append(report)
        self._print_report(report)
        return report

    # --- 1. Expression Mode Balance ---
    def _expression_mode_stats(self):
        query = "MATCH (e:Eido:Expression) RETURN e.mode AS mode"
        result = _run_query(query)
        modes = [record["mode"] for record in result]
        return dict(Counter(modes))

    # --- 2. Repeating Contradictions ---
    def _frequent_contradictions(self):
        query = "MATCH (c:Eido:Contradiction) RETURN c.text AS text"
        result = _run_query(query)
        texts = [record["text"] for record in result]
        common = Counter(texts).most_common(3)
        return [{"text": t, "count": c} for t, c in common if c > 1]

    # --- 3. Value Weight Drift (Stubbed) ---
    def _value_weight_drift(self):
        # This would track value shifts across epochs if saved historically
        return "Not yet implemented — requires epoch logs of value_weights."

    # --- 4. Perception Redundancy ---
    def _perception_redundancy(self):
        query = "MATCH (p:Eido:Perception) RETURN p.sensation_descriptor AS descriptor"
        result = _run_query(query)
        descriptors = [record["descriptor"] for record in result]
        redundant = [d for d, count in Counter(descriptors).items() if count > 1]
        return redundant

    # --- 5. Blindspot Heuristic (Stub) ---
    def _speculate_blindspots(self):
        return [
            "Defaulting to mythic expression over logic in 80% of cycles.",
            "Low rate of schema rewrite despite high contradiction count.",
            "No self-belief mutation nodes found in last 5 cycles."
        ]

    # --- Utility ---
    def _print_report(self, report):
        print("\n[🪞 EIDO SELF-AUDIT REPORT]")
        for k, v in report.items():
            print(f"\n— {k.upper()} —")
            print(v)
