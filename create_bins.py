import pandas as pd

# Load the CSV file
csv_file_path = "filtered_entity_probabilities_statistics_BERT.csv"  # Replace with the actual file path
df = pd.read_csv(csv_file_path)

# Verify that the required columns exist
if 'average_probability' not in df.columns or 'Entity' not in df.columns:
    raise ValueError("The required columns 'average_probability' and/or 'Entity' are not present in the CSV file.")

# Create 4 bins based on the 'average_probability' column
df['bins'] = pd.qcut(df['average_probability'], q=4, labels=["Bin 1 (Lowest)", "Bin 2", "Bin 3", "Bin 4 (Highest)"])

# Select only the 'Entity', 'average_probability', and 'bins' columns
df_binned = df[['Entity', 'average_probability', 'bins']]

# Sort the DataFrame by 'average_probability' in descending order
df_binned_sorted = df_binned.sort_values(by='average_probability', ascending=False)

# Save the new CSV file with 'Entity', 'average_probability', and 'bins', sorted by 'average_probability'
output_csv_file_path = "sorted_segregated_entity_bins.csv"  # Replace with the desired output path
df_binned_sorted.to_csv(output_csv_file_path, index=False)

print(f"CSV file with 'Entity', 'average_probability', and 'bins' (sorted) has been saved at {output_csv_file_path}")
