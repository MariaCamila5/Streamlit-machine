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

/* Timeline futurista */
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
    <img src="https://i.pinimg.com/736x/3e/2b/b7/3e2bb72a4410f0deebad22f332ad9b50.jpg" alt="Hwanwoong">
    <h1>🌟 Yeo Hwanwoong</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- PESTAÑAS ----------------
tab1, tab2, tab3 = st.tabs(["🧑‍🎤 Biografía", "📅 Línea de tiempo", "📸 Galería"])

# ---------------- TAB 1 ----------------
with tab1:
    st.success("✨ *'Talento, disciplina y dedicación'* – Hwanwoong")

    st.markdown("## 🧑‍🎤 Biografía")
    st.write("""
    Yeo Hwanwoong (여환웅), conocido artísticamente como Hwanwoong, es un cantante, bailarín y rapero surcoreano, 
    nacido el 26 de agosto de 1998 en Corea del Sur. Desde joven mostró interés en la música y la danza, 
    especializándose en street dance y taekwondo (cinturón negro 4º dan). Participó en **Produce 101** en 2017 
    y debutó oficialmente como miembro de **ONEUS** el 9 de enero de 2019 con el EP *Light Us*.
    """)

    st.markdown("### 🎵 Carrera Musical")
    st.write("""
    Hwanwoong ocupa el puesto de vocalista principal, sub-rapero y principal bailarín de ONEUS. 
    Participa activamente en la composición de coreografías y lidera entrenamientos internos, 
    demostrando su compromiso con la excelencia artística.
    """)

    st.markdown("### 🎭 Trayectoria y Logros")
    st.write("""
    - Debut con ONEUS: *Light Us* (2019)  
    - Participación en múltiples álbumes y giras del grupo  
    - Reconocido por su estilo de baile fluido y expresivo  
    - Participación en programas de televisión y contenido especial para fans
    """)

    st.markdown("### 🎓 Formación y Habilidades")
    st.write("""
    Especialización en street dance y taekwondo, toca la guitarra y desarrolla liderazgo dentro del grupo.
    """)

    st.markdown("### 📱 Datos Personales")
    st.write("""
    - Apodos: Sloth, Peanut, Dachshund, Woongie  
    - Hobbies: ver películas, beber té de burbujas, comer samgyeopsal  
    - Personalidad: reservado, disciplinado y motivador  
    - MBTI: ISTP
    """)

    st.markdown("### 🎬 Momentos destacados")
    st.image("https://i.pinimg.com/1200x/78/73/d2/7873d2d731852a6225bff873746334e8.jpg", caption="Hwanwoong en escenario", use_container_width=True)
    st.video("https://www.youtube.com/watch?v=OpNTbooOSN4&list=RDOpNTbooOSN4&start_radio=1")

# ---------------- TAB 2 ----------------
with tab2:
    st.markdown("""
    <div class="timeline">
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">1998</div><p>Nace Yeo Hwanwoong el 26 de agosto en Corea del Sur.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2017</div><p>Participa en Produce 101 (temporada 2), eliminado en el episodio 8 (#42).</p></div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">2018</div><p>Entrenamiento intensivo en canto, danza y artes escénicas.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2019</div><p>Debuta oficialmente con ONEUS el 9 de enero con el EP Light Us.</p></div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">2019-2020</div><p>Participa en giras y promociones de ONEUS, destacándose por sus habilidades de baile.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2021</div><p>Contribuye en coreografías y contenidos especiales para fans.</p></div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content"><div class="year">2022</div><p>Participa en nuevas promociones y álbumes, mostrando evolución artística.</p></div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content"><div class="year">2023</div><p>Continúa actividades musicales y shows en vivo, fortaleciendo su conexión con los fans.</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- TAB 3 ----------------

with tab3:
    st.markdown("## 📸 Galería")

    # Fila 1
    col1, col2, col3 = st.columns(3)
    with col1: st.image("https://i.pinimg.com/1200x/15/5d/b6/155db6a5f3a3eef78873596d7414f9a1.jpg")
    with col2: st.image("https://i.pinimg.com/1200x/dc/37/a7/dc37a78170398a40541cd5a1a977d5a4.jpg")
    with col3: st.image("https://i.pinimg.com/736x/72/0c/30/720c305be48ed125a3016d4236374057.jpg")

    # Fila 2
    col1, col2, col3 = st.columns(3)
    with col1: st.image("https://i.pinimg.com/736x/00/9a/f1/009af1eed994dd6ac5b3f6dc046a5103.jpg")
    with col2: st.image("https://i.pinimg.com/1200x/53/bf/79/53bf792744a0f9fcaea27ebe20759313.jpg")
    with col3: st.image("https://i.pinimg.com/736x/af/1a/9a/af1a9ae1b8e25cf39601c272551ec4de.jpg")
