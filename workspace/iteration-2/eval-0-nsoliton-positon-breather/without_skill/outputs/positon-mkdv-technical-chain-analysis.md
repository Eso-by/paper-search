# Positon-mKDV 技术路线链分析报告

## 技术路线概览

关注的技术链：**N-孤子解 → 光滑Positon（谱参数退化/特征值凝聚） → Breather/退化呼吸子（模共振或双重退化）**

这条链包含三个核心环节：
1. **N-孤子解**：通过 Darboux 变换（DT）或 Hirota 双线性方法从种子解生成
2. **Smooth Positon**：特征值凝聚 λ_j → λ_1（谱参数退化），高阶泰勒展开消除奇点，从 N-孤子得到 N-positon
3. **Breather / Degenerate Breather / b-Positon**：两种路径——
   - 路径A（模共振）：λ = -λ* 将孤子转为零背景呼吸子
   - 路径B（双重退化）：λ_j → λ_1 → λ_0，从周期解经 b-positon 到有理解/rogue wave

---

## 一、按方法分类

### (1) 使用 Darboux 变换退化极限的论文（核心方法）

| # | 论文 | 方程 | 种子解 | 退化类型 | 文件夹状态 |
|---|------|------|--------|---------|-----------|
| 1 | **Xing, Wu, Mihalache, He 2017** (Nonlinear Dynamics) | 聚焦实 mKdV | 零种子 | λ_j → λ_1 单步退化 | **PDF 在文件夹** |
| 2 | **Liu, Zhang, He 2018** (Waves Random Complex Media) | 复 mKdV | 零种子 | λ_{2j-1} → λ_1 单步退化 | **PDF 在文件夹** |
| 3 | **Zhang, Yang, Li 2020** (Appl. Math. Lett.) | 复 mKdV | 零种子+非零种子 | 半退化DT（部分λ退化） | **PDF 在文件夹** |
| 4 | **Xing, Wang, Mihalache, Porsezian, He 2017** (Chaos) | 实 mKdV | 常数种子（周期） | **双重退化**：λ_j→λ_1→λ_0 | **PDF 在文件夹** |
| 5 | **Song, Xu, Li, He 2019** (Nonlinear Dynamics) | 导数 NLS | 零种子 | λ_j → λ_1 单步退化 | **PDF 在文件夹** |
| 6 | **Huang, Lv 2021** (Nonlinear Dynamics) | 扩展 cmKdV | 零/周期种子 | 退化+双重退化DT | **PDF 在文件夹** |
| 7 | **Liu, Zhang, Li 2025** (arXiv) | 向量 cmKdV (3-分量) | 零种子 | 多重特征值退化 | **PDF 在文件夹** |
| 8 | **Liu, Li, Dong, Li 2025** (Chinese Phys. B) | 三阶流 GI | 零种子 | λ_j → λ_1 单步退化 | **PDF 在文件夹** |
| 9 | **Monisha et al. 2024** (arXiv) | 耦合 Hirota | 零/平波背景 | 退化DT + b-positon | **PDF 在文件夹** |
| 10 | **Sinthuja et al. 2025** (arXiv) | Kundu-Eckhaus | 零种子 | 退化DT + 外部势 | **PDF 在文件夹** |
| 11 | **Rybkin 2023** (Commun. Math. Phys.) | KdV | — | Binary DT（有界positon） | **PDF 在文件夹** |
| 12 | **Rahman, He 2026** (Phys. Lett. A) | PCF方程 | — | 退化DT | 摘要（不完整） |
| 13 | **Yuan 2023** (NP) | (2+1)D cmKdV | — | 退化DT→半有理解 | 摘要 |
| 14 | **Vishnu Priya 2025** (Nonlinear Dynamics) | 实/复 mKdV | 零种子 | 退化DT（退化解=positon）+ PINN | **PDF 在文件夹** |
| 15 | **Li, Li, Geng 2023** (Nonlinear Dynamics) | 一般向量 mKdV | — | 多重DT | 摘要 |
| 16 | **Wang, Tian, Yang 2025** (Acta Math. Appl. Sinica) | 聚焦 mKdV (NZBC) | 非零边界 | RH方法→多高阶极点（=positon） | **PDF 在文件夹** |

### (2) 使用 Hirota 双线性方法的论文

