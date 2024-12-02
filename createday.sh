#!/opt/homebrew/bin/bash

# Prompt the user for a day number
read -p "Enter the day number (1-31): " daynumber

# Validate the input
if [[ ! $daynumber =~ ^[0-9]+$ ]] || (( daynumber < 1 || daynumber > 31 )); then
    echo "Invalid day number. Please enter a number between 1 and 31."
    exit 1
fi

# Format the day number with a leading zero if necessary
daynumber_padded=$(printf "%02d" $daynumber)

# Define the directory path
dir_path="2024/day-$daynumber_padded"

# Create the directory
mkdir -p "$dir_path"

# Copy and rename the default.py file
if [[ -f "default.py" ]]; then
    cp "default.py" "$dir_path/main.py"
    touch "$dir_path/test_input.txt"
else
    echo "default.py not found in the current directory."
    exit 1
fi

# Ensure the AOC_SESSION environment variable is set
if [[ -z "$AOC_SESSION" ]]; then
    echo "Environment variable AOC_SESSION is not set. Please set it and try again."
    exit 1
fi

# Create the input.txt file by downloading it using curl with the session cookie
input_url="https://adventofcode.com/2024/day/$daynumber/input"
curl -s -o "$dir_path/input.txt" --cookie "session=$AOC_SESSION" "$input_url"

# Check if the curl command succeeded
if [[ $? -ne 0 ]]; then
    echo "Failed to download input file from $input_url"
    exit 1
else
    echo "Setup complete for day $daynumber (directory: $dir_path)"
fi
