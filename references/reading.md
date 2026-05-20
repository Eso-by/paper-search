# Reading Module

Extract text, tables, and figures from PDF papers.

## Environment

- Use `python` (not `python3` — returns exit code 49 on this machine)
- All Python commands need encoding prefix for Git Bash:
```bash
PYTHONIOENCODING=utf-8 python -X utf8 -c "..."
```
- For pymupdf stdout, wrap to avoid GBK crashes:
```python
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
```

## Text Extraction (pymupdf, recommended)

```bash
PYTHONIOENCODING=utf-8 python -X utf8 -c "
import sys, io; sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import fitz
doc = fitz.open(r'papers/<keyword>/<file>.pdf')
print(f'Pages: {len(doc)}')
for i in range(len(doc)):
    print(f'--- Page {i+1} ---')
    print(doc[i].get_text())
"
```

Why pymupdf over pypdf: handles more PDF formats, doesn't choke on the "password-protected" false alarm that pypdf throws, and can also extract images (see below).

## Image/Figure Extraction (pymupdf)

Many papers contain key information in figures (waveforms, phase diagrams, simulations). pymupdf extracts embedded images from PDF.

```bash
PYTHONIOENCODING=utf-8 python -X utf8 \
  "c:/Users/porfi/.claude/skills/paper-search/scripts/pdf_images.py" \
  "papers/<keyword>/<file>.pdf" -o "papers/<keyword>/figures"
```

Options: `--pages 10-15` to extract only specific pages.

After extraction, use the Read tool to view each image — Claude is multimodal and can interpret the charts.

**Caveat**: Some PDFs use vector graphics (not embedded bitmaps) — `get_images()` returns empty for those.

## Table Extraction (pdfplumber)

```bash
PYTHONIOENCODING=utf-8 python -X utf8 \
  "c:/Users/porfi/.claude/skills/paper-search/pdf_extract.py" \
  "papers/<keyword>/<file>.pdf" --mode tables
```

Options: `--pages 3-7`, `--json`.

## Quick Topic Verification (after download)

Always read the first page after downloading to confirm the paper matches the search topic (arXiv has mis-titled papers):

```bash
PYTHONIOENCODING=utf-8 python -X utf8 -c "
import sys, io; sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import fitz
doc = fitz.open(r'papers/<keyword>/<file>.pdf')
print(doc[0].get_text()[:1500])
"
```

## Figure Analysis

To analyze figures in a paper: (1) read full text for formulas and parameter choices, (2) scan for figure references ("Fig. 1") and read captions to know what each figure plots, (3) extract with pdf_images.py, (4) use Read tool to view charts, (5) cross-reference with the discussing paragraph. Parameter variation is the core analytical method — identify which parameter each figure varies and what effect it produces.

## Password-Protected PDFs

pypdf sometimes reports "password-protected" falsely. Always try pymupdf first:
```python
import fitz
doc = fitz.open(r'path/to/file.pdf')
print(doc.needs_pass)  # 0 = not encrypted
```
