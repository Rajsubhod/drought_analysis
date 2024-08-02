# Drought Analysis Multiclass Classification

## Overview

The Drought Analysis Multiclass Classification project aims to build a machine learning model to classify drought severity based on various environmental factors. This project demonstrates the full machine learning pipeline, from data preparation and feature engineering to model training and evaluation. It also includes a web application to deploy the model for interactive predictions.

## Table of Contents

1. [Packages](#packages)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Modifying the Project](#modifying-the-project)
5. [License](#license)

## Packages

### Scikit-learn <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" alt="Scikit-learn Logo" width="50" height="15">

### Pandas <img src="https://github.com/pandas-dev/pandas/raw/main/web/pandas/static/img/pandas_mark.svg" alt="Pandas Logo" width="50" height="30">

### Flask <img src="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png" alt="Flask Logo" width="50" height="20">

## Installation

To get started with the Drought Analysis project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Rajsubhod/drought_analysis.git
   cd drought_analysis
   ```

2. **Create a Virtual Environment:**

   ```bash
   conda create -p ./.venv python=3.10
   conda activate ./.venv
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Setup Script:** (Optional)
   ```bash
   python setup.py install
   ```

## Usage

### Training the Model

    python src/models/train_model.py

### Evaluating the Model

    python src/models/predict_model.py

### Running the Application

    python app/app.py

## Modifying the Project

### Guidelines

- **Data Preparation (`data/`):** Modify `make_dataset.py` to change data loading and cleaning processes. Ensure you save cleaned data in the `data/interim/` directory.

- **Feature Engineering (`src/features/`):** Update `build_features.py` to add or modify feature engineering techniques. Ensure features are compatible with model training. After processing save it in `data/processed` directory.

- **Model Training (`src/models/`):** Modify `train_model.py` to change the model or training parameters. Update `predict_model.py` for prediction changes.

- **Web Application (`app/`):** Customize `app.py` and the templates in `templates/` for changes in the user interface or deployment behavior.

### What to Avoid

- **Do Not Modify**'<br>
  **`requirements.txt`** unless you are adding new dependencies that are critical for the project.<br>
  **`setup.py`** except adding or changing project meta data.

## License

TThis project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
