import os
import re
from datetime import datetime

def batch_rename_files(directory, naming_option="skip", new_extension=None, regex_pattern=None, replacement_string=""):
    """
    Enhanced script for batch renaming files in a specified directory, featuring:

    - Flexible Naming Options: Choose between unique timestamp naming, sequential numbering, or skipping renaming.
    - Extension Changing: Optionally change file extensions for all files.
    - Advanced Pattern Replacement: Use regular expressions for specific pattern identification and replacement in filenames.

    Parameters:
    - directory: The directory containing the files to be renamed.
    - naming_option: Determines the naming convention. Options are "timestamp", "sequence", or "skip".
    - new_extension: New file extension to apply to all files. Set to None to keep the original extension.
    - regex_pattern: The regex pattern to search for in filenames for replacement.
    - replacement_string: The string to replace the matched pattern with.

    Note: The script modifies file system contents by renaming files, which is a significant action.
    Users are reminded to ensure they have the appropriate permissions for the directories they are working with and to use the script responsibly.

    Provides a versatile approach to file renaming for cleanup, organization, and systematic naming adjustments.
    """
    # Ensure the directory exists to prevent errors
    if not os.path.isdir(directory):
        print(f"The specified directory '{directory}' does not exist.")
        return

    # Ensure regex pattern is provided before compiling
    if regex_pattern:
        pattern = re.compile(regex_pattern)
    else:
        print("No regex pattern provided. Skipping pattern replacement.")
        pattern = None

    for index, filename in enumerate(os.listdir(directory), start=1):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            name, extension = os.path.splitext(filename)
            
            # Replace pattern with specified string if pattern is provided
            if pattern:
                name = pattern.sub(replacement_string, name)
            
            # Apply new naming convention based on user choice
            if naming_option == "timestamp":
                name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{index:04d}"
            elif naming_option == "sequence":
                name = f"{index:04d}"
            # Skip option does not change the name
            
            # Apply new extension if specified
            if new_extension:
                extension = new_extension
            
            new_filename = name + extension
            new_path = os.path.join(directory, new_filename)
            if new_filename != filename:
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"No changes made to '{filename}'.")

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    naming_option = input("Choose naming option (timestamp/sequence/skip): ").lower()
    new_extension_input = input("Enter new file extension (include '.', leave blank to keep original): ")
    regex_pattern = input("Enter the regex pattern to replace (leave blank to skip): ")
    replacement_string = input("Enter the replacement string (leave blank to remove the pattern): ")
    
    batch_rename_files(directory_path, naming_option=naming_option, new_extension=new_extension_input or None, regex_pattern=regex_pattern, replacement_string=replacement_string)
