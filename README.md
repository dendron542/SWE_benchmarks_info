# SWE-bench AIランキング (2025年11月版)

## 📊 概要

このプロジェクトは、2025年11月時点でのSWE-benchベンチマークにおける各種AIモデルの最新スコアとランキングを提供します。

## 🏆 トップ5モデル（SWE-bench Verified）

1. **Claude Sonnet 4.5**: 77.2% （2025年9月リリース）
2. **GPT-5.1**: 76.3% （2025年11月リリース）
3. **Gemini 3 Pro**: 76.2% （2025年11月リリース）
4. **GPT-5**: 74.9% （2025年8月リリース）
5. **Grok 4**: 73.5% （2025年7月リリース）

### 新着のトップモデル

#### Claude Sonnet 4.5 🏆 NEW #1
- **77.2%** - SWE-bench Verified（2025年9月29日リリース）
- **世界最高のコーディングモデル** - Anthropicが公式に「best coding model in the world」と発表
- **並列計算で82.0%** - テスト時並列計算を使用した場合の最高スコア
- **長時間集中** - 30時間以上の複雑なマルチステップタスクに対応
- **Agentic Terminal Coding** - 50.0%を達成（Claude Sonnet 4の36.4%から大幅向上）
- **API価格** - $3.00/1M入力（<200K）、$15/1M出力（<200K）

#### GPT-5.1
- **76.3%** - SWE-bench Verified（2025年11月12日リリース）
- **効率改善** - GPT-5より30%少ないトークンで実行
- **2つのバリエーション** - GPT-5.1 Instant（高速）とGPT-5.1 Thinking（高度な推論）
- **キャッシング機能** - 90%割引、24時間保持
- **API価格** - $1.25/1M入力、$10/1M出力

#### Gemini 3 Pro
- **76.2%** - SWE-bench Verified（2025年11月18日リリース）
- **超大容量コンテキスト** - 1Mトークン対応
- **LMArena首位** - 1501 Eloスコア獲得
- **マルチモーダル** - 最先端のマルチモーダル理解能力
- **API価格** - $2.00/1M入力（<200K）、$12/1M出力（<200K）

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
- **2025年**: 77.2% - Claude Sonnet 4.5による新記録達成（9月）、GPT-5.1（76.3%）とGemini 3 Pro（76.2%）が僅差で続く

## 📊 完全ランキング（SWE-bench Verified）

