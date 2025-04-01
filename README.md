# Lead Conversion Prediction

## 📌 Overview
The **Lead Conversion Prediction** project aims to analyze lead data, clean it, visualize key insights, and implement a simple rule-based prediction model to estimate the likelihood of lead conversion. This helps businesses prioritize high-potential leads and improve conversion rates.

## 📊 Features
- **Data Cleaning**: Handles missing values, removes duplicates, and normalizes column names.
- **Exploratory Data Analysis (EDA)**: Visualizes lead scores, conversion rates, and correlations.
- **Rule-Based Prediction Model**: Uses predefined conditions to estimate lead conversion likelihood.
- **Performance Evaluation**: Compares predicted conversions with actual results and calculates model accuracy.

## 🔧 Technologies Used
- **Python**
- **Pandas**
- **Seaborn & Matplotlib** (for data visualization)

## 📂 Dataset
The dataset contains the following columns:
- `lead_id`: Unique identifier for each lead.
- `lead_score`: Numerical score indicating lead potential.
- `lead_source`: Source from which the lead originated.
- `total_time_spent`: Time spent by the lead on the platform.
- `email_opened`: Whether the lead opened an email (Yes/No).
- `converted`: Whether the lead was successfully converted (1 = Yes, 0 = No).

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/lead-conversion-prediction.git
   ```
2. Navigate to the project folder:
   ```bash
   cd lead-conversion-prediction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Python script:
   ```bash
   python lead_conversion.py
   ```

## 📈 Visualization
- Histogram of **Lead Scores**
- Conversion rate by **Lead Source**
- **Correlation Heatmap** of numerical features
- **Boxplot** showing Lead Score vs. Conversion Status

## 📊 Model Logic
The rule-based model predicts conversion if:
- Lead score > 50
- Email opened = Yes
- Total time spent > 100 seconds

## 📌 Results
- **Accuracy** of the rule-based model is displayed after execution.
- Sample predictions are shown in tabular format.

## 🤝 Contributing
Feel free to contribute by improving the model, adding more visualizations, or optimizing the data pipeline.

## 📝 License
This project is licensed under the MIT License.

---
📢 **Author:** [Prajyesh Gollapalli]  
📧 Contact: [prajyeshgollapalli9@gmail.com]

