# Supply Chain Analytics – End-to-End Data Science Case Study

This repository showcases a full data analytics and data science project focused on Supply Chain Management (SCM).  
It includes real-world-inspired data cleaning, KPI calculation, visual exploration, and predictive modeling using Python.

## Project Structure

| Notebook                                | Description                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| `01_data_exploration.ipynb`             | First look at the dataset: structure, missing values, unique values, basic stats |
| `02_data_cleaning.ipynb`                | Data cleaning: handling missing values, standardizing types, fixing issues |
| `03_eda_visualization.ipynb`            | Visual EDA: analyzing cost, availability, transport, sales, and more       |
| `04_predictive_modeling.ipynb`          | Linear Regression model to predict shipping costs based on product & order data |
| `05_scm_specific_kpis.ipynb`            | Key SCM metrics like EOQ, Inventory Turnover, Lead Time analysis           |
| `06_clustering_product_profiles.ipynb`  | KMeans clustering to group products by behavior (order, lead time, cost)   |
| `07_summary_conclusions.ipynb` *(opt.)* | Summary of insights and business recommendations                           |

## Dataset

- Based on a supply chain dataset with 100+ original records  
- Augmented to 400+ realistic records with intentionally injected data quality issues
- Cleaned, analyzed, and used for training and visualization

## Key Topics Covered

### Exploration & Cleaning
- Detect missing or inconsistent entries
- Fix categorical noise, inconsistent text formats
- Fill missing values using domain logic (e.g. median, 'Unknown')

### Visualization & Analysis
- Understand relationships: availability vs. sales, defects vs. cost
- Identify outliers and operational inefficiencies (e.g. overstock)
- Visual EDA with matplotlib and seaborn

### Supply Chain KPIs
- EOQ (Economic Order Quantity)
- Inventory Turnover
- Average Lead Time
- Visual comparison of real orders vs. optimal quantities

### Predictive Modeling
- Linear Regression to estimate shipping costs
- Preprocessing with pipelines (ColumnTransformer, OneHotEncoder, StandardScaler)
- Evaluation via MAE, RMSE, R²

### Clustering Analysis
- KMeans Clustering to segment products by:
  - Order quantities  
  - Shipping costs  
  - Lead times  
  - Defect rates
- Helps identify product groups for:
  - Quality improvement  
  - Cost optimization  
  - Potential phase-out decisions

## Example Business Questions Answered

- Which products are overstocked and underselling?
- How do transport modes affect shipping costs?
- How efficient is our inventory based on turnover rates?
- Can we predict shipping costs using basic order features?
- Are there product segments with shared supply chain patterns?

## Dataset

- Based on a supply chain dataset with 100+ original records  
- Augmented to 400+ realistic records using synthetic data generation
- Additional data was created via ChatGPT with matching structure and value distributions to extend the dataset while preserving realistic patterns
- This was necessary because the original dataset was too small to support reliable modeling and segmentation
- All cleaning steps, missing value patterns, and data inconsistencies were preserved in the extended data to maintain consistency

## Tech Stack

- Python (Jupyter Notebooks)
- pandas, numpy
- matplotlib, seaborn
- scikit-learn for modeling and clustering
- faker for synthetic data generation
