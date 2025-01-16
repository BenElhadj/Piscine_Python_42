# tester++.py

from load_csv import load


# test_files = [
#     "life_expectancy_years.csv",  # Valid file
#     "nonexistent_file.csv",       # File does not exist
#     "empty_file.csv",             # Empty file
#     "invalid_format.csv",         # Invalid CSV format
#     123,                          # Invalid path (not a string)
#     "corrupted_file.csv",         # Corrupted file
# ]

# for file in test_files:
#     print(f"Testing file: {file}")
#     print(load(file))
#     print("_" * 40)

print("_" * 40)
file = "life_expectancy_years.csv"
print(f"Valid file\nTesting file: {file}")
print(load(file))
print("_" * 40)
file = "nonexistent_file.csv"
print(f"File does not exist\nTesting file: {file}")
print(load(file))
print("_" * 40)
file = "empty_file.csv"
print(f"Empty file\nTesting file: {file}")
print(load(file))
print("_" * 40)
file = "invalid_format.csv"
print(f"Invalid CSV format\nTesting file: {file}")
print(load(file))
print("_" * 40)
file = 123
print(f"Invalid path (not a string)\nTesting file: {file}")
print(load(file))
print("_" * 40)
file = "corrupted_file.csv"
print(f"Corrupted file\nTesting file: {file}")
print(load(file))
print("_" * 40)
