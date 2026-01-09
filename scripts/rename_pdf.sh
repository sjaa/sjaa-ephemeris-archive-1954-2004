#!/bin/bash

# Find all files with .PDF extension and rename them to .pdf
find . -name "*.PDF" -type f | while read -r file; do
    # Get the new filename by replacing .PDF with .pdf
    newfile="${file%.PDF}.pdf"

    # Rename the file
    mv -v "$file" "$newfile"
done

echo "Done! All .PDF files have been renamed to .pdf"
