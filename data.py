import pandas as pd
import numpy as np

# Number of rows
num_rows = 1000

# Data Generation
data = {
    'lead_id': np.arange(1, num_rows + 1),
    'lead_source': np.random.choice(['Website', 'Email', 'Referral', 'Social Media', 'Cold Call'], num_rows),
    'total_time_spent': np.random.randint(1, 500, num_rows),  # Time spent in minutes
    'pages_visited': np.random.randint(1, 50, num_rows),      # Pages visited
    'email_opened': np.random.choice(['Yes', 'No'], num_rows),
    'last_activity': np.random.choice(['Clicked Ad', 'Submitted Form', 'Downloaded Brochure', 'Contacted Support'], num_rows),
    'lead_score': np.random.randint(10, 100, num_rows),       # Engagement score (0-100 scale)
    'converted': np.random.choice([0, 1], num_rows, p=[0.7, 0.3])  # 70% not converted, 30% converted
}

# Creating DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv('synthetic_lead_data.csv', index=False)

print("Dataset successfully created as 'synthetic_lead_data.csv'")
