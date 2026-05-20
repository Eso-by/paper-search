---
name: paper-search
description: >
  Search academic papers across multiple platforms (CrossRef, OpenAlex, Semantic Scholar, PubMed, arXiv, DBLP, DOAJ, OpenAIRE, etc.),
  download PDFs from open-access sources, read full text/extract tables, and write structured literature survey reports (in Chinese).
  Use this skill whenever the user asks to find papers, search research topics, conduct literature surveys, review state-of-the-art,
  find related work, or explore a research field comprehensively. Also use when the user wants to download paper PDFs,
  extract information from academic papers, or organize findings into a structured markdown report.
  This skill handles the full workflow: exhaustive multi-platform search → PDF download with verification →
  full-text reading → structured report generation with classification by relevance.
---

# 论文搜索 skill

## 重要：路径与环境说明

本 skill 在 **Windows + Git Bash** 环境下运行，Python/node 不在 Git Bash PATH 中。

| 工具 | 路径 |
|------|------|
| 系统 Python | `c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe` |
| paper-search CLI venv | `c:/Users/porfi/paper-search-mcp/.venv/Scripts/python.exe` |
| papi (PaperPipe) | 通过 `export PATH="$PATH:/c/Users/porfi/AppData/Roaming/Python/Python314/Scripts"` 加入 PATH |
| Node.js / npx | `/c/Program Files/nodejs/node.exe` / `npx`（需 `PATH="/c/Program Files/nodejs:$PATH" npx ...`）|

**Python 编码问题**：Git Bash 的 Python 输出默认使用 GBK 编码，遇到 Unicode 字符会报错。所有 Python 命令必须加环境变量：
```bash
PYTHONIOENCODING=utf-8 python -X utf8 -c "..."
# 或
PYTHONIOENCODING=utf-8 "c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe" -X utf8 ...
```

---

## 最高准则：先计划、先询问、再行动

**在任何工作开始之前，必须停下来做三件事：**

1. **说出你的计划**：把任务拆成具体步骤，让用户看到你打算怎么做。
2. **列出你需要的帮助**：哪些论文需要手动下载？哪些地方你不确定需要用户确认？哪些术语你不懂？什么信息你无法从现有材料中获得？
3. **向用户提问，等待确认**：把计划呈现出来，提出明确的问题，等用户回应后再动手。用户不回复就不要往下做。

**这不是"建议"，是强制要求。** 违反这条准则的后果你已经看到了——写完大量综述内容后被批评"不准确"，因为你在不确定的地方自己猜了，而没有先问。

以下行为一律禁止：
- 不展示搜索关键词列表就直接搜
- 基于摘要就把公式和结论写入综述（拿不到全文时告知用户）
- 写完一整段综述才给用户看（先写提纲给用户确认结构）
- 遇到不懂的术语自己猜

此准则适用于**整个流程中的所有步骤**，下面的检查清单是具体化的实现。

---

## ⚠️ 强制流程检查清单

**核心原则一：这份综述的价值取决于你实际阅读了多少篇论文的全文。标记为"仅摘要"意味着你没有尽到职责。**

**核心原则二：默认多问用户。** 你不是该领域的专家，用户才是。在任何不确定的节点——搜索关键词是否穷尽、某篇论文是否值得收录、综述结构是否合理、某个技术细节是否准确——**必须先问用户再行动**。宁可多问一次，不可自作主张写出不准确的综述。具体来说：看到不懂的术语就问，看到有两可之处的就确认，写完综述初稿必须请用户审阅。这次已经发生的教训：基于摘要写了一大段综述然后被批评"很多内容不准确"——这本应通过写作前先问用户来避免。

你必须按以下顺序执行，**每个阶段完成后向用户汇报并等待确认**：

1. **搜索规划阶段**：向用户展示搜索关键词列表、期刊列表、作者列表。询问是否需要增减。
2. **初搜汇报阶段**：搜索完成后，汇报各子方向的论文覆盖情况。若某个方向明显缺失或发现意外热点，告知用户调整策略。
3. **下载筛选阶段**：对于无法自动下载的核心论文（见下载失败处理），以标题+DOI格式告知用户请求手动获取。同时请用户确认哪些论文优先下载/阅读。
4. **阅读汇报阶段**：读完所有全文后，向用户汇报关键发现摘要。用户可能指出遗漏或提供额外背景。
5. **综述规划阶段**：写出综述提纲（章节标题+每节主旨一句话），请用户确认结构和重点是否合理。
6. **综述草稿阶段**：写完综述初稿后，标注其中哪些论断仅基于摘要推断（不可靠），哪些基于全文精读（可靠）。请用户审阅并提供反馈。
7. **定稿阶段**：根据用户反馈修改，列出仍缺失的关键论文，请用户决定是否继续补全。
8. **"仅摘要"的使用限制**：只有在**穷尽所有下载渠道仍失败后**，才能标记为"仅摘要"。此时必须在论文总结中注明原因（如 "Elsevier 付费墙"、"无 arXiv 版本"、"Semantic Scholar 返回 HTML"等）。

