# Changelog

All notable changes to the **Customer Churn Prediction System** are documented in this file.

The project follows a practical version-based development history as the system moves from machine learning experimentation toward a production-oriented ML Engineering application.

---

## [0.8.0] — Streamlit Frontend

### Added

- Streamlit frontend for interacting with the loan credit risk API.
- User input fields for:
  - Customer Age
  - Monthly Expenditure
  - Days Since Logged in
  - Customer Service Calls
  
- API request integration using `requests`.
- Prediction display.
- Probability display.

### Status

✅ Frontend integration completed.

---

## [0.7.0] — Cloud Deployment

### Added

- Dockerized FastAPI application prepared for cloud deployment.
- Cloud-compatible application startup command.
- Support for the platform-provided `PORT` environment variable.
- FastAPI configured to listen on `0.0.0.0`.

### Deployment Architecture

```text
Docker Image
     ↓
Container Registry
     ↓
Cloud Platform
     ↓
FastAPI
     ↓
Loan Credit Risk Model
```

### Status

✅ API deployment completed / deployment stage reached.

---

## [0.6.0] — Docker Containerization

### Added

- Dockerfile for the Loan Credit Risk API.
- Python 3.13 slim base image.
- Dependency installation through `requirements.txt`.
- Model files copied into the container.
- FastAPI application copied into the container.
- Port `8000` exposed.
- Uvicorn configured as the container entrypoint.
- Cloud `PORT` environment variable support.

### Docker Runtime

```text
python:3.13-slim
```

### Main Runtime Dependencies

```text
fastapi==0.141.1
uvicorn[standard]==0.52.1
pandas==2.3.3
numpy==2.3.5
scikit-learn==1.7.2
```

---

## [0.5.0] — FastAPI Model Serving

### Added

- FastAPI application for serving the trained model.
- `/predict` endpoint.
- Pydantic request validation.
- Prediction response schema.
- Model loading through Joblib.
- Probability generation through `predict_proba()`.
- API-ready model inference pipeline.

### Input Validation

Added validation for:

```text
Customer_Age
Monthly_Expenditure
Customer_Service_Calls
Days_Since_Last_Login
```

---

## [0.4.0] — Final Model Packaging

### Added

- Final trained RandomForest model saved with Joblib.
- Model saved as:

```text
CustomerChurn_Predictor.pkl
```

- Model loading tested successfully.
- Model prepared for API integration.

### Model Loader

```python
model = joblib.load("LoanModel/CustomerChurn_Predictor.pkl")
```

---

## [0.3.0] — Model Tuning & Final Evaluation

### Added

- GridSearchCV hyperparameter tuning.
- 5-fold cross-validation.
- Macro Recall optimization.
- Final unseen test evaluation.
- Feature importance analysis.

### Hyperparameters Tuned

```text
n_estimators:
    200
    300
    500

max_depth:
    3
    5
    7
    None
```

### Best Parameters

```text
n_estimators = 500
max_depth = None
```

---

## [0.2.0] — Model Comparison & Feature Analysis

### Added

Comparison of multiple classification algorithms:

- Random Forest
- Logistic Regression
- Decision Tree

### Result

Random Forest produced the strongest overall performance on the unseen test set among the models evaluated.

---

## [0.1.0] — Initial Machine Learning Pipeline

### Added

- PostgreSQL data extraction through SQLAlchemy.
- Loan credit risk dataset preparation.
- Target encoding:

```text
Stay → 0
Leave  → 1
```

- Train/test split.
- Stratified splitting.
- Validation split.
- Numerical feature detection.
- Categorical feature detection.
- Class imbalance handling using balanced sample weights.
- Numerical preprocessing with `StandardScaler`.
- Categorical preprocessing with `OneHotEncoder`.
- `ColumnTransformer` preprocessing pipeline.
- XGBoost classifier.
- Initial model evaluation.

### Dataset

The training process used up to:

```text
10,000 rows
```

---

# 🗺️ Development Roadmap

The project is progressing from a machine learning experiment toward a production-oriented ML Engineering system.

```text
[1] Data Extraction
       ↓
[2] Data Preprocessing
       ↓
[3] Model Training
       ↓
[4] Model Comparison
       ↓
[5] Hyperparameter Tuning
       ↓
[6] Final Model
       ↓
[7] Model Persistence
       ↓
[8] FastAPI
       ↓
[9] Docker
       ↓
[10] Cloud Deployment
       ↓
[11] Streamlit Frontend
       ↓
[12] Logging
       ↓
[13] Monitoring
       ↓
[14] Model Versioning
       ↓
[15] Data Drift Detection
       ↓
[16] Model Drift Detection
       ↓
[17] Automated Retraining
       ↓
[18] CI/CD
```

---

# 🚧 Upcoming

## Planned

- Complete Streamlit frontend.
- Improve API error handling.
- Add structured logging.
- Add prediction monitoring.
- Add model monitoring.
- Add data drift detection.
- Add model drift detection.
- Introduce model versioning.
- Add automated tests.
- Add CI/CD pipeline.
- Add experiment tracking.
- Build automated retraining workflow.
- Improve frontend visualization.
- Add authentication/API security.

---

# 🔐 Security Improvements

Database credentials should be moved out of source code and into environment variables.

Example:

```text
DATABASE_URL=your_database_connection_string
```

`.env` files should not be committed to GitHub.

If credentials have previously been committed to a public repository, they should be rotated.

---

# 📌 Current Status

```text
Model Training              ✅
Model Evaluation            ✅
Model Comparison            ✅
Hyperparameter Tuning       ✅
Feature Importance          ✅
Model Persistence           ✅
FastAPI                     ✅
Input Validation            ✅
Docker                      ✅
Cloud Deployment            ✅
Streamlit Frontend          ✅
Logging                     🚧
Monitoring                  🚧
Model Versioning            🚧
Data Drift Detection        🚧
Model Drift Detection       🚧
Automated Retraining        🚧
CI/CD                       🚧
```

---

## Version Summary

| Version | Milestone | Status |
|---|---|---|
| `0.1.0` | Initial ML Pipeline | ✅ |
| `0.2.0` | Model Comparison & Feature Analysis | ✅ |
| `0.3.0` | Tuning & Final Evaluation | ✅ |
| `0.4.0` | Model Packaging | ✅ |
| `0.5.0` | FastAPI Serving | ✅ |
| `0.6.0` | Docker Containerization | ✅ |
| `0.7.0` | Cloud Deployment | ✅ |
| `0.8.0` | Streamlit Frontend | ✅ |

---

## Project Direction

The long-term goal is to evolve this project from:

```text
A trained ML model
```

into:

```text
A complete production-oriented ML system
```

with:

```text
Data
 ↓
Model
 ↓
API
 ↓
Container
 ↓
Cloud
 ↓
Frontend
 ↓
Monitoring
 ↓
CI/CD
 ↓
Model Versioning
 ↓
Drift Detection
 ↓
Automated Retraining
```

