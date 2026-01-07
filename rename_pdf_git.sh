#!/bin/bash

# Find all files with .PDF extension and rename them to .pdf
# Handles both git-tracked and untracked files
find . -name "*.PDF" -type f | while read -r file; do
    # Get the new filename by replacing .PDF with .pdf
    newfile="${file%.PDF}.pdf"

    # Check if file is tracked by git
    if git ls-files --error-unmatch "$file" &>/dev/null; then
        # File is tracked, use git mv
        git mv -v "$file" "$newfile"
    else
        # File not tracked, use regular mv then add
        mv -v "$file" "$newfile"
        git add "$newfile"
        echo "Renamed and added: $file -> $newfile"
    fi
done

echo "Done! All .PDF files have been renamed to .pdf"
