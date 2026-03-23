import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="MST Research Lab", layout="wide")
st.title("Möbius Spacetime Theory (MST) Visualizer")
st.write("Exploring Non-Orientable Temporal Manifolds and Paradox-Free Frameworks.")

# --- 1. THE TOPOLOGICAL MATH (The Surface) ---
# Create the u (angle) and v (width) coordinates
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 20)
u, v = np.meshgrid(u, v)

# Parametric equations for a Möbius Strip
x = (1 + v/2 * np.cos(u/2)) * np.cos(u)
y = (1 + v/2 * np.cos(u/2)) * np.sin(u)
z = v/2 * np.sin(u/2)

# Flatten for Plotly Mesh3d
x_flat, y_flat, z_flat = x.flatten(), y.flatten(), z.flatten()

# --- 2. THE OBSERVER PATH MATH (The Red Line) ---
# This simulates a particle traveling exactly one lap (360 degrees)
t_path = np.linspace(0, 2 * np.pi, 100)
w_path = 0  # Stay in the middle of the strip width
x_p = (1 + w_path/2 * np.cos(t_path/2)) * np.cos(t_path)
y_p = (1 + w_path/2 * np.cos(t_path/2)) * np.sin(t_path)
z_p = w_path/2 * np.sin(t_path/2)

# --- 3. BUILDING THE 3D PLOT ---
# Create the figure object
fig = go.Figure()

# Add the Möbius Surface
fig.add_trace(go.Mesh3d(
    x=x_flat, y=y_flat, z=z_flat,
    intensity=z_flat,
    colorscale='Viridis',
    opacity=0.5,
    name='MST Manifold',
    showscale=False
))

# Add the Red Observer Path
fig.add_trace(go.Scatter3d(
    x=x_p, y=y_p, z=z_p,
    mode='lines',
    line=dict(color='red', width=6),
    name='Observer Path (1 Lap)'
))

# Add Start (Green) and End (Yellow) markers
fig.add_trace(go.Scatter3d(
    x=[x_p[0], x_p[-1]], 
    y=[y_p[0], y_p[-1]], 
    z=[z_p[0], z_p[-1]],
    mode='markers',
    marker=dict(size=10, color=['#00FF00', '#FFFF00']),
    name='Start vs End of Lap'
))

# --- 4. LAYOUT SETTINGS ---
fig.update_layout(
    scene=dict(
        xaxis_title='Space (X)',
        yaxis_title='Space (Y)',
        zaxis_title='Time (Z)'
    ),
    margin=dict(l=0, r=0, b=0, t=0),
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

# --- 5. DISPLAY IN STREAMLIT ---
st.plotly_chart(fig, use_container_width=True)

st.sidebar.header("Research Parameters")
st.sidebar.write("Theory: MST (Non-Orientable)")
st.sidebar.info("The Red Path shows that after one lap ($2\pi$), the observer is flipped, preventing interaction with the past self.")
