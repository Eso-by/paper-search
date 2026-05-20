# Positon 技术链分析报告：n-孤子 → 光滑 Positon → 呼吸子 / 退化呼吸子

## 技术路线全景

```
n-Soliton (离散谱)
    │
    ├── 谱参数退化 (λⱼ→λ₁) ──────────────→ Smooth Positon (光滑 Positon)
    │         (Darboux 退化极限 / Hirota 极限)
    │
    ├── 模共振 (λ = -λ*) + 谱参数退化 ──→ Breather-Positon (b-Positon)
    │         (零背景)
    │
    └── 双重退化 (λⱼ→λ₁→λ₀) ────────────→ Rational Solution / Rogue Wave
              (周期种子 → b-positon → 有理解/怪波)
```

---

## 一、按方法论分类

### A. 使用 Darboux 变换退化极限的论文 (谱参数凝聚 / 退化 DT)

| # | 论文 | 年份 | 方程 | 退化类型 | 笔记 |
|---|------|------|------|---------|------|
| 1 | **He 2017 (Xing-Wu-Mihalache-He)** — Smooth positon solutions of the focusing mKdV | 2017 | 聚焦实 mKdV | λⱼ→λ₁ 退化 DT + 高阶 Taylor 展开 | **奠基性工作**。给出 n 重 Darboux 变换行列式表示，n-孤子→n-光滑 positon。建立分解方法、弯曲轨迹、时变相移三大标准研究范式。 |
| 2 | **Xing 2017** — Construction of rational solutions of the real mKdV from its periodic solutions | 2017 | 实 mKdV | **双重退化**：(1) λⱼ→λ₁ 周期解→breather-positon；(2) λ₁→λ₀ 周期→∞→rational sol. | 与 He 2017 互补：He 从零种子+退化得 smooth positon；本文从周期种子+两步退化得 b-positon→有理解 |
| 3 | **Liu 2018** — Dynamics of the smooth positons of the complex mKdV | 2018 | 复 mKdV | λ₂ⱼ₋₁→λ₁ 退化 DT | 首次将 smooth positon 推广到 cmKdV。引入**模平方分解法**（不是解分解，而是模平方分解）。首提时变相移 ~ ln(t²) |
| 4 | **Zhang 2020a** — Soliton molecules and novel smooth positons for cmKdV | 2020 | 复 mKdV | 半退化 DT（部分特征值退化） | 速度共振得孤子分子 + 非零种子得**有理 Positon**（相移 ~ t¹/³，非对数）。半退化 DT → 孤子分子与光滑 positon 混合解 |
| 5 | **Zhang 2020b** — Novel soliton molecules and breather-positon on zero background for cmKdV | 2020 | 复 mKdV | 退化 DT + **模共振** (λ₄ₖ₊₁ = -λ*₄ₖ₊₃) | **首获零背景 b-positon**。此前 Wang 2017 的 b-positon 在非零背景（NLS），Qiu-Cheng 2019 的 Kundu-Eckhaus b-positon 也在非零背景 |
| 6 | **Wang 2017** — Generation of higher-order rogue waves from multibreathers by double degeneracy | 2017 | NLS | **双重退化** DT | **提出"b-positon"概念**（breather-positon）和"双重退化"机制。多 breather → b-positon → 高阶 rogue wave。虽对象是 NLS，但机制具跨方程普适性 |
| 7 | **Song 2019** — Generating mechanism and dynamic of smooth positons for DNLS | 2019 | DNLS | λⱼ→λ₁ 退化 DT | 将 He 2017 方法论系统推广到导数 NLS 方程。相移 ~ ln(t⁴)（比 mKdV 的 ln(t²) 更剧烈） |
| 8 | **Huang 2021** — Soliton Molecules, Rational Positon and Rogue Waves for Extended cmKdV | 2021 | ecmKdV | 退化 DT + 双重退化 DT | 从周期种子通过双重退化 DT 获高阶 rogue wave。将有理 positon 从标准 cmKdV 推广到 ecmKdV |
| 9 | **Liu 2025** — Soliton, breathers, positons and rogue waves for vector cmKdV | 2025 | vcmKdV | 多重特征值退化 DT | 首次将 positon 推广到三分量向量 mKdV |
| 10 | **Monisha 2024** — Degenerate soliton solutions in coupled Hirota equation | 2024 | 耦合 Hirota | 退化 DT + 平波背景 breather-positon | 首次在耦合 Hirota 系统中报道 breather-positon 解。发现弹性和非弹性碰撞共存 |
| 11 | **Liu 2025 (TOFGI)** — Darboux transformation, positon and breather of third-order flow GI equation | 2025 | TOFGI | λⱼ→λ₁ 退化 DT | 将退化 DT 用于 GI 方程的高阶流。比较了 TOFGI 与 GI 的 positon 速度与轨迹差异 |
| 12 | **Vishnu Priya 2025** — Hybrid solutions of mKdV and predictions through deep learning | 2025 | 实/复 mKdV | 退化 DT → 退化孤子 | **PINN 预测退化孤子**。与传统 DT 结合的深度学习新方向 |
| 13 | **Wang 2025** — RH problem and multiple high-order poles solutions of focusing mKdV with NZBC | 2025 | 聚焦 mKdV (NZBC) | **Riemann-Hilbert 方法** + 高阶极点 | 多高阶极点等价于 positon 的谱参数凝聚。首次用 RH 方法处理 mKdV NZBC 下的多高阶极点解 |
| 14 | **Rahman & He 2026** — Degenerate Darboux transformations for PCF equation | 2026 | PCF | 退化 DT | 将 He 2017 框架推广到主手征场方程，验证退化 DT 的跨系统普适性 |
| 15 | **Yuan 2023** — Semi-rational solutions of (2+1)D cmKdV | 2023 | (2+1)D cmKdV | 半退化 DT（λ₂ₖ₋₁→λ₀） | 半有理解构造方法与 positon 的退化 DT 完全相同，获四类混合解 |

