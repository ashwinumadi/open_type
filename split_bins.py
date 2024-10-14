import pandas as pd
import json

# Load the sorted CSV file with 'Entity' and 'bins'
csv_file_path = "sorted_segregated_entity_bins.csv"  # Replace with your actual sorted CSV file path
df_bins = pd.read_csv(csv_file_path)

# Convert the CSV 'Entity' and 'bins' columns to a dictionary for quick lookup
entity_to_bin = dict(zip(df_bins['Entity'], df_bins['bins']))

# Open the input JSONL file
input_jsonl_file = "test.jsonl"  # Replace with your actual JSONL file path

# Create output JSONL files for each bin
output_files = {
    "Bin 4 (Highest)": open("bin_4_highest.jsonl", "w"),
    "Bin 2": open("bin_2.jsonl", "w"),
    "Bin 3": open("bin_3.jsonl", "w"),
    "Bin 1 (Lowest)": open("bin_1_lowest.jsonl", "w"),
}

# Process each line in the input JSONL file
with open(input_jsonl_file, 'r') as jsonl_file:
    for line in jsonl_file:
        data = json.loads(line)
        mention_span = data.get('mention_span')
        print(mention_span)
        # Check if 'mention_span' exists in the CSV's 'Entity' column
        if mention_span in entity_to_bin:
            # Get the bin based on the CSV data
            bin_name = entity_to_bin[mention_span]
        else:
            # If no match is found, assign it to 'Bin 4 (Lowest)'
            bin_name = "Bin 1 (Lowest)"
        
        # Write the data to the corresponding bin file
        output_files[bin_name].write(json.dumps(data) + '\n')

# Close all output files
for f in output_files.values():
    f.close()

print("Data has been segregated into respective bin JSONL files, with unmatched data assigned to Bin 4 (Lowest).")