| # | 论文 | 方程 | 方法细节 | 文件夹状态 |
|---|------|------|---------|-----------|
| 1 | **Zhang, Li, Chen, Guo 2021** (Nonlinear Dynamics) | 实 mKdV | k₂=k₁+ε, η含ε⁻¹, ε→0 → positon | **PDF 在文件夹** |
| 2 | **Zhang, Teng, Li 2026** (Physica Scripta) | 高阶 mKdV | 同法+多重极点+退化breather | **PDF 在文件夹** |
| 3 | **Raut, Ma, Barman, Roy 2023** (Chaos Solitons Fractals) | 非自治 Gardner | Hirota+BT+极限法 | **PDF 在文件夹** |
| 4 | **Hu, Gegen 2025** (Chinese Phys. B) | 复 mKdV | KP双线性约化→N-breather | 摘要 |
| 5 | **Ren, Lin, Liu 2020** (Commun. Theor. Phys.) | 扩展 mKdV | CRE/CTE方法（非DT） | **PDF 在文件夹** |

### (3) 涉及 b-positon (breather-positon) 和退化呼吸子的论文

| # | 论文 | 方程 | b-positon 类型 | 关键机制 | 文件夹状态 |
|---|------|------|---------------|---------|-----------|
| 1 | **Xing et al. 2017** (Chaos) | 实 mKdV | 常数种子→b-positon | λ_j→λ_1（第一步） | **PDF 在文件夹** |
| 2 | **Wang, He et al. 2017** (PRE) | NLS | **首次定义 b-positon** | 双重退化 | **PDF 在文件夹** |
| 3 | **Zhang, Yang, Li 2020** (Nonlinear Dynamics) | 复 mKdV | **首个零背景 b-positon** | 模共振+退化 | **PDF 在文件夹** |
| 4 | **Zhang, Li, Chen, Guo 2021** (Nonlinear Dynamics) | 实 mKdV | Hirota构造 b-positon | 复数参数+极限 | **PDF 在文件夹** |
| 5 | **Raut et al. 2023** (Chaos Solitons Fractals) | Gardner | Hirota构造 b-positon | 极限法 | **PDF 在文件夹** |
| 6 | **Monisha et al. 2024** (arXiv) | 耦合 Hirota | 平波背景 b-positon | 退化DT | **PDF 在文件夹** |
| 7 | **Qiu, Cheng 2019** (Commun. Nonlinear Sci.) | Kundu-Eckhaus | 退化breather/b-positon | n重退化DT | 摘要 |
| 8 | **Yuan 2020** (Nonlinear Dynamics) | NLS-MB | b-positon | 退化DT | 摘要 |
| 9 | **Yang, Tian 2022** (Nonlinear Dynamics) | 离散NLS | b-positon | 退化DT | 摘要 |
| 10 | **Monisha et al. 2022** (CSF) | 扩展NLS (cubic+quartic) | b-positon | 退化DT | 摘要 |
| 11 | **Vishnu Priya et al. 2022** (Eur. Phys. J. Plus) | 广义NLS | b-positon | 退化DT | 摘要 |
| 12 | **Li, He, Li 2024** (Nonlinear Dynamics) | 复短脉冲 | b-positon | 退化DT | 摘要 |
| 13 | **Zhang, Wang, Yang 2024** (Phys. Scr.) | 高阶NLS | b-positon | 广义DT | 摘要 |
| 14 | **Wang, Zhang 2025** (Wave Motion) | 变系数Kundu-NLS | 非自治b-positon | 退化DT | 摘要 |

---

## 二、核心论文逐篇方法描述

### 1. He 2017: Xing, Wu, Mihalache, He — "Smooth positon solutions of the focusing mKdV equation"
- **期刊**: Nonlinear Dynamics, Vol. 89, pp. 2299-2310 (2017)
- **PDF**: `Smooth positon solutions of the focusing mKdV equation - Xing Wu Mihalache He 2017.pdf`
- **方法**: N重Darboux变换的行列式表示 + 退化极限 λ_j → λ_1
- **具体做法**:
  - 从Lax对出发，构造n重DT的显式行列式公式（n-soliton解）
  - 令所有特征值 λ_j → λ_1（谱参数凝聚），利用高阶Taylor展开消除0/0不定式
  - 从N-孤子解获得非奇异N-positon解（封闭公式 Eq. 20）
  - 研究大|t|渐近分解：2-positon ≈ q_{1-s}(H + c₁) + q_{1-s}(H - c₁)
  - 提取时变相移 c₁ = -ln(64t²)/4 和弯曲轨迹 x + t ± ln(64t²)/4 = 0
