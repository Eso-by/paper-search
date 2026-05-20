"""Extract text and tables from PDF using pdfplumber."""
import pdfplumber, json, sys, argparse

def extract_text(pdf_path, pages=None):
    """Extract plain text from PDF. Returns list of {page, text}."""
    results = []
    with pdfplumber.open(pdf_path) as pdf:
        target = pages or range(1, len(pdf.pages) + 1)
        for i in target:
            if 1 <= i <= len(pdf.pages):
                page = pdf.pages[i - 1]
                text = page.extract_text()
                if text:
                    results.append({"page": i, "text": text})
    return results

def extract_tables(pdf_path, pages=None):
    """Extract tables from PDF. Returns list of {page, table_index, headers, rows}."""
    results = []
    with pdfplumber.open(pdf_path) as pdf:
        target = pages or range(1, len(pdf.pages) + 1)
        for i in target:
            if 1 <= i <= len(pdf.pages):
                page = pdf.pages[i - 1]
                tables = page.extract_tables()
                for j, table in enumerate(tables):
                    if table:
                        results.append({
                            "page": i,
                            "table_index": j + 1,
                            "rows": table
                        })
    return results

def extract_all(pdf_path, pages=None):
    """Extract both text and tables."""
    return {
        "text": extract_text(pdf_path, pages),
        "tables": extract_tables(pdf_path, pages)
    }

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("pdf", help="PDF file path")
    p.add_argument("--mode", choices=["text", "tables", "all"], default="all")
    p.add_argument("--pages", help="Page range, e.g. 1-5 or 3")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    args = p.parse_args()

    pages = None
    if args.pages:
        if "-" in args.pages:
            a, b = args.pages.split("-", 1)
            pages = range(int(a), int(b) + 1)
        else:
            pages = [int(args.pages)]

    if args.mode == "tables":
        result = extract_tables(args.pdf, pages)
    elif args.mode == "text":
        result = extract_text(args.pdf, pages)
    else:
        result = extract_all(args.pdf, pages)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if args.mode == "tables":
            for t in result:
                print(f"\n=== Page {t['page']}, Table {t['table_index']} ===")
                for row in t["rows"]:
                    print(" | ".join(c or "" for c in row))
        elif args.mode == "text":
            for t in result:
                print(f"\n--- Page {t['page']} ---")
                print(t["text"])
        else:
            for t in result["text"]:
                print(f"\n--- Page {t['page']} (text) ---")
                print(t["text"])
            for t in result["tables"]:
                print(f"\n=== Page {t['page']}, Table {t['table_index']} (table) ===")
                for row in t["rows"]:
                    print(" | ".join(c or "" for c in row))