### B. 使用 Hirota 双线性方法的论文

| # | 论文 | 年份 | 方程 | 方法细节 | 笔记 |
|---|------|------|------|---------|------|
| 1 | **Zhang 2021** — Construction of higher-order smooth positons and breather positons via Hirota's bilinear method | 2021 | 实 mKdV | Hirota bilinear + 极限法：k₂=k₁+ε, η₁⁰含 ε⁻¹, ε→0 | **核心优势**：比 GDT 更简单快速，能区分亮/暗 positon（β>0亮/β<0暗）。**局限**：无法给出 n 阶光滑 positon 的通式。复数参数下构建 breather-positon |
| 2 | **Zhang 2026** — Construction of soliton solutions for weakly bound states of higher-order mKdV | 2026 | 高阶 mKdV | Hirota bilinear + 解析极限过程 | 多重极点解等价于 positon。参数约束：k₂=k₁+ε, η₂⁰=η₁⁰+ln(ε)/2。推广 Zhang 2021 方法到高阶 mKdV |
| 3 | **Raut 2023** — Non-autonomous Gardner equation: solitons, positons and breathers | 2023 | Gardner（含mKdV型三次项） | Hirota bilinear + BT | 构造二阶/三阶光滑 positon 和 breather-positon。考虑阻尼和外力对 positon 的影响 |
| 4 | **Hu 2025** — N-breather solution for cmKdV | 2025 | 复 mKdV | 双线性 KP 约化 + 广义长波极限 | 提供与 positon 方法互补的 KP 约化方法 |
| 5 | **Ren 2020** — Soliton molecules and CRE method in extended mKdV | 2020 | 扩展 mKdV | CRE/CTE 方法 | 非 DT 路线的孤子分子构造和周期波相互作用 |
| 6 | **Zhao 2023** — Soliton molecules for combined mKdV-type bilinear equation | 2023 | 组合 mKdV | Hirota bilinear + 速度共振 | 孤子分子与 positon 的方法学互参照 |

> **关键对比**：Darboux 退化极限可给出紧凑行列式通式但计算复杂；Hirota 极限法对单次计算更便捷但无通式。两者结果等价（多重极点解 = positon）。

---

## 二、Breather-Positon (b-Positon) 与退化呼吸子专题

### b-Positon 研究的时间线

```
2017 Wang & He (NLS) ──→ 首次提出 b-positon 概念 + 双重退化机制
                          （非零背景）
                              │
2017 Xing et al. (mKdV) ───→ mKdV 的 b-positon（双重退化，周期种子背景）
                              │
2019 Qiu & Cheng (KE) ─────→ Kundu-Eckhaus 方程的退化 breather/b-positon
                              │
2020 Zhang et al. (cmKdV) ──→ 首获零背景 b-positon（模共振 λ = -λ*）
                              │
2021 Zhang et al. (mKdV) ───→ Hirota 双线性法构建 breather-positon
                              │
2022 Lv & Huang (ecmKdV) ──→ 扩展 cmKdV 的 breather-孤子分子和 breather-positon
                              │
2022 Monisha et al. (NLS) ──→ 扩展 NLS（三次+四次）高阶 breather-positon
                              │
2024 Monisha et al. (coupled Hirota) → 耦合 Hirota 方程首次报道 breather-positon
                              │
2025 Sinthuja et al. (KE) ──→ 非线性电传输线中 KE 方程的 breather 和 positon
```

### 文件夹中涉及 b-Positon / 退化呼吸子的论文

