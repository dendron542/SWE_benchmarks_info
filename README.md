# SWE-bench AIランキング (2025年8月版)

## 📊 概要

このプロジェクトは、2025年8月時点でのSWE-benchベンチマークにおける各種AIモデルの最新スコアとランキングを提供します。

## 🏆 トップ3モデル（SWE-bench Verified）

1. **OpenAI o3**: 72.0% （未公開モデル）
2. **DeepSeek R1 (Agentic)**: 65.8% （オープンソース）  
3. **Mini-SWE-agent**: 65.0% （100行のPythonコードで実現）

## 📁 ファイル構成

```
tmp/
├── swe_bench_ranking.json    # 完全なランキングデータ（JSON形式）
├── swe_bench_ranking.csv     # ランキングデータ（CSV形式）
├── swe_rank_viewer.py        # ランキング表示ツール
└── README.md                # このファイル
```

## 🛠️ 使用方法

### 基本的な使い方

```bash
# サマリー表示（デフォルト）
python swe_rank_viewer.py

# 詳細なランキング表示
python swe_rank_viewer.py --format full

# SWE-bench Verified のみ表示
python swe_rank_viewer.py --format full --benchmark verified

# 全ベンチマーク表示
python swe_rank_viewer.py --format full --benchmark all

# JSON形式で出力
python swe_rank_viewer.py --format json
```

### オプション

- `--format`: 表示形式
  - `summary`: トップモデルとトレンドのサマリー（デフォルト）
  - `full`: 詳細なランキング表示
  - `json`: JSON形式で出力

- `--benchmark`: ベンチマークタイプ
  - `verified`: SWE-bench Verified（デフォルト）
  - `full`: SWE-bench Full
  - `lite`: SWE-bench Lite  
  - `all`: 全てのベンチマーク

## 📈 パフォーマンストレンド

- **2023年**: 4.4% - 初期のAIコーディング能力
- **2024年**: 71.7% - コーディング能力の大幅改善
- **2025年**: 72.0% - 継続的な改良と最適化

## 🔍 ベンチマーク詳細

### SWE-bench Verified
- **タスク数**: 500問
- **特徴**: 人間によって検証された高品質なデータセット
- **目的**: より信頼性の高いAI評価

### SWE-bench Full
- **タスク数**: 2,294問
- **特徴**: GitHubの実際のissueから構成された完全データセット
- **目的**: 実世界のソフトウェア工学タスクでのAI評価

### SWE-bench Lite
- **タスク数**: 300問
- **特徴**: 高速評価用の厳選されたサブセット
- **目的**: 効率的なモデル評価

## 💻 追加メトリクス

### Codeforces ELO ランキング
1. **OpenAI o3**: 2,727 ELO (99.9パーセンタイル)
2. **Qwen3-235B**: 2,056 ELO (95.0パーセンタイル)
3. **DeepSeek R1**: 2,029 ELO (96.3パーセンタイル)

### AIME スコア
- **OpenAI o3**: 96.7% (2024年)
- **Qwen3-235B**: 85.7% (2024年), 81.4% (2025年)

## ⚠️ 注意事項

- OpenAI o3は発表されているものの、まだ一般公開されていません
- スコアはモデル単体ではなく、エージェントシステム全体の性能を示します
- 計算コストは実装方法により大きく異なります
- データは2025年8月7日時点の情報に基づいています

## 📚 データソース

- SWE-bench公式リーダーボード
- 各AI企業の公式発表
- 学術論文および技術レポート
- オープンソースプロジェクトの実績

## 🔄 更新履歴

- **2025-08-07**: 初版作成、最新のSWE-benchランキングを収集・整理