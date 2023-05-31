from neo4j import GraphDatabase

# Define Neo4j database connection parameters
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"

# Connect to Neo4j database
driver = GraphDatabase.driver(uri, auth=(user, password))

# Define query to create nodes and relationships for customer sentiments about HP printers
query = """
    MERGE (p:Printer {model: $printer_model})
    MERGE (s:Sentiment {type: $sentiment})
    MERGE (u:User {name: $user_name})
    MERGE (u)-[:POSTED]->(n:Node {text: $text})
    MERGE (n)-[:HAS_SENTIMENT]->(s)
    MERGE (n)-[:MENTIONS]->(p)
"""

# Define sample data
data = [
    {'text': 'My HP printer keeps jamming', 'user_name': 'user1', 'timestamp': '2022-01-01 10:00:00', 'sentiment': 'complaint', 'printer_model': 'OfficeJet Pro 9015e'},
    {'text': 'I love my new HP printer', 'user_name': 'user2', 'timestamp': '2022-01-02 11:00:00', 'sentiment': 'appreciation', 'printer_model': 'ENVY Pro 6455'},
    {'text': 'HP printer wifi setup is a nightmare', 'user_name': 'user3', 'timestamp': '2022-01-03 12:00:00', 'sentiment': 'complaint', 'printer_model': 'LaserJet Pro MFP M148fdw'},
    {'text': 'My HP printer is working great', 'user_name': 'user4', 'timestamp': '2022-01-04 13:00:00', 'sentiment': 'appreciation', 'printer_model': 'DeskJet 3755'},
    {'text': 'HP printer ink is too expensive', 'user_name': 'user5', 'timestamp': '2022-01-05 14:00:00', 'sentiment': 'complaint', 'printer_model': 'OfficeJet Pro 9025e'}
]

# Open Neo4j session and execute queries for each data point
with driver.session() as session:
    for d in data:
        session.run(query, d)