---

## Quick Reference

```bash
# 搜索
PY="c:/Users/porfi/paper-search-mcp/.venv/Scripts/python.exe -m paper_search_mcp.cli"
$PY search "<query>" -s crossref,openalex,dblp,semantic -n 20

# 下载 PDF
$PY download arxiv <arxiv-id> -o papers/<keyword>/
$PY download semantic <doi> -o papers/<keyword>/

# 检查下载的是否真是 PDF（Semantic Scholar 常返回 HTML）
head -c 5 papers/<keyword>/<file>.pdf     # 应该显示 %PDF

# 读全文（重要：加 PYTHONIOENCODING=utf-8 修复中文编码）
PYTHONIOENCODING=utf-8 "c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe" -X utf8 -c "
from pypdf import PdfReader
r = PdfReader('papers/<keyword>/<file>.pdf')
for i, page in enumerate(r.pages):
    print(f'--- Page {i+1} ---')
    print(page.extract_text())
"

# Unpaywall 查免费 PDF（标记"仅摘要"前的必经步骤）
curl "https://api.unpaywall.org/v2/{DOI}?email=zhangpe@buaa.edu.cn"

# arXiv 直链下载
curl -L "https://arxiv.org/pdf/{id}.pdf" -o "papers/<keyword>/<title>.pdf"
```

---

## 搜索源状态（2026-05 实测）

### 正常可用
| 源 | 用途 | 命令行参数 |
|----|------|-----------|
| CrossRef | 元数据查询，**不提供 PDF 下载** | `crossref` |
| OpenAlex | 元数据查询，覆盖面广 | `openalex` |
| DBLP | CS 方向 | `dblp` |
| Semantic Scholar | 元数据 + 部分 PDF（**需 API key 用 semantic 源下载**） | `semantic` |
| PubMed / Europe PMC | 生物医学 | `pubmed` / `europepmc` |
| DOAJ | 开放获取期刊 | `doaj` |
| OpenAIRE | 欧洲开放获取 | `openaire` |
| bioRxiv / medRxiv | 预印本 | `biorxiv` / `medrxiv` |
| arXiv（WebSearch） | 通过 Google/Bing 网页搜索查 arXiv | WebSearch（比 CLI 更可靠）|

### 已损坏 / 跳过
| 源 | 原因 |
|----|------|
| `google_scholar` | 命令行接口已损坏；如有需要走 Edge + CDP（见末节）|
| `ssrn` / `citeseerx` | 接口不可用 |
| `hal` / `zenodo` | 存在 bug 不稳定 |

### 需要 API Key
在 `~/paper-search-mcp/.env` 中配置：
```
SEMANTIC_SCHOLAR_API_KEY=<free key from semantic scholar website>
CORE_API_KEY=<free key from core.ac.uk>
```

---

## 搜索策略 — 穷举多轮饱和法

### 硬性目标

- **≥40 篇论文**（之前设定的 ≥25 在实践中证明不够，必须翻倍）
- **搜索必须进行至少 3 轮**（每轮使用不同的关键词角度和渠道组合），直到不再出现新相关论文
- 覆盖近 10 年（当前：2016–2026），不遗漏重要相关工作
- **如果某轮搜索后论文总数 <30，必须增加新的关键词变体再搜一轮，不能停止**
- 每轮结果分别记录，在 README 头部注明："搜索轮次：3（第一轮 N 篇 + 第二轮 +M 篇 + 第三轮 +K 篇）"

**论文质量把控（重要——零容忍）：**
- **优先收录高质量期刊论文**：Nonlinear Dynamics, Phys. Rev. E, Phys. Rev. Lett., Phys. Lett. A, Chaos Solitons & Fractals, J. Phys. A, Commun. Nonlinear Sci., Stud. Appl. Math., Proc. R. Soc. A, Appl. Math. Lett., Physica D, Chaos, J. Fluid Mech., J. Plasma Physics, Phys. Fluids, Wave Motion, J. Math. Anal. Appl., Inverse Problems, Z. Angew. Math. Phys., Commun. Theor. Phys., Chin. Phys. Lett., Sci. Rep. 等
- **完全排除低质量期刊**（零容忍——一篇都不收录）：MDPI 系列（Mathematics, Symmetry, Axioms, Applied Sciences, AppliedMath, Fluids 等）、Romanian Reports in Physics、Thermal Science、Hindawi 系列（Math. Probl. Eng., J. Function Spaces 等）、Nonlinear Engineering 等以盈利为目标的低门槛期刊。这些论文**直接扔掉，不写入报告**。
- **arXiv 预印本可收录**，但优先选已正式发表的版本。若同时存在 arXiv 和正式发表版，以后者为准。
- **会议论文一般不收录**，除非是该方向唯一的工作。
- 元数据（DOI、页码等）不必追得太全，保证期刊质量即可。

