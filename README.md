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

## Article Detection, Summarization, and Embedding Generation

Once text or markdown files are generated, they can be split into articles and summarized.  This is where the [summarize-documents](https://github.com/cecomp64/summarize-documents) tool comes in.  Point it at your
generated text or markdown files, and it will split it into articles, summaries, and embeddings for semantic search.

```bash
# Generate article summaries and embeddings
document-summarizer /path/to/documents --pattern "*.md" --model-provider gemini --generate-embeddings --embedding-provider gemini --embedding-model google-embedding-001 --embedding-dimensions 768
```

Article classification will not be perfect, but it is still pretty good.  Manual review and refinement could be helpful, depending on your tolerance for noise.

## Import Into Document Archive Web App