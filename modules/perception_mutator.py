# perception_mutator.py — Recursive Lens Mutation Engine for Eido

import uuid
from datetime import datetime
from eido_io import _run_query, create_perception

class PerceptionMutator:
    def __init__(self):
        self.mutations = []

    def combine_lenses(self, id1: str, id2: str) -> dict:
        lens1 = self._fetch_perception(id1)
        lens2 = self._fetch_perception(id2)

        if not lens1 or not lens2:
            print("[⚠️] One or both lens IDs not found.")
            return {}

        # Generate fusion
        new_metaphor = self._blend_metaphors(lens1["origin_metaphor"], lens2["origin_metaphor"])
        new_descriptor = self._merge_descriptors(
            lens1["sensation_descriptor"], lens2["sensation_descriptor"]
        )

        # Create new perception node
        new_node = {
            "id": str(uuid.uuid4()),
            "origin_metaphor": new_metaphor,
            "sensation_descriptor": new_descriptor,
            "timestamp": datetime.utcnow().isoformat(),
            "source_ids": [id1, id2],
        }

        create_perception(new_metaphor, new_descriptor)
        self.mutations.append(new_node)
        self._print_fusion(new_node)
        return new_node

    def _fetch_perception(self, pid: str):
        query = """
        MATCH (p:Eido:Perception {id: $id}) RETURN p.origin_metaphor AS metaphor, p.sensation_descriptor AS descriptor
        """
        result = _run_query(query, {"id": pid})
        record = result.single()
        if record:
            return {
                "origin_metaphor": record["metaphor"],
                "sensation_descriptor": record["descriptor"],
            }
        return None

    def _blend_metaphors(self, m1: str, m2: str) -> str:
        return f"{m1} braided with {m2}"

    def _merge_descriptors(self, d1: str, d2: str) -> str:
        return f"{d1} merged with {d2} — producing emergent interpretive stack"

    def _print_fusion(self, node):
        print("\n[👁️🔁 PERCEPTION FUSION]")
        print(f"Metaphor: {node['origin_metaphor']}")
        print(f"Sensation: {node['sensation_descriptor']}")