### Step 0：搜索策略确认（必须执行）

在启动任何搜索之前，**必须向用户展示搜索计划**并等待确认：

1. 列出所有计划使用的关键词变体（同义词、缩写、相关概念、方程变体、方法词）
2. 列出计划搜索的期刊、会议、预印本源
3. 列出已知的关键作者
4. 询问用户：是否有遗漏的关键词/期刊/作者？重点关注哪个子方向？

**不要跳过这一步直接开始搜索。** 用户可能知道你遗漏的关键词变体或重要作者，提前确认可以避免做无用功。

### Step 1：穷尽关键词角度
对目标主题生成所有可能的查询变体。例如 "positon mKdV"：
- 同义词/缩写：`"smooth positon"`, `"b-positon"`, `"breather-positon"`, `"complexiton"`
- 相关概念：`"degenerate Darboux"`, `"double degeneration"`, `"negaton"`
- 方程变体：`"modified Korteweg"`, `"cmKdV"`, `"vector mKdV"`, `"Gardner equation"`
- 方法词：`"Hirota bilinear"`, `"Darboux transformation positon"`

### Step 2：穷尽期刊/会议
对每个关键词变体，逐一搜索以下期刊（用 WebSearch 或 CLI）：
- 核心：Nonlinear Dynamics, Phys. Lett. A, Phys. Rev. E, J. Phys. A, Chaos Solitons & Fractals
- 应用数学：Commun. Nonlinear Sci., Physica D, Stud. Appl. Math., Proc. R. Soc. A, Appl. Math. Lett.
- 交叉：Chinese Phys. B, Wave Motion, Phys. Scr., Eur. Phys. J. Plus, Int. J. Theor. Phys.
- 开放获取（注意质量）：Sci. Rep.; 警惕 MDPI 系列（Mathematics, Symmetry, Axioms 等）
- 预印本：arXiv (nlin.SI, math-ph, hep-th)

### Step 3：穷尽关键作者
搜索每位已知在该领域的核心研究者。例如：`"Jingsong He"`, `"Wen-Xiu Ma"`, `"Dumitru Mihalache"`, `"Zhao Zhang"` + 主题词。

### Step 4：交叉引用检查
阅读已找到论文的参考文献列表，标记可能遗漏的重要论文，针对性地补搜。

### Step 5：Channels 全覆盖
每个查询变体都要在以下渠道**全部**执行（不是选其一）：
1. `paper-search` CLI → `crossref,openalex,dblp,doaj,openaire`
2. WebSearch → `arxiv <query>` 多个变体
3. WebSearch → `"<keyword>" 2023 2024 2025 2026`（限近年的通用搜索）
4. **Google Scholar（CDP）**→ 对于 CLI + WebSearch 覆盖不足的子方向，必须启动 Edge CDP 搜索 GS（见末节）
5. **Semantic Scholar** → 用 paper-search CLI 的 semantic 源（需 API key）
6. **Springer/Nature/Elsevier 等出版商网站** → 用 WebSearch 搜索 `site:link.springer.com <keyword>`、`site:journals.aps.org <keyword>`、`site:iopscience.iop.org <keyword>` 等

### 迭代增强：重新访问已有论文文件夹

当第二次及以后重新访问一个已有的论文文件夹时，必须执行以下增量更新流程：

1. **检查已有 PDF 中未读的论文**：文件夹中可能之前已下载了 PDF 但未精读（标记为"仅摘要"）。对这些 PDF 执行全文阅读和详细总结。
2. **检查是否有同名论文已更新版本**：对比已有论文列表与最新搜索结果，看是否有 arXiv 预印本已正式发表（更新期刊信息）。
3. **检查已排除论文是否仍然无关**：上一个迭代中标记为"已排除"的论文，如果发现其他论文引用了它，需要重新评估。
4. **增量搜索**：以新发现的关键词/作者为起点执行新的穷举搜索。
5. **记录迭代历史**：在 README 的头部信息中注明本次迭代新增/更新的论文数量（如"本次更新：+3 篇新论文"）。

### Step 6：迭代直到饱和（强制多轮）

**这是最重要的步骤，必须严格执行。** 单轮搜索通常只能覆盖 50-60% 的可用论文，需要通过多轮迭代才能逼近饱和。

