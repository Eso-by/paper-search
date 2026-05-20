# paper-search

`Academic Research`

## Installation

```bash
npx skills add https://github.com/Eso-by/paper-search --skill paper-search
```

## Summary

- Autonomous end-to-end academic literature pipeline: search across 9+ platforms (CrossRef, OpenAlex, Semantic Scholar, PubMed, arXiv, DBLP, DOAJ, OpenAIRE, Google Scholar) → download PDFs with 3-tier fallback (arXiv → Semantic Scholar → Unpaywall) → full-text reading with formula/table/figure extraction → structured survey report with credibility labels
- On-the-fly journal quality gate filters low-quality publishers (MDPI, Hindawi, etc.) at search time, not after the fact — zero wasted effort on irrelevant papers
- Reference tracing automatically extracts cited works from each paper's bibliography, cross-checks against the local folder, and surfaces hidden foundational papers the user never knew to search for
- Two workflows: **Full Search** (4-phase pipeline from scratch with iterative 3+ round search, progressive reporting, and graceful failure handling with DOI tracking) and **Local Q&A** (answer specific questions from an existing paper folder with full-text reading, not abstract skimming)
- Every full-text summary includes concrete formulas, parameter conditions, and methodological steps — abstract-only content is explicitly labeled "needs verification"

## Motivation

Most academic research agents today have limited autonomy and low automation. They can handle "keyword search → return list", but everything after that — PDF acquisition, full-text reading, formula extraction, survey writing — still depends on manual work. Even LLM-based academic assistants tend to stay at the abstract level, unable to dive into the full text to extract specific formulas, parameter conditions, and methodological details.

paper-search automates the entire chain: search → download → read → survey. Claude Code acts as the execution engine, making judgment calls at each step (journal quality filtering, download channel selection, reference tracing). The final deliverable is not a pile of links, but a structured narrative survey report with credibility labels.

## Architecture

```
paper-search/
├── SKILL.md                    # Skill definition (Claude Code entry point)
├── pdf_extract.py              # PDF text/table extraction utility
├── references/                 # Per-stage instructions (loaded on demand)
│   ├── search.md               # Search strategy: keyword variants, 3+ round exhaustive, GS CDP
│   ├── download.md             # Download strategy: channel priority, verification, retry, failure format
│   ├── reading.md              # Reading strategy: pymupdf full-text, table/figure extraction
│   └── report.md               # Report template: survey structure, per-paper summary, credibility labels
├── scripts/
│   └── pdf_images.py           # PDF figure extraction script
├── evals/
│   └── evals.json              # Evaluation test cases
└── workspace/                  # Iteration benchmark records
```

Design principles:
- **Deferred loading**: `references/` modules are only read when the agent reaches that stage, avoiding context bloat
- **Progressive reporting**: each phase completes → report to user → wait for confirmation before next phase
- **Transparent failure**: failed downloads are never silently discarded; DOI + failure reason + severity level are always reported
- **Full text first**: 5 full-text summaries > 50 abstract summaries; abstract-only content is always labeled

## Benchmark

Evaluated on 3 literature search scenarios (with skill vs without skill):

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| Pass Rate | 100% ± 0% | 62% ± 54% | +38% |
| Time | 300s ± 90s | 189s ± 157s | +111s |
| Tokens | 87K ± 9K | 57K ± 50K | +30K |

Without the skill, pass rate variance is extreme (±54%) — LLMs produce unstable results without structured guidance.

## Prerequisites

- Python 3.13+ with `pymupdf`, `pdfplumber`
- `paper-search-mcp` CLI (Semantic Scholar search/download)
- `papi` (PaperPipe)
- Git Bash on Windows

## License

MIT
