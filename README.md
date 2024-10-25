# ConnectionMap

## Overview
**ConnectionMap** is a LinkedIn-inspired visualization tool that maps a user’s professional network as an interactive, connection tree. Users can view and explore connections organized by categories such as skills, job titles, and mutual connections. The app provides an intuitive interface that helps users better understand their network structure and find optimal paths to reach specific connections.

## Technologies Used
- **Streamlit**: For creating a fast, interactive web interface.
- **React**: For building responsive front-end components.
- **Plotly**: For generating interactive graphs and visualizations.
- **Python**: For handling backend logic and data processing.

## Features
- Visualize connections in a radial layout, with user at the center and connections grouped by category.
- Search functionality to find specific individuals and trace the shortest connection path to them.
- Node sizing based on connection count, providing visual insight into each node's network reach.

## Installation

### Prerequisites
Ensure the following are installed on your machine:
- Python (v3.7 or higher)
- Node.js (v14 or higher)

### Clone the Repository
    ```bash
    git clone https://github.com/your-username/connectionmap.git
    cd connectionmap

### Backend Setup
- Create a virtual environment:

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

- Install Python dependencies:

  ```bash
  pip install -r requirements.txt

- Run Streamlit:
  ```bash
  streamlit run app.py

### Frontend Setup
- Navigate to the frontend directory:

  ```bash
  cd frontend

- Install dependencies:

  ```bash
  npm install

- Run the frontend:
  ```bash
  npm start
- Access the front-end application at http://localhost:3000.

### Usage
- Open the Streamlit and React apps.
- Explore the connection tree to visualize and analyze your network.
- Use the search feature to locate individuals and find the shortest connection path.

### Contributing
- Contributions are welcome! Please feel free to fork this repository, open issues, or submit pull requests.

### License
- This project is licensed under the MIT License.

### Acknowledgments
- Inspired by LinkedIn's connection network.

Let me know if you’d like any further customization!
