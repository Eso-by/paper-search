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

## Why This Exists

当前市面上的科研 Agent 自由度不高，自动化水平低。大多数工具只能做到"关键词搜索 → 返回列表"这一步，后续的 PDF 获取、全文阅读、公式提取、文献综述撰写仍然依赖人工完成。即使是基于 LLM 的学术助手，也往往停留在摘要层面的浅层总结，无法深入论文全文提取具体的公式、参数条件和方法细节。

paper-search 将"搜索 → 下载 → 阅读 → 综述"整条链路自动化，由 Claude Code 作为执行引擎，在每个环节做出判断（期刊质量筛选、下载渠道选择、参考文献追踪），最终交付的不是一堆链接，而是一篇有叙事结构、标注可信度的文献综述报告。

## Architecture

```
paper-search/
├── SKILL.md                    # Skill 主定义文件（Claude Code 入口）
├── pdf_extract.py              # PDF 文本/表格提取工具
├── references/                 # 各阶段详细指令（按需加载）
│   ├── search.md               # 搜索策略：关键词变体、3+ 轮穷尽、GS CDP
│   ├── download.md             # 下载策略：渠道优先级、验证、重试、失败通知格式
│   ├── reading.md              # 阅读策略：pymupdf 全文提取、表格/图片处理
│   └── report.md               # 报告模板：综述结构、单篇总结格式、可信度标注
├── scripts/
│   └── pdf_images.py           # PDF 图片提取脚本
├── evals/
│   └── evals.json              # 评测用例定义
└── workspace/                  # 迭代评测记录
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
