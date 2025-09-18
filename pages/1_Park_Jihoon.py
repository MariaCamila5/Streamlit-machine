import streamlit as st

# ---------------- ESTILOS FUTURISTAS ----------------
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

/* Tabs futuristas */
.css-1avcm0n.e1fqkh3o1 button {
    background: linear-gradient(90deg, rgba(0,255,255,0.12), rgba(255,0,255,0.12));
    color: #eaf6ff;
    font-weight: bold;
    border-radius: 10px;
    padding: 6px 12px;
    transition: 0.3s;
    border: 1px solid rgba(255,255,255,0.06);
}
.css-1avcm0n.e1fqkh3o1 button:hover {
    box-shadow: 0 0 10px #00ffff, 0 0 20px #ff00ff;
}

/* Timeline moderna */
.timeline {
    position: relative;
    margin: 40px auto;
    padding: 20px 0;
    width: 90%;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    width: 4px;
    height: 100%;
    background: linear-gradient(180deg, #00ffff, #ff00ff);
    border-radius: 2px;
}
.timeline-item {
    position: relative;
    width: 50%;
    padding: 20px;
}
.timeline-item.left {
    left: 0;
    text-align: right;
}
.timeline-item.right {
    left: 50%;
    text-align: left;
}
.timeline-item::before {
    content: '';
    position: absolute;
    top: 25px;
    width: 18px;
    height: 18px;
    background: #00ffff;
    border: 3px solid #fff;
    border-radius: 50%;
    box-shadow: 0 0 12px #00ffff, 0 0 18px #ff00ff;
}
.timeline-item.left::before {
    right: -9px;
}
.timeline-item.right::before {
    left: -9px;
}
.timeline-content {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    transition: 0.3s;
}
.timeline-content:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px #00ffff, 0 0 35px #ff00ff;
}
.timeline-content .year {
    font-size: 20px;
    font-weight: bold;
    color: #00ffff;
    margin-bottom: 6px;
}
</style>

<div class="aurora"></div>
<div class="particles"></div>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="title-container">
    <img src="https://i.pinimg.com/736x/c6/a0/eb/c6a0eba58fd11a17ad61b63525773c6b.jpg" alt="Park Jihoon">
    <h1>🌟 Park Jihoon</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- PESTAÑAS ----------------
tab1, tab2, tab3 = st.tabs(["🧑‍🎤 Biografía", "📅 Línea de tiempo", "📸 Galería"])

# ---------------- TAB 1 ----------------
with tab1:
    st.success("✨ *'내 마음속에 저장 - ¡Te guardo en mi corazón!'* – Park Jihoon")
    st.markdown("## 🧑‍🎤 Biografía")
    st.write("""
    Park Ji-hoon (박지훈) es un cantante y actor surcoreano nacido el 29 de mayo de 1999 en Masan, Corea del Sur.
    Comenzó su carrera como actor infantil y modelo publicitario antes de ganar notoriedad en 2017 como subcampeón
    de Produce 101. Tras el éxito del programa, se unió a **Wanna One** (2017-2019).
    """)
    st.markdown("### 🎵 Carrera Musical")
    st.write("""
    - Debut solista: **26 marzo 2019** con *O'Clock*  
    - Firma con **YY Entertainment** en 2024  
    - Fandom: **MAY** | Colores: *Spring Bouquet*, *Lemon Tonic*, *Peach Pink*
    """)
    st.markdown("### 🎭 Carrera Actoral")
    st.write("""
    - Flower Crew: Joseon Marriage Agency (2019)  
    - Love Revolution (2020)  
    - At a Distance, Spring Is Green (2021)  
    - Weak Hero Class 1 (2022)  
    - Weak Hero Class 2 (2025)
    """)
    st.markdown("### 🎓 Educación")
    st.write("Escuela de Artes Escénicas de Seúl (2018) | Universidad Chung-Ang (Cine y Teatro)")
    st.markdown("### 📱 Redes Sociales")
    st.write("Instagram: [@0529.jihoon.ig](https://www.instagram.com/0529.jihoon.ig)")
    st.markdown("### 🎬 Momentos destacados")
    st.image("https://i.pinimg.com/736x/bc/f1/74/bcf174b6cb477d5ff953f188774eed1f.jpg", caption="Park Jihoon en concierto", use_container_width=True)
    st.video("https://www.youtube.com/watch?v=5U9_FjHELnY&list=RD5U9_FjHELnY&start_radio=1")

# ---------------- TAB 2 ----------------
with tab2:
    st.markdown("""
    <div class="timeline">
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">1999</div><p>Nace Park Jihoon en Masan, Corea del Sur.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2017</div><p>Participa en Produce 101 y debuta con Wanna One.</p></div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">2019</div><p>Debuta como solista con el álbum O'Clock.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2020</div><p>Protagoniza la serie web Love Revolution.</p></div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">2021</div><p>Actúa en At a Distance, Spring Is Green.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2022</div><p>Protagonista de Weak Hero Class 1.</p></div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">2024</div><p>Firma con YY Entertainment.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2025</div><p>Protagoniza Weak Hero Class 2.</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- TAB 3 ----------------
with tab3:
    st.markdown("## 📸 Galería")
    
    # Fila 1 - Fotos
    col1, col2, col3 = st.columns(3)
    with col1: st.image("https://i.pinimg.com/736x/29/ab/46/29ab4604df03f9c95c915be301bf9dd1.jpg")
    with col2: st.image("img/jihoon1.jpeg")
    with col3: st.image("img/bebe.jpeg")
    
    # Fila 2 - Fotos
    col1, col2, col3 = st.columns(3)
    with col1: st.image("https://i.pinimg.com/736x/37/8f/17/378f176a26d886406788d3e1132b5409.jpg")
    with col2: st.image("https://i.pinimg.com/736x/0c/ca/ec/0ccaec1d6904f12fe1c8990b6814eec6.jpg")
    with col3: st.image("https://i.pinimg.com/736x/c8/9f/57/c89f57d8ed4781616f90b3ef716e0e68.jpg")

