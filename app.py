import streamlit as st
from data.mock_data import create_demo_data
from graph_logic import find_nearest_connection
import plotly.graph_objects as go
import networkx as nx

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    # Return some JSON data
    data = {
        "nodes": ["User1", "Alice", "Bob", "Carol", "Dave"],
        "edges": [(0, 1), (1, 2), (2, 3)]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# Streamlit UI
st.title("LinkedIn-Like Connection Tree")

# Search functionality
start = st.text_input("Enter your name:")
target = st.text_input("Enter the person you're looking for:")

if st.button("Find Nearest Connection"):
    result = find_nearest_connection(graph, start, target)
    if result:
        st.success(f"The nearest connection to {target} is {result[0]} at level {result[1]}")
    else:
        st.error("No connection found.")

# Visualize the Network
import math
import plotly.graph_objects as go
import networkx as nx


def plot_radial_network(graph, central_user, groups):
    pos = {}  # Position dictionary
    radius_step = 2  # Distance between layers

    # Center user at (0,0)
    pos[central_user] = (0, 0)

    # Function to calculate positions on a circle
    def calculate_circle_positions(radius, num_nodes):
        angle_step = 2 * math.pi / num_nodes
        return [(radius * math.cos(i * angle_step), radius * math.sin(i * angle_step)) for i in range(num_nodes)]

    # Place nodes in concentric circles based on groups
    current_radius = radius_step
    for group_name, group_nodes in groups.items():
        positions = calculate_circle_positions(current_radius, len(group_nodes))
        for i, node in enumerate(group_nodes):
            pos[node] = positions[i]
        current_radius += radius_step

    # Create edge traces (connections)
    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += (x0, x1, None)
        edge_trace['y'] += (y0, y1, None)
    
    # Create node traces (users)
    # Create node traces (users)
    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],  # Ensure this is initialized as an empty list
        mode='markers+text',
        textposition="top center",
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color=[],
            size=[],
            line_width=2
        )
    )

    # Ensure that text is always an empty list
    node_trace['text'] = ()

    # Adjust node size based on the number of branches
    for node in graph.nodes():
        x, y = pos[node]
        node_trace['x'] += (x,)
        node_trace['y'] += (y,)

        # Debugging: Check the type of node_trace['text']
        
        node_trace['text'] += (node,)  # This should work if text is a list

        # Adjust size based on number of connections (degree)
        node_size = 20 + (len(list(graph.neighbors(node))) * 5)
        node_trace['marker']['size'] += (node_size,)


    # Create plot layout
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='Radial Connection Tree',
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=40),
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False),
                        height=800, width=800
                    ))

    return fig





# Example: Group your nodes into categories
groups = {
    "skills": ["Python", "Data Science", "Web Development"],
    "connections": ["Alice", "Bob", "Carol", "Dave"],
    "job_titles": ["Software Engineer", "Data Analyst", "Web Developer"]
}

# Central user
central_user = "User1"

# Calling the function with the graph and organized groups
st.plotly_chart(plot_radial_network(graph, central_user, groups))

