import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------- Datos ----------------
data = {
    "Artista": ["Park Jihoon", "Hwanwoong"],
    "Edad": [24, 25],
    "Debut": [2017, 2019],
    "Anios_Carrera": [6, 4],
    "Num_Canciones": [25, 20],
    "Fans_millones": [2.5, 1.8]
}
df = pd.DataFrame(data)

# ---------------- Estilos Futuristas ----------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">

<style>
body {
    font-family: 'Orbitron', sans-serif;
    background: linear-gradient(120deg, #07071a 0%, #0d1633 35%, #2b0047 100%);
    color: #eaf6ff;
}

/* Aurora + partículas */
.aurora {
    position: fixed;
    inset: 0;
    background: radial-gradient(600px 300px at 10% 20%, rgba(0,255,255,0.05), transparent 10%),
                radial-gradient(500px 250px at 80% 80%, rgba(255,0,255,0.04), transparent 12%),
                radial-gradient(700px 350px at 50% 60%, rgba(100,80,255,0.03), transparent 10%);
    pointer-events: none;
    z-index: 0;
    animation: moveAurora 18s ease-in-out infinite;
    mix-blend-mode: screen;
}
@keyframes moveAurora {
    0% { transform: translate3d(-3%,0,0) scale(1); }
    50% { transform: translate3d(3%,2%,0) scale(1.02); }
    100% { transform: translate3d(-3%,0,0) scale(1); }
}
.particles {
    position: fixed;
    inset: 0;
    background-image: url("https://i.pinimg.com/736x/ed/a5/91/eda591215d6bc2911c23d732ebd28a0f.jpg");
    background-repeat: repeat;
    opacity: 0.12;
    z-index: 0;
    animation: stars 100s linear infinite;
    pointer-events: none;
}
@keyframes stars {
    from { background-position: 0 0; }
    to { background-position: 2000px 2000px; }
}

/* Header futurista con glow */
.title-container {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 20px;
    font-weight: bold;
}
.title-container img {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #00ffff;
    box-shadow: 0 0 12px #00ffff, 0 0 24px #ff00ff;
}
.title-container h1 {
    font-size: 2.2rem;
    color: #ffffff;
    text-shadow: 0 0 8px rgba(0,255,255,0.7),
                 0 0 18px rgba(255,0,255,0.4);
}

/* Tabla estilo neón */
[data-testid="stDataFrame"] {
    border: 2px solid #00ffff !important;
    border-radius: 10px;
}

/* Hover filas */
tbody tr:hover {
    background-color: rgba(255,255,255,0.1) !important;
}

/* Selectbox estilo futurista */
.css-1cpxqw2.e1tzin5v1 {
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
    border: 2px solid #ff00ff !important;
    border-radius: 12px;
    font-weight: bold;
}
</style>

<div class="aurora"></div>
<div class="particles"></div>
""", unsafe_allow_html=True)

# ---------------- Título con diseño futurista ----------------
st.markdown("""
<div class="title-container">
    <h1>🎤 Comparativa Futurista: Park Jihoon vs Hwanwoong</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("✨ Explora estadísticas y gráficas interactivas de estos dos artistas del K-pop ✨")

# ---------------- Tabla ----------------
st.markdown("## 📊 Tabla Comparativa")
st.dataframe(df.style.set_properties(**{
    'background-color': '#111122',
    'color': 'white',
    'border-color': '#00ffff'
}).set_table_styles([{
    'selector': 'th',
    'props': [('background-color', '#00ffff'), ('color', 'black')]
}]))

# ---------------- Selector de Gráfica ----------------
st.markdown("## 🎨 Selecciona una gráfica")
opciones = ["Años de Carrera", "Fans (millones)", "Canciones vs Carrera"]
grafica_seleccionada = st.selectbox("Ir a gráfica:", opciones)

# ---------------- Mostrar gráfica ----------------
if grafica_seleccionada == "Años de Carrera":
    fig = px.bar(df, x="Artista", y="Anios_Carrera", 
                 color="Artista", color_discrete_sequence=["#00ffff","#ff00ff"],
                 text="Anios_Carrera")
    fig.update_layout(title="🎵 Años de Carrera", 
                      plot_bgcolor='#111122', paper_bgcolor='#111122',
                      font_color="white")
    st.plotly_chart(fig, use_container_width=True)
    st.info("💡 Park Jihoon ha tenido una carrera ligeramente más larga que Hwanwoong, reflejado en sus años activos.")

elif grafica_seleccionada == "Fans (millones)":
    fig = px.pie(df, values="Fans_millones", names="Artista",
                 color="Artista", color_discrete_sequence=["#00ffff","#ff00ff"])
    fig.update_layout(title="🎵 Distribución de Fans (millones)",
                      plot_bgcolor='#111122', paper_bgcolor='#111122',
                      font_color="white")
    st.plotly_chart(fig, use_container_width=True)
    st.info("💡 Park Jihoon tiene una base de fans ligeramente mayor que Hwanwoong, representando un 58% frente al 42% de Hwanwoong.")

elif grafica_seleccionada == "Canciones vs Carrera":
    fig = px.scatter(df, x="Anios_Carrera", y="Num_Canciones", 
                     color="Artista", size="Num_Canciones",
                     color_discrete_sequence=["#00ffff","#ff00ff"],
                     text="Artista")
    fig.update_traces(textposition='top center')
    fig.update_layout(title="🎵 Canciones vs Años de Carrera",
                      xaxis_title="Años de Carrera",
                      yaxis_title="Número de Canciones",
                      plot_bgcolor='#111122', paper_bgcolor='#111122',
                      font_color="white")
    st.plotly_chart(fig, use_container_width=True)
    st.info("💡 Aunque Park Jihoon tiene más años de carrera, la diferencia en número de canciones no es tan grande, mostrando que Hwanwoong también ha sido productivo.")