- **技术链位置**: 奠基性工作。完整实现了**N-孤子 → smooth positon**的第一步退化。
- **种子解**: 零种子（zero seed）
- **未覆盖**: 未涉及呼吸子或b-positon（仅处理了零种子下的孤子→positon）

### 2. Xing et al. 2017: Xing, Wang, Mihalache, Porsezian, He — "Construction of rational solutions of the real mKdV equation from its periodic solutions"
- **期刊**: Chaos, Vol. 27, 053102 (2017)
- **PDF**: `Construction of rational solutions of the real mKdV equation from its periodic solutions - Xing Wang Mihalache Porsezian He 2017.pdf`
- **方法**: 双重退化 Darboux 变换
- **具体做法**:
  - 从常数种子解（平面波）出发，由n重DT产生n阶多重周期解
  - **第一步退化** λ_j → λ_1：多周期解 → **breather-positon (b-positon)**
  - **第二步退化** λ_1 → λ_0（φ(λ_0)=0，使周期→∞）：b-positon → n阶有理（rogue）解
  - 两步退化机制与 Wang-He 2017 (PRE) 在NLS方程的双重退化平行，但对象是mKdV
- **技术链位置**: 实现了**周期解 → b-positon → 有理解/rogue wave**的完整双重退化链。b-positon是其关键中间态。
- **种子解**: 常数种子（plane wave / periodic background）
- **与He 2017的关系**: 互补。He 2017从零种子+λ_j→λ_1得smooth positon；本文从常数种子+两步退化得b-positon和有理解。

### 3. Liu, Zhang, He 2018 — "Dynamics of the smooth positons of the complex modified KdV equation"
- **期刊**: Waves in Random and Complex Media, Vol. 28, pp. 203-214 (2018)
- **PDF**: `Dynamics of the smooth positons of the complex modified KdV equation.pdf`
- **方法**: 退化 Darboux 变换（扩展到复系统）
- **具体做法**:
  - 将He 2017的smooth positon方法论从实mKdV推广到复mKdV（cmKdV：q_t + q_xxx + 6|q|^2 q_x = 0）
  - 零种子下退化DT：λ_{2j-1} → λ_1，获得n阶光滑positon的行列式公式（Proposition 1）
  - **首创模平方分解方法**：|q_{n-p}|^2 ≈ Σ |q_{1-s}(H ± c_{ij})|^2（大|t|极限下）
  - 研究了复数特征值（λ = ξ + iη）情况下的弯曲轨迹和时变相移
- **技术链位置**: 将N-孤子→smooth positon链从实mKdV推广到复mKdV，扩展了适用范围。

### 4. Zhang, Yang, Li 2020a — "Soliton molecules and novel smooth positons for the complex modified KdV equation"
- **期刊**: Applied Mathematics Letters, Vol. 103, 106168 (2020)
- **PDF**: `Soliton molecules and novel smooth positons for the complex modified KdV equation.pdf`
- **方法**: 退化DT + 速度共振 + 半退化DT
- **具体做法**:
  - **速度共振**（λ₁ = -λ₃）构造相同高度孤子分子
  - **半退化DT**（部分特征值退化、部分不变）构造孤子分子与光滑高阶positon的弹性相互作用
  - **有理positon（rational positon）**: 从非零种子 q = c 发现，与经典smooth positon本质不同
    - 有理positon公式：q_{1-r} = -c + 4c/(4c²H² + 1)
    - 相移尺度 ~ t^{1/3}（幂函数），而经典positon ~ ln t（对数函数）
- **技术链位置**: 引入新类型的positon（有理positon），将谱参数退化技术推广到混合解构造。
- **种子解**: 零种子 + 非零种子 c

### 5. Zhang, Yang, Li 2020b — "Novel soliton molecules and breather-positon on zero background for the complex modified KdV equation"
- **期刊**: Nonlinear Dynamics, Vol. 100, pp. 1551-1557 (2020)
- **PDF**: `Novel soliton molecules and breather-positon on zero background for the complex modified KdV equation.pdf`
- **方法**: 模共振 + 退化DT
- **具体做法**:
  - **模共振条件** λ_{4k+1} = -λ*_{4k+3}：将N-孤子解转变为**零背景breather**（此前breather都在非零背景上）
  - **breather分子**: 同时施加模共振+速度共振
  - **零背景b-positon**: 在模共振后的breather上施加退化极限，首次在零背景上获得b-positon
  - **b-positon + smooth positon混合解**: 退化DT + 部分模共振，展示两类positon的弹性相互作用
  - b-positon相移比同阶smooth positon更剧烈（Remark 1）
