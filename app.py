import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="MST Research Lab", layout="wide")

# --- SIDEBAR: THE "PAGE 7" NOTES ---
st.sidebar.title("🔬 MST Research Lab")
st.sidebar.markdown("**Researcher:** Chris (Nairobi, Kenya)")
st.sidebar.divider()

# 1. Assumptions
with st.sidebar.expander("📝 Core Assumptions", expanded=False):
    st.write("""
    1. **Continuity:** Time modeled as a continuous strip.
    2. **Topology:** Structure is non-orientable (Möbius analogy).
    3. **Evolution:** Systems evolve *within* the structure.
    4. **Causality:** Preserved via local continuity, not global direction.
    """)

# 2. Limitations
with st.sidebar.expander("⚠️ Boundaries & Limitations", expanded=False):
    st.write("""
    * Lacks full mathematical formalism.
    * Analogy is structurally suggestive, not yet physically derived.
    * Entropy/Quantum connections are currently interpretive.
    """)

# 3. Open Questions
with st.sidebar.expander("❓ Open Questions", expanded=True):
    st.info("""
    * Can non-orientability be expressed in Spacetime models?
    * How does entropy interact with this structure?
    * Are there observable consequences?
    * What is the minimal math required for formalization?
    """)

# --- MAIN INTERFACE ---
st.title("Möbius Spatetime Theory (MST)")
st.subheader("Visualizing Global Non-Orientability and Temporal Entropy")

# User Controls
col1, col2 = st.columns([1, 3])

with col1:
    st.write("### Controls")
    entropy_level = st.slider("Select Entropy Intensity", 0.0, 0.5, 0.05)
    st.caption("Adjusting this simulates stochastic noise over a 4π rotation.")

# --- THE MATH ENGINE ---
u = np.linspace(0, 4 * np.pi, 100)
v = np.linspace(-1, 1, 10)
u, v = np.meshgrid(u, v)

# Möbius Parametric Equations
x = (1 + 0.5 * v * np.cos(u / 2)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2)

# Apply Entropy "Noise" based on slider
noise = np.random.normal(0, entropy_level, x.shape) * (u / (4 * np.pi))
x_n, y_n, z_n = x + noise, y + noise, z + noise

# --- THE VISUALIZATION ---
fig = go.Figure(data=[go.Surface(x=x_n, y=y_n, z=z_n, colorscale='Viridis', opacity=0.8)])
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene_camera=dict(eye=dict(x=1.5, y=1.5, z=0.8)))

with col2:
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.write("**Researcher Note:** This simulation visualizes the transition from a locally orientable path to a globally non-orientable state, incorporating a linear entropy gradient.")

with st.sidebar.expander("🛡️ What MST Does Not Claim", expanded=False):
    st.warning("""
    1. **Physicality:** Does not claim time travel is possible/impossible.
    2. **Supersession:** Does not supersede GR or Quantum Mechanics.
    3. **Verification:** Structure is not experimentally verified.
    4. **Definitive Solution:** Does not 'solve' paradoxes, but reframes them.
    """)

with st.sidebar.expander("🌀 The Paradox-Free Framework", expanded=True):
    st.info("""
    **Insight:** Paradoxes may be artifacts of linear-orientation assumptions. 
    **Topology:** Using Munkres' Quotient Topology, MST suggests that a 2π traversal results in a topological 'flip,' rendering standard 'Grandfather Paradoxes' null by altering the system's global state before intersection occurs.
    """)
    

# 1. First, you create the main Möbius surface
fig = go.Figure(data=[go.Mesh3d(...)]) 

# 2. THE PATH CODE MUST GO HERE (Before the chart is called)
fig.add_trace(go.Scatter3d(
    x=x_path, y=y_path, z=z_path,
    mode='lines',
    line=dict(color='red', width=5),
    name='Observer Path'
))

# 3. ONLY THEN DO YOU CALL THE CHART
st.plotly_chart(fig)

import numpy as np
import plotly.graph_objects as go

# ... (Keep your existing strip code) ...

# 1. Define the Observer's Path
t_path = np.linspace(0, 2*np.pi, 100) # One full lap
w_path = 0 # Staying in the center of the strip

# 2. Calculate the coordinates for the path
x_path = (1 + w_path/2 * np.cos(t_path/2)) * np.cos(t_path)
y_path = (1 + w_path/2 * np.cos(t_path/2)) * np.sin(t_path)
z_path = w_path/2 * np.sin(t_path/2)

# 3. Add the path to your figure
fig.add_trace(go.Scatter3d(
    x=x_path, y=y_path, z=z_path,
    mode='lines',
    line=dict(color='red', width=5),
    name='Observer Path'
))

# 4. Add the "Start" and "Halfway" points to show the flip
fig.add_trace(go.Scatter3d(
    x=[x_path[0], x_path[-1]], 
    y=[y_path[0], y_path[-1]], 
    z=[z_path[0], z_path[-1]],
    mode='markers',
    marker=dict(size=8, color=['green', 'yellow']),
    name='Start vs End of Lap'
))
