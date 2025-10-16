import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Angel Salazar | Portafolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ESTILOS CSS ---
st.markdown("""
<style>
    /* Estilo general */
    .stApp {
        background-color: black;
    }
    /* Estilo de la barra lateral */
    .css-1d391kg {
        background-color: #ffffff;
        border-right: 2px solid #e0e0e0;
    }
    /* Estilo de las cabeceras */
    h1, h2, h3 {
        color: #1E3A8A; /* Azul oscuro */
    }
    /* Estilo de los contenedores */
    .st-emotion-cache-183lzff {
        padding: 2rem;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("Angel Isaí Salazar")
    st.write("Full Stack Developer")
    st.markdown("---")
    st.markdown("### 📧 Contacto")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/angelisaiszr/)")
    st.write("🐙 [GitHub](https://github.com/AngelIsaiSzr)")
    st.write("💻 [CodePen](https://codepen.io/Angel-Szr)")
    st.write("📸 [Instagram](https://www.instagram.com/angel_szr1/)")
    st.markdown("---")
    st.success("¡Gracias por visitar mi portafolio!")

# --- CONTENIDO PRINCIPAL ---
st.title("Angel Isaí Salazar")
st.subheader("Full Stack Developer con más de 5 años de experiencia")

# --- SECCIÓN SOBRE MÍ ---
with st.container():
    st.header("Sobre Mí")
    st.write("""
    Soy Técnico en Programación y cuento con especializaciones en **Integridad Web, Big Data y Programación Web**. 
    Apasionado por el Desarrollo Full Stack, he dedicado más de 5 años al aprendizaje autodidacta. 
    Actualmente, busco activamente una oportunidad de empleo en el campo de la programación para 
    adquirir experiencia valiosa y fortalecer mi carrera profesional.
    """)
 
# --- HABILIDADES ---
col1, col2 = st.columns(2)

with col1:
    st.header("🛠️ Habilidades Técnicas")
    st.write("""
    - **Lenguajes:** HTML5, CSS3, JavaScript, TypeScript, Java, PHP, MySQL, Python, C, C#, C++, Kotlin y Swift.
    - **Herramientas:** Photoshop, Git y GitHub.
    """)

with col2:
    st.header("🤝 Habilidades Blandas")
    st.write("""
    - Empatía y entusiasmo.
    - Trabajo en equipo y liderazgo.
    - Comunicación asertiva.
    - Proactividad y resolución de problemas.
    """)

st.markdown("---")

# --- SECCIÓN DE PROYECTOS DESTACADOS ---
st.header("🚀 Proyectos Destacados")

# Proyecto 1: Web Code Academy
with st.expander("Web Code Academy - Academia de Programación en Línea"):
    st.write("""
    - **Descripción:** Una academia en línea con cursos gratuitos de programación y tecnología, que busca combatir el analfabetismo digital.
    - **Objetivo:** Facilitar el acceso a la educación tecnológica de calidad para todos.
    """)

# Proyecto 2: Portafolio Personal
with st.expander("Portafolio Personal - Mi Marca Digital"):
    st.write("""
    - **Descripción:** Mi portafolio personal, donde muestro mis proyectos, habilidades y formación.
    - **Tecnologías:** Desarrollado para ser una carta de presentación interactiva y profesional.
    """)

# Proyecto 3: SkillSync
with st.expander("SkillSync - App Móvil de Intercambio de Conocimientos"):
    st.write("""
    - **Descripción:** Una aplicación móvil para Android que conecta mentores y aprendices para intercambiar conocimientos.
    - **Plataforma:** Android (Kotlin/Swift).
    """)

# Proyecto 4: Salsas El Molcajete
with st.expander("Salsas El Molcajete - Página Web Culinaria"):
    st.write("""
    - **Descripción:** Una página web que muestra los sabores auténticos de la cocina mexicana, inspirada en la tradición culinaria de Veracruz.
    - **Enfoque:** Diseño web atractivo y representativo de la cultura mexicana.
    """)

# Proyecto 5: Mates
with st.expander("Mates - Herramienta Matemática Web"):
    st.write("""
    - **Descripción:** Una herramienta web con funciones matemáticas para ayudar en tareas cotidianas.
    - **Utilidad:** Simplificar cálculos y ofrecer soluciones rápidas a problemas matemáticos comunes.
    """)

st.markdown("---")
st.info("Esta página fue creada con ❤️ usando **Streamlit** en Python.")