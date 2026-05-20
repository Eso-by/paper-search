# Report Module

Write structured literature survey reports (in Chinese).

## Core Principles

- **Reading depth determines survey quality**. A survey written from 5 full texts is worth more than one from 50 abstracts. Don't rush to collect papers — invest time in reading them. Every summary based on full text should include concrete formulas, parameter conditions, and methodological details.

## How to Handle Full Text vs Abstract vs Download-Failed

- If a PDF is available (via any download channel), your summary must be based on actual full-text reading, not the abstract. The download module provides multiple channels — use them.
- If you've exhausted all download channels and the PDF is still unavailable, write the summary based on the abstract and label it clearly as "abstract-only".
- **Download-failed papers**: If a paper was found during search but download failed for all channels, it can still be included in the report. Mark it as "download-failed" in the Reading depth column. The report can be updated later if PDFs are obtained — re-run the download phase and refresh the corresponding entries.
- **Why**: Summaries from abstracts alone miss concrete formulas, parameter conditions, and methodological details — but a properly labeled abstract summary is still useful when full text is unobtainable.

## Writing Standards

- Write like a mini review paper, not a paper list
- Must include a narrative survey section (500-1500 words) at the top, organized by theme

## Document Split Convention

The output can be split into two files to avoid conflating thematic narrative with individual paper summaries:

| File | Content | Created in |
|------|---------|------------|
| `README.md` | Per-paper summaries (one entry per paper, per template below) | Phase 3 (Read) |
| `<topic>-review.md` | Narrative survey + classification + methods summary + citation network | Phase 4 (Report) |

**Every paper must have a README.md entry.** When adding papers to an existing folder, append their summaries to README.md — do not leave new papers undocumented.

**Cross-reference at the top of each file** so the reader knows the other exists and what it covers. No duplicated content between the two files.

## User Confirmation Checkpoints

1. **Before writing**: Show outline (section titles + one-sentence summary each). Wait for approval.
2. **After draft**: Label credibility per section ("reliable" = from full text, "needs verification" = from abstract). List missing core papers.
3. **Gap report**: Which key claims can't be verified due to missing full texts.

## Per-Paper Summary Template

Each paper with full text must cover 4 elements:

```markdown
### [N]. [Title]
- **DOI/Authors/Journal/Year**
- **Reading depth**: Full text / Abstract only / Metadata only / Download failed
- **Relevance**: * / ** / ***
- **Equation**: (write the actual equation, not just "mKdV equation")
- **Method**: (specific technique — Darboux, Hirota, Painlevé, etc.)
- **Key results**: (concrete formulas, numerical values)
- **Innovation**: (what this paper does differently from others)
```

Bad: "Studied soliton solutions of the variable-coefficient mKdV equation"
Good: "Derived explicit 1-soliton solution χ₁ = M(t) - 2s₀e^{-L₄t}γ₁ sech(w₁) where w₁ = -2γ₁x + (4L₃γ₁³ - 2c(t)γ₁)t + 2m₁"

## Report Template

```markdown
# Literature Survey: <keyword>
> Date | Sources | Iteration: N (rounds: 3+) | Total: N papers (M full text, K abstract-only, L download-failed)

## Classification
### Direct (***)
| # | Title | Authors | Year | Journal | Reading depth |
### Related (**)
### Supplementary (*)

## Narrative Survey
(500-1500 word themed overview)

> Per-paper summaries for individual papers are in [`README.md`](README.md) — this file covers only the thematic narrative, classification, and methods summary.

## Methods Summary
## Terminology
## PDF File List
## Older Foundational Works (>10 years)
```

## Guidelines

- Reference high-quality papers' introductions for writing style
- Papers >10 years: list separately at the end
- Metadata completeness is secondary — don't waste time filling in missing DOIs
- Mark reading depth honestly
