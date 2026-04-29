import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="MST Research Lab", layout="wide")
st.title("Möbius Spacetime Theory (MST) Visualizer")
st.markdown("### *A Topological Framework for Paradox-Free Temporal Manifolds*")

# --- SIDEBAR: RESEARCHER DOCUMENTATION ---
st.sidebar.header("🔬 MST Research Framework")
st.sidebar.info("**Researcher:** Chris")

# 1. ASSUMPTIONS (Your exact words)
with st.sidebar.expander("📝 ASSUMPTIONS"):
    st.write("1. Time can be modeled as a continuous structure.")
    st.write("2. This structure is non-orientable, analogous to a Möbius strip.")
    st.write("3. Physical systems evolve within this structure, not outside it.")
    st.write("4. Causality is preserved through local continuity, not global direction.")
    st.caption("*These assumptions are chosen for coherence, not proof.*")

# 2. WHAT MST DOES NOT CLAIM
with st.sidebar.expander("🚫 WHAT MST DOES NOT CLAIM"):
    st.write("1. That time travel is physically possible/impossible.")
    st.write("2. That it supersedes relativity or QM.")
    st.write("3. That its structure has been experimentally verified.")
    st.write("4. That paradoxes are 'solved' in a definitive sense.")

# 3. LIMITATIONS
with st.sidebar.expander("⚠️ LIMITATIONS"):
    st.write("1. MST currently lacks a full mathematical formalism.")
    st.write("2. The Möbius analogy is not yet derivable from physical law.")
    st.write("3. Connections to entropy/QM are interpretive.")
    st.caption("*These limitations are boundaries to be respected.*")

# --- INTERACTIVE CONTROLS & DATA LOGGING ---
st.sidebar.divider()
st.sidebar.subheader("Simulation Controls")
progress = st.sidebar.slider("Temporal Progress (Radians)", 0.0, float(4*np.pi), 0.0, step=0.1)

# Logic for Orientation State
orientation = "NORMAL" if progress < 2*np.pi or progress > 3.9*np.pi else "INVERTED"

# --- MATH SECTION ---
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 20)
u, v = np.meshgrid(u, v)

# The Manifold
x = (1 + v/2 * np.cos(u/2)) * np.cos(u)
y = (1 + v/2 * np.cos(u/2)) * np.sin(u)
z = v/2 * np.sin(u/2)

# The Observer Position
obs_x = (1 + 0 * np.cos(progress/2)) * np.cos(progress)
obs_y = (1 + 0 * np.cos(progress/2)) * np.sin(progress)
obs_z = 0 * np.sin(progress/2)

# Create a Log Entry
log_data = pd.DataFrame({
    "Parameter": ["Temporal Progress (Rad)", "X-Coordinate", "Y-Coordinate", "Z-Coordinate", "State"],
    "Value": [round(progress, 2), round(obs_x, 4), round(obs_y, 4), round(obs_z, 4), orientation]
})

# Sidebar Data Export
st.sidebar.subheader("📓 Lab Notebook")
st.sidebar.table(log_data)
csv = log_data.to_csv(index=False).encode('utf-8')
st.sidebar.download_button("Download Current Log", csv, "mst_coordinate_log.csv", "text/csv")

# --- BUILDING THE PLOT ---
fig = go.Figure()

# The Surface
fig.add_trace(go.Mesh3d(x=x.flatten(), y=y.flatten(), z=z.flatten(), opacity=0.3, color='cyan', name='Manifold'))

# Static Timeline
t_p_full = np.linspace(0, 4 * np.pi, 200)
x_p_f = (1 + 0 * np.cos(t_p_full/2)) * np.cos(t_p_full)
y_p_f = (1 + 0 * np.cos(t_p_full/2)) * np.sin(t_p_full)
z_p_f = 0 * np.sin(t_p_full/2)
fig.add_trace(go.Scatter3d(x=x_p_f, y=y_p_f, z=z_p_f, mode='lines', line=dict(color='red', width=2), name='Timeline'))

# Active Observer
fig.add_trace(go.Scatter3d(
    x=[obs_x], y=[obs_y], z=[obs_z],
    mode='markers+text',
    marker=dict(size=12, color='gold', symbol='diamond'),
    text=[f"STATE: {orientation}"], textposition="top center",
    name='Observer'
))

fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Time (Z)'), margin=dict(l=0, r=0, b=0, t=0))

st.plotly_chart(fig, use_container_width=True)

# Status Message
if orientation == "INVERTED":
    st.warning(f"CRITICAL STATE: Observer at {round(progress, 2)} rad has undergone Parity Inversion. Interaction with origin state is topologically prohibited.")
else:
    st.success(f"STABLE STATE: Observer at {round(progress, 2)} rad is in an orientable phase.")
