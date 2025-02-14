import csv
import re  # Import regex module

# File paths (update as needed)
input_file = r"C:\Users\User\Downloads\PURHSTHDR.csv"
output_file = r"C:\Users\User\Downloads\PURHSTHDR_Cleaned.csv"

# Open CSV and clean headers
with open(input_file, "r", newline="", encoding="utf-8") as infile, open(output_file, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Clean header row (replace multiple spaces with a single underscore)
    headers = next(reader)
    cleaned_headers = [re.sub(r"\s+", "_", col.strip()) for col in headers]  # Fix long underscores
    writer.writerow(cleaned_headers)

    # Write the rest of the data
    for row in reader:
        writer.writerow(row)

print(f"Fixed column names and saved as {output_file}")