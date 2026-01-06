# Configuration du portfolio - Cheikh Niang
# Toutes les informations sont basées sur l'analyse réelle des projets

PERSONAL_INFO = {
    "nom": "Cheikh Niang",
    "titre": "Data Scientist / Analyst",
    "email": "cheikhniang159@gmail.com",
    "telephone": "+221 77 636 27 14",
    "linkedin": "https://www.linkedin.com/in/cheikh-niang-5370091b5/",
    "github": "https://github.com/chniang",
    "localisation": "Dakar, Sénégal"
}

PROJECTS = [
    {
        "icon": "⚡",
        "titre": "⚡ Prédiction de puissance à Dakar",
        "tagline": "Prédiction des coupures d'électricité à Dakar",
        "description": "Application ML de prédiction des risques de coupures d'électricité dans les quartiers de Dakar basée sur les conditions météorologiques et la consommation énergétique.",
        "statut": "Déployé",
        "technologies": ["Python", "LightGBM", "TensorFlow", "Streamlit", "Plotly", "Scikit-learn", "Pandas"],
        "metriques": {
            "Dataset": "70,001 obs",
            "Quartiers": "8",
            "Précision LightGBM": "88%",
            "Précision LSTM": "90%"
        },
        "details": {
            "dataset_size": "4.69 MB",
            "code_lines": "1,426 lignes",
            "models": ["LightGBM (266 KB)", "LSTM (Keras)", "StandardScaler"],
            "features": [
                "Prédiction temps réel avec paramètres météo",
                "Carte interactive Dakar (8 quartiers)",
                "Statistiques et tendances par quartier",
                "Export CSV des prédictions",
                "Jauge de risque visuelle"
            ],
            "ml_approach": "Ensemble de LightGBM et LSTM avec moyenne pondérée"
        },
        "liens": {
            "github": "https://github.com/chniang/dakar-power-prediction.git",
            "demo": "https://dakar-power-prediction-bzt6vmueywrgumdwjukj5p.streamlit.app/"
        }
    },
    {
        "icon": "🎬",
        "titre": "🎬 TidianeFlix",
        "tagline": "Système de billetterie cinéma avec Analytics & ML",
        "description": "Application full-stack de gestion de billetterie pour cinéma avec analytics avancés, prédictions ML et segmentation clients. Interface style Netflix.",
        "statut": "Déployé",
        "technologies": ["Streamlit", "SQLite", "SQLAlchemy", "Pandas", "Plotly", "Scikit-learn"],
        "metriques": {
            "Revenu total": "109K FCFA",
            "Tickets vendus": "34",
            "Prix moyen": "3,406 FCFA",
            "Clients": "20"
        },
        "details": {
            "database": "SQLite (32 KB)",
            "tables": "5 tables relationnelles",
            "code_lines": "2,428 lignes",
            "data": {
                "films": "15 (Inception, Titanic, Avengers...)",
                "salles": "3 (capacité totale 350 places)",
                "projections": "20",
                "clients": "20",
                "tickets": "34"
            },
            "features": [
                "KPIs financiers temps réel",
                "Segmentation clients (VIP ≥10K, Fidèle ≥5K, Occasionnel)",
                "Prédiction ventes (régression linéaire, 7 jours)",
                "Scoring probabilité réachat",
                "Recommandations films par genre",
                "Dashboard interactif Plotly"
            ],
            "ml_models": ["Régression linéaire (prédiction)", "Scoring RFM personnalisé", "Content-based filtering"]
        },
        "liens": {
            "github": "https://github.com/chniang/TIDIANE_FLIX.git",
            "demo": "https://chniang-tidiane-flix-app-complete-cvsmk3.streamlit.app/"
        }
    },
    {
        "icon": "📊",
        "titre": "📊 SentimentScope",
        "tagline": "Analyse de sentiments NLP avec TextBlob",
        "description": "Application d'analyse de sentiments utilisant le Natural Language Processing pour classifier automatiquement des textes selon leur tonalité émotionnelle (Positif/Négatif/Neutre).",
        "statut": "Déployé",
        "technologies": ["Streamlit", "TextBlob", "NLTK", "Plotly", "WordCloud", "Pandas", "Scikit-learn"],
        "metriques": {
            "Modes d'analyse": "3",
            "Métriques NLP": "2",
            "Classifications": "3",
            "Visualisations": "4"
        },
        "details": {
            "code_lines": "341 lignes",
            "nlp_engine": "TextBlob 0.18.0",
            "features": [
                "Analyse texte simple (polarité + subjectivité)",
                "Analyse multiple (2-10 textes simultanés)",
                "Upload CSV (analyse en masse)",
                "Graphiques interactifs (camembert, barres)",
                "Word Cloud des sentiments",
                "Export résultats CSV"
            ],
            "metrics": {
                "Polarité": "Score -1 (négatif) à +1 (positif)",
                "Subjectivité": "Score 0 (objectif) à 1 (subjectif)",
                "Seuils": "Positif >0.1, Neutre -0.1 à +0.1, Négatif <-0.1"
            },
            "use_cases": ["E-commerce (avis clients)", "Service client (tickets)", "Réseaux sociaux", "Marketing (réputation)"]
        },
        "liens": {
            "github": "https://github.com/chniang/sentiment-analysis-nlp.git",
            "demo": "https://sentiment-analysis-nlpgit-7qwekuqxgvgtipzuqb4m9a.streamlit.app/"
        }
    },
    {
        "icon": "🌍",
        "titre": "🌍 Analyse du climat africain",
        "tagline": "Analyse climatique 1980-2023",
        "description": "Étude approfondie du changement climatique en Afrique sur 43 ans (1980-2023) avec visualisations scientifiques et rapport PDF complet. Analyse de 5 pays africains.",
        "statut": "Complet",
        "technologies": ["Python", "Jupyter", "Pandas", "Plotly", "Matplotlib", "NumPy"],
        "metriques": {
            "Observations": "464,815",
            "Période": "43 ans",
            "Pays analysés": "5",
            "Réchauffement": "+1.51°F"
        },
        "details": {
            "dataset": "Africa_climate_change.csv (18.5 MB)",
            "period": "1980-2023 (43 ans)",
            "code_lines": "352 lignes",
            "countries": {
                "Cameroun": "+2.63°F (le plus touché)",
                "Tunisie": "+1.71°F",
                "Angola": "+1.69°F",
                "Égypte": "+1.06°F",
                "Sénégal": "+0.45°F"
            },
            "variables": ["DATE", "PRCP (précipitation)", "TAVG", "TMAX", "TMIN", "COUNTRY"],
            "deliverables": [
                "Notebook Jupyter complet",
                "Rapport PDF (Rapport_Climat_Afrique_20251230.pdf)",
                "5 visualisations PNG scientifiques",
                "Scripts automatisés (generate_visualizations.py, generate_report.py)"
            ],
            "visualizations": [
                "Évolution températures moyennes",
                "Comparaison avant/après 2000",
                "Heatmap températures",
                "Distribution températures",
                "Augmentation par pays"
            ]
        },
        "liens": {
            "github": "https://github.com/chniang/Africa_climate_change_visualisation.git",
            "notebook": "https://github.com/chniang/Africa_climate_change_visualisation/blob/main/climate_analysis.ipynb"
        }
    }
]
