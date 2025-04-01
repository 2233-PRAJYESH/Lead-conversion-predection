import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('synthetic_lead_data.csv')

# Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.dropna()
df['lead_score'] = df['lead_score'].fillna(df['lead_score'].mean())
df['total_time_spent'] = df['total_time_spent'].fillna(df['total_time_spent'].median())
if 'lead_source' in df.columns and not df['lead_source'].empty:
    df['lead_source'] = df['lead_source'].fillna(df['lead_source'].mode()[0])
df = df.drop_duplicates()

# Visualization with Navigation (Seamless Switching)
plt.ion()  # Interactive mode for seamless flow

def show_plots():
    plt.figure(figsize=(8, 5))
    sns.histplot(df['lead_score'], bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Lead Score')
    plt.xlabel('Lead Score')
    plt.ylabel('Count')
    plt.show()
    input("Press Enter to view the next plot...")

    plt.figure(figsize=(8, 5))
    sns.barplot(x='lead_source', y='converted', data=df, estimator=lambda x: sum(x)/len(x))
    plt.title('Conversion Rate by Lead Source')
    plt.ylabel('Conversion Rate')
    plt.xticks(rotation=45)
    plt.show()
    input("Press Enter to view the next plot...")

    plt.figure(figsize=(10, 6))
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()
    input("Press Enter to view the next plot...")

    plt.figure(figsize=(8, 5))
    sns.boxplot(x='converted', y='lead_score', data=df)
    plt.title('Lead Score vs Conversion Status')
    plt.xlabel('Converted (0 = No, 1 = Yes)')
    plt.ylabel('Lead Score')
    plt.show()

show_plots()

# Rule-Based Prediction Model
df['predicted_conversion'] = (
    (df['lead_score'] > 50) &
    (df['email_opened'] == 'Yes') &
    (df['total_time_spent'] > 100)
).astype(int)

# Model Evaluation
correct_predictions = (df['predicted_conversion'] == df['converted']).sum()
total_predictions = len(df)
accuracy = correct_predictions / total_predictions
print(f'Model Accuracy: {accuracy:.2%}')

# Display Sample Predictions
print(df[['lead_id', 'converted', 'predicted_conversion']].head(10))
