import pandas as pd
import os

# Path to the original large CSV file
original_file_path = "data/creditcard_2023.csv"

# Load the original CSV file
df = pd.read_csv(original_file_path)

# Split into a smaller chunk (for example, 100,000 rows per chunk)
chunk_size = 100000  # Number of rows per chunk
chunk_prefix = "creditcard_chunk_"  # Prefix for chunk files

# Generate the chunk and save it as a temporary chunk file
for i in range(0, len(df), chunk_size):
    chunk = df[i:i + chunk_size]
    chunk_filename = f"data/{chunk_prefix}{i // chunk_size + 1}.csv"
    chunk.to_csv(chunk_filename, index=False)

    print(f"Created chunk: {chunk_filename}")

# Check if the renamed original file already exists, and delete it if it does
renamed_file_path = "data/creditcard_2023.csv"
if os.path.exists(renamed_file_path):
    os.remove(renamed_file_path)
    print(f"Deleted the existing file: {renamed_file_path}")

# Now rename the first chunk file to match the original file name
first_chunk_filename = f"data/{chunk_prefix}1.csv"

# Rename the first chunk file to original file name
os.rename(first_chunk_filename, renamed_file_path)
print(f"Renamed the first chunk to: {renamed_file_path}")

# Delete the remaining chunk files (if any)
for i in range(2, len(df) // chunk_size + 2):
    chunk_file = f"data/{chunk_prefix}{i}.csv"
    if os.path.exists(chunk_file):
        os.remove(chunk_file)
        print(f"Deleted extra chunk file: {chunk_file}")

print("Chunking and renaming process completed.")
