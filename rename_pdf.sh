#!/bin/bash

# Find all files with .PDF extension and rename them to .pdf
find . -name "*.pdf" -type f | while read -r file; do
    # Get the new filename by replacing .PDF with .pdf
    newfile="${file%.pdf}.PDF"

    # Rename the file
    mv -v "$file" "$newfile"
done

echo "Done! All .PDF files have been renamed to .pdf"
