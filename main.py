# app.py
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="K-pop Futurista",
    page_icon="🎤",
    layout="wide",
)

# --- Paths (ajusta si tus archivos están en otra carpeta) ---
ASSETS = Path("img")
AUDIO_JIHOON = ASSETS / "Jungkook_StillWithYou.mp3"  # usa tu audio; si no existe, Streamlit ignora
IMG_JIHOON = ASSETS / "img/jihoon1.jpeg"
IMG_HWAN = ASSETS / "img/Hwanwoong.jpeg"
IMG_HWAN_ALT = ASSETS / "img/Hwanwoong.jpeg"
FALLBACK_JIHOON = "https://i.pinimg.com/736x/b6/3d/30/b63d3064ee99903763dcb8a53543266e.jpg"
FALLBACK_HWAN = "https://i.pinimg.com/736x/21/8e/ed/218eedb01ea056f6e73e15bf90ecd9ed.jpg"

# --- Styles: fondo animado, neón, particles, cards, timeline, animaciones ---
st.markdown(
    """
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">

<style>
/* Reset básico */
section.main { padding: 0 3rem 3rem 3rem; }
body {
    font-family: 'Orbitron', sans-serif;
    background: linear-gradient(120deg, #07071a 0%, #0d1633 35%, #2b0047 100%);
    color: #eaf6ff;
}

/* Animated gradient overlay (aurora) */
.aurora {
    position: fixed;
    inset: 0;
    background: radial-gradient(600px 300px at 10% 20%, rgba(0,255,255,0.06), transparent 10%),
                radial-gradient(500px 250px at 80% 80%, rgba(255,0,255,0.04), transparent 12%),
                radial-gradient(700px 350px at 50% 60%, rgba(100,80,255,0.03), transparent 10%);
    pointer-events: none;
    z-index: 0;
    animation: moveAurora 20s ease-in-out infinite;
    mix-blend-mode: screen;
}
@keyframes moveAurora {
    0% { transform: translate3d(-3%,0,0) scale(1); }
    50% { transform: translate3d(3%,2%,0) scale(1.02); }
    100% { transform: translate3d(-3%,0,0) scale(1); }
}

/* Partículas (png externo ligero) */
.particles {
    position: fixed;
    inset: 0;
    background-image: url("https://i.pinimg.com/736x/ed/a5/91/eda591215d6bc2911c23d732ebd28a0f.jpg");
    background-repeat: repeat;
    opacity: 0.12;
    z-index: 0;
    animation: stars 80s linear infinite;
    pointer-events: none;
}
@keyframes stars {
    from { background-position: 0 0; }
    to { background-position: 2000px 2000px; }
}

/* Header neon */
.header-wrap {
    position: relative;
    z-index: 2;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}
.title-neon {
    font-size: 2.4rem;
    text-align: left;
    color: #ffffff;
    letter-spacing: 1px;
    text-shadow:
      0 0 6px rgba(0,255,255,0.7),
      0 0 18px rgba(255, 50, 150, 0.28),
      0 0 36px rgba(120, 80, 255, 0.18);
}
.subtitle {
    font-size: 1rem;
    color: #d7eaff;
    opacity: 0.9;
    margin-top: -6px;
}

    .card {
        width: 260px;
        height: 380px;
        perspective: 1000px;
        margin-bottom: 15px;
    }
    .card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }
    .card:hover .card-inner {
        transform: rotateY(180deg);
    }
    .card-front, .card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    }
    .card-front img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .card-back {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #fff;
        transform: rotateY(180deg);
        padding: 15px;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-back h3 {
        margin-bottom: 10px;
    }
    .card-back p {
        font-size: 14px;
    }

/* Timeline */
.timeline {
    position: relative;
    margin: 24px 0;
    padding-left: 28px;
    z-index:2;
}
.timeline::before {
    content: "";
    position: absolute;
    left: 8px;
    top: 0;
    bottom: 0;
    width: 6px;
    border-radius: 6px;
    background: linear-gradient(180deg, rgba(0,255,255,0.8), rgba(255,0,255,0.6));
    box-shadow: 0 0 18px rgba(0,255,255,0.06);
}
.event {
    position: relative;
    margin-bottom: 18px;
    padding: 12px 18px;
    background: rgba(255,255,255,0.03);
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.5);
}
.event .dot {
    position: absolute;
    left: -12px;
    top: 12px;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #ffffff, rgba(0,255,255,0.9) 10%, rgba(255,0,255,0.3));
    box-shadow: 0 0 16px rgba(0,255,255,0.25), 0 0 26px rgba(255,0,255,0.12);
    border: 2px solid rgba(255,255,255,0.06);
}

/* Fade-in animations for content blocks */
.fade-in {
    opacity: 0;
    transform: translateY(8px);
    animation: fadeUp 0.9s ease forwards;
}
.fade-in.delay-1 { animation-delay: .08s; }
.fade-in.delay-2 { animation-delay: .16s; }
.fade-in.delay-3 { animation-delay: .24s; }
@keyframes fadeUp {
    to { opacity: 1; transform: translateY(0); }
}

/* Buttons (simples) */
.btn-link {
    display:inline-flex;
    align-items:center;
    gap:8px;
    padding:8px 14px;
    border-radius: 10px;
    background: linear-gradient(90deg, rgba(0,255,255,0.12), rgba(255,0,255,0.08));
    color: #eaf6ff;
    text-decoration:none;
    border: 1px solid rgba(255,255,255,0.04);
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    font-weight:700;
}
.small-note { color: #cfeeff; font-size: 0.9rem; opacity:0.9; }

/* Responsive tweaks */
@media (max-width: 880px) {
    .cards-row { flex-direction: column; align-items:center; }
    .card-inner { height: 280px; }
}
</style>

<div class="aurora"></div>
<div class="particles"></div>
""",
    unsafe_allow_html=True,
)