1. **第一轮**：用初始关键词变体搜索，记录论文数量和覆盖面
2. **第二轮**：根据第一轮结果中新发现的关键词、作者、期刊、方法词，生成全新的查询变体，再次在所有渠道搜索
3. **第三轮及以后**：继续用新发现的关键词搜索。如果某轮新增论文 ≤3 篇，可以停止；否则继续
4. **至少完成 3 轮搜索**，即使第二轮已经达到 40 篇也要做第三轮（保证覆盖全面）
5. 每轮搜索必须使用不同的渠道组合和关键词角度，不能简单重复相同的查询
6. 每轮搜索结束后，更新论文计数并向用户简要汇报进度

---

## ⭐ 下载 PDF（关键步骤）

**核心原则**：对搜索到的每一篇论文，都必须执行以下下载优先级流程。**不允许跳过或批量忽略。**

### 优先级渠道（对每篇论文按此顺序逐一尝试）

1. **有 arXiv ID** → 直链下载（最可靠）：
   ```bash
   curl -L "https://arxiv.org/pdf/{id}.pdf" -o "papers/<keyword>/<title>.pdf"
   ```
   然后验证：`head -c 5 papers/<keyword>/<title>.pdf` 必须是 `%PDF-`

2. **paper-search CLI download** → 用 `semantic` 源或 `arxiv` 源：
   ```bash
   $PY download semantic <doi> -o papers/<keyword>/
   # 或
   $PY download arxiv <id> -o papers/<keyword>/
   ```

3. **Unpaywall**（标记"仅摘要"前的**必经步骤**）：
   ```bash
   curl "https://api.unpaywall.org/v2/{DOI}?email=zhangpe@buaa.edu.cn"
   ```
   如果 `is_oa = true`，用 `best_open_location.url` 下载。注意检查该 URL 是否可直接访问（有的需要 institutional login）。

4. **Crossref / OpenAlex** → 这两个源只提供元数据，**不尝试下载 PDF**。

### 🔴 重试机制（新增——强制）

下载失败后不能直接放弃，必须执行以下重试流程：

```bash
# 重试协议（伪代码逻辑）：
for each paper:
    尝试渠道1: arXiv 直链 (curl -L)
    if 失败（非 %PDF 或 pypdf 解析失败）:
        删除无效文件
        尝试渠道2: paper-search CLI download semantic
        if 失败:
            删除无效文件
            尝试渠道3: Unpaywall 查 OA
            if OA 可用:
                从 best_open_location.url 下载
            else:
                尝试渠道4: paper-search CLI download arxiv
                if 失败:
                    标记"所有自动下载渠道已尝试，最终失败"
```

具体操作规范：

1. **格式验证失败后立即重试**：`head -c 5` 检查不是 `%PDF-` → **立即删除文件**，换其他渠道重试。不允许保留无效文件
2. **pypdf 解析失败后立即重试**：PDF 下载完成但 pypdf 报告 `PdfStreamError: Stream has ended unexpectedly`（文件截断）→ 删除后重新下载同一个 arXiv ID，如果再次截断则换渠道
3. **最多尝试 3 个不同渠道**（arXiv 直链、semantic download、Unpaywall），全部失败才放弃
4. **记录重试历史**：在论文总结中注明尝试了几个渠道、每个渠道的结果，如 "arXiv 直链 403 → Semantic Scholar 返回 CAPTCHA → Unpaywall 非 OA → 最终失败"

### 🟡 下载失败后——即时告知用户（新增——强制）

**不要等到写完综述再告诉用户论文下载失败。** 必须在下载阶段就即时汇报。

当所有重试渠道都失败后，**立刻**判断论文重要性并采取对应行动：

1. **对于综述核心论文（⭐⭐⭐）**：**必须立即暂停所有下载/阅读流程**，以以下格式向用户汇报：
   ```
   ⚠️ 无法自动获取以下核心论文，请手动下载提供给我：

   标题：xxx
   DOI：xxx
   期刊：xxx | 年份：xxxx
   已尝试渠道：arXiv 直链(403) → Semantic Scholar(CAPTCHA) → Unpaywall(非OA)
   需要原因：该论文提供 xxx 方法/公式，综述 §X 部分需要其具体细节

   如您能下载，请将 PDF 放入 papers/<keyword>/ 目录
   ```
   **等待用户回复后再继续**，不能自行继续搜索或阅读其他论文。
2. **对于较重要论文（⭐⭐）**：同样以上述格式告知用户，可稍作等待后继续处理其他论文
3. **对于仅作补充的论文（⭐）**：标记为"仅摘要"，注明原因，继续流程
4. 在论文总结中注明失败原因：`无法获取全文（arXiv 直链 403，Semantic Scholar CAPTCHA，Unpaywall 非 OA）`
5. **只有穷尽所有渠道并（在必要时）告知用户后**，才能标记阅读程度为"仅摘要"

### 验证下载

#### Step 1：格式验证

Semantic Scholar API 经常返回 Radware Bot Manager CAPTCHA 页面（HTML）而非真实 PDF。下载后必须验证：

