# Download Module

Download PDFs from open-access sources, verify, retry on failure.

## Priority Channels (try in order per paper)

1. **arXiv direct** (most reliable): `curl -L "https://arxiv.org/pdf/{id}.pdf" -o "papers/<keyword>/<title>.pdf"`
2. **paper-search CLI**: `$PY download semantic <doi> -o papers/<keyword>/`
3. **Unpaywall** (mandatory before marking "abstract-only"): `curl "https://api.unpaywall.org/v2/{DOI}?email=zhangpe@buaa.edu.cn"` — if `is_oa=true`, use `best_open_location.url`
4. CrossRef/OpenAlex: metadata only, no PDF.

## Verify Every Download

```bash
head -c 5 file.pdf   # Must start with %PDF-
```

Then confirm completeness with pypdf (catches truncation). Note: pypdf is only used here for download verification — for actual text extraction, always use pymupdf (pypdf falsely reports password errors on some PDFs):
```python
from pypdf import PdfReader
try:
    r = PdfReader('file.pdf')
    print(f'OK: {len(r.pages)} pages')
except Exception as e:
    print(f'CORRUPT: {e}'); exit(1)
```

Then verify topic matches (read first page, see reading module).

Delete invalid files immediately — don't keep corrupted downloads.

## Retry Protocol

For each paper, try up to 3 channels. Record what was tried:
```
arXiv 403 → Semantic Scholar CAPTCHA → Unpaywall non-OA → failed
```

## Notify User on Failure

Every paper that fails all download channels follows this unified notification:

1. **Chat output** (always, one line per paper):
   ```
   DOI: xxx | 失败: [渠道+结果]
   ```
2. **Severity-level action**:
   - **Core (***)**: Pause everything. Show expanded format, wait for user to provide PDF.
     ```
     ⚠️ Cannot auto-download:
     Title: xxx | DOI: xxx | Journal: xxx | Year: xxxx
     Tried: [list channels + results]
     Please download and place in papers/<keyword>/
     ```
   - **Important (**)**: Same expanded format, notify user, then continue.
   - **Supplementary (*)**: Mark "abstract-only" with reason, continue.
3. **In report**: Failed papers can be included (mark as "download-failed"). Reports are updatable — if PDFs are obtained later, refresh corresponding entries.

## Chinese Filenames

Git Bash `curl -o` mishandles Chinese paths. Download as temp, then rename via Python:
```bash
curl -L "https://arxiv.org/pdf/1234.pdf" -o "papers/<keyword>/tmp.pdf"
PYTHONIOENCODING=utf-8 python -X utf8 -c "import os; os.rename('papers/<keyword>/tmp.pdf', 'papers/<keyword>/真实标题.pdf')"
```