- **技术链位置**: 实现了**N-孤子 → 零背景breather（模共振）→ b-positon（退化极限）**路径的关键链接。完整覆盖了技术链第三步。
- **种子解**: 零种子

### 6. Zhang, Li, Chen, Guo 2021 — "Construction of higher-order smooth positons and breather positons via Hirota's bilinear method"
- **期刊**: Nonlinear Dynamics, Vol. 105, pp. 2611-2618 (2021)
- **PDF**: `Construction of higher-order smooth positons and breather positons via Hirotas bilinear method mKdV - Zhang Li Chen Guo 2021.pdf`
- **方法**: Hirota 双线性方法 + 解析极限
- **具体做法**:
  - 核心技巧：令2-孤子参数 k₂ = k₁ + ε，同时调整 η₁⁽⁰⁾ 含 ε⁻¹ 项
  - ε→0 的极限从双线性N-孤子解中提取高阶光滑positon（无需构建广义DT）
  - β > 0 → 亮（bright）smooth positon，β < 0 → 暗（dark）smooth positon（DT方法无法直接区分）
  - 复数参数下构造了breather-positon
- **技术链位置**: 提供了与DT互补的全新方法论——Hirota双线性极限法构建positon。覆盖了N-孤子→smooth positon和b-positon。
- **与DT对比**: 优点：简单快速，可控制亮暗；缺点：无n阶通式

### 7. Wang, He et al. 2017 — "Generation of higher-order rogue waves from multibreathers by double degeneracy in an optical fiber"
- **期刊**: Physical Review E, Vol. 95, 042217 (2017)
- **PDF**: `Generation of higher-order rogue waves from multibreathers by double degeneracy - Wang He 2017.pdf`
- **方法**: 双重退化DT（在NLS方程上，非mKdV，但机制普适）
- **具体做法**:
  - **首次提出"双重退化"机制**
  - 第一步 λ_j → λ_1：n重breather（周期解）→ **b-positon**（首次定义）
  - 第二步 λ_1 → λ_0：b-positon → 高阶rogue wave
  - 提出了在光纤中用频率梳+Waveshaper实验观测高阶rogue wave的方案
  - b-positon是连接breather和rogue wave的中间态
- **技术链位置**: 揭示了**breather-b-positon-rogue wave**三者之间的理论联系。b-positon概念首次在此定义。虽然对象是NLS，但双重退化机制具有跨方程普适性。

### 8. Zhang, Teng, Li 2026 — "Construction of soliton solutions for weakly bound states of the higher-order mKdV equation"
- **期刊**: Physica Scripta, Vol. 101, 195202 (2026)
- **PDF**: `Construction of soliton solutions for weakly bound states of the higher-order mKdV equation.pdf`
- **方法**: Hirota双线性 + 解析极限
- **具体做法**:
  - 从N-孤子解出发，通过参数约束（k₂ = k₁ + ε, η₂⁽⁰⁾ = η₁⁽⁰⁾ + ln(ε)/2 等）获得多重极点解（double, triple, quadruple pole）
  - N阶退化breather的一般条件（Corollary 3.1）
  - 通过对数分离验证双峰距 ∝ ln|t|，确认多重极点解与positon等价
  - k_j扩展到实数域（DT方法限定在纯虚数）
  - 亮暗通过γ符号控制（同Zhang 2021的β符号机制）
- **技术链位置**: 提供了Hirota框架下的**多重极点解（=positon）+ 退化breather**的完整构造路径，将正谱解推广到高阶mKdV系统。

### 9. Raut et al. 2023 — "A non-autonomous Gardner equation: solitons, positons and breathers"
- **期刊**: Chaos, Solitons & Fractals, Vol. 176, 114089 (2023)
- **PDF**: `A non-autonomous Gardner equation and its integrability Solitons, positons and breathers.pdf`
- **方法**: Hirota + 双线性Baecklund变换
- **具体做法**:
  - 在Gardner方程（含mKdV型三次非线性项）中构造positon和b-positon
  - 二阶/三阶光滑positon、b-positon、positon-孤子相互作用解
  - 研究阻尼和外力对positon/breather的影响
- **技术链位置**: 将技术链推广到非自治+Dissipative系统

### 10. Monisha et al. 2024 — "Degenerate soliton solutions and their interactions in coupled Hirota equation with trivial and nontrivial background"
- **期刊**: arXiv:2401.03815 (2024)
- **PDF**: `Degenerate soliton solutions in coupled Hirota equation - Monisha 2024.pdf`
- **方法**: 退化DT
- **具体做法**:
  - 耦合Hirota方程中构建退化解：零背景→各阶positon
  - 平波背景→**首次在耦合Hirota系统中报道breather-positon解**
  - 发现弹性与非弹性碰撞共存现象
