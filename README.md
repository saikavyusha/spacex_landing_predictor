# 🚀 SpaceX Falcon 9 Launch Predictor

This project aims to **predict the success of Falcon 9 first stage landings** using real-world SpaceX data. The project applies data collection, wrangling, exploratory analysis, interactive dashboards, and machine learning models to analyze and predict landing outcomes.

---

## 📦 Project Structure


---

## 🔍 Key Questions Explored

- How do variables like **payload mass**, **launch site**, and **orbit type** affect landing success?
- How has the **landing success rate changed over time**?
- What is the **best ML model** to predict a successful landing?

---

## 🧪 Assignments Overview

### ✅ Assignment 1 & 2: Data Collection  
- REST API: [`spacexdata.com`](https://api.spacexdata.com/v4/launches)
- Web Scraping: Wikipedia Falcon 9 launch history

### ✅ Assignment 3: Data Wrangling  
- Standardized column names  
- Handled missing values  
- Applied one-hot encoding for categorical columns  

### ✅ Assignment 4 & 5: EDA & Visuals  
- SQL queries using DuckDB (launch count, avg payload, landing rate)  
- Visualizations: bar plots, pie charts, scatter plots

### ✅ Assignment 6 & 7: Interactive Analytics  
- Folium maps: visualize launch locations  
- Dash dashboard: dynamic graphs for site-wise outcomes

### ✅ Assignment 8: Classification Models  
- Models: Logistic Regression, Random Forest, Support Vector Machine  
- **Best accuracy:** ~93% with Logistic Regression and SVM  
- Evaluated with accuracy, F1 score, and ROC AUC

---

## 📊 Model Performance Snapshot

| Model                | Accuracy | ROC AUC |
|---------------------|----------|---------|
| Logistic Regression | 92.8%    | 0.98    |
| SVM                 | 92.8%    | 0.85    |
| Random Forest       | 89.2%    | 0.58    |

---

## 🛠️ Tech Stack

- **Python** (pandas, sklearn, plotly, dash, folium)
- **DuckDB** (for SQL-based EDA)
- **scikit-learn** (for modeling and evaluation)
- **Jupyter/VS Code** for development

---

## 📍 Usage

1. Clone the repo  
2. Activate virtual environment  
3. Run each script step-by-step (or follow assignments)
4. Launch dashboard:  
   ```bash
   python assignment7_plotlydash.py
