#  Projet house-prices-mlops

##  Objectif
Ce projet a pour objectif d'appliquer les **principes MLOps** sur un projet complet de Machine Learning, depuis l'exploration des données jusqu'au déploiement, en mettant l'accent sur la **reproductibilité**, la **collaboration** et l'**industrialisation**.

##  Sujet
Le projet consiste à développer un modèle de **régression** capable de prédire le prix de vente des maisons en fonction de leurs caractéristiques physiques, spatiales et environnementales.

### **Problématique business :**
- Aider les agents immobiliers à estimer le prix de vente des propriétés
- Identifier les facteurs qui influencent le plus le prix des maisons
- Fournir des estimations précises et transparentes

##  Jeu de données
**Source :** [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)

### **Caractéristiques du dataset :**
- ** 1,460 observations** de maisons
- ** 81 variables** descriptives
- ** Target :** `SalePrice` (prix de vente)

### **Catégories de features :**
- **Caractéristiques physiques :** Surface, nombre de pièces, année de construction
- **Qualité et état :** Évaluation globale, matériaux, finitions
- **Localisation :** Quartier, proximité des commodités
- **Équipements :** Garage, piscine, cheminée, etc.

##  Structure du projet
house-prices-mlops/
\
│
\
├──  data/ # Données
\
│ ├── raw/ # Données brutes (originales)
\
│ ├── processed/ # Données transformées
\
│ └── external/ # Données externes
\
│
\
├──  models/ # Modèles entraînés
\
│ ├── model.pkl # Modèle sérialisé
\
│ └── model_metrics.json # Métriques des modèles
\
│
\
├──  notebooks/ # Notebooks d'exploration
\
│ ├── 01_data_exploration.ipynb # Analyse exploratoire
\
│ ├── 02_feature_engineering.ipynb # Ingénierie des features
\
│ └── house_prices_poc.ipynb # Preuve de concept initiale
\
│
\
├──  src/ # Code source structuré
\
│ ├── data/ # Processing des données
\
│ │ ├── init.py
\
│ │ ├── preprocess.py
\
│ │ └── feature_engineering.py
\
│ │
\
│ ├── models/ # Entraînement des modèles
\
│ │ ├── init.py
\
│ │ ├── train.py
\
│ │ └── evaluate.py
\
│ │
\
│ └── utils/ # Utilitaires
\
│ ├── init.py
\
│ └── config.py
\
│
\
├──  tests/ # Tests unitaires
\
│ ├── test_data.py
\
│ └── test_models.py
\
│
\
├──  docs/ # Documentation
\
│ ├── methodology.md
\
│ └── results.md
\
│
\
├──  requirements.txt # Dépendances Python
\
├──  .gitignore # Fichiers ignorés par Git
\
├──  README.md # Ce fichier
\
└──  setup.py # Installation du package


##  Stack technique

### **Machine Learning :**
- ** Exploration :** Pandas, NumPy, Matplotlib, Seaborn
- ** Modèles :** Scikit-learn, XGBoost, LightGBM
- ** Évaluation :** MLflow, Weights & Biases

### **MLOps & DevOps :**
- ** Versioning :** Git, GitHub, DVC (Data Version Control)
- ** Environnements :** Docker, Conda, Virtualenv
- ** CI/CD :** GitHub Actions, MLflow Pipelines
- ** Déploiement :** FastAPI, Streamlit, Heroku/AWS

##  Workflow MLOps

### **Phase 1 : Exploration & POC** 
- [x] Notebook exploratoire
- [x] Preuve de concept (Linear Regression)
- [x] Métriques baseline

### **Phase 2 : Industrialisation** 
- [ ] Structuration du code
- [ ] Versionnement (Git + DVC)
- [ ] Pipelines modulaires
- [ ] Expérimentation tracking

### **Phase 3 : Production** 
- [ ] API de prédiction
- [ ] Monitoring
- [ ] Re-entraînement automatique

##  Équipe
- **Team Lead :** ines anane
- **ML Engineer :** zeineb ben naceur & maram jouini

##  Planning
| Phase | Durée | Statut |
|-------|--------|---------|
| Setup & Exploration | 3 jours |  **Terminé** |
| Versionnement & Structuration | 2 jours |  **En cours** |
| Pipelines & Expérimentation | 4 jours |  **À venir** |
| Déploiement & Monitoring | 3 jours |  **À venir** |

---

** "Codez comme si la personne qui maintiendra votre code était un psychopathe qui connaît votre adresse." - Martin Golding**
