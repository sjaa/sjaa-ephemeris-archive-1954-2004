#!/usr/bin/env python3
"""
Vision-based PDF text extractor using Claude's multimodal capabilities.
Extracts clean text from scanned PDFs by having Claude "read" each page.
"""

import sys
import os
import base64
import json
from anthropic import Anthropic
import fitz  # PyMuPDF

def pdf_to_images(pdf_path):
    """Convert PDF pages to base64-encoded images."""
    doc = fitz.open(pdf_path)
    images = []

    for page_num in range(len(doc)):
        page = doc[page_num]

        # Render page to image (PNG)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better quality
        img_data = pix.pil_tobytes(format="PNG")

        # Encode to base64
        img_base64 = base64.b64encode(img_data).decode('utf-8')
        images.append(img_base64)

    doc.close()
    return images


def extract_text_from_page(client, image_base64, page_num):
    """Use Claude to extract text from a single page image."""

    prompt = """Please extract all the text from this scanned document page.

Rules:
- Preserve the original formatting as much as possible
- Maintain paragraph breaks and line breaks
- Include all text exactly as it appears
- Do not add any commentary or explanations
- Just output the raw text content

Text:"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",  # Use latest Sonnet with vision
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": image_base64
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )

        # Extract text from response
        text = message.content[0].text

        # Clean up any "Text:" prefix if Claude added it
        if text.startswith("Text:"):
            text = text[5:].strip()

        return text

    except Exception as e:
        print(f"Error extracting text from page {page_num + 1}: {e}", file=sys.stderr)
        return f"[Error extracting page {page_num + 1}]"


def extract_pdf_text(pdf_path, output_path, api_key=None):
    """
    Extract text from PDF using Claude's vision capabilities.
    """

    # Get API key
    if api_key is None:
        api_key = os.environ.get('ANTHROPIC_API_KEY')

    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set", file=sys.stderr)
        print("Set it with: export ANTHROPIC_API_KEY='your-key-here'", file=sys.stderr)
        sys.exit(1)

    # Initialize Claude client
    client = Anthropic(api_key=api_key)

    print(f"Converting PDF to images: {pdf_path}")
    images = pdf_to_images(pdf_path)

    print(f"Extracting text from {len(images)} pages using Claude vision...")

    all_text = []

    for i, img_base64 in enumerate(images):
        print(f"  Processing page {i + 1}/{len(images)}...", end=' ', flush=True)

        text = extract_text_from_page(client, img_base64, i)
        all_text.append(f"=== PAGE {i + 1} ===\n{text}")

        print("✓")

    # Write output
    output_text = "\n\n".join(all_text)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_text)

    print(f"\nText extracted successfully: {output_path}")
    print(f"Total pages: {len(images)}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_pdf_text.py <input.pdf> <output.txt> [api_key]")
        print()
        print("Extracts text from scanned PDFs using Claude's vision capabilities.")
        print("Requires ANTHROPIC_API_KEY environment variable or pass as 3rd argument.")
        print()
        print("Example:")
        print("  export ANTHROPIC_API_KEY='your-key-here'")
        print("  python extract_pdf_text.py scan.pdf output.txt")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_txt = sys.argv[2]
    api_key = sys.argv[3] if len(sys.argv) > 3 else None

    if not os.path.exists(input_pdf):
        print(f"Error: Input file not found: {input_pdf}", file=sys.stderr)
        sys.exit(1)

    extract_pdf_text(input_pdf, output_txt, api_key)


if __name__ == '__main__':
    main()
