"""Extract images from PDF using pymupdf (fitz).

Usage:
    python pdf_images.py <pdf_path> -o <output_dir> [--pages 10-15]

Requirements:
    pip install pymupdf
"""
import argparse
import os
import sys


def extract_images(pdf_path, output_dir, pages=None):
    """Extract embedded images from PDF.

    Args:
        pdf_path: Path to PDF file.
        output_dir: Directory to save extracted images.
        pages: Optional page range (0-indexed list). None = all pages.
    """
    import fitz

    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)

    target_pages = pages if pages is not None else range(len(doc))
    img_count = 0

    for page_num in target_pages:
        if page_num < 0 or page_num >= len(doc):
            continue
        page = doc[page_num]
        images = page.get_images(full=True)
        for img_idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            img_count += 1
            fname = f"page{page_num + 1}_img{img_idx + 1}.{ext}"
            with open(os.path.join(output_dir, fname), "wb") as f:
                f.write(image_bytes)
            print(f"Saved: {fname} ({len(image_bytes)} bytes)")

    print(f"\nTotal: {img_count} images")
    print(f"Directory: {output_dir}")
    return img_count


def parse_pages(pages_str):
    """Parse page range string like '10-15' or '3' into 0-indexed list."""
    if "-" in pages_str:
        a, b = pages_str.split("-", 1)
        return list(range(int(a) - 1, int(b)))  # convert to 0-indexed
    else:
        return [int(pages_str) - 1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract images from PDF")
    parser.add_argument("pdf", help="PDF file path")
    parser.add_argument("-o", "--output", default="figures_extracted",
                        help="Output directory (default: figures_extracted)")
    parser.add_argument("--pages", help="Page range, e.g. 10-15 or 3")
    args = parser.parse_args()

    pages = parse_pages(args.pages) if args.pages else None
    extract_images(args.pdf, args.output, pages)
