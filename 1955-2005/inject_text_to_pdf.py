#!/usr/bin/env python3
"""
Inject extracted text into a PDF as an invisible text layer.
This makes the PDF searchable while preserving the original image.
"""

import sys
import fitz  # PyMuPDF

def inject_text_to_pdf(input_pdf, output_pdf, text_file):
    """
    Add text layer to PDF from extracted text file.
    Text file should have page markers like "=== PAGE 1 ===" to separate pages.
    """

    # Read the text file
    with open(text_file, 'r', encoding='utf-8') as f:
        full_text = f.read()

    # Open the PDF
    doc = fitz.open(input_pdf)

    # Split text by pages (we'll add all text to each page for now)
    # For better results, the text file should have page markers
    pages_text = full_text.split('=== PAGE')

    if len(pages_text) > 1:
        # Text file has page markers
        for i, page in enumerate(doc):
            if i + 1 < len(pages_text):
                page_text = pages_text[i + 1].split('===')[0].strip()
            else:
                page_text = ""

            if page_text:
                # Add invisible text layer
                add_invisible_text(page, page_text)
    else:
        # No page markers, try to distribute text across pages
        # This is less accurate but better than nothing
        words_per_page = len(full_text.split()) // len(doc)
        words = full_text.split()

        for i, page in enumerate(doc):
            start_idx = i * words_per_page
            end_idx = (i + 1) * words_per_page if i < len(doc) - 1 else len(words)
            page_text = ' '.join(words[start_idx:end_idx])

            if page_text:
                add_invisible_text(page, page_text)

    # Save the output
    doc.save(output_pdf, garbage=4, deflate=True)
    doc.close()
    print(f"Text layer added successfully: {output_pdf}")


def add_invisible_text(page, text):
    """
    Add invisible text to a PDF page.
    The text is added as a transparent overlay for searching/copying.
    """
    rect = page.rect

    # Add text in very small font size, transparent
    # This makes it searchable but invisible
    text_writer = fitz.TextWriter(page.rect)

    # Split text into lines and position them across the page
    lines = text.split('\n')
    y_position = 50
    line_height = 12

    for line in lines:
        if line.strip():
            # Position text roughly where it might appear
            point = fitz.Point(50, y_position)
            text_writer.append(point, line, fontsize=1)  # Very small font
            y_position += line_height

            # Wrap to next column if we exceed page height
            if y_position > rect.height - 50:
                y_position = 50

    # Write the text to the page with transparency
    text_writer.write_text(page, color=(0, 0, 0), opacity=0.0)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python inject_text_to_pdf.py <input.pdf> <output.pdf> <text_file.txt>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    text_file = sys.argv[3]

    inject_text_to_pdf(input_pdf, output_pdf, text_file)
