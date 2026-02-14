# SJAA Document Archive

This repository is the official source of SJAA archival documents.  It includes metadata for each
document that helps with categorizing, sorting, and searching.  This feeds a Document Archive web
app, hosted on membership.sjaa.net.  Instructions for preparing data for upload to the web app are below.

## PDF Text Extraction, MD Conversion

Some PDF files may not have OCR'ed text.  Even those that do, are not machine-readable in the
intended sentence, paragraph, article structure of the original documents.  The [pdf-text-extractor](https://github.com/cecomp64/pdf-text-extractor) tool solves either or both of these problems.

```bash
# Generate just the markdown for PDFs that are already searchable
pdf-batch --skip-ocr --mode claude --format markdown /path/to/pdfs

# Generate both searchable PDF and markdown
pdf-batch --mode claude --format markdown /path/to/pdfs
```
