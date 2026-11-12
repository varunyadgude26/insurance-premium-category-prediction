# Insurance Premium Category Prediction API

An end-to-end Machine Learning web service built with **FastAPI**, **Pydantic**, and **Scikit-learn** that predicts an individual's insurance premium category (`Low`, `Medium`, or `High`) based on demographic, lifestyle, and financial attributes.

## Overview

This project serves a trained Random Forest classification pipeline via a RESTful API. It handles raw user inputs, validates constraints, dynamically engineers health and demographic risk features on the fly, and returns real-time insurance tier predictions.

## Architecture & Project Structure

```text
├── app.py               # FastAPI application and HTTP endpoints
├── user_data.py         # Pydantic data validation and dynamic feature engineering
├── requirement.txt      # Project dependencies and pinned versions
└── model/               # Serialized ML pipeline & prediction logic
```

### Key Components

1. **Web API Layer (`app.py`)**:
   * `GET /`: Root endpoint verifying that the API service is active.
   * `GET /health`: Health check endpoint confirming system status and model readiness.
   * `POST /predict`: Core inference endpoint accepting user data and returning the predicted insurance tier.
2. **Validation & Feature Engineering (`user_data.py`)**:
   * Enforces strict input validation (e.g., age bounds, allowed occupations, normalized city strings) using Pydantic `BaseModel` and `Field` constraints.
   * Dynamically computes derived features using `@computed_field`:
     * **`bmi`**: Body Mass Index calculated as $\frac{\text{weight}}{\text{height}^2}$.
     * **`life_risk`**: Evaluates health risk (`low`, `medium`, `high`) based on smoking status and BMI thresholds.
     * **`age_group`**: Categorizes age into `young`, `adult`, `middle_aged`, or `senior`.
     * **`city_tier`**: Maps the resident city into `tier1`, `tier2`, or `tier3`.
3. **Machine Learning Pipeline**:
   * Uses a Scikit-learn `Pipeline` with a `ColumnTransformer` (`OneHotEncoder` for categorical features and `passthrough` for numerical features) feeding into a `RandomForestClassifier`.

## Getting Started

### Prerequisites

* Python 3.9+
* `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

### Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app:app --reload
```

Once running, the API will be available at `http://127.0.0.1:8000`.

* **Interactive Swagger UI Docs:** `http://127.0.0.1:8000/docs`
* **ReDoc Documentation:** `http://127.0.0.1:8000/redoc`

## API Usage Example

### Request (`POST /predict`)

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "age": 32,
           "weight": 75.0,
           "height": 1.75,
           "income_lpa": 12.5,
           "smoker": false,
           "city": "Mumbai",
           "occupation": "private_job"
         }'
```

### Response (`200 OK`)

```json
{
  "predicted_category": "Medium"
}
```

## Tech Stack

* **Framework:** FastAPI, Uvicorn
* **Data Validation:** Pydantic v2
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-learn