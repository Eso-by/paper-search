# Search Module

Multi-platform exhaustive paper search.

## Quality Filter

**Zero tolerance for low-quality journals**: MDPI (Mathematics, Symmetry, Axioms, Applied Sciences, Fluids, etc.), Romanian Reports in Physics, Thermal Science, Hindawi (Math. Probl. Eng., J. Function Spaces, etc.), Nonlinear Engineering. Exclude these entirely — never count or summarize them.

**Prioritize**: Nonlinear Dynamics, Phys. Rev. E, Phys. Rev. Lett., Phys. Lett. A, Chaos Solitons & Fractals, J. Phys. A, Commun. Nonlinear Sci., Stud. Appl. Math., Proc. R. Soc. A, Appl. Math. Lett., Physica D, Chaos, J. Fluid Mech., Wave Motion, J. Math. Anal. Appl., Inverse Problems, Sci. Rep. (注意质量)

**Why**: Past reviews have been criticized for including low-quality sources.

## Sources (2026-05 tested)

| Source | Use | Arg |
|--------|-----|-----|
| CrossRef | Metadata only | `crossref` |
| OpenAlex | Broad metadata | `openalex` |
| DBLP | CS | `dblp` |
| Semantic Scholar | Metadata + some PDFs | `semantic` |
| PubMed / Europe PMC | Biomedical | `pubmed` / `europepmc` |
| DOAJ | Open access journals | `doaj` |
| arXiv (WebSearch) | More reliable than CLI | WebSearch |

Broken: `google_scholar` CLI (use Edge+CDP instead), `ssrn`, `citeseerx`.

## Strategy: Exhaustive Multi-Round Saturation

**Targets**: >=40 papers, >=3 rounds, cover 2016-2026.

**Before starting**: Show keyword list + journal list + author list to user for confirmation.

### Per-round process:
1. **Keywords**: Generate all variants (synonyms, abbreviations, equation variants, method terms)
2. **Sources**: Run each variant on `crossref,openalex,dblp,doaj,openaire` + WebSearch for arXiv + Semantic Scholar
3. **Cross-ref**: Check references of found papers for missed work. Add newly identified candidates to the next search iteration.
4. **Author search**: Search known key authors + topic
5. **Publisher sites**: `site:link.springer.com <keyword>`, `site:journals.aps.org <keyword>`, `site:iopscience.iop.org <keyword>` etc.
6. **GS CDP**: When CLI + WebSearch coverage is thin. See GS section below.

Stop when a round adds <=3 new papers (count by search discovery, not download status). The stopping criterion is global — check only after ALL search activities are complete (initial rounds + cross-ref/reference chasing + author search + publisher site search). Minimum 3 rounds.

## Google Scholar (Edge + CDPSearch)

CLI broken. Use Edge CDP:
1. Kill Edge, relaunch with `--remote-debugging-port=9222`
2. Open tab: `curl -X PUT "http://localhost:9222/json/new?https://scholar.google.com/scholar?q=QUERY&hl=en&as_ylo=2016"`
3. Extract via Python websockets (see old SKILL.md for full code)
4. One query per tab, 30s+ between queries, `?hl=en`
5. CAPTCHA → user handles it. "unusual traffic" → stop 24h+

## CLI Quick Reference

```bash
PY="c:/Users/porfi/paper-search-mcp/.venv/Scripts/python.exe -m paper_search_mcp.cli"
$PY search "<query>" -s crossref,openalex,dblp,doaj,openaire,semantic -n 20
$PY read <source> <id> -o papers/<keyword>/
```