| 论文 | b-positon 类型 | 背景 | 构造方法 | 关键结论 |
|------|---------------|------|---------|---------|
| **Wang 2017** | 多重breather退化 | 非零背景 (NLS) | 双重退化DT | 提出b-positon概念；双重退化链：multi-breather→b-positon→rogue wave |
| **Xing 2017** | breather-positon | 周期种子背景 (mKdV) | 双重退化DT | 第一步λⱼ→λ₁：周期解→b-positon；第二步λ₁→λ₀：b-positon→有理解 |
| **Zhang 2020b** | **零背景 b-positon** | 零背景 (cmKdV) | 模共振λ=-λ* + 退化DT | **首次零背景b-positon**。相移比同阶smooth positon更剧烈 |
| **Zhang 2021** | breather-positon | 零背景 (mKdV) | Hirota极限法 | 复数参数下构造breather-positon；周期→∞可转化为smooth positon |
| **Monisha 2024** | breather-positon | 平波背景 (耦合Hirota) | 退化DT | 耦合系统中首次b-positon报告；中央区域有rogue wave状局域增强 |
| **Vishnu Priya 2025** | 退化孤子（退化breather） | 零背景 (mKdV) | 退化DT | PINN预测退化孤子；八类碰撞类型分类 |
| **Huang 2021** | b-positon→rogue wave | 周期种子 (ecmKdV) | 双重退化DT | 三种rogue wave模式：基础、三角、环 |

---

## 三、核心论文的参考文献追踪

### 3.1 He 2017 — 参考文献分析

**He 2017** 共引用 73 篇文献。关键引用链：

**Positon 开创性文献（Matveev 学派）：**
- Matveev 1992 (Phys. Lett. A 166, 205) — **广义 Wronskian 公式，首次提出 positon 概念** → 未在文件夹
- Matveev 1992 (Phys. Lett. A 166, 209) — Positon-positon 和 soliton-positon 碰撞 → 未在文件夹
- Matveev 2002 (Theor. Math. Phys. 131, 483) — Positon: slowly decreasing analogue of solitons → 未在文件夹

**mKdV Positon 先驱：**
- Stahlhofen 1992 (Ann. Phys. 504, 554) — mKdV 方程 positon 最早的论文（奇异 positon） → 未在文件夹
- Maisch & Stahlhofen 1995 (Phys. Scr. 52, 228) — Positon 动态性质 → 未在文件夹

**多重极点解基础：**
- Wadati & Ohkuma 1982 (J. Phys. Soc. Jpn. 51, 2029) — mKdV 多重极点解 → 未在文件夹
- Takahashi & Konno 1989 (J. Phys. Soc. Jpn. 58, 3585) — mKdV 双极点解和 breather 解 → 未在文件夹
- Takahashi & Konno 1989 (J. Phys. Soc. Jpn. 58, 3505) — Hirota 方法下的 N-双极点解 → 未在文件夹
- Olmedilla 1987 (Physica D 25, 330) — NLS 多重极点解 → 未在文件夹

**团队前期工作：**
- He 2014 (PRE 89, 062917) — 复 mKdV 少周期光学怪波 → 未在文件夹
- He 2013 (PRE 87, 052914) — 高阶 rogue wave 产生机制 → 未在文件夹

**与文件夹重叠：** He 2017 引用的论文中，Stahlhofen 1992（mKdV positon）和 Wadati 1982（多重极点解）是重要但不在文件夹中的早期文献。Matveev 的开创性工作（1992a, 1992b）也未在文件夹中，建议获取。

> **建议获取（不在文件夹）：**
> 1. Matveev 1992 (Phys. Lett. A) — 正本清源的 positon 概念原始论文
> 2. Stahlhofen 1992 (Ann. Phys.) — mKdV positon 最早工作（奇异 positon）
> 3. Wadati & Ohkuma 1982 (J. Phys. Soc. Jpn.) — 多重极点解与 positon 的联系
> 4. Takahashi & Konno 1989 (J. Phys. Soc. Jpn.) — mKdV 双极点解

### 3.2 Xing 2017 — 参考文献分析

**Xing 2017** 共引用 72+ 篇文献，聚焦双重退化从周期解构造有理解。

**关键引用：**
- He 2014 (PRE 89, 062917) — 复 mKdV 怪波（**同团队前期**）
- Matveev 1992a,b — Positon 原始概念
- Stahlhofen 1992 — mKdV positon
- Chowdhury 2016 (Eur. Phys. J. D 70, 104) — mKdV 周期解和有理解 → 未在文件夹
- Ankiewicz 2010 (PRE 81, 046602) — Hirota 方程的有理解和怪波 → 未在文件夹
- Dubard & Matveev 2011 — KP-I 多怪波解 → 未在文件夹
- Guo & Ling 2011 — 广义 Darboux 变换和怪波解 → 未在文件夹

**与文件夹重叠：** 基本同 He 2017，无新增文件夹包含的论文引用。

> **建议获取（不在文件夹）：**
> 5. Chowdhury, Ankiewicz, Akhmediev 2016 (Eur. Phys. J. D) — mKdV 周期/有理解
> 6. Guo & Ling 2011 (PRE 85) — 广义 Darboux 变换（GDT）原始论文

