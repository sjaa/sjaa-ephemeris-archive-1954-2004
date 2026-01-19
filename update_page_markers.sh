find . -type f -name "*.md" | while read -r f; do
  sed -E 's/=== PAGE ([0-9]+) ===/<!-- PAGE \1 -->/g' "$f" > "$f.tmp" \
    && mv "$f.tmp" "$f"
done

