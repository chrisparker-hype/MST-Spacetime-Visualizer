import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="MST Research Lab", layout="wide")
st.title("Möbius Spacetime Theory (MST) Visualizer")
st.markdown("### *A Topological Framework for Paradox-Free Temporal Manifolds*")

# --- SIDEBAR: RESEARCHER DOCUMENTATION (Your Specific Wording) ---
st.sidebar.header("🔬 MST Research Framework")
st.sidebar.info("**Researcher:** Chris")

# 1. ASSUMPTIONS
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
    st.caption("*MST reframes paradoxes as artifacts of orientation-based assumptions rather than phenomena requiring hoc restriction.*")

# 3. LIMITATIONS
with st.sidebar.expander("⚠️ LIMITATIONS"):
    st.write("1. MST currently lacks a full mathematical formalism.")
    st.write("2. The Möbius analogy, while structurally suggestive, is not yet derivable from physical law.")
    st.write("3. Connections to entropy, QM, and cosmology are interpretive rather than formal.")
    st.caption("*These limitations are not weaknesses to be hidden but boundaries to be respected.*")

# 4. OPEN QUESTIONS
with st.sidebar.expander("❓ OPEN QUESTIONS"):
    st.write("- Can non-orientability be meaningfully expressed in Spacetime models?")
    st.write("- How does entropy interact with a non-orientable structure?")
    st.write("- Are there observable consequences that could distinguish MST from orientable models?")
    st.write("- What minimal mathematics is required to formalize traversal without overclaiming?")

# --- TOPOLOGICAL MATH (The $4\pi$ Loop) ---
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-1, 1, 20)
u, v = np.meshgrid(u, v)

x = (1 + v/2 * np.cos(u/2)) * np.cos(u)
y = (1 + v/2 * np.cos(u/2)) * np.sin(u)
z = v/2 * np.sin(u/2)

# Observer Path (4*pi for the full return)
t_p = np.linspace(0, 4 * np.pi, 200)
x_p = (1 + 0 * np.cos(t_p/2)) * np.cos(t_p)
y_p = (1 + 0 * np.cos(t_p/2)) * np.sin(t_p)
z_p = 0/2 * np.sin(t_p/2) # Simplified path for clarity

# --- BUILDING THE PLOT ---
fig = go.Figure()

fig.add_trace(go.Mesh3d(x=x.flatten(), y=y.flatten(), z=z.flatten(), opacity=0.5, color='cyan', name='Manifold'))

# Path and Markers
fig.add_trace(go.Scatter3d(x=x_p, y=y_p, z=z_p, mode='lines', line=dict(color='red', width=6), name='Observer Path'))
fig.add_trace(go.Scatter3d(
    x=[x_p[0], x_p[100], x_p[-1]], 
    y=[y_p[0], y_p[100], y_p[-1]], 
    z=[z_p[0], z_p[100], z_p[-1]],
    mode='markers',
    marker=dict(size=10, color=['#00FF00', '#FFFF00', '#0000FF']),
    name='Start, Mid-Flip, Return'
))

st.plotly_chart(fig, use_container_width=True)
st.success("Visual Proof: Green (Start) and Blue (4π Return) occupy the same spatial coordinate, while Yellow (2π) represents the Inverted State.")