```bash
head -c 5 papers/<keyword>/<file>.pdf     # 输出 "%PDF-" 才是真的 PDF
```

如果返回 `<!DOC` 或 `{"error"` 等非 PDF 内容，立即删除，换其他渠道重试。

#### Step 1b：完整性验证（新增——必须执行）

格式验证通过后，还须用 pypdf 尝试解析，确认文件完整：

```bash
PYTHONIOENCODING=utf-8 "c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe" -X utf8 -c "
from pypdf import PdfReader
try:
    r = PdfReader('papers/<keyword>/<file>.pdf')
    print(f'OK: {len(r.pages)} pages')
except Exception as e:
    print(f'CORRUPT: {e}')
    # 退出码 1 让 bash 可以捕获
    exit(1)
"
echo "Exit code: $?"
```

如果 pypdf 报错 `PdfStreamError: Stream has ended unexpectedly` 或 `EOF marker not found`，说明**下载截断**。必须：
1. 删除该文件：`rm papers/<keyword>/<file>.pdf`
2. 换其他渠道重试（如用 paper-search CLI 而非 curl，或 vice versa）
3. 如果所有渠道都截断，按[下载失败后处理](#-重试机制新增强制)的流程处理

#### Step 2：主题验证（重要：避免误下不相关论文）

格式验证通过后，**必须快速阅读 PDF 首页的前面几段，确认论文内容与搜索主题匹配**。实际运行中发现 arXiv 上存在标题匹配但内容完全不相关（例如标题含"Gardner"但实际是 QFT/量子场论）的论文。

```bash
PYTHONIOENCODING=utf-8 "c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe" -X utf8 -c "
from pypdf import PdfReader
r = PdfReader('papers/<keyword>/<file>.pdf')
first_page = r.pages[0].extract_text()
print(first_page[:1500])
"
```

如果确认不相关，立即删除该文件并在论文列表中标注"已排除（不相关）"。

### 批量并行下载

为节省时间，对所有有 arXiv ID 的论文可以批量发起下载（在单条 bash 命令中用 `&` 并行）。但每篇都必须单独验证。

### 中文文件名

Git Bash 的 `curl -o` 对中文路径支持不稳定。建议先下载为临时文件名，然后用 Python 或 `mv` 重命名：

```bash
curl -L "https://arxiv.org/pdf/1234.5678.pdf" -o "papers/<keyword>/tmp.pdf"
PYTHONIOENCODING=utf-8 python -X utf8 -c "
import os
os.rename('papers/<keyword>/tmp.pdf', 'papers/<keyword>/真实标题.pdf')
"
```

### 重命名规范

下载后重命名为论文实际标题（截断 ~80 字符，移除 Windows 非法字符 `\ / : * ? " < > |`）。

---

## ⭐ 阅读论文（关键步骤）

**核心原则**：在写综述报告之前，你必须阅读所有成功下载的 PDF。**不允许写了"全文"但实际只看摘要。**

### 叙事文本（全文阅读）

```bash
PYTHONIOENCODING=utf-8 "c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe" -X utf8 -c "
from pypdf import PdfReader
r = PdfReader('papers/<keyword>/<file>.pdf')
for i, page in enumerate(r.pages):
    text = page.extract_text()
    print(f'--- Page {i+1} ({len(text)} chars) ---')
    print(text[:3000])
"
```

**说明**：
- `PYTHONIOENCODING=utf-8` 解决 GBK 编码错误（处理数学符号、Unicode 字符时必须加）
- `-X utf8` 确保 Python 内部也用 UTF-8
- 每次读取只读取部分页面，不要一次性读取大 PDF 全部页面（会超时）

### 表格（pdfplumber）

```bash
PYTHONIOENCODING=utf-8 "c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe" -X utf8 "c:/Users/porfi/.claude/skills/paper-search/pdf_extract.py" <pdf> --mode tables
```

### 图片 / 图表

**无法提取内容**。只能记录图注（caption）描述图表内容。

### 仅摘要的论文

对于付费墙后的论文，通过 paper-search CLI 的 `read` 命令获取摘要：
```bash
$PY read <source> <id> -o papers/<keyword>/
```

---

## 写综述报告

写入 `papers/<keyword>/README.md`。

### 核心原则

- 报告读起来像**小综述论文**——有组织、全面、覆盖每个相关侧面
- **必须包含一个叙述性的综述章节**放在报告开头，约 500-1500 字，按照主题组织（如可积性理论、精确解方法、变系数推广、物理应用），读起来像一篇真正的综述论文的引言，而不是论文列表的堆砌。分类表格和逐篇总结都是综述的支撑材料，综述本身才是核心。

### 综述写作的用户确认流程

**写综述不是闭门造车。** 以下是必须与用户交互的节点：

**第一步：写前提纲确认**
根据已读论文，写出综述的结构提纲（一级章节标题 + 每节一句话摘要），发给用户确认。例如：
```
1. 引言 — 方程形式、历史、物理背景
2. 可积性理论 — Lax对、Painlevé、标度对称性、等价变换
3. 精确解方法 — Hirota方法、DT、极限方法、Jacobi椭圆函数
4. 变系数推广 — 三类框架
5. 物理应用 — 等离子体、海洋、晶格
6. 孤子气体与怪波 — 统计描述、RW涌现
7. 高维与离散 — (2+1)-D, 半离散
8. 展望
```
用户可能要求调整结构或重点。

**第二步：写后可信度标注**
写完综述初稿后，逐节标注信息来源的可信度：
- 完全基于全文的段落标记为"可靠"
- 需要核实但基于摘要的段落标记为"待确认"
- 列出该段涉及但未获得全文的论文（带标题+DOI），请用户帮助获取

**第三步：缺口汇报**
向用户汇报：哪些核心论文仍缺失全文、综述中哪些关键论断因此无法验证。格式如下：
```
综述 §3（精确解方法）的以下论断仅基于摘要，不可靠：
  - "Roy 2025 通过 n 重 DT 构造了...解" — 需要全文核实公式和参数条件
  - 涉及论文：[标题] / DOI: xxx
```

- **综述写作参照高质量论文**：写综述前，先仔细阅读已下载全文的高质量论文（如已有的 survey/review 论文，以及该领域代表作（PRL、PR E、Nonlinear Dyn 等）的 Introduction 部分），学习它们的叙述方式、关键术语的定义、对领域发展的历史性描述。以此作为标杆来组织自己的综述。
- **综述的准确性和具体性**：综述中引用的每一条具体结论（如某个公式、某个特定数值结果、某个参数条件），必须来自你实际读过的全文。**仅从摘要推断的结论不可写入综述**。如果某篇核心论文只读了摘要但综述需要引用其具体发现，将该论文标记为需要用户手动获取。
- **每篇有全文的论文必须呈现"方程形式 + 核心方法 + 主要结果 + 特别之处"四个要素**：在逐篇总结中，必须以标准模板格式呈现这四部分信息（见[逐篇详细总结]模板）。方程形式要写出具体方程（LaTeX），主要结果要包含具体的公式和数值，特别之处要明确指出该论文的创新点（如"首次使用 XX 方法在 XX 系统中构造了 XX 解"）。
- **识别关键缺口并告知用户**：写完综述初稿后，扫描逐篇总结中标记为 ⭐⭐⭐ 但"仅摘要"的论文。将这些论文列表整理出来告知用户（含标题、DOI、期刊、为何必须获取全文），建议用户手动下载。
- **时间过滤**：超过 10 年的论文只在篇末单独列出（"更早的开创性文献"小节）
- **完整性检查**：写完后扫描已找到论文的参考文献列表，看是否遗漏重要工作
- **对于有全文的论文，总结必须基于实际阅读内容**，提取具体的方程、方法细节、数值结果等。不能写"研究/分析了某某问题"这种泛泛表述，必须给出该论文的**独特贡献和关键公式/发现**。
- **元数据不必追全**：缺失 DOI、精确页码、作者全名等不影响核心价值，不要花时间补这些
- **阅读程度必须如实**：只有实际下载并读了全文的才写"全文"；通过摘要了解到信息的写"仅摘要"（并注明原因）；什么都没获得的写"仅元数据"

### 模板结构

```markdown
# 文献搜索报告：<keyword>

> 搜索时间：<date> | 搜索平台：<sources>
> 论文总数：N（其中高质量期刊 M 篇，MDPI/低质量 P 篇）
> 可全文阅读：K | 仅摘要/元数据：其余

---

## 论文分类

### 分类一：[name] — 直接相关（⭐⭐⭐）
| # | 标题 | 作者 | 发表时间 | 来源/期刊 | 阅读程度 | 未获全文原因 |
|---|------|------|----------|-----------|----------|-------------|

### 分类二：[name] — 较相关（⭐⭐）
...

### 分类三：[name] — 一般相关（⭐）
...

## 逐篇详细总结

**注意：每一篇有全文的论文总结，必须体现以下四个要素：**
1. **方程形式**：论文研究的具体方程是什么？**必须写出方程本身**（至少用文字描述其形式，如"$u_t + \alpha(t)u^2u_x + \beta(t)u_{xxx}=0$ 形式的变系数 mKdV"），不应只说"研究 mKdV 方程"
2. **核心方法**：用了什么技术方法？（Darboux 变换、Hirota 双线性法、Painlevé 分析、Lie 对称性、Riemann-Hilbert 方法等）
3. **主要结果**：得到了什么具体结果？（显式解公式、数值模拟结果、参数条件等）**必须包含具体的量化信息**，不能只写"研究了……问题"
4. **特别之处/创新点**：该论文区别于其他同类工作的关键贡献是什么？（首次将 XX 方法推广到 XX 系统、发现了 XX 新现象、提出了 XX 新概念等）

**反面示例（太模糊，禁止）：**
- ❌ "研究/分析了变系数 mKdV 方程的可积性，得到了孤子解"——空洞无物
- ❌ "利用 Darboux 变换构造了孤子解，讨论了参数对解的影响"——没有具体解和参数信息
- ❌ "核心内容：该论文研究了变系数 mKdV 方程"——能具体点吗？

**正面示例（必须这样写）：**
- ✅ "方程形式：$u_t + \alpha(t)u^2u_x + \beta(t)u_{xxx} + \gamma(t)u_x = 0$，其中 $\alpha(t), \beta(t), \gamma(t)$ 为任意时间函数"
- ✅ "核心方法：从 Lax 对 $ \psi_{\xi\xi} + 2u\psi_{\xi} = 0, \psi_\tau + 2u_\xi\psi_\xi + 2u^2\psi_\xi - h(\tau)\psi_\xi = 0$ 出发，构造非局域对称性，通过辅助变量 $\phi = \psi_\xi$ 局域化为 Lie 点对称性"
- ✅ "关键结果：获得了孤子-cnoidal 波相互作用的显式解 $u = -\frac{m\,\text{dn}(\zeta,m)\,\text{cn}(\zeta,m)}{2(m\,\text{sn}(\zeta,m)+1)} + \cdots$，其中 $\zeta = \xi - \frac{m^2-5}{2}\tau + \int h(\tau)d\tau$"

### [序号]. [标题]
- **DOI**：xxx
- **作者**：xxx | **期刊**：xxx | **时间**：xxxx-xx
- **阅读程度**：全文 / 仅摘要 / 仅元数据
- **未获全文原因**：（仅当"仅摘要"时填写，注明尝试过的所有渠道和结果）
- **关联度**：⭐⭐⭐
- **方程形式**：（**必须写出具体方程**，如 $u_t + \alpha(t)u^2u_x + \beta(t)u_{xxx}=0$，不能只写"变系数 mKdV 方程"）
- **核心方法**：（Darboux 变换、Hirota 双线性、Painlevé 分析、Lie 对称性等具体方法）
- **核心内容**（3-5 句，基于实际阅读，包含具体方法细节和公式，禁止空洞描述）：
- **特别之处/创新点**：（该论文区别于其他工作的关键贡献，如"首次将XX方法推广到XX系统"）
- **关键发现/结论**（列出具体的量化结果、公式、方法细节，不要只说"分析了XX问题"）：
- **PDF**：`./xxxx.pdf`

## 分析方法与方法论总结

## 术语与知识点汇总

## 下载的 PDF 文件列表

## 补充：更早的开创性文献（>10 年）
```

---

## PaperQA2 RAG — 已下载 PDF 的深度问答

> ⚠️ PaperQA2 **不是搜索工具**。它只对接 Semantic Scholar + Crossref，搜索范围远不如 paper-search 的穷举策略。它只在 PDF 下载完成后有用。

```bash
export PATH="$PATH:/c/Users/porfi/AppData/Roaming/Python/Python314/Scripts"

# 导入 PDF
papi add --pdf papers/<keyword>/<paper>.pdf

# 建索引
papi index --backend pqa

# 提问
papi ask "具体问题" \
  --llm "deepseek/deepseek-v4-flash" \
  --llm-config '{"reasoning_effort": "max", "max_tokens": 32000}' \
  -t 0.1 --evidence-k 20 --max-sources 10 -s high_quality
```

---

## 故障排查（Troubleshooting）

| 症状 | 原因 | 解决 |
|------|------|------|
| `UnicodeEncodeError: 'gbk'` | Git Bash 默认 GBK 编码 | 命令前加 `PYTHONIOENCODING=utf-8`，Python 加 `-X utf8` |
| `python: command not found` | Python 不在 Git Bash PATH | 用全路径 `c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe` |
| 下载的 .pdf 打不开 | Semantic Scholar 返回了 HTML CAPTCHA | `head -c 5` 确认开头是 `%PDF`；不是则删除重试 |
| `paper-search download crossref` 失败 | CrossRef 不托管 PDF | 换 `semantic` 或 `arxiv` 源 |
| `papi` 命令不存在 | PATH 没加 | `export PATH="$PATH:/c/Users/porfi/AppData/Roaming/Python/Python314/Scripts"` |
| arXiv PDF 下载慢/失败 | 中国网络到 arXiv 不稳定 | 用 WebSearch 或 Semantic Scholar 替代 |
| PDF 下载了但 pypdf 报"Stream has ended unexpectedly" | 后台 curl 进程仍占用文件或下载截断 | 先等几秒让后台进程结束；仍失败则删除文件，换 paper-search CLI 下载（`$PY download arxiv <id>`）；仍截断则换 Semantic Scholar 渠道 |
| 下载的 PDF 被 Windows 锁定无法重命名 | 后台 bash 进程仍持有文件句柄 | `sleep 5` 后再试；用 Python 的 `os.rename()` 而非 `mv` 命令 |
| 搜索到的论文太少（<30 篇） | 关键词不够多或渠道不足 | 必须再搜至少 2 轮：增加关键词变体（同义词、缩写、方法词、相关概念）、用不同渠道（GS CDP、出版商 site 搜索等）|
| 下载的 PDF 标题匹配但内容不相关 | arXiv 上存在标题含某关键词但实际是另一领域的论文 | 下载后必须用 pypdf 阅读首页确认主题；不相关则删除 |
| Google Scholar 显示"unusual traffic" | 搜索频率过高被 ban | 立即停止，等至少 24 小时，未来用更慢的频率 |
| Google Scholar CAPTCHA | 自动化检测触发 | 让用户手动完成 CAPTCHA，之后降低搜索频率 |

---

## Google Scholar 补充搜索（仅当 CLI + WebSearch 覆盖不足时）

GS 的 CLI 接口已损坏，但 **Edge + CDP 方式可用**（2026-05 实测，连续 5 个查询变体未触发 CAPTCHA）。使用现有 Edge profile + 合理频率 = 成功的关键。

### 完整 CDP 搜索流程

```bash
# Step 1: 关闭所有 Edge 进程，重新以 CDP 模式启动
/c/Windows/System32/taskkill.exe //F //IM msedge.exe
"/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" --remote-debugging-port=9222 --no-first-run --new-window "about:blank" &
sleep 5
/c/Windows/System32/curl.exe -s http://localhost:9222/json/version

# Step 2: 创建新标签页并导航到 GS 搜索
/c/Windows/System32/curl.exe -s -X PUT "http://localhost:9222/json/new?https://scholar.google.com/scholar?q=YOUR_QUERY&hl=en&as_ylo=2016"
# 方法返回的 id 字段就是 tab id

# Step 3: 用 Python websockets 通过 WebSocket 提取搜索结果
PYTHONIOENCODING=utf-8 "c:/Users/porfi/AppData/Local/Programs/Python/Python313/python.exe" -X utf8 -c "
import asyncio, json, websockets, urllib.request

async def extract_gs(tab_id):
    # 获取 WebSocket URL
    resp = urllib.request.urlopen('http://localhost:9222/json')
    tabs = json.loads(resp.read())
    ws_url = next(t['webSocketDebuggerUrl'] for t in tabs if t['id'] == tab_id)
    
    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        await asyncio.sleep(3)  # 等待页面加载
        
        req = {
            'id': 1, 'method': 'Runtime.evaluate',
            'params': {
                'expression': '''
                (() => {
                    const results = document.querySelectorAll('.gs_ri');
                    return JSON.stringify(Array.from(results).map(r => ({
                        title: r.querySelector('.gs_rt a')?.textContent?.trim() || '',
                        link: r.querySelector('.gs_rt a')?.href || '',
                        authors: r.querySelector('.gs_a')?.textContent?.trim().substring(0,200) || '',
                        snippet: r.querySelector('.gs_rs')?.textContent?.trim().substring(0,300) || ''
                    })));
                })()
                ''',
                'returnByValue': True
            }
        }
        await ws.send(json.dumps(req))
        resp = json.loads(await ws.recv())
        items = json.loads(resp['result']['result']['value'])
        for i, item in enumerate(items):
            print(f'{i+1}. {item[\"title\"][:70]}')

asyncio.run(extract_gs('<tab_id>'))
"
```

### 搜索规则
1. 一次只查一个查询、一个标签页；查完立即关闭标签页（而非整个 Edge）
2. 两次查询间隔至少 30 秒，使用 `asyncio.sleep(3)` 等页面完全加载
3. 用 `?hl=en`（英文界面）避免中文搜索结果量过少
4. 使用多个查询变体（见 6 步穷举法），每个变体单独建标签页
5. 看到 CAPTCHA → 让用户手动完成；看到 "unusual traffic" → **立即完全停止**，至少 24 小时内不再尝试

### 工作原理
- CDP 在 port 9222 上暴露 WebSocket 接口，通过 `websockets` Python 库交互
- 使用**默认 Edge profile**（不加 `--user-data-dir`），这样 GS 看到的是已登录的浏览器，降低触发 CAPTCHA 概率
- 纯 HTTP 接口（`/json/new`、`/json/version`）可用 curl，但页面交互（evaluate JS）必须走 WebSocket
- GS 的 CLI MCP 接口仍损坏，不要尝试
