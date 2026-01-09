# Quick Start Guide

## Installation

The package is already installed! It provides two command-line tools:
- `pdf-extract` - Extract text from PDFs using Claude vision
- `pdf-inject` - Inject text into PDFs as searchable layer

## Setup

You'll need an Anthropic API key. Get one at https://console.anthropic.com/

Set it as an environment variable:

```bash
export ANTHROPIC_API_KEY='sk-ant-your-key-here'
```

Or add to your shell profile (~/.zshrc or ~/.bashrc):

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

## Usage

### Extract text from a single PDF

```bash
pdf-extract Seventies/7007/Eph70_07.pdf ocr-output/Eph70_07.txt
```

### Create searchable PDF

```bash
pdf-inject Seventies/7007/Eph70_07.pdf Seventies/7007/Eph70_07_searchable.pdf ocr-output/Eph70_07.txt
```

### Complete workflow

```bash
# 1. Extract text
pdf-extract input.pdf extracted.txt

# 2. Create searchable PDF
pdf-inject input.pdf searchable.pdf extracted.txt

# 3. Test it
pdftotext searchable.pdf - | head -20
```

## Batch Processing

See `examples/batch_process.py` for batch processing multiple PDFs:

```bash
cd examples
python3 batch_process.py ../Seventies/7007 ../processed
```

## Cost Estimate

- ~$0.003 per page
- 100-page document ≈ $0.30
- 1000-page archive ≈ $3.00

## Tips

1. **Test first**: Try on 1-2 PDFs before batch processing
2. **Check quality**: Compare extracted text with original
3. **Save text files**: Keep the extracted .txt files for backup
4. **File naming**: Use consistent naming (e.g., `filename_searchable.pdf`)

## Troubleshooting

### "ANTHROPIC_API_KEY not set"
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

### "Module not found"
```bash
pip3 install --break-system-packages -e /path/to/pdf-text-extractor
```

### API rate limits
If you hit rate limits, add delays in batch processing or reduce concurrency.

## What's Better Than Tesseract?

This tool produces cleaner text because:
- ✓ Handles multi-column layouts correctly
- ✓ Preserves paragraph structure
- ✓ Better with poor quality scans
- ✓ Understands tables and formatting
- ✓ No training or configuration needed

Tesseract often produces jumbled text with complex layouts like your astronomy bulletins!