- **技术链位置**: 将positon/b-positon链推广到耦合可积系统

### 11. Vishnu Priya et al. 2025 — "Hybrid solutions of real and complex modified Korteweg-de Vries equations and their predictions through deep learning algorithm"
- **期刊**: Nonlinear Dynamics (2025)
- **PDF**: `Hybrid solutions of real and complex modified Korteveg-de Vries equations and their predictions through deep learning algorithm.pdf`
- **方法**: 退化DT + PINN深度学习
- **具体做法**:
  - 系统构造实/复mKdV的混合解（孤子+退化孤子即positon）
  - 八类碰撞类型分类（Table 2，取决于λ₁符号组合）
  - 首次用PINN预测高阶退化孤子和混合解，MSE验证
- **技术链位置**: 将PINN方法与退化孤子（=positon）构造结合，代表深度学习方向的推广

### 12. Liu, Zhang, Li 2025 — "Soliton, breathers, positons and rogue waves for the vector cmKdV equation"
- **期刊**: arXiv:2510.03062 (2025)
- **PDF**: `Soliton breathers positons and rogue waves for vector cmKdV - Liu Zhang Li 2025.pdf`
- **方法**: 多重特征值退化DT
- **具体做法**:
  - 三分量cmKdV（4x4 Lax对）
  - 多重特征值退化获得全局有界解：N-positon、N-breather、N阶rogue wave
  - 首次将positon推广到三分量向量系统
- **技术链位置**: 将完整技术链（孤子→positon→breather→rogue wave）推广到向量系统

---

## 三、技术路线完整链的覆盖

### 链1：N-孤子 → Smooth Positon（谱参数退化）

```
He 2017 (mKdV, DT退化) ────  Liu 2018 (cmKdV, DT退化)
    │                              │
    ├── Zhang 2020 AML (半退化DT)  ├── Zhang 2020 AML (cmKdV有理positon)
    ├── Song 2019  (DNLS)         ├── Huang 2021 (ecmKdV, DT+退化)
    ├── Qiu 2019 (KE, DT退化)      ├── Monisha 2024 (耦合Hirota, DT退化)
    └── Liu 2025 (TOFGI)          └── Liu 2025 (向量cmKdV, DT退化)

Hirota替代方法:
Zhang 2021 (mKdV, Hirota极限) ──── Zhang 2026 (高阶mKdV, Hirota多重极点) ──── Raut 2023 (Gardner, Hirota)
```

### 链2：Smooth Positon → Breather-Positon / 退化呼吸子

**路径A：模共振（零背景）**
```
Zhang 2020b:  λ_{4k+1} = -λ*_{4k+3}  →  零背景breather  →  退化 → 零背景b-positon
```

**路径B：双重退化（非零背景）**
```
Xing 2017 (mKdV):  λ_j → λ_1 → λ_0  →  周期解 → b-positon → 有理解
Wang 2017 (NLS):   λ_j → λ_1 → λ_0  →  multibreather → b-positon → rogue wave
Huang 2021 (ecmKdV): 双重退化DT → 周期种子→rogue wave
```

### 链3：技术链在各类方程中的完整性

| 方程 | 孤子→positon | b-positon | 退化呼吸子 | 参考文献 |
|------|-------------|-----------|-----------|---------|
| 实mKdV | Yes (He 2017, Zhang 2021) | Yes (Xing 2017) | Yes (Xing 2017) | 全部在文件夹 |
| 复mKdV | Yes (Liu 2018, Zhang 2020) | Yes (Zhang 2020b) | Yes (Zhang 2020b) | 全部在文件夹 |
| 扩展cmKdV | Yes (Huang 2021) | Yes (Lv Huang 2022) | Yes (Huang 2021) | 仅Huang在文件夹 |
| 向量cmKdV | Yes (Liu 2025) | (Liu 2025 breather) | (Liu 2025 rogue) | 在文件夹 |
| NLS | Yes (推广) | Yes (Wang 2017) | Yes (Wang 2017) | Wang在文件夹 |
| DNLS | Yes (Song 2019) | — | — | 在文件夹 |
| KE方程 | Yes (Qiu 2019) | Yes (Qiu 2019) | Yes (Qiu 2019) | 摘要 |
| 耦合Hirota | Yes (Monisha 2024) | Yes (Monisha 2024) | — | 在文件夹 |
| 高阶mKdV | Yes (Zhang 2026) | Yes (Zhang 2026) | Yes (Zhang 2026) | 在文件夹 |
| Gardner | Yes (Raut 2023) | Yes (Raut 2023) | Yes (Raut 2023) | 在文件夹 |
| GI/TOFGI | Yes (Liu 2025) | — | — | 在文件夹 |

