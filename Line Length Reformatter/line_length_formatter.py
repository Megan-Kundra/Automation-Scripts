import os
import re

def wrap_text_line(line, max_length=100):
    words = line.split(' ')
    wrapped_lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + (1 if current_line else 0) > max_length:
            if current_line:
                wrapped_lines.append(current_line)
                current_line = ""

            while len(word) > max_length:
                wrapped_lines.append(word[:max_length])
                word = word[max_length:]

            current_line = word
        else:
            current_line += (" " if current_line else "") + word

    if current_line:
        wrapped_lines.append(current_line)

    return wrapped_lines

def reformat_file(input_file, output_file, max_length=100):
    i = 0  # Initialize line counter

    # Always read all lines first
    with open(input_file, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()

    with open(output_file, 'w', encoding='utf-8') as fout:
        for i, line in enumerate(lines, 1):
            line = line.rstrip('\n')
            if not line.strip():
                fout.write('\n')
                continue
            try:
                wrapped = wrap_text_line(line, max_length)
                for wline in wrapped:
                    fout.write(wline + '\n')
            except Exception as e:
                print(f"Error processing line {i}: {e}")
                fout.write(line + '\n')
            if i % 100 == 0:
                print(f"Processed {i} lines...")

    print(f"✅ Done processing {i} lines. Output saved to {output_file}")

if __name__ == "__main__":
    while True:
        input_path = input("Enter the path to the file you want to reformat (e.g., README.txt) or 'q' to quit: ").strip()
        if input_path.lower() in ['q', 'quit']:
            print("Exiting.")
            exit()
        if not os.path.isfile(input_path):
            print(f"❌ File '{input_path}' does not exist. Please try again or enter 'q' to quit.")
            continue
        break

    # Ask user for line length
    while True:
        max_cols_input = input("Enter the maximum line length (press Enter for default 100): ").strip()
        if not max_cols_input:
            max_cols = 100
            break
        if max_cols_input.isdigit() and int(max_cols_input) > 0:
            max_cols = int(max_cols_input)
            break
        print("Please enter a positive integer or press Enter for the default.")

    print("Do you want to overwrite the original file or save to a new file?")
    print("1. Overwrite original")
    print("2. Save to new file")
    while True:
        choice = input("Enter 1 or 2 (or 'q' to quit): ").strip()
        if choice.lower() in ['q', 'quit']:
            print("Exiting.")
            exit()
        if choice in ["1", "2"]:
            break
        print("Invalid choice. Please enter 1, 2, or 'q' to quit.")

    if choice == "1":
        output_path = input_path
    else:
        invalid_chars = r'[<>:"/\\|?*]'
        while True:
            output_path = input("Enter the output file name (e.g., output.txt) or 'q' to quit: ").strip()
            if output_path.lower() in ['q', 'quit']:
                print("Exiting.")
                exit()
            if not output_path:
                print("Output file name cannot be empty. Try again or enter 'q' to quit.")
                continue
            if re.search(invalid_chars, output_path):
                print("❌ Invalid file name. File names cannot contain any of the following characters: <>:\"/\\|?*")
                continue
            break

    reformat_file(input_path, output_path, max_cols)
