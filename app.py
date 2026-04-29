import streamlit as st
import numpy as np
import plotly.graph_objects as go

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
    st.caption("*These assumptions are chosen for coherence, not proof. Their validity remains open to examination.*")

# 2. WHAT MST DOES NOT CLAIM
with st.sidebar.expander("🚫 WHAT MST DOES NOT CLAIM"):
    st.write("1. That time travel is physically possible or impossible.")
    st.write("2. That it supersedes relativity or QM.")
    st.write("3. That its structure has been experimentally verified.")
    st.write("4. That paradoxes are 'solved' in a definitive sense.")
    st.caption("*MST reframes paradoxes as artifacts of orientation-based assumptions.*")

# 3. LIMITATIONS
with st.sidebar.expander("⚠️ LIMITATIONS"):
    st.write("1. MST currently lacks a full mathematical formalism.")
    st.write("2. The Möbius analogy is not yet derivable from physical law.")
    st.write("3. Connections to entropy/QM are interpretive.")
    st.caption("*These limitations are boundaries to be respected.*")

# 4. INTERACTIVE CONTROLS
st.sidebar.divider()
st.sidebar.subheader("Simulation Controls")
# This slider controls the "Current Position" of the observer
progress = st.sidebar.slider("Temporal Progress (Radians)", 0.0, float(4*np.pi), 0.0, step=0.1)

# --- MATH SECTION ---
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 20)
u, v = np.meshgrid(u, v)

# Manifold
x = (1 + v/2 * np.cos(u/2)) * np.cos(u)
y = (1 + v/2 * np.cos(u/2)) * np.sin(u)
z = v/2 * np.sin(u/2)

# Full Red Path (Reference)
t_p_full = np.linspace(0, 4 * np.pi, 200)
x_p_f = (1 + 0 * np.cos(t_p_full/2)) * np.cos(t_p_full)
y_p_f = (1 + 0 * np.cos(t_p_full/2)) * np.sin(t_p_full)
z_p_f = 0 * np.sin(t_p_full/2)

# The Active Observer (Linked to the Slider)
obs_x = (1 + 0 * np.cos(progress/2)) * np.cos(progress)
obs_y = (1 + 0 * np.cos(progress/2)) * np.sin(progress)
obs_z = 0 * np.sin(progress/2)

# --- BUILDING THE PLOT ---
fig = go.Figure()

# The Surface
fig.add_trace(go.Mesh3d(x=x.flatten(), y=y.flatten(), z=z.flatten(), opacity=0.3, color='cyan', name='MST Manifold'))

# The Static Red Path
fig.add_trace(go.Scatter3d(x=x_p_f, y=y_p_f, z=z_p_f, mode='lines', line=dict(color='red', width=2), name='Timeline'))

# The Active Observer Marker
fig.add_trace(go.Scatter3d(
    x=[obs_x], y=[obs_y], z=[obs_z],
    mode='markers+text',
    marker=dict(size=12, color='gold', symbol='diamond'),
    text=["OBSERVER"], textposition="top center",
    name='Current Observer State'
))

# Critical State Markers (Start, Flip, Return)
fig.add_trace(go.Scatter3d(
    x=[x_p_f[0], x_p_f[100], x_p_f[-1]], 
    y=[y_p_f[0], y_p_f[100], y_p_f[-1]], 
    z=[z_p_f[0], z_p_f[100], z_p_f[-1]],
    mode='markers',
    marker=dict(size=8, color=['green', 'yellow', 'blue'], opacity=0.8),
    name='Critical Coordinates'
))

fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'), margin=dict(l=0, r=0, b=0, t=0))

st.plotly_chart(fig, use_container_width=True)

# Dynamic text based on the slider
if progress == 0:
    st.info("Observer is at the Origin State (T=0). Orientation: Normal.")
elif 3.0 < progress < 3.3:
    st.warning("Observer is passing the twist. Parity inversion in progress.")
elif 6.1 < progress < 6.4:
    st.error("2π Reached: Observer is now in an INVERTED state. Paradox prevented by topological separation.")
elif progress >= 12.5:
    st.success("4π Reached: Restoration complete. Observer has returned to the original orientation.")