---

## 四、参考链追踪

### 4.1 He 2017 引用文献中与退化/positon/b-positon相关的关键文献

| 在He 2017中的引用编号 | 文献 | 在文件夹中？ | 备注 |
|---------------------|------|------------|------|
| [44-45] = [52-53] | Matveev 1992, Phys. Lett. A — Generalized Wronskian / Positon-positon collisions | No | 经典开创性文献，positon概念起源 |
| [52] | Stahlhofen 1992, Ann. Phys. — Positons of the mKdV | No | mKdV positon最早的工作（奇异positon） |
| [55] | Dubard et al. 2010, Eur. Phys. J. Special Topics — Multi-rogue wave & positon | No | 连接positon与rogue wave |
| [67] | Wadati & Ohkuma 1982, J. Phys. Soc. Jpn. — Multiple-pole solutions of mKdV | No | 多重极点解（positon等价概念） |
| [69-70] | Takahashi & Konno 1989 — N-double pole for mKdV via Hirota's method | No | Hirota方法多重极点 |
| [44] | He et al. 2013, PRE — Generating mechanism for higher-order rogue waves | No | 高阶rogue wave生成机制（He团队前期工作） |
| [57] | Maisch & Stahlhofen 1995, Phys. Scr. — Dynamic properties of positons | No | 早期positon动力学 |
| [58] | Beutler 1993, J. Math. Phys. — sine-Gordon positon solutions | No | 另一方程的positon |
| [56] = [48] | Stahlhofen 1992, Ann. Phys. — mKdV positons | No | 同上，重复引用 |
| [51] | He et al. 2014, PRE — Few-cycle optical rogue waves: cmKdV | No | He团队前期cmKdV工作 |

### 4.2 Xing 2017 引用文献中与退化/positon相关的关键文献

| 在Xing 2017中的引用编号 | 文献 | 在文件夹中？ | 备注 |
|----------------------|------|------------|------|
| [44-45] | Matveev 1992 — Wronskian / Positon collisions | No | 经典开创性 |
| [48] | Stahlhofen 1992 — mKdV positons | No | 早期mKdV positon |
| [52] | Matveev 2002, Theor. Math. Phys. — Positons: slowly decreasing analogue | No | Matveev后期综述 |
| [53] | Chowdury, Ankiewicz, Akhmediev 2016, Eur. Phys. J. D — Periodic & rational solutions of mKdV | No | 周期解→有理解的连接 |
| [59] | Guo, Ling, Liu 2011, PRE — Generalized DT and rogue wave solutions for NLS | No | 广义DT（将标准DT推广到退化情况）— **值得获取** |
| [68] | He et al. 2013, PRE — Generating mechanism for higher-order rogue waves | No | 同上，He团队前期工作 |
| [69] | Kibler et al. 2010, Nat. Phys. — Peregrine soliton in optical fibre | No | 实验观察 |
| [54] | Ablowitz & Satsuma 1978 — Solitons and rational solutions | No | 有理解方法学基础 |

### 4.3 Zhang 2021 (Hirota) 引用文献中与退化/positon相关的关键文献

| 在Zhang 2021中的引用编号 | 文献 | 在文件夹中？ | 备注 |
|------------------------|------|------------|------|
| [11-12] | Matveev 1992 | No | 经典 |
| **13** | **Liu, Zhang, He 2018** — cmKdV smooth positons | **Yes** | 重要引用 |
| **14** | **Xing, Wu, Mihalache, He 2017** — mKdV smooth positons (He 2017) | **Yes** | 核心引用 |
| **15** | **Wang, He et al. 2017** — Double degeneracy / b-positon | **Yes** | 核心引用 |
| [16] | Wadati & Ohkuma 1982 — Multiple-pole of mKdV | No | 多重极点解先导 |
| [17] | Wu, Zhang, Hang 2021, AML — Breather & double-pole of 5th-order mKdV | No | **值得获取** |
| **18** | **Zhang, Yang, Li 2020** — Novel soliton molecules/b-positon (ND) | **Yes** | 核心引用 |
| **19** | **Zhang, Yang, Li 2020** — AML smooth positons | **Yes** | 核心引用 |
| [22] | Takahashi & Konno 1989 — N-double pole via Hirota | No | Hirota多重极点先驱 |
| **23** | **Xing, Wang, Mihalache, Porsezian, He 2017** — Chaos (双重退化) | **Yes** | 核心引用 |
| [24] | Demontis 2011 — Exact solutions of mKdV | No | — |
| [25] | Chen & Pelinovsky 2018, Nonlinearity — Rogue periodic waves of mKdV | No | **值得获取**（周期波退化的另一视角） |

