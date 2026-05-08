
# Projet de Fin D'année

Une entreprise de e-commerce utilise un fichier Excel pour suivre ses ventes. Le volume de
données devient trop important pour un tableur classique. Notre mission est de créer un script
Python capable d'automatiser l'analyse de ces données.




## Auteurs

- [Ikbel Jadlaoui]()
- [Yasmine Aouichi]()
- [Adam Selmane](https://github.com/AdamLMan)

# ⚙️ Travail Réalisé

Le script exécute les étapes suivantes :

## 1️⃣ Génération des données
- Création automatique du fichier `ventes.csv`

## 2️⃣ Calculs financiers
- **Chiffre d'Affaires Brut (CA Brut)**  
  CA Brut = Prix × Quantité  

- **Chiffre d'Affaires Net (CA Net)**  
  CA Net = CA Brut après remise (%)  

- **TVA (20%)**  
  TVA = 20% × CA Net  

## 3️⃣ Analyse
- Identification automatique du produit le plus rentable

## 4️⃣ Export
- Génération d’un fichier final enrichi :  
  `resultats_final.csv`

# 📌 Résultats

- 📄 Fichier traité : `resultats_final.csv`
- 📈 Indicateurs de performance calculés

  
# 🚀 Installation et Démarrage

## 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/
```

## 2️⃣ Créer un environnement virtuel
```bash
python -m venv venv
```

## 3️⃣ Activer l’environnement

### Windows
```bash
.\venv\Scripts\activate
```

### macOS / Linux
```bash
source venv/bin/activate
```

## 4️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

## Librairies
csv

random
