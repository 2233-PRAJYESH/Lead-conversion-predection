import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with specified encoding with specified encoding
df = pd.read_csv('SampleData.csv', encoding='latin1') 
# Step 1: Data Cleaning
# Display column names to identify correct names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')  # Normalize column names
print("Columns in dataset:", df.columns)

# Drop missing values
df = df.dropna()

# Fill missing numerical values
df['engagement_score'] = df['engagement_score'].fillna(df['engagement_score'].mean())
df['totalvisits'] = df['totalvisits'].fillna(df['totalvisits'].median())

# Fill missing categorical values
if 'lead_source' in df.columns and not df['lead_source'].empty:
    df['lead_source'] = df['lead_source'].fillna(df['lead_source'].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Check for any remaining missing values
print("Remaining missing values:\n", df.isnull().sum())

# Step 2: Exploratory Data Analysis (EDA)
plt.figure(figsize=(8, 5))
sns.histplot(df['engagement_score'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Engagement Score')
plt.xlabel('Engagement Score')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='lead_source', y='lead_stage', data=df, estimator=lambda x: sum(x == 'Qualified')/len(x))
plt.title('Conversion Rate by Lead Source')
plt.ylabel('Conversion Rate')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
numeric_cols = df.select_dtypes(include=['float64', 'int64'])  # Select numeric columns only
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='lead_stage', y='engagement_score', data=df)
plt.title('Engagement Score vs Conversion Status')
plt.xlabel('Lead Stage (Qualified / Not Interested)')
plt.ylabel('Engagement Score')
plt.show()

# Step 3: Rule-Based Prediction Model
df['predicted_conversion'] = (
    (df['engagement_score'] > 50) &
    (df['last_activity'] == 'Email Opened') &
    (df['totalvisits'] > 2)
).astype(int)

# Step 4: Model Evaluation
# Manual Accuracy Calculation
df['converted'] = (df['lead_stage'] == 'Qualified').astype(int)
correct_predictions = (df['predicted_conversion'] == df['converted']).sum()
total_predictions = len(df)
accuracy = correct_predictions / total_predictions
print(f'Model Accuracy: {accuracy:.2%}')

# Display Sample Predictions
print(df[['prospect_id', 'converted', 'predicted_conversion']].head(10))