### 4.4 Zhang 2020 (b-positon Nonlinear Dynamics) 引用文献中与退化/positon相关的关键文献

| 引用编号 | 文献 | 在文件夹中？ | 备注 |
|---------|------|------------|------|
| [9-10] | Matveev 1992 | No | 经典 |
| [11] | Dubard et al. 2010 — Multi-rogue wave/positon | No | — |
| [12] | Beutler, Stahlhofen, Matveev 1994 — What do solitons, breathers and positons have in common? | No | **值得获取**（直接讨论三者的关系） |
| [15] | Stahlhofen & Matveev 1995 — Toda positons | No | — |
| **18** | **Wang, He et al. 2017** — Double degeneracy / b-positon | **Yes** | 核心引用 |
| [19] | Qiu & Cheng 2019, AML — KE degenerate breather | 摘要 | 仅摘要，**值得获取全文** |
| **20** | **Liu, Zhang, He 2018** — cmKdV smooth positons | **Yes** | 核心引用 |
| **21** | **Song, Xu, Li, He 2019** — DNLS smooth positons | **Yes** | 核心引用 |
| [22] | Guo, Ling, Liu 2012, PRE — Generalized DT for NLS | No | **值得获取** |
| [24-25] | Wadati 1972-1973 — mKdV exact solution | No | 经典基础 |
| [28] | Zha 2013, Phys. Scr. — Nth-order rogue wave cmKdV | No | **值得获取** |
| [30] | He et al. 2014, PRE — Few-cycle optical rogue waves: cmKdV | No | He团队前期 |
| [34-37] | Serkin & Belyaeva 2018, Optik — cmKdV breather conditions (4篇) | No | **值得获取**（模共振的理论来源） |
| **39** | **Zhang, Yang, Li 2020** — AML (论文3) | **Yes** | 自引用 |

### 4.5 Wang-He 2017 (PRE, NLS双重退化) 引用文献中与退化/positon相关的关键文献

| 引用编号 | 文献 | 在文件夹中？ | 备注 |
|---------|------|------------|------|
| [35] | He et al. 2013, PRE — Generating mechanism for higher-order rogue waves | No | **值得获取**（He团队前期，高阶怪波生成机制） |
| [39] | Kedziora, Ankiewicz, Akhmediev 2013 — Classifying rogue wave hierarchy | No | — |
| **[40]** | **Kedziora, Ankiewicz, Akhmediev 2012, PRE — Second-order NLS breather in degenerate and rogue wave limits** | No | **高度推荐获取**（退化breather的有理解极限，与b-positon概念直接对应） |
| [41] | Matveev & Salle 1991 — Darboux Transformations and Solitons (book) | No | DT标准教材 |
| [45-46] | Matveev 1992 | No | 经典 |

### 4.6 Zhang 2026 (高阶mKdV Hirota) 引用文献中与退化/positon相关的关键文献

| 引用编号 | 文献 | 在文件夹中？ | 备注 |
|---------|------|------------|------|
| **29** | **Xing, Wu, Mihalache, He 2017** — mKdV smooth positons | **Yes** | 核心引用 |
| **30** | **Zhang, Yang, Li 2020** — Novel soliton molecules/b-positon (ND) | **Yes** | 核心引用 |
| [28] | Zhang, Li, Wazwaz, Guo 2022, EPJP — Multiple-pole solutions for 5th-order mKdV | No | **值得获取**（Zhang团队前期多重极点工作） |
| [36] | Wadati & Ohkuma 1982 — Multiple-pole of mKdV | No | — |
| [27] | Li & Li 2022 — Weakly bound states for higher-order Ito | No | — |

### 总结：关键未获取文献优先级推荐