# --- Header ---
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        """
        <div class="header-wrap">
            <div class="title-neon">💍Mis esposos</div>
            <div class="subtitle">Proyecto: Park Jihoon & Hwanwoongo</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    # Small side titles as user requested smaller side text
    st.markdown(
        """
        <div style="text-align:right;">
            <div style="font-size:0.9rem; color:#dbeeff; opacity:0.9;">📋 Machine Learning</div>
            <div style="font-size:0.9rem; color:#ffd9f0; opacity:0.9; margin-top:6px;">✨ Maria Camila A.R</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")


# --- Audio + Controls (una sola canción) ---
st.markdown('<div class="fade-in delay-1">', unsafe_allow_html=True)
st.write("### 🎧 Banda sonora")

# Si tienes el MP3 en tu carpeta img/
if AUDIO_JIHOON.exists():
    st.audio(str(AUDIO_JIHOON), format="audio/mp3")
else:
    # Fallback: YouTube oculto (solo audio)
    st.markdown(
        """
        <iframe width="0" height="0"
        src="https://www.youtube.com/watch?v=VuGeHsSRWwo&list=RDVuGeHsSRWwo&start_radio=1"
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)



st.markdown("---")

# --- Intro + Quotes ---
st.markdown('<div class="fade-in delay-2">', unsafe_allow_html=True)
st.markdown(
    """
    <div style="display:flex; gap:1rem; align-items:center;">
        <div style="flex:1;">
            <p style="font-size:1.05rem; color:#eaf6ff; margin:0;">
            El K-pop es un fenómeno global gracias a su mezcla de música pegadiza, coreografías 
            impresionantes y la cercanía entre artistas y fans. En este proyecto exploraremos dos 
            artistas destacados: Park Jihoon, versátil cantante y actor, y Hwanwoong, un
            talentoso bailarín y vocalista.
            </p>
        </div>
        <div style="min-width:260px; text-align:right">
            <div style="margin-bottom:8px;" class="small-note">🌌 <i>'Siempre sueña en grande y nunca te rindas.'</i> — Park Jihoon</div>
            <div class="small-note">🔥 <i>'El escenario es el lugar donde soy realmente libre.'</i> — Hwanwoong</div>
        </div>
    </div>
    """
, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- Header ---
st.subheader("👉 Elige a quién quieres conocer primero")

# Selector
opcion = st.radio(
    "Selecciona un artista:",
    ["--- Selecciona un artista ---", "Park Jihoon", "Hwanwoong - ONEUS"],
    index=0,
    horizontal=True,
)

# --- Función para flip cards ---
def render_flip_card(title, img_path, alt_img, desc, button_action=None, button_label="Ver más", key=None):
    img_src = img_path if Path(img_path).exists() else alt_img
    # Parte visual de la card
    st.markdown(
        f"""
        <div class="card">
            <div class="card-inner">
                <div class="card-front">
                    <img src="{img_src}" alt="{title}" />
                </div>
                <div class="card-back">
                    <div>
                        <h3>{title}</h3>
                        <p>{desc}</p>
                    </div>
                    <div id="button-{key}"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Botón colocado después, pero con su propio contenedor
    placeholder = st.empty()
    with placeholder.container():
        if st.button(button_label, key=f"btn-{key}"):
            st.switch_page(button_action)

# --- Render según selección ---
col_a, col_b = st.columns([1, 2])

if opcion == "Park Jihoon":
    with col_a:
        desc = "Cantante, actor y bailarín. Ex-miembro de Produce 101 / Wanna One. Solista con versatilidad y carisma."
        render_flip_card(
            "🌟 Park Jihoon",
            IMG_JIHOON,
            FALLBACK_JIHOON,
            desc,
            button_action="pages/1_Park_Jihoon.py",
            button_label="👉 Conocer a Park Jihoon",
            key="jihoon",
        )
    with col_b:
        st.write("### Sobre Park Jihoon")
        st.write(
            """
            🌟 Park Jihoon es cantante, actor y bailarín.  
            • Participó en *Produce 101*.  
            • Fue miembro de *Wanna One*.  
            • Actualmente es solista, reconocido por su versatilidad y carisma.  
            """
        )

elif opcion == "Hwanwoong - ONEUS":
    with col_a:
        desc = "Bailarín principal y vocalista de ONEUS. Energía escénica, movimientos precisos y presencia única."
        render_flip_card(
            "🌟 Hwanwoong - ONEUS",
            IMG_HWAN,
            FALLBACK_HWAN,
            desc,
            button_action="pages/2_Hwanwoong.py",
            button_label="👉 Conocer a Hwanwoong",
            key="hwanwoong",
        )
    with col_b:
        st.write("### Sobre Hwanwoong")
        st.write(
            """
            🌟 Hwanwoong es integrante de *ONEUS*.  
            • Es bailarín principal y vocalista.  
            • Destaca por su energía y estilo único, siendo uno de los miembros más queridos del grupo.  
            """
        )

else:
    with col_a:
        render_flip_card(
            "🌟 Park Jihoon",
            IMG_JIHOON,
            FALLBACK_JIHOON,
            "Cantante, actor y bailarín. Ex-miembro de Wanna One.",
            button_action="pages/1_Park_Jihoon.py",
            button_label="👉 Ver a Jihoon",
            key="jihoon-card",
        )
    with col_b:
        render_flip_card(
            "🌟 Hwanwoong - ONEUS",
            IMG_HWAN,
            FALLBACK_HWAN,
            "Bailarín principal y vocalista de ONEUS.",
            button_action="pages/2_Hwanwoong.py",
            button_label="👉 Ver a Hwanwoong",
            key="hwanwoong-card",
        )

st.markdown("---")

# --- Timeline futurista (HTML + CSS) ---
st.subheader("📅 Línea del tiempo — Momentos clave")
st.markdown(
    """
    <div class="timeline">
      <div class="event fade-in">
        <div class="dot"></div>
        <strong>2017</strong> — Park Jihoon debuta como solista tras su paso por Wanna One. Lanzamientos que mostraron su versatilidad.
      </div>

      <div class="event fade-in">
        <div class="dot"></div>
        <strong>2019</strong> — ONEUS debuta; Hwanwoong se destaca como bailarín principal y vocalista.
      </div>

      <div class="event fade-in">
        <div class="dot"></div>
        <strong>2020 - 2024</strong> — Ambos consolidan carreras con giras, premios y colaboraciones internacionales.
      </div>

      <div class="event fade-in">
        <div class="dot"></div>
        <strong>Futuro</strong> — Nuevos lanzamientos, performances visualmente cautivantes y expansión internacional.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# --- Footer pequeño con tips de estilo y navegación ---
st.markdown(
    """
    <div style="display:flex; justify-content:space-between; align-items:center; gap:12px;">
      <div style="font-size:0.95rem; color:#cfeeff;">
        Camsu - Maria Camila A.R
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- End ---
st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