### 3.3 Zhang 2020a — 参考文献分析

**Zhang 2020a** (Soliton molecules and novel smooth positons) 引用 15 篇。

**关键引用链（退化方法和 positon）：**
- Liu 2018 — **在文件夹** ✅ Dynamics of smooth positons of cmKdV
- Song 2019 — **在文件夹** ✅ DNLS smooth positons
- Qiu & Cheng 2019 — **摘要，不在文件夹** ❌ Kundu-Eckhaus 退化 breather
- He 2014 — 复 mKdV 怪波 → 不在文件夹
- Lou 2019 — 孤子分子速度共振理论 → 未在文件夹

**直接引用：**
- [4] Lou 2019 (arXiv) — 速度共振的孤子分子理论 → **建议获取**
- [6] Qiu & Cheng 2019 (AML 98, 13) — Kundu-Eckhaus 退化 breather → 仅摘要
- [13] He 2013 (PRE 87, 052914) — 高阶怪波产生机制 → 不在文件夹

> **建议获取（不在文件夹）：**
> 7. Lou 2019 (arXiv:1909.03399) — 速度共振孤子分子原始论文，Zhang 2020a 的方法论基础
> 8. Qiu & Cheng 2019 (AML 98, 13-21) — Kundu-Eckhaus 退化 breather（摘要已有）

### 3.4 Zhang 2020b — 参考文献分析

**Zhang 2020b** (Novel soliton molecules and breather-positon on zero background) 引用 40 篇。

**关键引用链：**
- Wang 2017 — **在文件夹** ✅ 双重退化/ b-positon 原始概念
- Qiu & Cheng 2019 — **摘要** ❌ Kundu-Eckhaus 退化 breather
- Liu 2018 — **在文件夹** ✅ cmKdV smooth positon
- Song 2019 — **在文件夹** ✅ DNLS smooth positon
- Matveev 1992a,b — Positon 原始论文 → 不在文件夹
- Beutler, Stahlhofen, Matveev 1994 — Soliton, breather, positon 共同基础 → 不在文件夹
- Serkin & Belyaeva 2018 — cmKdV 呼吸子新条件 → 不在文件夹

**模共振（breather 构造的核心）的引用来源：**
- [34] Serkin & Belyaeva 2018 (Optik 172, 1117) — cmKdV 呼吸子条件 → **建议获取**
- [35-37] Serkin & Belyaeva 2018 — Hirota、cmKdV 呼吸子系列 → **建议获取**

> **建议获取（不在文件夹）：**
> 9. Serkin & Belyaeva 2018 (Optik 172, 1117) — 模共振条件原始论文
> 10. Beutler, Stahlhofen, Matveev 1994 (Phys. Scr. 50, 9) — Soliton、breather、positon 的关系

### 3.5 Zhang 2021 — 参考文献分析

