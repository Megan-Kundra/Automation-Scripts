import os

# === SETTINGS ===
folder_path = "test_files"  # replace with your folder path

def get_and_validate_extensions():
    def is_valid_extension(ext):
        return ext.startswith('.') and len(ext) > 1 and ext.replace('.', '').isalnum()
    while True:
            old_ext = input("Enter the current file extension (e.g., .txt) or 'q' to quit: ").strip()
            if old_ext.lower() in ['q', 'quit']:
                print("Exiting.")
                exit()
            new_ext = input("Enter the desired file extension (e.g., .md) or 'q' to quit: ").strip()
            if new_ext.lower() in ['q', 'quit']:
                print("Exiting.")
                exit()
            if is_valid_extension(old_ext) and is_valid_extension(new_ext):
                return old_ext, new_ext
            else:
                print("❌ Invalid extension(s). Extensions must start with a dot and contain only letters/numbers. Try again or enter 'q' to quit.")
def pick_new_extension(current_extention, desired_extention):
    # This function can be used to dynamically pick a new extension if needed
    return desired_extention


# === FUNCTION ===
def rename_extensions(folder, old_extension, new_extension):
    count = 0
    for filename in os.listdir(folder):
        if filename.endswith(old_extension):
            base = filename[:-len(old_extension)]
            new_filename = base + new_extension
            old_file = os.path.join(folder, filename)
            new_file = os.path.join(folder, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} → {new_filename}")
            count += 1
    print(f"\n✅ Done. {count} file(s) renamed.")

# === RUN ===
old_ext, new_ext = get_and_validate_extensions()
rename_extensions(folder_path, old_ext, new_ext)
# === END OF SCRIPT ===