| ランク | モデル名 | スコア | 組織 | リリース時期 | API価格（入力/出力） |
|--------|----------|--------|------|--------------|---------------------|
| 1 | Claude Sonnet 4.5 | 77.2% | Anthropic | 2025年9月 | $3.00/$15.00 per 1M tokens |
| 2 | GPT-5.1 | 76.3% | OpenAI | 2025年11月 | $1.25/$10.00 per 1M tokens |
| 3 | Gemini 3 Pro | 76.2% | Google | 2025年11月 | $2.00/$12.00 per 1M tokens |
| 4 | GPT-5 | 74.9% | OpenAI | 2025年8月 | $1.25/$10.00 per 1M tokens |
| 5 | Grok 4 | 73.5% | xAI | 2025年7月 | $5.00/$15.00 per 1M tokens (est.) |
| 6 | Claude 4 Sonnet | 72.7% | Anthropic | 2025年5月 | $3.00/$15.00 per 1M tokens |
| 7 | Claude 4 Opus | 72.5% | Anthropic | 2025年5月 | $15.00/$75.00 per 1M tokens |
| 8 | OpenAI o3 | 71.7% | OpenAI | 2025年4月 | 未公開 |
| 9 | OpenAI o3 (Low Compute) | 70.3% | OpenAI | 2024年12月 | 未公開 |
| 10 | Kimi K2 (Parallel) | 71.6% | Moonshot AI | 2025年 | $0.15/$2.50 per 1M tokens |
| 11 | o4-mini | 68.1% | OpenAI | 2025年4月 | 未公開 |
| 12 | DeepSeek V3.1 | 66.0% | DeepSeek | 2025年8月 | $0.27/$1.10 per 1M tokens |
| 13 | DeepSeek R1 (Agentic) | 65.8% | DeepSeek | 2025年 | $0.55/$2.19 per 1M tokens |
| 14 | Kimi K2 | 65.8% | Moonshot AI | 2025年 | $0.15/$2.50 per 1M tokens |
| 15 | Mini-SWE-agent | 65.0% | Open Source | 2025年 | 無料/オープンソース |
| 16 | GLM-4.5 | 64.2% | Zhipu AI | 2025年 | $2.00/$6.00 per 1M tokens (est.) |
| 17 | Gemini 2.5 Flash | 63.8% | Google | 2025年 | $0.30/$2.50 per 1M tokens |
| 18 | Gemini 2.5 Pro | 63.2% | Google | 2025年 | $5.00/$15.00 per 1M tokens (est.) |
| 19 | Claude 3.7 Sonnet | 62.3% | Anthropic | 2025年 | $1.00/$5.00 per 1M tokens (est.) |
| 20 | GPT-OSS-120b | 62.4% | OpenAI | 2025年 | 無料/オープンソース |
| 21 | CodeStory Midwit Agent | 62.0% | CodeStory | 2025年 | N/A |
| 22 | GPT-4.1 | 54.6% | OpenAI | 2025年 | $5.00/$15.00 per 1M tokens (est.) |
| 23 | Claude 3.5 Sonnet (Latest) | 50.8% | Anthropic | 2024年 | $3.00/$15.00 per 1M tokens |
| 24 | DeepSeek R1 | 49.2% | DeepSeek | 2025年 | $0.55/$2.19 per 1M tokens |
| 25 | Claude 3.5 Sonnet (Upgraded) | 49.0% | Anthropic | 2024年 | $3.00/$15.00 per 1M tokens |
| 26 | OpenAI o1 | 48.9% | OpenAI | 2024年 | $15.00/$60.00 per 1M tokens |
| 27 | Grok 3 | 46.8% | xAI | 2025年 | $2.00/$8.00 per 1M tokens (est.) |
| 28 | GPT-4o | 33.2% | OpenAI | 2024年 | $2.50/$10.00 per 1M tokens |

### 主要モデルの詳細情報

#### トップ3モデルの特徴

**1位: Claude Sonnet 4.5 (77.2%)**
- 並列計算で82.0%達成
- Agentic Terminal Coding: 50.0%
- 30時間以上の長時間タスク対応
- 計算コスト: Medium

**2位: GPT-5.1 (76.3%)**
- GPT-5より30%効率化
- 2つのバリエーション（Instant/Thinking）
- キャッシング90%割引（24時間）
- 計算コスト: High

**3位: Gemini 3 Pro (76.2%)**
- 1Mトークンコンテキスト
- LMArena Elo: 1501（首位）
- マルチモーダル最先端
- 計算コスト: High

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

### Codeforces ELO ランキング（2025年11月最新版）
1. **OpenAI o3**: 2,700 ELO (99.9パーセンタイル) - 国際グランドマスターレベル
2. **Gemini 3 Pro**: 2,439 ELO (LiveCodeBench Pro, 2025年11月)
3. **GPT-5.1**: ~2,240 ELO (LiveCodeBench, 2025年11月)
4. **Claude Sonnet 4.5**: 2,121 ELO (Div1, 2025年9月)
5. **DeepSeek R1**: 2,029 ELO (96.3パーセンタイル, 2025年1月)
6. **DeepSeek R1-0528**: 1,930 ELO (2025年5月アップグレード版)
7. **Qwen3-235B**: 2,056 ELO (95.0パーセンタイル)
8. **OpenAI o1**: 1,891 ELO (前世代比較用)

### AIME 2025 スコア（最新版）

**ツール使用あり:**
- **Claude Sonnet 4.5**: 100% (Python tools)
- **Gemini 3 Pro**: 100% (Code execution)
- **GPT-5.1**: 94.0%
- **o4-mini**: 92.7% - o3を上回る驚異的スコア
- **OpenAI o3**: 88.9% (2025年最新), 96.7% (2024年発表時)