**Zhang 2021** (Hirota's bilinear method) 引用 26 篇。

**关键引用链：**
- Liu 2018 — **在文件夹** ✅ cmKdV smooth positon
- Xing/He 2017 — **在文件夹** ✅ Smooth positon of mKdV（He 2017）
- Wang 2017 — **在文件夹** ✅ 双重退化/b-positon
- Zhang 2020a — **在文件夹** ✅ Soliton molecules and novel smooth positons
- Zhang 2020b — **在文件夹** ✅ Novel soliton molecules and breather-positon
- Xing 2017 — **在文件夹** ✅ Construction of rational solutions
- Matveev 1992a,b — Positon 原始概念 → 不在文件夹
- Wadati & Ohkuma 1982 — 多重极点解 → 不在文件夹
- Takahashi & Konno 1989 — Hirota 法 N-双极点解 → 不在文件夹
- Chen & Pelinovsky 2018 (Nonlinearity 31, 1955) — mKdV 周期怪波 → 不在文件夹

> **建议获取（不在文件夹）：**
> 11. Chen & Pelinovsky 2018 (Nonlinearity 31, 1955) — mKdV 周期怪波/有理解

---

## 四、完整技术链论文分类总结

### 4.1 n-孤子 → 光滑 Positon（谱参数退化）

| 论文 | 方法 | 方程 | 特色 |
|------|------|------|------|
| He 2017 | 🔷 退化DT | 聚焦实mKdV | **奠基**：行列式通式 + 分解方法 + 相移 ~ ln(64t²)/4 |
| Liu 2018 | 🔷 退化DT | 复mKdV | 模平方分解法，相移 ~ ln(t²) |
| Song 2019 | 🔷 退化DT | DNLS | 推广到导数NLS，相移 ~ ln(t⁴) |
| Zhang 2021 | 🟢 Hirota极限 | 实mKdV | 简单快速，区分亮/暗 |
| Zhang 2026 | 🟢 Hirota极限 | 高阶mKdV | 多重极点解=positon，推广到高阶mKdV |
| Raut 2023 | 🟢 Hirota+BT | Gardner | 非自治系统(阻尼+外力) |
| Liu 2025 | 🔷 退化DT | vcmKdV | 三分量向量推广 |
| Li 2024 | 🔷 退化DT | 短脉冲方程 | 推广到短脉冲模型 |
| Zhang 2024 | 🔷 GDT | 高阶NLS | 光纤光学应用 |
| Wang 2025 | 🔶 RH方法 | mKdV(NZBC) | 非零边界条件的多高阶极点 |

**图例：** 🔷 = Darboux 变换退化极限，🟢 = Hirota 双线性方法，🔶 = Riemann-Hilbert 方法

### 4.2 光滑 Positon → 有理 Positon（非零种子）

| 论文 | 方法 | 方程 | 特色 |
|------|------|------|------|
| Zhang 2020a | 🔷 退化DT+q=c种子 | cmKdV | 相移~t¹/³（幂函数vs对数），不能模平方分解 |
| Huang 2021 | 🔷 退化DT+q=c种子 | ecmKdV | 推广到扩展cmKdV |

### 4.3 n-孤子 → 零背景 Breather → Breather-Positon（模共振 + 退化）

| 论文 | 方法 | 方程 | 特色 |
|------|------|------|------|
| Zhang 2020b | 🔷 模共振(λ=-λ*)+退化DT | cmKdV | **首获零背景b-positon**，b-positon+smooth positon混合 |
| Zhang 2021 | 🟢 Hirota极限(复数参数) | mKdV | 零背景breather-positon |
| Monisha 2024 | 🔷 退化DT+平波背景 | 耦合Hirota | 耦合系统b-positon，弹性和非弹性碰撞 |

### 4.4 双重退化链：Breather → b-Positon → Rogue Wave / 有理解

| 论文 | 方法 | 方程 | 退化步骤 |
|------|------|------|---------|
| Wang 2017 | 🔷 双重退化DT | NLS | multi-breather → b-positon(λⱼ→λ₁) → rogue wave(λ₁→λ₀) |
| Xing 2017 | 🔷 双重退化DT | 实mKdV | 周期解 → b-positon(λⱼ→λ₁) → 有理解(λ₁→λ₀) |
| Huang 2021 | 🔷 双重退化DT | ecmKdV | 周期种子 → b-positon → 高阶rogue wave |

### 4.5 退化呼吸子（Degenerate Breather）专题

退化呼吸子是指多重 breather 通过谱参数退化极限得到的态，通常是 b-positon 的前身或中间态。

| 论文 | 类型 | 方程 | 方法 |
|------|------|------|------|
| Wang 2017 | N重breather退化 | NLS | λⱼ→λ₁退化极限 |
| Xing 2017 | 周期解→breather→有理解 | 实mKdV | 双重退化 |
| Qiu & Cheng 2019 | n阶退化breather | Kundu-Eckhaus | n重DT退化极限 |
| Zhang 2026 | 多重极点breather退化 | 高阶mKdV | Hirota双线性+解析极限 |
| Hu 2025 | N-breather解 | cmKdV | KP约化+长波极限 |
| Vishnu Priya 2025 | 二阶/三阶退化孤子 | mKdV | 退化DT+PINN预测 |

---

## 五、文件夹文献 vs 外部引文对照表

### 已在文件夹中的关键文献 ✅

| 简称 | 全名 | 方法角色 |
|------|------|---------|
| He 2017 | Smooth positon of focusing mKdV | 🔷 Darboux 退化DT奠基 |
| Xing 2017 | Rational solutions from periodic solutions | 🔷 双重退化（mKdV） |
| Liu 2018 | Dynamics of smooth positons of cmKdV | 🔷 cmKdV推广，模平方分解 |
| Zhang 2020a | Soliton molecules and novel smooth positons for cmKdV | 🔷 有理positon |
| Zhang 2020b | Novel soliton molecules and breather-positon on zero background | 🔷 零背景b-positon |
| Zhang 2021 | Construction via Hirota's bilinear method | 🟢 Hirota方法 |
| Wang 2017 | Generation of higher-order rogue waves by double degeneracy | 🔷 双重退化/b-positon概念 |
| Song 2019 | Smooth positons for DNLS | 🔷 DNLS推广 |
| Huang 2021 | Soliton Molecules, Rational Positon, Rogue Waves for ecmKdV | 🔷 ecmKdV |
| Monisha 2024 | Degenerate soliton in coupled Hirota | 🔷 耦合Hirota |
| Vishnu Priya 2025 | Hybrid solutions + deep learning | 🔷 mKdV退化孤子+PINN |
| Liu 2025 (vcmKdV) | Vector cmKdV positon | 🔷 三分量向量 |
| Wang 2025 (NZBC) | RH problem for mKdV with NZBC | 🔶 RH方法 |
| Zhang 2026 (weakly bound) | Weakly bound states of higher-order mKdV | 🟢 Hirota多重极点 |
| Ren 2020 | Soliton molecules and CRE method | CRE方法 |
| Raut 2023 | Non-autonomous Gardner | 🟢 Hirota+BT |
| Liu 2025 (TOFGI) | Darboux transformation of GI equation | 🔷 退化DT |
| Sinthuja 2025 | Breather and Positon in KE transmission line | 电路应用 |
| Rahman & He 2026 | Degenerate DT for PCF | 🔷 退化DT推广 |

### 值得进一步获取的关键外部文献 🔴

| # | 文献 | 年份 | 期刊 | 重要性 | 理由 |
|---|------|------|------|--------|------|
| 1 | **Matveev VB** — Generalized Wronskian formula for solutions of the KdV equations: first applications | 1992 | Phys. Lett. A 166, 205 | ⭐⭐⭐ | **Positon 概念的源头**，所有正谱解研究的理论基石 |
| 2 | **Matveev VB** — Positon-positon and soliton-positon collisions: KdV case | 1992 | Phys. Lett. A 166, 209 | ⭐⭐⭐ | 碰撞特性的首次分析，"超反射less"概念来源 |
| 3 | **Stahlhofen AA** — Positons of the modified Korteweg-de Vries equation | 1992 | Ann. Phys. 504, 554 | ⭐⭐⭐ | **mKdV positon 最早工作**（奇异 positon），He 2017 的对比基准 |
| 4 | **Wadati & Ohkuma** — Multiple-pole solutions of the modified Korteweg-de Vries equation | 1982 | J. Phys. Soc. Jpn. 51, 2029 | ⭐⭐⭐ | 多重极点解=positon的谱等价性，Zhang 2021/2026的核心参考 |
| 5 | **Takahashi & Konno** — N-double pole solution for mKdV by Hirota's method | 1989 | J. Phys. Soc. Jpn. 58, 3505 | ⭐⭐ | Hirota 法构建多重极点解的原始工作，Zhang 2021 的方法论先驱 |
| 6 | **Lou SY** — Soliton molecules and asymmetric solitons in fluid systems via velocity resonance | 2019 | arXiv:1909.03399 | ⭐⭐⭐ | 孤子分子速度共振的原始论文，Zhang 2020a/b 的核心方法论来源 |
| 7 | **Serkin & Belyaeva** — Novel conditions for soliton breathers of cmKdV | 2018 | Optik 172, 1117 | ⭐⭐⭐ | **模共振条件**的原始论文，Zhang 2020b 零背景b-positon的基础 |
| 8 | **Guo & Ling** — Nonlinear Schrodinger equation: Generalized Darboux transformation and rogue wave solutions | 2012 | PRE 85, 026607 | ⭐⭐⭐ | **广义 Darboux 变换 (GDT)** 的标准参考 |
| 9 | **Beutler, Stahlhofen, Matveev** — What do solitons, breathers and positons have in common? | 1994 | Phys. Scr. 50, 9 | ⭐⭐ | 三类解的统一理论框架 |
| 10 | **Chen & Pelinovsky** — Rogue periodic waves of the modified KdV equation | 2018 | Nonlinearity 31, 1955 | ⭐⭐ | mKdV 周期怪波，与 Xing 2017 形成互补 |
| 11 | **Chowdhury, Ankiewicz, Akhmediev** — Periodic and rational solutions of mKdV | 2016 | Eur. Phys. J. D 70, 104 | ⭐⭐ | mKdV 周期解/有理解 |
| 12 | **Matveev VB** — Positons: slowly decreasing analogue of solitons | 2002 | Theor. Math. Phys. 131, 483 | ⭐⭐ | positon 理论综述 |
| 13 | **Qiu & Cheng** — The nth-order degenerate breather solution for KE equation | 2019 | Appl. Math. Lett. 98, 13 | ⭐⭐ | 退化 breather 方法（已有摘要） |

---

## 六、关于"从 n-孤子出发"的技术链完整性评估

### 6.1 完整覆盖的技术链环节

```
n-Soliton
    │
    ├── [He 2017, Liu 2018, Zhang 2021] ✅ → Smooth Positon (相移~ln t)
    │      利用 λⱼ→λ₁ 退化，n-孤子行列式→n-positon 行列式
    │
    ├── [Zhang 2020a, Huang 2021] ✅ → Rational Positon (相移~t¹/³)  
    │      非零种子+退化，与经典 smooth positon 本质不同
    │
    ├── [Zhang 2020b, Zhang 2021] ✅ → Zero-background b-Positon
    │      模共振 λ=-λ* 将孤子→breather，再加退化→b-positon
    │
    ├── [Xing 2017, Wang 2017] ✅ → Double Degeneration
    │      period/breather → b-positon → rational/rogue wave
    │
    └── [Vishnu Priya 2025] ✅ → PINN prediction of degenerate solitons
            AI方法预测退化孤子/混合解
```

### 6.2 技术链中的缺失环节

1. **n-孤子 → n-breather 的显式谱条件**：尽管 Zhang 2020b 使用了模共振条件 λ₄ₖ₊₁ = -λ*₄ₖ₊₃ 将 n-孤子转变为 n-breather，但对该条件的系统谱分析（特别是 breather 的分类和共振条件的一般化）在文件夹中较为薄弱。建议获取 **Serkin & Belyaeva 2018** 系列论文，它们是模共振条件的原始来源。

2. **非零边界条件（NZBC）下的 positon 完整理论**：Wang 2025 的 RH 方法虽然覆盖了 NZBC 的多高阶极点解，但该方法与非零种子下的退化 DT 之间的等价性尚未系统建立。

3. **从 breather 到 b-positon 再到 rogue wave 的连续过渡的严格数学描述**：Wang 2017 和 Xing 2017 的"双重退化"为两步极限，但两步之间的连续过渡（b-positon 逼近 rogue wave 的速率）的描述不够系统。

4. **向量/耦合系统的 positon 分类学**：Liu 2025 (vcmKdV) 和 Monisha 2024 (耦合 Hirota) 虽有突破，但向量 positon 的分类体系仍未建立（亮-亮-亮、亮-暗-亮等组合的全面分类）。

---

## 七、各论文对方法链的具体贡献（按技术路线排序）

### 路线1：谱参数退化路线（n-孤子 → 光滑 Positon）

```
He 2017:
  n-fold DT + 行列式 → λⱼ→λ₁ + 高阶Taylor展开 → n-光滑positon
  ├── 分解：n-positon → Σ 单孤子(H±cᵢ(t))
  ├── 相移：c₁ = -ln(64t²)/4
  └── 轨迹：x + t ± ln(64t²)/4 = 0

Liu 2018:
  推广到复mKdV
  ├── 模平方分解：|qₙ₋ₚ|² → Σ|q₁₋ₛ(H±cᵢ(t))|²
  ├── 关键区别：q₁₋ₛ(H±cᵢ) 不是 cmKdV 的解
  └── 相移：1-positon ~ ln(t²)；2-positon ~ ln(t⁴)

Song 2019:
  推广到DNLS方程
  ├── 相移 ~ ln(t⁴)（比mKdV更剧烈）
  └── 混合解：1-positon+2-positon, 2-positon+2-positon, 1-soliton+3-positon

Zhang 2021:
  Hirota双线性+极限法（替代GDT）
  ├── 优势：简单快速，区分亮/暗（β>0亮，β<0暗）
  ├── 局限：无通式
  └── 等价性：Hirota多重极点解 ≡ DT退化positons
```

### 路线2：Breather-Positon 路线（n-孤子 → Breather → b-Positon → 退化 Breather）

```
Wang 2017 (NLS):
  双重退化DT
  ┌── Step 1: n-breather (λⱼ=λ₁+εⱼ) → b-positon (λⱼ→λ₁)
  │           特征：空间周期→∞，轮廓平滑，中央类rogue wave结构
  └── Step 2: b-positon (λ₁) → rogue wave (λ₁→λ₀, φ(λ₀)=0)
              特征：周期→∞，局域化程度增加

Xing 2017 (mKdV):
  双重退化DT（与Wang 2017平行）
  ┌── Step 1: n-周期解(常数种子+n-DT) → b-positon (λⱼ→λ₁)
  └── Step 2: b-positon → n阶有理解 (λ₁→λ₀, φ(λ₀)=0)
      验证：b-positon 是有理解的优良近似

Zhang 2020b (cmKdV):
  模共振 + 退化DT（零背景）
  ┌── 模共振：n-孤子 → n-零背景breather (λ₄ₖ₊₁ = -λ*₄ₖ₊₃)
  ├── 退化DT：n-零背景breather → m阶零背景b-positon
  ├── 相移：b-positon 相移比同阶 smooth positon 更剧烈
  └── 混合解：b-positon与smooth positon的弹性碰撞
```

### 路线3：混合与推广路线

```
Zhang 2020a:
  半退化DT（部分特征值退化）
  ├── 速度共振 → 孤子分子（同高度孤子绑定）
  ├── 半退化DT → 孤子分子与smooth positon混合解
  └── 非零种子+退化DT → 有理positon（相移~t¹/³）

Huang 2021:
  双重退化DT在ecmKdV上的实现
  └── 周期种子 → b-positon → 三种模式rogue wave（基础/三角/环）

Monisha 2024:
  耦合Hirota系统
  ├── 零背景：各阶positon + positon-positon碰撞（时变相移）
  ├── 平波背景：首次耦合系统b-positon
  └── 弹性和非弹性碰撞共存
```

---

## 八、研究空白与前沿方向

1. **向量 mKdV 的 b-positon 理论**：Liu 2025 在 vcmKdV 中构造了 positon，但未涉及 b-positon。向量系统的模共振条件及其导致的 b-positon 尚未被研究。

2. **b-positon 向量的 norming constant 理论**：Rybkin 2023 从 KdV 的规范常数角度给出了有界 positon 的理论基础，但 b-positon 的类似理论尚未建立。

3. **非零边界条件（NZBC）下的 b-positon**：Wang 2025 的 RH 方法处理了 NZBC 下的多高阶极点解（即 positon），但 NZBC 下的 b-positon 和双重退化尚未涉及。

4. **退化的连续谱参数化**：当前所有退化 DT 都采用 λⱼ = λ₁ + εⱼ 的等距退化。更一般的非等距退化参数化及其对 positon 结构的影响尚需研究。

5. **深度学习方法在 b-positon 预测中的应用**：Vishnu Priya 2025 的 PINN 方法仅用于退化孤子（positon）预测，尚未推广到 b-positon 和双重退化链。

---

## 附录：PDF 文件名与论文对应关系

| PDF 文件名 | 简称 | 方法分类 |
|-----------|------|---------|
| Smooth positon solutions of the focusing mKdV equation - Xing Wu Mihalache He 2017.pdf | He 2017 | 🔷 退化DT |
| Construction of rational solutions of the real mKdV equation from its periodic solutions - Xing Wang Mihalache Porsezian He 2017.pdf | Xing 2017 | 🔷 双重退化DT |
| Construction of higher-order smooth positons and breather positons via Hirotas bilinear method mKdV - Zhang Li Chen Guo 2021.pdf | Zhang 2021 | 🟢 Hirota |
| Soliton molecules and novel smooth positons for the complex modified KdV equation.pdf | Zhang 2020a | 🔷 半退化DT |
| Novel soliton molecules and breather-positon on zero background for the complex modified KdV equation.pdf | Zhang 2020b | 🔷 模共振+退化DT |
| Generation of higher-order rogue waves from multibreathers by double degeneracy - Wang He 2017.pdf | Wang 2017 | 🔷 双重退化DT（NLS） |
| Dynamics of the smooth positons of the complex modified KdV equation.pdf | Liu 2018 | 🔷 退化DT |
| Generating mechanism and dynamic of smooth positons for DNLS equation - Song Xu Li He 2019.pdf | Song 2019 | 🔷 退化DT |
| Soliton Molecules, Rational Positon Solution and Rogue Waves for the Extended Complex Modified KdV Equation.pdf | Huang 2021 | 🔷 退化DT |
| Soliton breathers positons and rogue waves for vector cmKdV - Liu Zhang Li 2025.pdf | Liu 2025 | 🔷 退化DT |
| Degenerate soliton solutions in coupled Hirota equation - Monisha 2024.pdf | Monisha 2024 | 🔷 退化DT |
| Hybrid solutions of real and complex modified Korteveg-de Vries equations and their predictions through deep learning algorithm.pdf | Vishnu Priya 2025 | 🔷 退化DT+PINN |
| Construction of soliton solutions for weakly bound states of the higher-order mKdV equation.pdf | Zhang 2026 | 🟢 Hirota |
| Riemann-Hilbert Problem and Multiple High-order Poles Solutions of the Focusing mKdV Equation with Nonzero Boundary Conditions.pdf | Wang 2025 | 🔶 RH方法 |
| A non-autonomous Gardner equation and its integrability Solitons, positons and breathers.pdf | Raut 2023 | 🟢 Hirota+BT |
| Darboux transformation positon and breather of third-order flow GI equation - Liu 2025.pdf | Liu 2025 (TOFGI) | 🔷 退化DT |
| Breather and Positon excitations in nonlinear transmission line Kundu-Eckhaus - Sinthuja 2025.pdf | Sinthuja 2025 | 🔷 推广（电路） |
| Soliton molecules and CRE method in extended mKdV - Ren Lin Liu 2020.pdf | Ren 2020 | CRE方法 |
| Norming constants of embedded bound states and bounded positon solutions of KdV - Rybkin 2023.pdf | Rybkin 2023 | 理论（有界positon） |
| Numerical inverse scattering transform for coupled mKdV equation - Zhang Chen 2026.pdf | Zhang 2026 (NIST) | 数值方法 |
| Negaton and positon solutions of the KdV and mKdV hierarchy - Rasinariu Sukhatme Khare 1996.pdf | Rasinariu 1996 | 早期分类学 |

---

*报告生成时间：2026-05-16*
*分析范围：C:\Users\porfi\Desktop\工作文档\Lax\改稿子\papers\positon-mkdv\（23篇PDF + README）*
