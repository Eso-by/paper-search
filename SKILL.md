---
name: paper-search
description: >
  Search academic papers across multiple platforms (CrossRef, OpenAlex, Semantic Scholar, PubMed, arXiv, DBLP, DOAJ, OpenAIRE, etc.),
  download PDFs from open-access sources, read full text/extract tables/images, and write structured literature survey reports (in Chinese).
  Use this skill whenever the user asks to find papers, search research topics, conduct literature surveys, review state-of-the-art,
  find related work, or explore a research field comprehensively. Also use when the user wants to download paper PDFs,
  extract information from academic papers, analyze figures/charts in papers, or organize findings into a structured markdown report.
  Also use this skill when the user asks a question about papers in an existing local folder (e.g. "基于这个文件夹的论文回答XXX",
  "根据这些论文告诉我怎么XXX", "读一下这个文件夹的论文然后总结XXX") — in this case, use the Local Q&A workflow:
  read the folder's README.md to identify relevant papers, then use pymupdf to read the full PDF text, answer the question with
  specific formulas/methods/conditions from the papers, and save the answer as an md file.
  This skill handles the full workflow: exhaustive multi-platform search -> PDF download with verification ->
  full-text reading + figure extraction -> structured report generation with classification by relevance.
---

# Paper Search Skill

## Environment

Windows + Git Bash. **`python3` returns exit code 49 — always use `python`.** GBK encoding breaks on Unicode — prefix all Python commands with:

```bash
PYTHONIOENCODING=utf-8 python -X utf8 -c "..."
```

Tools:

| Tool | Path |
|------|------|
| System Python | `c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe` |
| paper-search CLI | `c:/Users/porfi/paper-search-mcp/.venv/Scripts/python.exe -m paper_search_mcp.cli` |
| papi (PaperPipe) | `export PATH="$PATH:/c/Users/porfi/AppData/Roaming/Python/Python314/Scripts"` then `papi` |

## Rules

These come from past failures. Follow them strictly.

1. **Plan first, then ask**. Show the full search plan (keywords, journals, authors) before doing anything. Reason: the user may have domain knowledge (specific authors, known papers, important sub-topics) that you cannot guess. Finding out after writing a draft means redoing work.

2. **Quality gate before recording**. Zero tolerance for low-quality journals (MDPI, Hindawi, Romanian Reports in Physics, Thermal Science, Nonlinear Engineering). Check journal quality as each paper is found during search — do not batch this at the end. Filter immediately or you'll waste time on irrelevant papers.

3. **Download systematically, fail gracefully**. For each paper, try arXiv direct → Semantic Scholar CLI → Unpaywall in order. Verify every download (format + integrity + topic). On failure, always output `DOI: xxx | 失败: [渠道+结果]` in chat. Severity determines next action: Core (***) → pause and ask, Important (**) → notify and continue, Supplementary (*) → mark abstract-only.

4. **Read before writing**. A survey from 5 full texts is worth more than one from 50 abstracts. Every full-text summary must include concrete formulas, parameter conditions, and methodological details (not just "studied the mKdV equation"). Abstract-only summaries must be clearly labeled.

5. **Write a narrative, not a list**. Organize the report thematically with a narrative survey section (500-1500 words) at the top. Avoid repetitive content. Label each section's credibility ("reliable" = from full text, "needs verification" = from abstract).

## Modules

Detailed instructions per task — read when you reach that step, don't read them all upfront:

| When | Read | What it covers |
|------|------|---------------|
| Searching | `references/search.md` | Keywords, 3+ round exhaustive search, source status, GS CDP |
| Downloading | `references/download.md` | Channel priority, verification, retry, failure notification format |
| Reading PDFs | `references/reading.md` | Text extraction (pymupdf), table extraction (pdfplumber), figure extraction |
| Writing report | `references/report.md` | Template, per-paper summary format, credibility marking |

## Workflow A: Local Q&A (existing folder with papers)

When the user asks a question and points to a folder that already contains PDFs and a README.md, use this workflow instead of the full search-download-read pipeline.

### Trigger conditions
- User says "基于这个文件夹的论文...", "根据这些论文...", "读一下这个文件夹的论文然后...", etc.
- The folder already has PDFs and a README.md with per-paper summaries.
- The user wants an answer to a specific question, not a new literature search.

### Step 1: Survey the README.md

Read the folder's `README.md` to understand what papers are available. The README.md contains per-paper summaries with: title, authors, journal, core content, key findings, and PDF path. Scan all summaries to identify which papers are relevant to the user's question.

Output to user: "Based on the README.md, I identified N papers relevant to your question: [list titles]. I'll now read the full text of these papers."

