import json

# List of JSONL files you want to merge
input_files = ['bin_1.jsonl', 'bin_2.jsonl', 'bin_3.jsonl', 'bin_4.jsonl']
output_file = 'merged_output.jsonl'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    for input_file in input_files:
        # Open each input file and read it line by line
        with open(input_file, 'r') as infile:
            for line in infile:
                # Load the JSON object and write it to the output file
                outfile.write(line)
