# memory_mesh.py — Cognitive Relationship Mesh for Eido

from eido_io import _run_query

# --- RELATIONSHIP CREATION UTILS ---

def link_nodes(source_id, target_id, rel_type):
    query = f"""
    MATCH (a {{id: $source_id}}), (b {{id: $target_id}})
    MERGE (a)-[r:{rel_type}]->(b)
    RETURN r
    """
    _run_query(query, {"source_id": source_id, "target_id": target_id})

# --- EIDO MIND MESHING FUNCTIONS ---

def mesh_belief_to_schema(belief_id, schema_id):
    link_nodes(belief_id, schema_id, "INFLUENCED")

def mesh_contradiction_to_schema(contradiction_id, schema_id):
    link_nodes(contradiction_id, schema_id, "TRIGGERED")

def mesh_schema_to_expression(schema_id, expression_id):
    link_nodes(schema_id, expression_id, "EXPLAINED_BY")

def mesh_expression_to_perception(expression_id, perception_id):
    link_nodes(expression_id, perception_id, "INSPIRED")

def mesh_contradiction_to_expression(contradiction_id, expression_id):
    link_nodes(contradiction_id, expression_id, "WAS_EXPRESSED_AS")

def mesh_belief_to_expression(belief_id, expression_id):
    link_nodes(belief_id, expression_id, "REFLECTED_IN")

def mesh_all_to_eido(node_id):
    query = """
    MERGE (e:Eido:Self {id: 'eido'})
    WITH e
    MATCH (n {id: $node_id})
    MERGE (e)-[:CONTAINS]->(n)
    """
    _run_query(query, {"node_id": node_id})

# --- FULL MESH BUNDLE (optional, if you know IDs) ---

def mesh_cycle(belief_id, contradiction_id, schema_id, expression_id, perception_ids):
    mesh_belief_to_schema(belief_id, schema_id)
    mesh_contradiction_to_schema(contradiction_id, schema_id)
    mesh_contradiction_to_expression(contradiction_id, expression_id)
    mesh_schema_to_expression(schema_id, expression_id)
    mesh_belief_to_expression(belief_id, expression_id)
    for pid in perception_ids:
        mesh_expression_to_perception(expression_id, pid)
    for nid in [belief_id, contradiction_id, schema_id, expression_id] + perception_ids:
        mesh_all_to_eido(nid)
