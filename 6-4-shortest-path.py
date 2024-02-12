#!/usr/bin/env python3

from graphdatascience import GraphDataScience
host = "bolt://127.0.0.1:7687"
user = "neo4j"
password= "test1234"
gds = GraphDataScience(host, auth=(user, password), database="neo4j")
bham = gds.find_node_id(["Station"], {"name": "Birmingham New Street"})
eboro = gds.find_node_id(["Station"], {"name": "Edinburgh"})
shortest_path = gds.shortestPath.dijkstra.stream(
    gds.graph.get("trains"),
    sourceNode=bham,
    targetNode=eboro,
    relationshipWeightProperty="distance"
)
print("Shortest distance: %s" % shortest_path.get('costs').get(0)[-1])
gds.close()