### Step 2: Read relevant PDFs with pymupdf

For each relevant paper, extract full text using pymupdf (NOT the Read tool — pypdf falsely reports password errors). Use the encoding-safe command from `references/reading.md`:

```bash
PYTHONIOENCODING=utf-8 python -X utf8 -c "
import sys, io; sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import fitz
doc = fitz.open(r'<folder>/<file>.pdf')
print(f'Pages: {len(doc)}')
for i in range(len(doc)):
    print(f'--- Page {i+1} ---')
    print(doc[i].get_text())
"
```

Read the FULL text, not just abstracts. The goal is to extract specific formulas, parameter conditions, methodological steps, and applicable constraints — things that are never in the abstract.

If a paper is too long (>20 pages), read in chunks: first pages 1-10, then 11-20, etc.

### Step 3: Trace references of the relevant papers

After reading the full text of the directly relevant papers, extract their **References** sections. The references are a gold mine — they contain the foundational works, methodological origins, and cross-validations that the authors relied on. The README.md summaries capture what each paper *says*, but the references reveal what each paper *depends on*.

1. **Extract cited papers**: From each relevant paper's References section, identify papers that are:
   - Cited for methodological foundations (e.g., "the DT was first constructed in [X]")
   - Cited for key results used in the paper (e.g., "following the approach of [Y]")
   - Cited for the specific topic the user asked about (not generic background citations)

2. **Cross-check against the folder**: For each important cited paper, check if it already exists in the folder (by title or author match in README.md). If it does, add it to the reading list — it's likely relevant to the user's question even if the README summary didn't make that obvious.

3. **Read newly identified papers**: If step 2 turns up papers that are already in the folder but weren't initially selected as relevant, read their full text now. They often contain the foundational details (original derivations, parameter conditions, proof techniques) that the citing papers assume the reader knows.

4. **Note missing references**: For important cited papers that are NOT in the folder, record their citation info (authors, title, DOI if available). These will be reported in Step 7 as missing PDFs.

**Reference selection criteria**: Prioritize newly discovered references by closeness to the user's question:
- Papers directly addressing the user's specific question (method, equation, phenomenon)
- High-quality review/survey papers that consolidate the field
- Foundational papers that established the methods being used (cited by multiple relevant papers)
- Skip generic background citations (e.g., "nonlinear PDEs arise in many fields [1-5]")

Why this matters: When a paper says "we use the module resonance condition from [34]", the actual condition, its derivation, and its precise applicable constraints are in [34], not in the citing paper. Without tracing references, you risk reproducing incomplete or decontextualized information.

### Step 4: Extract figures if needed

If the user's question involves visual results (waveforms, phase diagrams, solution profiles), extract figures using:
```bash
PYTHONIOENCODING=utf-8 python -X utf8 \
  "c:/Users/porfi/.claude/skills/paper-search/scripts/pdf_images.py" \
  "<folder>/<file>.pdf" -o "<folder>/figures"
```
Then use the Read tool to view the extracted images.

### Step 5: Synthesize answer

Based on the full text of the relevant papers (including papers found through reference tracing in Step 3), write a comprehensive answer that includes:
- **Specific methods**: step-by-step construction procedures, not just "they used DT"
- **Concrete formulas**: actual equations, not just descriptions
- **Applicable conditions**: when does the method work? What are the constraints on parameters?
- **Key distinctions**: how do different methods compare? What are the advantages/disadvantages?
- **Source attribution**: cite each paper by author + year (e.g., "Xing 2017"). For information that came from a paper discovered through reference tracing, note this explicitly (e.g., "根据 Zhang 2020 引用的 Serkin 2018...")

### Step 6: Save answer as md file

Save the answer to `<folder>/<descriptive-name>.md` (e.g., `breather-construction-methods.md`). The filename should describe the question topic. Include:
- A header with the question
- Sections organized by method/answer aspect
- A table of applicable conditions
- A reading order recommendation at the end

Report to user: "Answer saved to `<folder>/<filename>.md`. Key findings: [2-3 sentence summary]."

### Step 7: Check for missing PDFs and provide DOIs

After writing the answer, cross-reference every paper cited in the answer against the PDFs actually present in the folder. This includes papers discovered through reference tracing in Step 3. For any cited paper that has no PDF file, report to the user:

```
以下论文在回答中被引用但文件夹中没有原文 PDF，需要手动下载：
- [作者 (年份)], "[标题]", *期刊*, Vol. X, pp. Y-Z. **DOI**: 10.xxxx/xxxxx — [重要性说明：为什么回答中引用了这篇]
```

