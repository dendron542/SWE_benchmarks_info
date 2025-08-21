# SWE-bench AIランキング (2025年8月版)

## 📊 概要

このプロジェクトは、2025年8月時点でのSWE-benchベンチマークにおける各種AIモデルの最新スコアとランキングを提供します。

## 🏆 トップ5モデル（SWE-bench Verified）

1. **GPT-5**: 74.9% （2025年8月リリース）
2. **Grok 4**: 73.5% （2025年7月リリース）
3. **Claude 4 Sonnet**: 72.7% （2025年5月リリース）
4. **OpenAI o3**: 71.7% （2024年12月発表、2025年4月正式リリース）
5. **o4-mini**: 68.1% （2025年4月リリース）

### 新着の DeepSeek V3.1
- **66.0%** - SWE-bench Verified（2025年8月21日リリース）
- **ハイブリッドモデル** - Think/Non-Thinkモード切り替え可能
- **128Kコンテキスト** - 長文対応、エージェント機能強化
- **コスパ優秀** - $0.07-0.27/1M入力、$1.10/1M出力

## 📁 ファイル構成

```
SWE_bench_rank/
├── README.md                   # このファイル（プロジェクト説明書）
├── swe_bench_ranking.json      # 完全なランキングデータ（JSON形式）
├── swe_bench_ranking.csv       # ランキングデータ（CSV形式）
├── swe_rank_viewer.py          # インタラクティブランキング表示ツール
├── .gitignore                  # Git除外設定
└── plan/
    └── plan.md                # 開発計画書・進捗管理
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
- **2024年**: 71.7% - OpenAI o3発表による大幅改善（12月）
- **2025年**: 74.9% - GPT-5による新記録達成、o3正式リリース（4月）

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
1. **OpenAI o3**: 2,727 ELO (99.9パーセンタイル) - 国際グランドマスターレベル
2. **Qwen3-235B**: 2,056 ELO (95.0パーセンタイル)
3. **DeepSeek R1**: 2,029 ELO (96.3パーセンタイル)
4. **OpenAI o1**: 1,891 ELO (前世代比較用)

### AIME スコア
- **o4-mini**: 92.7% (2025年) - o3を上回る驚異的スコア
- **OpenAI o3**: 88.9% (2025年最新), 96.7% (2024年発表時)
- **Qwen3-235B**: 85.7% (2024年), 81.4% (2025年)

### DeepSeek V3.1 その他のベンチマーク
- **Aider**: 71.6% - 多言語プログラミングテスト
- **SWE-bench Multilingual**: 54.5% - 多言語対応
- **Terminal-bench**: 31.3% - ターミナル操作

## ⚠️ 注意事項

- **OpenAI o3**: 2025年4月16日に正式リリース済み、ツール使用可能なエージェント推論モデル
- **o4-mini**: o3の効率版として同時リリース、一部ベンチマークでo3を上回る性能
- **DeepSeek V3.1**: 2025年8月21日リリース、ハイブリッド推論モデル（Think/Non-Thinkモード）
- スコアはモデル単体ではなく、エージェントシステム全体の性能を示します
- 計算コストは実装方法により大きく異なります
- データは2025年8月21日時点の最新公式情報に基づいています

## 📚 データソース

- SWE-bench公式リーダーボード
- 各AI企業の公式発表
- 学術論文および技術レポート
- オープンソースプロジェクトの実績

## 🔄 更新履歴

- **2025-08-21**: OpenAI o3/o4-mini最新公式情報でアップデート（2025年4月16日正式リリース）
- **2025-08-07**: 初版作成、最新のSWE-benchランキングを収集・整理