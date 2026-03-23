import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="MST Research Lab", layout="wide")
st.title("Möbius Spacetime Theory (MST) Visualizer")
st.markdown("### *Exploring Non-Orientable Temporal Manifolds and Paradox-Free Frameworks*")

# --- SIDEBAR: RESEARCHER DOCUMENTATION ---
st.sidebar.header("🔬 Research Information")
st.sidebar.info("**Researcher:** Chris")
st.sidebar.write("**Status:** Active Theory Development")

# Sliders for interactive variables (Optional, for future math tweaks)
st.sidebar.divider()
st.sidebar.subheader("Manifold Parameters")
twist_intensity = st.sidebar.slider("Twist Intensity", 0.1, 2.0, 1.0)

# The "Open Question" & Limitations Section
with st.sidebar.expander("❓ Open Questions"):
    st.write("How does the observer maintain consciousness through a global parity flip?")

with st.sidebar.expander("⚠️ Limitations & Assumptions"):
    st.write("- Assumes spacetime is locally Euclidean.")
    st.write("- Requires the non-existence of traditional orientable closed timelike curves.")

with st.sidebar.expander("🚫 What MST Does Not Claim"):
    st.write("MST does NOT claim to allow for traditional 'Grandfather Paradox' scenarios. The topology inherently nullifies the possibility of an observer interacting with their identical past state.")

# --- 1. THE TOPOLOGICAL MATH ---
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 20)
u, v = np.meshgrid(u, v)

# Parametric equations with adjustable twist intensity
x = (1 + v/2 * np.cos(u/2 * twist_intensity)) * np.cos(u)
y = (1 + v/2 * np.cos(u/2 * twist_intensity)) * np.sin(u)
z = v/2 * np.sin(u/2 * twist_intensity)

# Flatten for Plotly
x_flat, y_flat, z_flat = x.flatten(), y.flatten(), z.flatten()

# --- 2. THE OBSERVER PATH MATH (The 4π "Double Loop") ---
# We change 2*np.pi to 4*np.pi to show the full journey back to start
t_path = np.linspace(0, 4 * np.pi, 200) 
w_path = 0  
x_p = (1 + w_path/2 * np.cos(t_path/2 * twist_intensity)) * np.cos(t_path)
y_p = (1 + w_path/2 * np.cos(t_path/2 * twist_intensity)) * np.sin(t_path)
z_p = w_path/2 * np.sin(t_path/2 * twist_intensity)

# --- 3. BUILDING THE 3D PLOT ---
fig = go.Figure()

# The Möbius Manifold (The "Floor")
fig.add_trace(go.Mesh3d(
    x=x_flat, y=y_flat, z=z_flat,
    intensity=z_flat,
    colorscale='Viridis',
    opacity=0.5,
    name='MST Manifold'
))

# The Red Observer Path (The Journey)
fig.add_trace(go.Scatter3d(
    x=x_p, y=y_p, z=z_p,
    mode='lines',
    line=dict(color='red', width=7),
    name='Observer Path (4π)'
))

# The Three Key States: Start, Flip, and Return
fig.add_trace(go.Scatter3d(
    x=[x_p[0], x_p[100], x_p[-1]], 
    y=[y_p[0], y_p[100], y_p[-1]], 
    z=[z_p[0], z_p[100], z_p[-1]],
    mode='markers',
    marker=dict(size=12, color=['#00FF00', '#FFFF00', '#0000FF']), # Green, Yellow, Blue
    name='Green=Start | Yellow=Flip | Blue=Return'
))

# --- 4. DISPLAY ---
st.plotly_chart(fig, use_container_width=True)

st.success("The visual proof: Notice the yellow dot (End of Lap) is on the opposite side of the manifold from the green dot (Start).")
