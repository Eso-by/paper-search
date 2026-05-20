# paper-search

> A Claude Code skill for autonomous academic literature search, download, reading, and survey generation.

## Why This Exists

当前市面上的科研 Agent 自由度不高，自动化水平低。大多数工具只能做到"关键词搜索 → 返回列表"这一步，后续的 PDF 获取、全文阅读、公式提取、文献综述撰写仍然依赖人工完成。即使是基于 LLM 的学术助手，也往往停留在摘要层面的浅层总结，无法深入论文全文提取具体的公式、参数条件和方法细节。

paper-search 试图解决这个问题：它将"搜索 → 下载 → 阅读 → 综述"整条链路自动化，由 Claude Code 作为执行引擎，在每个环节做出判断（期刊质量筛选、下载渠道选择、参考文献追踪），最终交付的不是一堆链接，而是一篇有叙事结构、标注可信度的文献综述报告。

## Features

- **多平台穷尽搜索** — CrossRef, OpenAlex, Semantic Scholar, PubMed, arXiv, DBLP, DOAJ, OpenAIRE, Google Scholar (CDP)
- **自动下载与验证** — arXiv → Semantic Scholar → Unpaywall 三级渠道，格式校验 + 完整性检查 + 主题核对
- **全文深度阅读** — pymupdf 提取全文，pdfplumber 提取表格，自定义脚本提取图片；不是摘要级总结，而是提取具体公式、参数条件、方法步骤
- **参考文献追踪** — 自动提取引用文献，交叉比对已有文件夹，发现隐含的关键文献
- **质量门禁** — 搜索阶段即时过滤低质量期刊（MDPI/Hindawi 等），不浪费时间在无关论文上
- **结构化综述** — 按主题组织的叙事性综述（500-1500 字），标注每段的可信度（全文/摘要/待验证）
- **本地问答** — 对已有论文文件夹提问，直接读取全文后给出包含公式和方法细节的回答

## Architecture

```
paper-search/
├── SKILL.md                    # Skill 主定义文件（Claude Code 入口）
├── pdf_extract.py              # PDF 文本/表格提取工具
├── references/                 # 各阶段详细指令（按需加载，不一次全读）
│   ├── search.md               # 搜索策略：关键词变体、3+ 轮穷尽、GS CDP
│   ├── download.md             # 下载策略：渠道优先级、验证、重试、失败通知格式
│   ├── reading.md              # 阅读策略：pymupdf 全文提取、表格/图片处理
│   └── report.md               # 报告模板：综述结构、单篇总结格式、可信度标注
├── scripts/
│   └── pdf_images.py           # PDF 图片提取脚本
├── evals/
│   └── evals.json              # 评测用例定义
└── workspace/                  # 迭代评测记录
    └── iteration-2/
        ├── benchmark.md        # 基准测试结果
        └── eval-*/             # 各评测场景（with/without skill 对比）
```

### 设计原则

- **延迟加载**: `references/` 下的模块只在执行到对应阶段时才读取，避免上下文膨胀
- **渐进式报告**: 每个阶段完成后向用户汇报，等待确认再进入下一阶段
- **失败透明**: 下载失败的论文不会被静默丢弃，而是标注 DOI 和失败原因，按重要性分级处理
- **全文优先**: 5 篇全文的综述 > 50 篇摘要的综述；摘要级内容必须标注"待验证"

## Workflows

### Workflow A: Local Q&A

对已有论文文件夹提问。触发词："基于这个文件夹的论文..."、"根据这些论文..."

1. 扫描 README.md 识别相关论文
2. pymupdf 提取全文（不是摘要）
3. 追踪引用文献，发现隐含的关键文献
4. 综合全文信息给出包含具体公式的回答
5. 标注缺失 PDF 的引用文献，提供 DOI 供手动获取

### Workflow B: Full Search

从零开始的完整文献调研。

| 阶段 | 内容 | 产出 |
|------|------|------|
| Phase 1: Search | 3+ 轮穷尽搜索，参考文献追踪，期刊质量过滤 | 候选论文列表 |
| Phase 2: Download | 三级渠道下载，格式/完整性/主题验证 | 带校验的 PDF 集合 |
| Phase 2.5: Handoff | 用户手动提供失败的 PDF，触发引用追踪和报告更新 | 补充文献 |
| Phase 3: Read | 全文提取 + 表格/图片 + 结构化总结 | README.md 中的单篇总结 |
| Phase 4: Report | 叙事性综述 + 可信度标注 | 文献综述报告 |

## Benchmark

在 3 个评测场景上的表现（有 skill vs 无 skill）：

| Metric | With Skill | Without Skill | Delta |
|--------|------------|---------------|-------|
| Pass Rate | 100% ± 0% | 62% ± 54% | +38% |
| Time | 300s ± 90s | 189s ± 157s | +111s |
| Tokens | 87K ± 9K | 57K ± 50K | +30K |

有 skill 的情况下通过率从 62% 提升到 100%，代价是更多的 token 消耗和时间。无 skill 的方差极大（±54%），说明 LLM 在没有结构化指引时表现不稳定。

## Usage

This skill is designed for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Install it by placing the `paper-search` directory in your Claude Code skills folder:

```
~/.claude/skills/paper-search/
```

Then invoke it in Claude Code with `/paper-search` or let it auto-trigger when you ask about literature search, paper download, or survey writing.

### Prerequisites

- Python 3.13+ with `pymupdf`, `pdfplumber`
- `paper-search-mcp` CLI (for Semantic Scholar search/download)
- `papi` (PaperPipe, for additional paper operations)
- Git Bash on Windows

## Future Directions

- **多语言支持**: 当前综述默认中文输出，计划支持英文和其他语言
- **引用图谱**: 自动构建论文引用关系图，识别核心节点和研究脉络
- **增量更新**: 对已有文献文件夹定期检查新发表的相关论文
- **协作模式**: 支持多人共享文献文件夹，合并各自的搜索结果
- **更多数据源**: 接入 IEEE Xplore, Springer, ScienceDirect 等付费数据库（需机构授权）

## License

MIT
