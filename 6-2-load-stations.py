#!/usr/bin/env python3

from graphdatascience import GraphDataScience
# Connect to the database
host = "bolt://127.0.0.1:7687"
user = "neo4j"
password= "test1234"
gds = GraphDataScience(host, auth=(user, password), database="neo4j")
# Load stations as nodes
gds.run_cypher( """
    LOAD CSV WITH HEADERS FROM "file:///nr-stations-all.csv" AS station
    CREATE (:Station {name: station.name, crs: station.crs})
    """
)
# Load tracks bewteen stations as relationships
gds.run_cypher( """
    LOAD CSV WITH HEADERS FROM "file:///nr-station-links.csv" AS track
    MATCH (from:Station {crs: track.from})
    MATCH (to:Station {crs: track.to})
    MERGE (from)-[:TRACK {distance: round( toFloat(track.distance), 2 )}]->(to)
    """
)
gds.close()