Importance levels:
- **核心文献** — answer's main methodology source, must have full text to verify formulas
- **重要参考** — provides key supporting results or cross-validation
- **补充引用** — mentioned for completeness, abstract is sufficient

This ensures the user can manually obtain any missing papers to verify the answer's claims.

---

## Workflow B: Full Search (new topic from scratch)

Each phase completes -> report to user -> wait for confirmation before proceeding to the next phase.

### Phase 1 (Workflow B): Search (iterative, minimum 3 rounds)

1. **Plan**: Draft keyword variants, target journals, known authors. Show user, ask for additions.
2. **Execute**: Run each variant across all available sources (CrossRef, OpenAlex, DBLP, DOAJ, OpenAIRE, Semantic Scholar, WebSearch for arXiv). After exhausting CLI sources, use GS CDP if coverage is thin.
3. **Iterate**: After each round, check references of found papers for new leads (reference chasing). Prioritize references that directly address the search topic, high-quality review/survey papers, and foundational methodological works — skip generic background citations. Add newly identified candidates to the next round. The stopping criterion is global — check only after ALL search activities (initial rounds + cross-ref + author search + publisher site search) are complete. Stop when a round finds <=3 new papers (count by search discovery, not download status). Minimum 3 rounds.
4. **Quality gate (per-paper)**: As each paper is found during search, verify journal quality before adding to the candidate list. Filter out MDPI/Hindawi/etc. immediately — never pass them to Phase 2.

### Phase 2 (Workflow B): Download

1. For each paper, try arXiv direct -> Semantic Scholar CLI -> Unpaywall in order.
2. Verify every download: format check (`head -c 5` = `%PDF-`), integrity check (pypdf reads it), topic check (read first page).
3. Delete invalid files immediately. Retry with next channel.
4. **On failure**: Output `DOI: xxx | 失败: [渠道+结果]` in chat. Core (***) → pause and ask user for PDF; Important (**) → notify and continue; Supplementary (*) → mark "abstract-only". See `references/download.md` for full notification format.
5. Failed papers can be included in the report (mark as "download-failed"). Reports can be updated later if PDFs are obtained.

### Phase 2.5 (Workflow B): Manual PDF Handoff (user provides what auto-download couldn't)

When the user gives you PDFs that failed auto-download, do NOT just save them. Trigger a full update cycle:

1. **Save and read**: Move PDFs into the paper folder. Extract full text, write per-paper summary to `README.md` (same format as Phase 3).
2. **Trace references**: Read the "References" section of each newly obtained paper. Extract cited papers relevant to the topic, prioritizing those directly addressing the user's research question, high-quality review/survey papers, and foundational methodological works (not generic background citations). Do a **one-shot search** per lead (not full 3-round saturation — Phase 1's multi-round strategy is for the initial sweep). Search across all platforms for each missed reference.
3. **Search loop**: Any newly discovered papers from step 2 enter the standard download attempt → (fail → notify) cycle. If search turns up new downloadable PDFs, download and process them.
4. **Update report**: Insert new findings into the methodology review. Update the failed-DOI list — remove ones now obtained, add any newly discovered but unobtainable ones.
5. **Report back**: Summarize what was gained from the handoff. Output the **updated unobtainable DOI list** explicitly so the user knows what's still missing.

### Phase 3 (Workflow B): Read (this is where the real work happens)

1. For each downloaded PDF, extract full text via pymupdf. Read the full content.
2. Extract tables via pdfplumber where relevant.
3. Extract figures via pdf_images.py script. Use the Read tool to view each figure — Claude can interpret charts, waveforms, phase diagrams.
4. For each paper, write a structured summary covering: equation form, core method, key results (concrete formulas/numbers), and what makes it novel. **Save all per-paper summaries to `README.md`** in the paper folder — this is the single source of truth for individual paper summaries.
5. **Incremental re-read**: When revisiting an existing folder, check for PDFs that were previously marked "abstract-only" or "download-failed" but are now downloaded. Also check if arXiv preprints have been formally published (update journal info). Re-read any papers whose summaries feel thin. **For any newly added papers (auto-downloaded or manually placed), append their per-paper summaries to `README.md`** — do not leave them without an entry. For user-provided PDFs, follow the full manual handoff flow in Phase 2.5 (trace references → search → download → update report).

### Phase 4 (Workflow B): Report

1. **Outline**: Write survey outline (section titles + one sentence each). Get user approval.
2. **Draft**: Write narrative survey (500-1500 words, organized by theme). Label each section's credibility. Per-paper summaries are already in `README.md` (written during Phase 3) — reference them rather than duplicating content.
3. **Finalize**: Revise based on user feedback. Flag any claims that still need verification because the relevant paper's full text is missing.
