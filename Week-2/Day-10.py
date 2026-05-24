# Sunday - 10:00 AM - 2:00 PM
# Practice & Review
# n File organiser: sort files in folder by extension
# n Use os.listdir(), os.rename(), os.makedirs()
# n Git commit all Week 2 work
# n Watch '100 seconds of Python' (Fireship)
# n Review unclear topics
# n The file organiser is genuinely

# a useful tool to have, so I encourage you to try it out even if you don't feel like it. You can always start with a simple version that just prints out the files and their extensions, and then add the renaming functionality later.

import os

def organize_files_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext[1:]  # Remove the dot from the extension
            if ext:  # Only organize files with an extension
                ext_folder = os.path.join(folder_path, ext)
                if not os.path.exists(ext_folder):
                    os.makedirs(ext_folder)
                new_file_path = os.path.join(ext_folder, filename)
                os.rename(file_path, new_file_path)
                print(f"Moved: {filename} to {ext}/")
            else:
                print(f"Skipped: {filename} (no extension)")

# Example usage:
if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder to organize: ")
    organize_files_by_extension(folder_to_organize) 