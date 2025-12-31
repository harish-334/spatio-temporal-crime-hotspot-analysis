# Spatio-Temporal Crime Hotspot Analysis Using Statistical Learning

This repository contains an end-to-end spatio-temporal crime analytics framework developed for large-scale crime data. The project applies statistical learning, spatial modeling, time-series forecasting, and natural language processing to predict crime hotspots, detect under-reporting, and identify behaviorally related crime incidents.

The work was completed as part of **EAS 508: Statistical Learning and Data Mining I** at the **University at Buffalo (SUNY)**.

---

## Motivation

Crime does not occur randomly across space or time. Instead, incidents cluster into hotspots, persist over time, and often spread to nearby areas. Traditional crime analysis tools rely on historical counts and static maps, which limits their ability to anticipate future risk, account for reporting bias, or identify related incidents.

This project addresses these limitations by building a unified, data-driven framework that:
- Predicts emerging crime hotspots
- Detects potential under-reporting of crime and victimization
- Links behaviorally related incidents using modern embedding techniques

---

## Datasets

The project integrates multiple datasets at different spatial and temporal resolutions:

- **NYPD Complaint Data (2022–2024)**  
  Incident-level crime data for New York City, including timestamps, offense descriptions, precincts, and geographic coordinates.

- **NIBRS (National Incident-Based Reporting System)**  
  Nationwide standardized crime data with rich incident attributes such as victim–offender relationships, weapons, property loss, and arrests.

- **New York State Crime Data**  
  County-level crime statistics used for broader regional analysis.

- **Supplementary Data**  
  Google Trends and NYC 311 service requests used as external behavioral signals.

---

## Methodology Overview

### Data Engineering
- Robust ingestion and cleaning of millions of crime records
- Timestamp normalization and coordinate validation
- Schema normalization and large-scale joins using PySpark

### Spatial Modeling
- Discretization of NYC into **500m × 500m grid cells**
- Weekly aggregation of crime counts per grid
- Continuous spatial risk modeling using **Kernel Density Estimation (KDE)**

### Temporal Feature Engineering
- Lagged crime counts (lag-1, lag-2)
- Rolling averages and short-term trends
- Seasonal and persistence indicators

### Hotspot Prediction
- Hotspots defined as the **top 10% high-crime spatial units per time window**
- **Random Forest classifier** trained on spatial, temporal, clustering, and offense features
- Probability calibration using **Platt (Sigmoid) scaling**

### Clustering Analysis
- **DBSCAN** for stable dense crime regions
- **HDBSCAN** for evolving and variable-density clusters
- Cluster persistence and transition features

### Under-Reporting Detection
- Multi-model time-series ensemble including:
  - Prophet
  - SARIMAX
  - Kalman Filter
  - Gradient Boosting models
  - LSTM
- Detection of systematic gaps between expected and observed crime and victim counts

### Crime Linkage
- Sentence-transformer embeddings (MiniLM) for offense descriptions
- Modus Operandi (MO) feature engineering
- Random Forest classifier for incident linkage
- Construction of similarity networks to identify crime series

---

## Key Results

### Hotspot Prediction (NYC Grid-Level)
- Accuracy: ~0.99
- Precision: ~0.87
- Recall: ~0.99
- F1-score (hotspots): ~0.92

### Calibration & Decision Metrics
- Brier Score: 0.0064
- Precision@5%: 0.995
- Predictive Accuracy Index (PAI@5%): 16.28

### Under-Reporting Detection
- Crime under-reporting detected in the range of **12–18%**
- Victim under-reporting estimated at **15–25%**
- Ensemble variance reduced by **22–35%**

### Crime Linkage
- Accuracy: ~0.87
- Precision: ~0.78
- Recall: ~0.72
- AUC: ~0.91

---

## Visualization & Outputs

- KDE heatmaps of spatial crime intensity
- DBSCAN and HDBSCAN hotspot clusters
- Probability-ranked hotspot maps
- Interactive Folium-based dashboards
- Poster-ready and report-ready figures

---

## Technologies & Skills

- Python, PySpark, Pandas, NumPy
- Machine Learning (Random Forest, Gradient Boosting)
- Time-Series Forecasting (Prophet, SARIMAX, LSTM)
- Geospatial Analytics (KDE, DBSCAN, HDBSCAN)
- NLP (Sentence Transformers, Text Embeddings)
- Visualization (Matplotlib, Seaborn, Folium)
- Git, GitHub, Jupyter Notebook, LaTeX

---

## Contributors

- Harish Harikrishnabhai Sondagar  
- Akaash Ramanathan Vontivillu  
- Riddhi Jaysukhbhai Vaghani  
- Sidharth Kirit Saholiya  

All team members contributed a similar amount of effort.

---

## Future Work

- Real-time data integration
- Graph-based crime network modeling
- City-to-city transfer learning
- Integration of additional socio-economic signals

---

## License

This project is intended for academic and research purposes.
