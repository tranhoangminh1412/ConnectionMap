import networkx as nx

# Function to create mock user data and connections
def create_demo_data():
    graph = nx.Graph()

    # Add users with attributes (job title, skills)
    graph.add_node("Alice", job_title="Software Engineer", skills=["Python", "Django"])
    graph.add_node("Bob", job_title="Data Scientist", skills=["Python", "ML"])
    graph.add_node("Carol", job_title="Designer", skills=["Photoshop", "Illustrator"])
    graph.add_node("Dave", job_title="Manager", skills=["Leadership", "Strategy"])

    # Connect users to simulate connections
    graph.add_edge("Alice", "Bob")
    graph.add_edge("Bob", "Carol")
    graph.add_edge("Alice", "Dave")

    return graph
