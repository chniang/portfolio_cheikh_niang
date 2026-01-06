import streamlit as st
from config import PERSONAL_INFO, PROJECTS
import base64

st.set_page_config(page_title="Portfolio - Cheikh Niang", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

st.markdown("""
<script>
(function() {
    // SCROLL
    function forceScroll() {
        window.scrollTo(0, 0);
        window.scroll(0, 0);
        document.documentElement.scrollTop = 0;
        document.body.scrollTop = 0;
        const main = document.querySelector('.main');
        if (main) main.scrollTop = 0;
        const stApp = document.querySelector('.stApp');
        if (stApp) stApp.scrollTop = 0;
    }
    forceScroll();
    setTimeout(forceScroll, 10);
    setTimeout(forceScroll, 50);
    setTimeout(forceScroll, 100);
    setTimeout(forceScroll, 200);
    setTimeout(forceScroll, 400);
    setTimeout(forceScroll, 800);
    

})();
</script>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    
    * {font-family: 'Inter', sans-serif; transition: all 0.3s ease;}
    .main {background: #0A0E27; color: #E8EAED;}
    .stApp {background: #0A0E27;}
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A1F3A 0%, #0D1117 100%);
        border-right: 1px solid rgba(0, 217, 255, 0.2);
    }
    [data-testid="stSidebar"] .stMarkdown {color: #FFFFFF !important; font-size: 1.1rem !important; font-weight: 500 !important;}
    [data-testid="stSidebar"] h3 {color: #00D9FF !important; font-size: 1.3rem !important;}
    [data-testid="stSidebar"] p {color: #B8C5D6 !important; font-size: 1rem !important;}
    
    [data-testid="stSidebar"] button[kind="secondary"] {
        background: rgba(26, 31, 58, 0.4) !important;
        color: #8B9DC3 !important;
        border: 1px solid rgba(0, 217, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        font-size: 1.05rem !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] button[kind="secondary"]:hover {
        background: rgba(0, 217, 255, 0.1) !important;
        border-color: rgba(0, 217, 255, 0.3) !important;
        color: #00D9FF !important;
        transform: translateX(3px) !important;
    }
    [data-testid="stSidebar"] button[kind="primary"] {
        background: linear-gradient(135deg, #00D9FF 0%, #667EEA 100%) !important;
        border: 1px solid #00D9FF !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(0, 217, 255, 0.3) !important;
    }
    /* AMÉLIORATION SIDEBAR - Boutons plus visibles */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A1F3A 0%, #0D1117 100%);
        border-right: 1px solid rgba(0, 217, 255, 0.3) !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #00D9FF !important; 
        font-size: 1.4rem !important;
        font-weight: 800 !important;
        text-shadow: 0 0 10px rgba(0, 217, 255, 0.3);
    }
    
    [data-testid="stSidebar"] p {
        color: #E8EAED !important; 
        font-size: 1rem !important;
    }
    
    [data-testid="stSidebar"] button[kind="secondary"] {
        background: rgba(26, 31, 58, 0.6) !important;
        color: #FFFFFF !important;
        border: 2px solid rgba(0, 217, 255, 0.3) !important;
        border-radius: 12px !important;
        padding: 0.85rem 1.2rem !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] button[kind="secondary"]:hover {
        background: rgba(0, 217, 255, 0.2) !important;
        border-color: #00D9FF !important;
        color: #00D9FF !important;
        transform: translateX(5px) !important;
        box-shadow: 0 0 15px rgba(0, 217, 255, 0.3);
    }
    
    [data-testid="stSidebar"] button[kind="primary"] {
        background: linear-gradient(135deg, #00D9FF 0%, #667EEA 100%) !important;
        border: 2px solid #00D9FF !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 0.85rem 1.2rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        box-shadow: 0 5px 20px rgba(0, 217, 255, 0.4) !important;
    }
    
    [data-testid="stSidebar"] button[kind="primary"]:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 30px rgba(0, 217, 255, 0.6) !important;
    }
    
    .profile-img {width: 200px !important; height: 200px !important; border-radius: 50% !important; border: 4px solid #00D9FF !important; box-shadow: 0 10px 40px rgba(0, 217, 255, 0.4) !important; object-fit: cover !important; display: block !important; margin: 2rem auto !important;}
    .hero-name {font-size: 3.5rem; font-weight: 700; background: linear-gradient(135deg, #667EEA 0%, #00D9FF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 1rem 0; text-align: center;}
    .hero-name:hover {transform: scale(1.05);}
    .hero-title {font-size: 1.5rem; color: #B8C5D6; text-align: center; margin-bottom: 1rem;}
    .hero-title:hover {color: #00D9FF;}
    .hero-quote {font-size: 1rem; color: #8B9DC3; font-style: italic; max-width: 600px; margin: 1rem auto; text-align: center;}
    .hero-quote:hover {color: #667EEA;}
    
    .metric-card {background: #1A1F3A; padding: 1.5rem; border-radius: 12px; text-align: center; border: 1px solid rgba(0, 217, 255, 0.2); transition: all 0.3s; height: 150px; display: flex; flex-direction: column; justify-content: center;}
    .metric-card:hover {border-color: #00D9FF; transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0, 217, 255, 0.3);}
    .metric-value {font-size: 2.5rem; color: #00D9FF; font-weight: 700;}
    .metric-card:hover .metric-value {transform: scale(1.1);}
    .metric-label {font-size: 0.9rem; color: #B8C5D6; margin-top: 0.5rem;}
    .metric-card:hover .metric-label {color: #FFFFFF;}
    
    .about-card {background: #1A1F3A; padding: 2.5rem; border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2); margin: 2rem 0;}
    .about-card:hover {border-color: #00D9FF; transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0, 217, 255, 0.2);}
    .about-title {font-size: 2rem; color: #FFFFFF !important; font-weight: 800 !important; margin-bottom: 1.5rem;}
    .about-card:hover .about-title {color: #00D9FF !important;}
    .about-text {color: #B8C5D6; font-size: 1rem; line-height: 1.8; margin-bottom: 1rem;}
    .about-card:hover .about-text {color: #E8EAED;}
    
    .equal-card {background: #1A1F3A; padding: 1.5rem; border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2); height: 280px; display: flex; flex-direction: column;}
    .equal-card:hover {border-color: #00D9FF; transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0, 217, 255, 0.3);}
    .card-title {font-size: 1.5rem; color: #FFFFFF !important; font-weight: 800 !important; margin-bottom: 0.5rem;}
    .equal-card:hover .card-title {color: #00D9FF !important;}
    .card-badge {display: inline-block; background: #10B981; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.7rem; margin-left: 0.5rem;}
    .card-desc {font-size: 0.95rem; color: #B8C5D6; line-height: 1.5; margin-bottom: 1rem; flex-grow: 1;}
    .tech-pills {margin-top: auto;}
    .tech-pill {display: inline-block; background: rgba(102, 126, 234, 0.3); color: #FFFFFF; padding: 0.3rem 0.8rem; border-radius: 15px; margin: 0.2rem; font-size: 0.75rem;}
    .tech-pill:hover {background: rgba(0, 217, 255, 0.4); transform: scale(1.05);}
    
    .project-full-card {background: #1A1F3A; padding: 2rem; border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2); margin-bottom: 2rem;}
    .project-full-card:hover {border-color: #00D9FF; box-shadow: 0 10px 30px rgba(0, 217, 255, 0.2); transform: translateY(-3px);}
    .project-title-big {font-size: 2rem; color: #FFFFFF !important; font-weight: 800 !important;}
    .project-full-card:hover .project-title-big {color: #00D9FF !important;}
    
    .skill-section {background: #1A1F3A; padding: 2rem; border-radius: 15px; margin: 1.5rem 0; border-left: 4px solid #00D9FF;}
    .skill-section:hover {box-shadow: 0 8px 25px rgba(0, 217, 255, 0.2); transform: translateX(5px);}
    .skill-title {font-size: 1.5rem; color: #FFFFFF !important; font-weight: 800 !important; margin-bottom: 1rem;}
    .skill-section:hover .skill-title {color: #00D9FF !important;}
    .skill-item {background: #0A0E27; padding: 1rem; border-radius: 10px; margin: 0.8rem 0;}
    .skill-item:hover {background: #141829; transform: translateX(10px);}
    .skill-name {color: #FFFFFF !important; font-size: 1.1rem; font-weight: 800 !important; margin-bottom: 0.5rem;}
    .skill-item:hover .skill-name {color: #00D9FF !important;}
    .skill-desc {color: #B8C5D6; font-size: 0.9rem; line-height: 1.6;}
    .skill-bar {background: #1A1F3A; height: 10px; border-radius: 10px; overflow: hidden; margin: 0.5rem 0;}
    .skill-progress {background: linear-gradient(90deg, #00D9FF 0%, #667EEA 100%); height: 100%;}
    

    

    /* RESPONSIVE - Adaptation à toutes les tailles d'écran */
    * {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    
    .hero-name {
        font-size: clamp(2rem, 5vw, 3.5rem) !important;
        word-wrap: break-word !important;
    }
    
    .hero-title {
        font-size: clamp(1rem, 2.5vw, 1.5rem) !important;
    }
    
    .hero-quote {
        font-size: clamp(0.85rem, 1.5vw, 1rem) !important;
        max-width: 90% !important;
    }
    
    .metric-value {
        font-size: clamp(1.5rem, 4vw, 2.5rem) !important;
    }
    
    .metric-label {
        font-size: clamp(0.75rem, 1.2vw, 0.9rem) !important;
    }
    
    .card-title {
        font-size: clamp(1.1rem, 2vw, 1.5rem) !important;
    }
    
    .card-desc {
        font-size: clamp(0.8rem, 1.2vw, 0.95rem) !important;
    }
    
    .about-title {
        font-size: clamp(1.3rem, 3vw, 2rem) !important;
    }
    
    .about-text {
        font-size: clamp(0.85rem, 1.2vw, 1rem) !important;
    }
    
    .project-title-big {
        font-size: clamp(1.3rem, 3vw, 2rem) !important;
    }
    
    .skill-title {
        font-size: clamp(1.1rem, 2vw, 1.5rem) !important;
    }
    
    .skill-name {
        font-size: clamp(0.9rem, 1.5vw, 1.1rem) !important;
    }
    
    .skill-desc {
        font-size: clamp(0.75rem, 1.1vw, 0.9rem) !important;
    }
    
    .tech-pill {
        font-size: clamp(0.65rem, 1vw, 0.75rem) !important;
        padding: 0.2rem 0.6rem !important;
    }
    
    /* Responsive pour petits écrans */
    @media (max-width: 768px) {
        .profile-img {
            width: 150px !important;
            height: 150px !important;
        }
        
        .metric-card {
            height: auto !important;
            min-height: 120px !important;
            padding: 1rem !important;
        }
        
        .equal-card {
            height: auto !important;
            min-height: 250px !important;
        }
    }
    
    /* Zoom élevé */
    @media (min-resolution: 150dpi) {
        .hero-name, .hero-title, .hero-quote,
        .about-text, .card-desc, .skill-desc {
            line-height: 1.6 !important;
        }
    }
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "Accueil"

with st.sidebar:
    st.markdown("### 🧭 Navigation")
    st.markdown("Explorez mon portfolio Data Science")
    st.markdown("---")
    
    if st.button("🏠 Accueil", type="primary" if st.session_state.page == "Accueil" else "secondary", use_container_width=True):
        st.session_state.page = "Accueil"
        st.rerun()
    
    if st.button("👤 À propos", type="primary" if st.session_state.page == "À propos" else "secondary", use_container_width=True):
        st.session_state.page = "À propos"
        st.rerun()
    
    if st.button("💼 Projets", type="primary" if st.session_state.page == "Projets" else "secondary", use_container_width=True):
        st.session_state.page = "Projets"
        st.rerun()
    
    if st.button("🎯 Compétences", type="primary" if st.session_state.page == "Compétences" else "secondary", use_container_width=True):
        st.session_state.page = "Compétences"
        st.rerun()
    
    if st.button("📬 Contact", type="primary" if st.session_state.page == "Contact" else "secondary", use_container_width=True):
        st.session_state.page = "Contact"
        st.rerun()

if st.session_state.page == "Accueil":
    profile_img = get_image_base64("images/profile/photo.jpg")
    if profile_img:
        st.markdown(f'<img src="data:image/jpeg;base64,{profile_img}" class="profile-img" alt="Cheikh Niang">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="hero-name">{PERSONAL_INFO["nom"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-title">{PERSONAL_INFO["titre"]}</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-quote">"Transformer les données en insights actionnables"</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-value">4</div><div class="metric-label">Projets</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-value">3</div><div class="metric-label">Apps en direct</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-value">534K+</div><div class="metric-label">Données</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-value">90%</div><div class="metric-label">Précision</div></div>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<h2 style="color: #00D9FF; text-align: center; margin: 2rem 0;">🚀 Projets Récents</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i, proj in enumerate(PROJECTS[:2]):
        with col1 if i == 0 else col2:
            clean_title = proj['titre'].replace(proj['icon'], '').strip()
            tech_pills = "".join([f'<span class="tech-pill">{tech}</span>' for tech in proj['technologies'][:3]])
            st.markdown(f'<div class="equal-card"><h3 class="card-title">{proj["icon"]} {clean_title}<span class="card-badge">{proj["statut"]}</span></h3><p class="card-desc">{proj["tagline"]}</p><div class="tech-pills">{tech_pills}</div></div>', unsafe_allow_html=True)

elif st.session_state.page == "À propos":
    st.markdown('<h1 style="color: #00D9FF; text-align: center; margin-bottom: 2rem; font-weight: 800;">👤 À propos de moi</h1>', unsafe_allow_html=True)
    st.markdown('<div class="about-card"><h2 class="about-title">🎓 Parcours</h2><p class="about-text">Data Scientist Junior passionné par l\'intelligence artificielle et l\'analyse de données. Fort d\'une formation solide en Data Science et Machine Learning, je développe des solutions innovantes pour transformer les données brutes en insights actionnables.</p><p class="about-text">Mon expertise couvre l\'ensemble du pipeline data : de la collecte et nettoyage des données jusqu\'au déploiement de modèles ML en production, en passant par l\'analyse exploratoire et la visualisation interactive.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="about-card"><h2 class="about-title">💡 Domaines d\'expertise</h2><p class="about-text">🔹 <strong>Machine Learning & Deep Learning</strong> : Développement de modèles prédictifs (régression, classification), réseaux de neurones (LSTM, CNN), et ensemble methods (LightGBM, XGBoost)<br><br>🔹 <strong>Natural Language Processing</strong> : Analyse de sentiments, classification de textes, traitement automatique du langage avec TextBlob et NLTK<br><br>🔹 <strong>Data Visualization</strong> : Création de dashboards interactifs avec Streamlit et Plotly, visualisation avancée pour la prise de décision<br><br>🔹 <strong>Big Data Analytics</strong> : Manipulation de larges datasets avec Pandas, optimisation de pipelines de traitement de données</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="about-card"><h2 class="about-title">🎯 Projets réalisés</h2><p class="about-text">⚡ <strong>Prédiction des coupures d\'électricité à Dakar</strong> : Modèle ML combinant LightGBM et LSTM pour prédire les risques de coupure avec 90% de précision sur 70K observations<br><br>🎬 <strong>Système de billetterie intelligent</strong> : Application full-stack avec analytics temps réel, segmentation clients ML et prédictions de ventes<br><br>📊 <strong>Analyse de sentiments NLP</strong> : Outil d\'analyse automatique de textes avec 3 modes (simple, multiple, CSV) et visualisations interactives<br><br>🌍 <strong>Étude climatique Afrique</strong> : Analyse de 464K observations sur 43 ans pour identifier les tendances du réchauffement climatique</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="about-card"><h2 class="about-title">🌟 Ce qui me motive</h2><p class="about-text">Je suis convaincu que la Data Science peut résoudre des problèmes concrets et améliorer la vie quotidienne. Chaque projet est une opportunité d\'apprendre, d\'innover et de créer de la valeur.</p><p class="about-text">Mon objectif : développer des solutions data robustes, éthiques et accessibles qui ont un impact réel sur les organisations et les communautés.</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "Projets":
    st.markdown('<h1 style="color: #00D9FF; text-align: center; margin-bottom: 2rem; font-weight: 800;">💼 Mes Projets Data</h1>', unsafe_allow_html=True)
    phare = PROJECTS[0]
    clean_phare_title = phare['titre'].replace(phare['icon'], '').strip()
    st.markdown(f'<div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(0, 217, 255, 0.2) 100%); padding: 2rem; border-radius: 15px; border-left: 4px solid #FFD700; margin-bottom: 2rem;"><h2 style="color: #FFD700; font-size: 2rem; font-weight: 800;">⭐ Projet Phare</h2><h3 style="color: #FFFFFF; font-size: 2rem; margin: 1rem 0; font-weight: 800;">{phare["icon"]} {clean_phare_title}</h3><p style="color: #B8C5D6; font-size: 1rem; line-height: 1.6;">{phare["tagline"]}</p></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #00D9FF; font-weight: 800;">📸 Aperçu de l\'application</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for i in range(1, 5):
        img_data = get_image_base64(f"images/projects/dakar_{i}.png")
        if img_data:
            with col1 if i % 2 == 1 else col2:
                st.image(f"data:image/png;base64,{img_data}", use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-label">Ensemble de données</div><div class="metric-value">70 001</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-label">Précision</div><div class="metric-value">~90%</div></div>', unsafe_allow_html=True)
    tech_pills = "".join([f'<span class="tech-pill">{tech}</span>' for tech in phare['technologies']])
    st.markdown(f'<div style="background: #1A1F3A; padding: 1.5rem; border-radius: 15px; margin: 2rem 0;"><h3 style="color: #FFFFFF; font-weight: 800; margin-bottom: 1rem;">🛠️ Technologies</h3>{tech_pills}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("💻 Code GitHub", phare["liens"]["github"], use_container_width=True)
    with col2:
        st.link_button("🌐 Démo en direct", phare["liens"]["demo"], use_container_width=True)
    st.markdown('<h2 style="color: #00D9FF; margin: 3rem 0 2rem 0; text-align: center; font-weight: 800;">📁 Autres projets</h2>', unsafe_allow_html=True)
    for proj in PROJECTS[1:]:
        clean_title = proj['titre'].replace(proj['icon'], '').strip()
        tech_pills = "".join([f'<span class="tech-pill">{tech}</span>' for tech in proj['technologies'][:4]])
        st.markdown(f'<div class="project-full-card"><h3 class="project-title-big">{proj["icon"]} {clean_title} <span class="card-badge">{proj["statut"]}</span></h3><p style="color: #B8C5D6; font-size: 1rem;">{proj["tagline"]}</p></div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if "TidianeFlix" in proj['titre']:
            for i in range(1, 5):
                img_data = get_image_base64(f"images/projects/tidianeflix_{i}.png")
                if img_data:
                    with col1 if i % 2 == 1 else col2:
                        st.image(f"data:image/png;base64,{img_data}", use_container_width=True)
        elif "SentimentScope" in proj['titre']:
            for i in range(1, 5):
                img_data = get_image_base64(f"images/projects/sentimentscope_{i}.png")
                if img_data:
                    with col1 if i % 2 == 1 else col2:
                        st.image(f"data:image/png;base64,{img_data}", use_container_width=True)
        elif "climat" in proj['titre'].lower() or "Climate" in proj['titre']:
            for i in range(1, 5):
                img_data = get_image_base64(f"images/projects/climate_change{i}.png")
                if img_data:
                    with col1 if i % 2 == 1 else col2:
                        st.image(f"data:image/png;base64,{img_data}", use_container_width=True)
        st.markdown(f'<div style="margin: 1rem 0;">{tech_pills}</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("💻 GitHub", proj["liens"]["github"], use_container_width=True)
        if 'demo' in proj['liens']:
            with col2:
                st.link_button("🌐 Démo", proj["liens"]["demo"], use_container_width=True)
        if 'notebook' in proj['liens']:
            with col2:
                st.link_button("📓 Notebook", proj["liens"]["notebook"], use_container_width=True)

elif st.session_state.page == "Compétences":
    st.markdown('<h1 style="color: #00D9FF; text-align: center; margin-bottom: 2rem; font-weight: 800;">🎯 Stack Technique</h1>', unsafe_allow_html=True)
    st.markdown('<div class="skill-section"><h3 class="skill-title">🐍 Langages & Frameworks</h3><div class="skill-item"><div class="skill-name">Python</div><div class="skill-bar"><div class="skill-progress" style="width: 90%;"></div></div><p class="skill-desc">Pandas, NumPy, Scikit-learn, TensorFlow, Keras, Matplotlib, Seaborn, Plotly</p></div><div class="skill-item"><div class="skill-name">SQL</div><div class="skill-bar"><div class="skill-progress" style="width: 85%;"></div></div><p class="skill-desc">MySQL, SQLite, SQLAlchemy, requêtes complexes, optimisation</p></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-section"><h3 class="skill-title">🤖 Machine Learning</h3><div class="skill-item"><div class="skill-name">Supervised Learning</div><div class="skill-bar"><div class="skill-progress" style="width: 85%;"></div></div><p class="skill-desc">Régression, Classification, Random Forest, XGBoost, LightGBM</p></div><div class="skill-item"><div class="skill-name">Deep Learning</div><div class="skill-bar"><div class="skill-progress" style="width: 75%;"></div></div><p class="skill-desc">CNN, RNN, LSTM, TensorFlow/Keras, Time series forecasting</p></div><div class="skill-item"><div class="skill-name">NLP</div><div class="skill-bar"><div class="skill-progress" style="width: 75%;"></div></div><p class="skill-desc">Sentiment analysis, TextBlob, NLTK, TF-IDF, word embeddings</p></div></div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-section"><h3 class="skill-title">📊 Visualisation</h3><div class="skill-item"><div class="skill-name">Streamlit</div><div class="skill-bar"><div class="skill-progress" style="width: 90%;"></div></div><p class="skill-desc">Applications web interactives, dashboards temps réel, déploiement</p></div><div class="skill-item"><div class="skill-name">Plotly</div><div class="skill-bar"><div class="skill-progress" style="width: 85%;"></div></div><p class="skill-desc">Graphiques interactifs avancés, animations, dashboards</p></div></div>', unsafe_allow_html=True)

elif st.session_state.page == "Contact":
    st.markdown('<h1 style="color: #00D9FF; text-align: center; margin-bottom: 2rem; font-weight: 800;">📬 Me Contacter</h1>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; background: #1A1F3A; padding: 3rem; border-radius: 15px; margin: 2rem 0;"><h2 style="color: #FFFFFF; margin-bottom: 1rem; font-weight: 800;">💬 Disponible pour</h2><p style="color: #B8C5D6; font-size: 1.1rem; line-height: 2;">🔹 Postes Data Scientist / Data Analyst<br>🔹 Missions Freelance<br>🔹 Alternance / Stage<br>🔹 Collaborations ML/AI</p></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="metric-card"><div style="font-size: 3rem; margin-bottom: 1rem;">📧</div><div class="metric-label">Email</div><div style="color: #00D9FF; font-size: 1.1rem; margin-top: 0.5rem;">{PERSONAL_INFO["email"]}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><div style="font-size: 3rem; margin-bottom: 1rem;">📱</div><div class="metric-label">Téléphone</div><div style="color: #00D9FF; font-size: 1.1rem; margin-top: 0.5rem;">{PERSONAL_INFO["telephone"]}</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.link_button("💼 LinkedIn", PERSONAL_INFO["linkedin"], use_container_width=True)
    with col4:
        st.link_button("💻 GitHub", PERSONAL_INFO["github"], use_container_width=True)

st.markdown('<p style="text-align: center; color: #8B9DC3; margin-top: 4rem; padding: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.1);">© 2025 Cheikh Niang • Data Scientist Junior • Dakar, Sénégal 🇸🇳</p>', unsafe_allow_html=True)