| 优先级 | 文献 | 理由 | 获取难度 |
|--------|------|------|---------|
| ★★★★★ | Kedziora, Ankiewicz, Akhmediev 2012, PRE — "Second-order NLS breather solutions in the degenerate and rogue wave limits" | Wang-He 2017的[40]号引用，b-positon概念的直接前驱，直接讨论了退化breather的rogue wave极限 | PRE付费，Sci-Hub可获取 |
| ★★★★★ | Wu, Zhang, Hang 2021, AML — "Breather, soliton-breather interaction and double-pole solutions of the fifth-order mKdV" | Zhang 2021的[17]号引用，在5阶mKdV上结合了breather和双极点解 | 可能可开放获取 |
| ★★★★ | Chen & Pelinovsky 2018, Nonlinearity — "Rogue periodic waves of the mKdV equation" | Zhang 2021的[25]号引用，mKdV周期波rogue化的另一视角 | IOP付费 |
| ★★★★ | Serkin & Belyaeva 2018, Optik — 4篇关于cmKdV breather条件的系列论文 | Zhang 2020b引用，模共振条件λ=-λ*的理论来源，**理解模共振的原始出处** | 部分可获取 |
| ★★★★ | He et al. 2013, PRE — "Generating mechanism for higher-order rogue waves" | 被所有He团队论文引用，是双重退化机制的理论前驱 | PRE付费 |
| ★★★★ | Qiu & Cheng 2019, AML — "nth-order degenerate breather solution for the Kundu-Eckhaus equation" | Zhang 2020b引用，KE方程退化breather与b-positon直接相关 | 可能可开放获取 |
| ★★★★ | Zhang, Li, Wazwaz, Guo 2022, EPJP — "Multiple-pole solutions for the fifth-order mKdV equation" | Zhang 2026引用，5阶mKdV多重极点解，是Zhang 2021→2026的中间工作 | Springer |
| ★★★ | Guo, Ling, Liu 2011/2012, PRE — "Generalized Darboux transformation and rogue wave solutions" | Xing 2017引用，广义DT（GDT）的奠基工作，退化DT的数学基础 | PRE付费 |
| ★★★ | Beutler, Stahlhofen, Matveev 1994, Phys. Scr. — "What do solitons, breathers and positons have in common?" | 直接讨论三者关系（见标题），历史视角重要 | IOP付费 |
| ★★★ | Zha 2013, Phys. Scr. — "Nth-order rogue wave solutions of cmKdV" | Zhang 2020b引用，cmKdV rogue波，与positon研究互补 | IOP付费 |

---

## 五、技术路线图总结

```
┌─────────────────────────────────────────────────────────────────────┐
│                   完整技术链：N-孤子 → Positon → B-positon/退化呼吸子   │
└─────────────────────────────────────────────────────────────────────┘

  零种子 → DT → N-孤子 ──λ_j→λ_1──→ Smooth Positon (He 2017, Liu 2018)
                                     │
                                     ├──有理Positon (Zhang 2020 AML, 零种子+非零种子)
                                     │
                                     ├──半退化DT → 孤子-positon混合 (Zhang 2020 AML)
                                     │
                                     ├──模共振 λ=-λ* → 零背景breather → 退化 → 零背景b-positon
                                     │  (Zhang 2020b Nonlinear Dynamics)
                                     │
  周期种子 → DT → 多breather ──λ_j→λ_1──→ b-positon ──λ_1→λ_0──→ 有理解/rogue wave
                                     │  (Xing 2017 mKdV; Wang 2017 NLS)
                                     │
                                     └──双重退化 → 高阶rogue wave (Huang 2021 ecmKdV)

  Hirota替代路线:
  N-孤子(Hirota) ──k_2=k_1+ε, ε→0──→ Smooth Positon (Zhang 2021)
                  ──参数约束──→ 多重极点解(=positon) (Zhang 2026)
```

**关键发现**：
1. 文件夹中已有论文覆盖了从N-孤子到光滑positon再到b-positon/退化呼吸子的**所有关键步骤**，技术链完整。
2. He 2017和Xing 2017是两条互补路径的起点：零种子→smooth positon（He 2017）vs 周期种子→b-positon→有理解（Xing 2017）。
3. Zhang 2020b（非线动力学）是**唯一完整实现"零背景breather-b-positon"的论文**，通过模共振+退化的组合。
4. 双重退化机制（λ_j→λ_1→λ_0）最早出现在Wang-He 2017 (NLS)中，Xing 2017将其平行推广到mKdV。
5. 最需要进一步获取的是Kedziora 2012 (退化breather→rogue极限)和He 2013 (高阶rogue wave生成机制)——它们是双重退化机制的理论源头。