**ツールなし（数学推論のみ）:**
- **Gemini 3 Pro**: 95.0%
- **DeepSeek R1-0528**: 91.4% (AIME 2024)
- **DeepSeek V3.1**: 88.4%
- **Claude Sonnet 4.5**: 87.0%
- **DeepSeek R1-0528**: 87.5% (AIME 2025)
- **Qwen3-235B**: 85.7% (2024年), 81.4% (2025年)
- **DeepSeek R1**: 79.8% (AIME 2024)

### Terminal-Bench 2.0（ターミナル操作）
1. **Gemini 3 Pro**: 54.2% - 最高スコア
2. **Claude Sonnet 4.5**: 50.0% (Agentic Terminal Coding)
3. **GPT-5.1**: 47.6%

### DeepSeek V3.1 その他のベンチマーク
- **Aider**: 71.6% - 多言語プログラミングテスト
- **SWE-bench Multilingual**: 54.5% - 多言語対応
- **Terminal-bench**: 31.3% - ターミナル操作（旧版）

## ⚠️ 注意事項

- **Claude Sonnet 4.5**: 2025年9月29日リリース、世界最高のコーディングモデル、並列計算で82.0%達成
- **GPT-5.1**: 2025年11月12日リリース、GPT-5より30%効率化、2つのバリエーション（Instant/Thinking）
- **Gemini 3 Pro**: 2025年11月18日リリース、1Mトークンコンテキスト、LMArenaで1501 Eloスコア獲得
- **OpenAI o3**: 2025年4月16日に正式リリース済み、ツール使用可能なエージェント推論モデル
- **o4-mini**: o3の効率版として同時リリース、一部ベンチマークでo3を上回る性能
- **DeepSeek V3.1**: 2025年8月21日リリース、ハイブリッド推論モデル（Think/Non-Thinkモード）
- **データ更新方針**: データ収集は自動化されていますが、最終的な更新は人間による検証を経て手動で行われます
- スコアはモデル単体ではなく、エージェントシステム全体の性能を示します
- 計算コストは実装方法により大きく異なります
- データは2025年11月23日時点の最新公式情報に基づいています

## 📚 データソース

- SWE-bench公式リーダーボード
- 各AI企業の公式発表
- 学術論文および技術レポート
- オープンソースプロジェクトの実績

## 🔄 データ更新について

### データ管理方針
- **自動データ収集**: 最新の公式発表やベンチマーク結果を自動検索・収集
- **手動データ更新**: 収集されたデータは人間が検証・精査してから適用
- **公式情報重視**: 各AI企業の公式発表とSWE-bench公式リーダーボードを最優先
- **品質管理**: WebSearchとWebFetchを活用した自動収集後、複数ソースで検証

### 更新プロセス
1. **自動検索**: 新モデルや重要なベンチマーク結果の自動検出
2. **情報収集**: 公式ドキュメントやAPIドキュメントから詳細データを自動取得
3. **人間による検証**: 収集データの正確性と信頼性を手動確認
4. **データベース更新**: 検証済みデータをJSON/CSV形式で手動更新
5. **公開**: GitHubリポジトリへの手動コミット・プッシュ

### 技術仕様
- **WebSearch**: 最新情報の自動検索
- **WebFetch**: 公式サイトからの自動データ抽出
- **Claude Code**: データ検証と構造化を支援
- **Git**: バージョン管理とデプロイメント

### 更新依頼
新しいモデル情報や修正が必要なデータがある場合は、GitHubのIssueでお知らせください。自動収集システムが対応します。

## 🔄 更新履歴

- **2025-11-23**: 追加メトリクスを大幅更新 - Codeforces ELO、AIME 2025、Terminal-Bench 2.0の最新スコアを反映。Claude Sonnet 4.5（100% AIME）、Gemini 3 Pro（2,439 ELO、100% AIME）、GPT-5.1（94.0% AIME）の最新ベンチマークを追加
- **2025-11-23**: Claude Sonnet 4.5を追加、新たな世界最高スコア（77.2%）を反映。GPT-5.1とGemini 3 Proも追加
- **2025-08-21**: DeepSeek V3.1追加、OpenAI o3/o4-mini最新公式情報でアップデート
- **2025-08-07**: 初版作成、最新のSWE-benchランキングを収集・整理