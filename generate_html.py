#!/usr/bin/env python3
"""swe_bench_ranking.json から自己完結 index.html を生成する"""

import json
from pathlib import Path

HERE = Path(__file__).parent
JSON_PATH = HERE / "swe_bench_ranking.json"
OUTPUT_PATH = HERE / "index.html"

ORG_COLORS: dict[str, str] = {
    "Anthropic": "#D97706",
    "Google": "#2563EB",
    "OpenAI": "#059669",
    "DeepSeek": "#7C3AED",
    "Moonshot AI": "#DB2777",
    "MiniMax": "#0891B2",
    "Alibaba (Qwen)": "#EA580C",
    "Zhipu AI": "#65A30D",
    "Zhipu AI (Z.AI)": "#65A30D",
    "xAI": "#6B7280",
    "Open Source": "#6366F1",
}

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SWE-bench Ranking</title>
<style>
  :root {{
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #222536;
    --border: #2d3148;
    --text: #e2e8f0;
    --text-muted: #8892b0;
    --accent: #6366f1;
    --accent-dim: rgba(99,102,241,.15);
    --green: #22c55e;
    --yellow: #eab308;
    --red: #ef4444;
    --radius: 10px;
    --font: "Inter", system-ui, sans-serif;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: var(--font); background: var(--bg); color: var(--text); min-height: 100vh; }}

  header {{
    padding: 32px 24px 0;
    text-align: center;
  }}
  header h1 {{ font-size: 2rem; font-weight: 700; letter-spacing: -.03em; }}
  header p {{ color: var(--text-muted); margin-top: 6px; font-size: .9rem; }}

  .tabs {{
    display: flex;
    gap: 4px;
    padding: 24px 24px 0;
    flex-wrap: wrap;
    justify-content: center;
  }}
  .tab-btn {{
    padding: 8px 20px;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text-muted);
    border-radius: 30px;
    cursor: pointer;
    font-size: .85rem;
    font-weight: 500;
    transition: all .2s;
  }}
  .tab-btn.active, .tab-btn:hover {{
    background: var(--accent-dim);
    border-color: var(--accent);
    color: var(--text);
  }}

  .panel {{ display: none; padding: 24px; max-width: 1300px; margin: 0 auto; }}
  .panel.active {{ display: block; }}

  .controls {{
    display: flex;
    gap: 12px;
    margin-bottom: 16px;
    flex-wrap: wrap;
    align-items: center;
  }}
  .search-box {{
    padding: 8px 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    font-size: .85rem;
    width: 220px;
    outline: none;
  }}
  .search-box:focus {{ border-color: var(--accent); }}
  .count-badge {{
    font-size: .78rem;
    color: var(--text-muted);
    margin-left: auto;
  }}

  .table-wrap {{ overflow-x: auto; border-radius: var(--radius); border: 1px solid var(--border); }}
  table {{ width: 100%; border-collapse: collapse; font-size: .82rem; }}
  thead tr {{ background: var(--surface2); }}
  th {{
    padding: 10px 14px;
    text-align: left;
    color: var(--text-muted);
    font-weight: 600;
    font-size: .75rem;
    text-transform: uppercase;
    letter-spacing: .06em;
    cursor: pointer;
    white-space: nowrap;
    user-select: none;
  }}
  th:hover {{ color: var(--text); }}
  th .sort-icon {{ opacity: .4; margin-left: 4px; font-size: .65rem; }}
  th.sort-asc .sort-icon::after {{ content: "▲"; opacity: 1; }}
  th.sort-desc .sort-icon::after {{ content: "▼"; opacity: 1; }}

  tbody tr {{ border-top: 1px solid var(--border); transition: background .15s; }}
  tbody tr:hover {{ background: var(--surface2); }}
  td {{ padding: 10px 14px; vertical-align: middle; }}

  .rank-cell {{ font-weight: 700; color: var(--text-muted); width: 42px; text-align: center; }}
  .rank-cell.gold   {{ color: #FFD700; }}
  .rank-cell.silver {{ color: #C0C0C0; }}
  .rank-cell.bronze {{ color: #CD7F32; }}

  .model-cell {{ font-weight: 600; max-width: 240px; }}
  .model-name {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block; }}
  .model-meta {{ font-size: .72rem; color: var(--text-muted); margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

  .score-cell {{ min-width: 120px; }}
  .score-val {{ font-weight: 700; font-size: .95rem; }}
  .score-bar-wrap {{ margin-top: 4px; height: 4px; background: var(--border); border-radius: 2px; }}
  .score-bar {{ height: 100%; border-radius: 2px; }}

  .org-badge {{
    display: inline-block;
    padding: 3px 9px;
    border-radius: 20px;
    font-size: .72rem;
    font-weight: 600;
    white-space: nowrap;
    background: rgba(255,255,255,.08);
  }}

  .cost-cell {{ font-size: .76rem; color: var(--text-muted); min-width: 130px; }}
  .cost-cell span {{ display: block; }}

  .notes-cell {{
    max-width: 260px;
    font-size: .76rem;
    color: var(--text-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  /* Trends tab */
  .trend-grid, .metrics-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 16px;
    margin-top: 8px;
  }}
  .card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
  }}
  .card-title {{ font-size: .78rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: .06em; margin-bottom: 8px; }}
  .card-value {{ font-size: 2rem; font-weight: 700; color: var(--accent); }}
  .card-sub {{ font-size: .8rem; color: var(--text-muted); margin-top: 4px; }}

  .section-heading {{
    font-size: 1rem;
    font-weight: 700;
    margin: 24px 0 12px;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .section-heading::after {{ content: ""; flex: 1; height: 1px; background: var(--border); }}

  footer {{
    text-align: center;
    padding: 40px 24px;
    color: var(--text-muted);
    font-size: .78rem;
  }}

  @media (max-width: 600px) {{
    header h1 {{ font-size: 1.4rem; }}
    .cost-cell, .notes-cell {{ display: none; }}
  }}
</style>
</head>
<body>

<header>
  <h1>SWE-bench Ranking</h1>
  <p>AIコーディングモデルの実力比較 — {last_updated} 更新</p>
</header>

<div class="tabs">
  <button class="tab-btn active" onclick="switchTab('verified')">✅ Verified (500)</button>
  <button class="tab-btn" onclick="switchTab('full')">📊 Full (2,294)</button>
  <button class="tab-btn" onclick="switchTab('lite')">⚡ Lite (300)</button>
  <button class="tab-btn" onclick="switchTab('pro')">🏆 Pro (1,865)</button>
  <button class="tab-btn" onclick="switchTab('trends')">📈 Trends</button>
</div>

<div id="panel-verified" class="panel active"></div>
<div id="panel-full" class="panel"></div>
<div id="panel-lite" class="panel"></div>
<div id="panel-pro" class="panel"></div>
<div id="panel-trends" class="panel"></div>

<footer>Data source: swe_bench_ranking.json &nbsp;|&nbsp; Updated {last_updated}</footer>

<script>
const DATA = {json_data};

const ORG_COLORS = {org_colors};

function scoreColor(s) {{
  if (s >= 75) return '#22c55e';
  if (s >= 60) return '#eab308';
  if (s >= 45) return '#f97316';
  return '#ef4444';
}}

function rankClass(r) {{
  if (r === 1) return 'gold';
  if (r === 2) return 'silver';
  if (r === 3) return 'bronze';
  return '';
}}

function orgBadge(org) {{
  const color = ORG_COLORS[org] || '#6B7280';
  return `<span class="org-badge" style="border:1px solid ${{color}}44;color:${{color}}">${{org}}</span>`;
}}

function buildRankingTable(panelId, rankingData, benchmarkName) {{
  const panel = document.getElementById(panelId);
  if (!rankingData || !rankingData.ranking) {{
    panel.innerHTML = `<p style="color:var(--text-muted);padding:24px">データなし</p>`;
    return;
  }}
  const rows = rankingData.ranking;
  const maxScore = Math.max(...rows.map(r => r.score || 0));

  let sortCol = 'rank';
  let sortDir = 1;

  function render(data) {{
    const countEl = panel.querySelector('.count-badge');
    if (countEl) countEl.textContent = `${{data.length}} モデル`;

    const tbody = panel.querySelector('tbody');
    tbody.innerHTML = data.map(item => {{
      const score = item.score || 0;
      const barWidth = maxScore > 0 ? (score / maxScore * 100).toFixed(1) : 0;
      const barColor = scoreColor(score);
      return `
        <tr>
          <td class="rank-cell ${{rankClass(item.rank)}}">${{item.rank || '—'}}</td>
          <td class="model-cell">
            <span class="model-name" title="${{item.model_name}}">${{item.model_name}}</span>
            ${{item.notes ? `<span class="model-meta" title="${{item.notes}}">${{item.notes}}</span>` : ''}}
          </td>
          <td class="score-cell">
            <span class="score-val" style="color:${{barColor}}">${{score.toFixed(1)}}%</span>
            <div class="score-bar-wrap"><div class="score-bar" style="width:${{barWidth}}%;background:${{barColor}}"></div></div>
          </td>
          <td>${{orgBadge(item.organization || '—')}}</td>
          <td class="cost-cell">
            ${{item.api_cost_input ? `<span>IN: ${{item.api_cost_input}}</span>` : ''}}
            ${{item.api_cost_output ? `<span>OUT: ${{item.api_cost_output}}</span>` : ''}}
            ${{!item.api_cost_input && !item.api_cost_output ? '<span>—</span>' : ''}}
          </td>
          <td class="notes-cell" title="${{item.computational_cost || ''}}">${{item.computational_cost || '—'}}</td>
        </tr>`;
    }}).join('');
  }}

  function sort(col) {{
    if (sortCol === col) {{ sortDir *= -1; }} else {{ sortCol = col; sortDir = 1; }}
    panel.querySelectorAll('th[data-col]').forEach(th => {{
      th.classList.remove('sort-asc', 'sort-desc');
      if (th.dataset.col === col) th.classList.add(sortDir === 1 ? 'sort-asc' : 'sort-desc');
    }});
    applyFilter();
  }}

  let currentSearch = '';
  function applyFilter() {{
    let data = rows.filter(r => r.model_name.toLowerCase().includes(currentSearch));
    data = [...data].sort((a, b) => {{
      let av = a[sortCol] ?? (sortCol === 'rank' ? 999 : '');
      let bv = b[sortCol] ?? (sortCol === 'rank' ? 999 : '');
      if (typeof av === 'string') av = av.toLowerCase();
      if (typeof bv === 'string') bv = bv.toLowerCase();
      return av < bv ? -sortDir : av > bv ? sortDir : 0;
    }});
    render(data);
    panel.querySelector('.count-badge').textContent = `${{data.length}} モデル`;
  }}

  panel.innerHTML = `
    <div class="controls">
      <input class="search-box" type="text" placeholder="モデル名で検索..." />
      <span class="count-badge">${{rows.length}} モデル</span>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th data-col="rank">順位<span class="sort-icon"></span></th>
            <th data-col="model_name">モデル<span class="sort-icon"></span></th>
            <th data-col="score">スコア<span class="sort-icon sort-desc"></span></th>
            <th data-col="organization">組織<span class="sort-icon"></span></th>
            <th>APIコスト</th>
            <th data-col="computational_cost">計算コスト<span class="sort-icon"></span></th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>`;

  panel.querySelectorAll('th[data-col]').forEach(th => {{
    th.addEventListener('click', () => sort(th.dataset.col));
    if (th.dataset.col === 'rank') th.classList.add('sort-asc');
  }});

  panel.querySelector('.search-box').addEventListener('input', e => {{
    currentSearch = e.target.value.toLowerCase();
    applyFilter();
  }});

  applyFilter();
}}

function buildTrendsPanel() {{
  const panel = document.getElementById('panel-trends');
  const trends = DATA.performance_trends;
  const metrics = DATA.coding_performance_metrics;

  let html = '';

  // Performance Trends
  html += `<div class="section-heading">年別パフォーマンストレンド (SWE-bench)</div>`;
  html += `<div class="trend-grid">`;
  for (const [year, d] of Object.entries(trends || {{}})) {{
    html += `
      <div class="card">
        <div class="card-title">${{year}}</div>
        <div class="card-value">${{d.swe_bench_success_rate}}%</div>
        <div class="card-sub">${{d.description}}</div>
      </div>`;
  }}
  html += `</div>`;

  // Codeforces ELO
  const cfe = metrics?.codeforces_elo || [];
  if (cfe.length) {{
    html += `<div class="section-heading">Codeforces ELO ランキング</div>`;
    html += `<div class="table-wrap"><table><thead><tr><th>モデル</th><th>ELO</th><th>パーセンタイル</th></tr></thead><tbody>`;
    cfe.forEach(item => {{
      const pct = typeof item.percentile === 'number' ? item.percentile.toFixed(1) + '%' : item.percentile;
      html += `<tr><td>${{item.model_name}}</td><td style="font-weight:700;color:#6366f1">${{item.elo_rating}}</td><td>${{pct}}</td></tr>`;
    }});
    html += `</tbody></table></div>`;
  }}

  // AIME Scores
  const aime = metrics?.aime_scores || [];
  if (aime.length) {{
    html += `<div class="section-heading">AIME スコア</div>`;
    html += `<div class="table-wrap"><table><thead><tr><th>モデル</th><th>スコア</th><th>年度</th></tr></thead><tbody>`;
    aime.forEach(item => {{
      html += `<tr><td>${{item.model_name}}</td><td style="font-weight:700;color:#22c55e">${{item.score.toFixed(1)}}%</td><td>${{item.year}}</td></tr>`;
    }});
    html += `</tbody></table></div>`;
  }}

  panel.innerHTML = html;
}}

function switchTab(name) {{
  document.querySelectorAll('.tab-btn').forEach((b, i) => {{
    const names = ['verified','full','lite','pro','trends'];
    b.classList.toggle('active', names[i] === name);
  }});
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + name).classList.add('active');
}}

// Initialize
buildRankingTable('panel-verified', DATA.swe_bench_verified_ranking, 'SWE-bench Verified');
buildRankingTable('panel-full', DATA.swe_bench_full_ranking, 'SWE-bench Full');
buildRankingTable('panel-lite', DATA.swe_bench_lite_ranking, 'SWE-bench Lite');
buildRankingTable('panel-pro', DATA.swe_bench_pro_ranking, 'SWE-bench Pro');
buildTrendsPanel();
</script>
</body>
</html>
"""


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    last_updated = (
        data.get("swe_bench_verified_ranking", {}).get("last_updated", "N/A")
    )

    org_colors_js = json.dumps(ORG_COLORS, ensure_ascii=False, indent=2)
    json_data_js = json.dumps(data, ensure_ascii=False)

    html = HTML_TEMPLATE.format(
        last_updated=last_updated,
        json_data=json_data_js,
        org_colors=org_colors_js,
    )

    OUTPUT_PATH.write_text(html, encoding="utf-8")
    print(f"Generated: {OUTPUT_PATH}")
    print(f"Open in browser: file://{OUTPUT_PATH.as_posix()}")


if __name__ == "__main__":
    main()
