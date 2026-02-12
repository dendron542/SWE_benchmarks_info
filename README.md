# SWE-bench AIランキング (2026年2月版)

## 📊 概要

このプロジェクトは、2026年2月時点でのSWE-benchベンチマークにおける各種AIモデルの最新スコアとランキングを提供します。

## 🏆 トップ10モデル（SWE-bench Verified）

1. **Claude Opus 4.5**: 80.9% （2025年11月リリース）
2. **Claude Opus 4.6**: 80.8% （2026年2月リリース）🆕
3. **GPT-5.2 Thinking**: 80.0% （2025年12月リリース）
4. **GLM-5**: 77.8% （2026年2月リリース）🆕
5. **Claude Sonnet 4.5**: 77.2% （2025年9月リリース）
6. **Kimi K2.5**: 76.8% （2026年1月リリース）
7. **GPT-5.1**: 76.3% （2025年11月リリース）
8. **Gemini 3 Pro**: 76.2% （2025年11月リリース）
9. **GPT-5**: 74.9% （2025年8月リリース）
10. **MiniMax M2.1**: 74.0% （2025年12月リリース）

### 新着のトップモデル

#### Claude Opus 4.6 #2 🆕
- **80.8%** - SWE-bench Verified（2026年2月5日リリース）
- **ARC-AGI-2 68.8%** - Opus 4.5の37.6%からほぼ倍増、抽象推論で歴史的な飛躍
- **1Mコンテキストウィンドウ** - ベータ版で100万トークン対応、128K出力上限
- **Adaptive Thinking** - タスクの複雑さに応じて推論深度を自動調整
- **Agent Teams** - マルチエージェント協調によるClaude Code高度オーケストレーション
- **OSWorld 72.7%** - エージェント型コンピュータ操作で最高スコア
- **Terminal-Bench 2.0** - 65.4%達成（Opus 4.5の59.3%から向上）
- **BrowseComp** - 84.0%達成、研究エージェントに最適
- **API価格** - $5.00/1M入力、$25.00/1M出力（Opus 4.5と同価格）

#### GLM-5 #4 🆕
- **77.8%** - SWE-bench Verified（2026年2月11日リリース）
- **オープンソース最強モデル** - MITライセンスで公開、Zhipu AI（Z.AI）による最新フラッグシップ
- **744B MoEアーキテクチャ** - 744億パラメータ（アクティブ40B）、GLM-4.5の355Bから大幅スケールアップ
- **SWE-bench Multilingual** - 73.3%達成（GLM-4.7から+6.6%向上）
- **Terminal-Bench 2.0** - 56.2%達成（GLM-4.7から+15.2向上）
- **AIME 2026 I** - 92.7%達成
- **Huaweiアセンドチップ** - 米国製ハードウェアに依存せず完全に訓練
- **API価格** - $0.80/1M入力、$2.56/1M出力（Claude Opus 4.6の約6分の1）

#### GPT-5.3 Codex 🆕
- **SWE-bench Pro 56.8%** - 新SOTA達成（GPT-5.2 Codexの56.4%を更新）
- **Terminal-Bench 2.0 77.3%** - 全モデル最高スコア（GPT-5.2 Codexの64.0%から大幅向上）
- **OSWorld-Verified 64.7%** - 人間の72%に迫るエージェント型コンピュータ操作能力
- **GPT-5.2 + GPT-5.2-Codexの統合** - コーディング能力と推論能力を統合した最新エージェントモデル
- **400Kコンテキスト** - 400,000トークン、128K出力上限
- **25%高速化** - GPT-5.2-Codexと比較して25%高速化
- **API価格** - 未発表（GPT-5.2参考価格: $1.75/$14.00 per 1M tokens）
- **SWE-bench Verified** - 未公開（OpenAIはSWE-bench Proに重点移行）

#### GPT-5.2 Thinking #3
- **80.0%** - SWE-bench Verified（2025年12月11日リリース）
- **SWE-bench Pro SOTA** - 55.6%を達成、複数言語対応の新記録
- **超大容量コンテキスト** - 400Kトークン（GPT-5の3倍）、128K出力上限
- **3つのバリアント** - Instant（速度重視）、Thinking（推論重視）、Pro（高度なタスク）
- **ARC-AGI** - 91.4%達成、人間レベルのAGI推論能力
- **API価格** - $1.75/1M入力、$14.00/1M出力（キャッシュ90%割引で$0.175/1M）
- **GDPval** - 70.9%達成、専門家レベルのパフォーマンス

#### Kimi K2.5 #4 🆕
- **76.8%** - SWE-bench Verified（2026年1月リリース）
- **最強のオープンソースマルチモーダルエージェントモデル** - Moonshot AIによる最新モデル
- **マルチモーダル対応** - 128Kコンテキストウィンドウ
- **エージェント機能** - 最大100エージェントのスウォーム対応
- **SWE-bench Multilingual** - 73.0%達成
- **Terminal-Bench 2.0** - 50.8%達成
- **LiveCodeBench V6** - 85.0%達成
- **API価格** - $0.60/1M入力、$2.50/1M出力

#### MiniMax M2.1 #8
- **74.0%** - SWE-bench Verified（2025年12月23日リリース）
- **最強のオープンソースモデル** - エージェントワークロードで最高性能
- **Sparse MoE アーキテクチャ** - 2300億パラメータ（アクティブは100億）
- **コスト効率** - Claude 4.5 Sonnetの8%のコストで2倍の推論速度
- **API価格** - $0.27/1M入力、$1.12/1M出力
- **SWE-bench Multilingual** - 72.5%達成、非Python言語（Rust、Go、Java）で競合を凌駕
- **知識カットオフ** - 2025年12月リリース

#### GLM-4.7 #9
- **73.8%** - SWE-bench Verified（2025年12月22日リリース）
- **GLM-4.6から+5.8%向上** - 前バージョンから大幅に改善
- **LiveCodeBench V6** - 84.9達成、Claude Sonnet 4.5を超える
- **SWE-bench Multilingual** - 66.7%（GLM-4.6から+12.9%向上）
- **Terminal Bench 2.0** - 41.0%（+16.5%改善）
- **API価格** - $0.60/1M入力、$2.20/1M出力（キャッシュ利用時$0.11/1M）
- **オープンウェイトモデル** - Zhipu AIによる最新のコーディング・推論モデル

#### MiniMax M2 #18
- **69.4%** - SWE-bench Verified（2025年10月27日リリース）
- **オープンウェイトモデル** - 2300億パラメータ（アクティブは100億）
- **驚異的なコスト効率** - Claude 4.5 Sonnetの8%のコストで2倍の推論速度
- **API価格** - $0.30/1M入力、$1.20/1M出力（キャッシュヒット時$0.03/1M）
- **Sparse MoE アーキテクチャ** - 最新のMixture-of-Expertsアーキテクチャ採用

#### Claude Opus 4.5 🏆 #1
- **80.9%** - SWE-bench Verified（2025年11月24日リリース）
- **世界初の80%超え** - SWE-bench Verifiedで初めて80%の壁を突破したモデル
- **200K コンテキストウィンドウ** - 200,000トークンの長文対応、64Kトークン出力上限
- **Effortパラメータ** - 推論深度を調整可能、中程度の努力でSonnet 4.5と同等の性能を76%少ないトークンで実現
- **多言語コーディング** - SWE-bench Multilingualで8つのプログラミング言語中7つでトップ
- **API価格** - $5.00/1M入力、$25/1M出力（前世代Opusより66%値下げ）
- **知識カットオフ** - 2025年3月までの確実な知識

#### Claude Sonnet 4.5 #3
- **77.2%** - SWE-bench Verified（2025年9月29日リリース）
- **世界最高のコーディングモデル** - Anthropicが公式に「best coding model in the world」と発表
- **並列計算で82.0%** - テスト時並列計算を使用した場合の最高スコア
- **長時間集中** - 30時間以上の複雑なマルチステップタスクに対応
- **Agentic Terminal Coding** - 50.0%を達成（Claude Sonnet 4の36.4%から大幅向上）
- **API価格** - $3.00/1M入力（<200K）、$15/1M出力（<200K）

#### GPT-5.1 #4
- **76.3%** - SWE-bench Verified（2025年11月12日リリース）
- **効率改善** - GPT-5より30%少ないトークンで実行
- **2つのバリエーション** - GPT-5.1 Instant（高速）とGPT-5.1 Thinking（高度な推論）
- **キャッシング機能** - 90%割引、24時間保持
- **API価格** - $1.25/1M入力、$10/1M出力

#### Gemini 3 Pro #5
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
- **2025年**: 80.9% - Claude Opus 4.5が80%の壁を突破（11月）、Claude Sonnet 4.5が77.2%達成（9月）、GPT-5.1（76.3%）とGemini 3 Pro（76.2%）が続く
- **2026年**: 80.8% - Claude Opus 4.6（2月）、GLM-5が77.8%でオープンソース最高記録（2月）、GPT-5.3 CodexがTerminal-Bench 2.0で77.3%達成（2月）

## 📊 完全ランキング（SWE-bench Verified + Pro）

| ランク | モデル名 | Verified | Pro | 組織 | リリース時期 | API価格（入力/出力） |
|--------|----------|----------|-----|------|--------------|---------------------|
| 1 | Claude Opus 4.5 | 80.9% | 45.9% | Anthropic | 2025年11月 | $5.00/$25.00 per 1M tokens |
| 2 | Claude Opus 4.6 🆕 | 80.8% | - | Anthropic | 2026年2月 | $5.00/$25.00 per 1M tokens |
| 3 | GPT-5.2 Thinking | 80.0% | 55.6% | OpenAI | 2025年12月 | $1.75/$14.00 per 1M tokens |
| 4 | GLM-5 🆕 | 77.8% | - | Zhipu AI (Z.AI) | 2026年2月 | $0.80/$2.56 per 1M tokens |
| 5 | Claude Sonnet 4.5 | 77.2% | 43.6% | Anthropic | 2025年9月 | $3.00/$15.00 per 1M tokens |
| 6 | Kimi K2.5 | 76.8% | - | Moonshot AI | 2026年1月 | $0.60/$2.50 per 1M tokens |
| 7 | GPT-5.1 | 76.3% | - | OpenAI | 2025年11月 | $1.25/$10.00 per 1M tokens |
| 8 | Gemini 3 Pro | 76.2% | 43.3% | Google | 2025年11月 | $2.00/$12.00 per 1M tokens |
| 9 | GPT-5 | 74.9% | 41.8% | OpenAI | 2025年8月 | $1.25/$10.00 per 1M tokens |
| 10 | MiniMax M2.1 | 74.0% | 36.8% | MiniMax | 2025年12月 | $0.27/$1.12 per 1M tokens |
| 11 | GLM-4.7 | 73.8% | - | Zhipu AI | 2025年12月 | $0.60/$2.20 per 1M tokens |
| 12 | Grok 4 | 73.5% | - | xAI | 2025年7月 | $3.00/$15.00 per 1M tokens |
| 13 | DeepSeek 3.2 Thinking | 73.1% | - | DeepSeek | 2025年9月 | $0.28/$0.42 per 1M tokens |
| 14 | Claude 4 Sonnet | 72.7% | 42.7% | Anthropic | 2025年5月 | $3.00/$15.00 per 1M tokens |
| 15 | Claude 4 Opus | 72.5% | - | Anthropic | 2025年5月 | $15.00/$75.00 per 1M tokens |
| 16 | OpenAI o3 | 71.7% | - | OpenAI | 2025年4月 | $0.40/$1.60 per 1M tokens |
| 17 | Kimi K2 (Parallel) | 71.6% | - | Moonshot AI | 2025年 | $0.15/$2.50 per 1M tokens |
| 18 | Kimi K2 Thinking | 71.3% | - | Moonshot AI | 2025年11月 | $0.15/$2.50 per 1M tokens |
| 19 | OpenAI o3 (Low Compute) | 70.3% | - | OpenAI | 2024年12月 | $0.40/$1.60 per 1M tokens |
| 20 | MiniMax M2 | 69.4% | - | MiniMax | 2025年10月 | $0.30/$1.20 per 1M tokens |
| 21 | o4-mini | 68.1% | - | OpenAI | 2025年4月 | $1.10/$4.40 per 1M tokens |
| 22 | GLM-4.6 | 68.0% | - | Zhipu AI | 2025年9月 | $0.60/$2.20 per 1M tokens |
| 23 | DeepSeek V3.1 | 66.0% | - | DeepSeek | 2025年8月 | $0.27/$1.10 per 1M tokens |
| 24 | DeepSeek R1 (Agentic) | 65.8% | - | DeepSeek | 2025年 | $0.55/$2.19 per 1M tokens |
| 25 | Kimi K2 | 65.8% | 27.7% | Moonshot AI | 2025年 | $0.15/$2.50 per 1M tokens |
| 26 | Mini-SWE-agent | 65.0% | - | Open Source | 2025年 | 無料/オープンソース |
| 27 | GLM-4.5 | 64.2% | - | Zhipu AI | 2025年 | $0.60/$2.20 per 1M tokens |
| 28 | Gemini 2.5 Flash | 63.8% | - | Google | 2025年 | $0.30/$2.50 per 1M tokens |
| 29 | Gemini 2.5 Pro | 63.2% | - | Google | 2025年 | $1.25/$10.00 per 1M tokens (<200K) |
| 30 | GPT-OSS-120b | 62.4% | - | OpenAI | 2025年 | 無料/オープンソース |
| 31 | Claude 3.7 Sonnet | 62.3% | - | Anthropic | 2025年 | $3.00/$15.00 per 1M tokens |
| 32 | CodeStory Midwit Agent | 62.0% | - | CodeStory | 2025年 | N/A |
| 33 | GPT-4.1 | 54.6% | - | OpenAI | 2025年 | $5.00/$15.00 per 1M tokens (est.) |
| 34 | Claude 3.5 Sonnet (Latest) | 50.8% | - | Anthropic | 2024年 | $3.00/$15.00 per 1M tokens |
| 35 | DeepSeek R1 | 49.2% | - | DeepSeek | 2025年 | $0.55/$2.19 per 1M tokens |
| 36 | Claude 3.5 Sonnet (Upgraded) | 49.0% | - | Anthropic | 2024年 | $3.00/$15.00 per 1M tokens |
| 37 | OpenAI o1 | 48.9% | - | OpenAI | 2024年 | $15.00/$60.00 per 1M tokens |
| 38 | Grok 3 | 46.8% | - | xAI | 2025年 | $2.00/$8.00 per 1M tokens (est.) |
| 39 | GPT-4o | 33.2% | - | OpenAI | 2024年 | $2.50/$10.00 per 1M tokens |
| - | GPT-5.3 Codex 🆕 | N/A | 56.8% 🏆 | OpenAI | 2026年2月 | 未発表 |

*Pro列の「-」はデータ未公開を示します。Pro列の🏆はSWE-bench Pro SOTAを示します。GPT-5.3 CodexはSWE-bench Verified未公開のためランク外。*

### 主要モデルの詳細情報

#### トップ3モデルの特徴

**1位: Claude Opus 4.5 (80.9%)**
- 世界初の80%超え達成
- Effortパラメータで推論深度調整可能
- SWE-bench Multilingualで7/8言語トップ
- 200Kコンテキスト、64K出力上限
- 計算コスト: High
- 前世代Opusより66%値下げ

**2位: Claude Opus 4.6 (80.8%)** 🆕
- ARC-AGI-2: 68.8%（Opus 4.5の37.6%からほぼ倍増）
- 1Mコンテキストウィンドウ（ベータ）、128K出力上限
- OSWorld: 72.7%（エージェント型コンピュータ操作）
- Adaptive Thinking、Agent Teams機能搭載
- 計算コスト: High

**3位: GPT-5.2 Thinking (80.0%)**
- SWE-bench Pro SOTA: 55.6%
- 400Kコンテキスト、128K出力上限
- ARC-AGI: 91.4%
- 計算コスト: Very High

## 🔍 ベンチマーク詳細

### SWE-bench Verified
- **タスク数**: 500問
- **特徴**: 人間によって検証された高品質なデータセット
- **目的**: より信頼性の高いAI評価

### SWE-bench Pro 🆕
- **タスク数**: 1,865問（公開セット: 731問）
- **リポジトリ数**: 41の専門リポジトリ
- **特徴**: エンタープライズレベルの複雑な問題を含む大規模ベンチマーク
- **対応言語**: Go、Python、JavaScript、TypeScriptなど複数言語
- **汚染耐性**: GPL等の強いコピーレフトライセンスを使用し、トレーニングデータへの混入を防止
- **目的**: 実際の企業環境に近い複雑なソフトウェア工学タスクでの評価
- **データソース**: [Scale AI SWE-Bench Pro Leaderboard](https://scale.com/leaderboard/swe_bench_pro_public)

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
1. **GPT-5.3 Codex**: 77.3% - 全モデル最高スコア 🆕
2. **Claude Opus 4.6**: 65.4% 🆕
3. **GLM-5**: 56.2% 🆕
4. **Gemini 3 Pro**: 54.2%
5. **Kimi K2.5**: 50.8%
6. **Claude Sonnet 4.5**: 50.0% (Agentic Terminal Coding)
7. **GPT-5.1**: 47.6%

### DeepSeek V3.1 その他のベンチマーク
- **Aider**: 71.6% - 多言語プログラミングテスト
- **SWE-bench Multilingual**: 54.5% - 多言語対応
- **Terminal-bench**: 31.3% - ターミナル操作（旧版）

## ⚠️ 注意事項

- **Claude Opus 4.6**: 2026年2月5日リリース、ARC-AGI-2で68.8%（Opus 4.5の37.6%からほぼ倍増）、1Mコンテキストウィンドウ（ベータ）、Adaptive Thinking・Agent Teams搭載
- **GLM-5**: 2026年2月11日リリース、Zhipu AI（Z.AI）による744B MoEオープンウェイトモデル、SWE-bench Verified 77.8%でオープンソース最強、MITライセンス
- **GPT-5.3 Codex**: 2026年2月5日リリース、GPT-5.2とGPT-5.2-Codexを統合、SWE-bench Pro 56.8%（SOTA）、Terminal-Bench 2.0 77.3%（全モデル最高）、API価格未発表
- **Claude Opus 4.5**: 2025年11月24日リリース、SWE-bench Verifiedで初の80%超え達成、前世代Opusより66%値下げ
- **Claude Sonnet 4.5**: 2025年9月29日リリース、世界最高のコーディングモデル、並列計算で82.0%達成
- **GPT-5.1**: 2025年11月12日リリース、GPT-5より30%効率化、2つのバリエーション（Instant/Thinking）
- **Gemini 3 Pro**: 2025年11月18日リリース、1Mトークンコンテキスト、LMArenaで1501 Eloスコア獲得
- **OpenAI o3**: 2025年4月16日に正式リリース済み、ツール使用可能なエージェント推論モデル
- **o4-mini**: o3の効率版として同時リリース、一部ベンチマークでo3を上回る性能
- **DeepSeek V3.1**: 2025年8月21日リリース、ハイブリッド推論モデル（Think/Non-Thinkモード）
- **データ更新方針**: データ収集は自動化されていますが、最終的な更新は人間による検証を経て手動で行われます
- スコアはモデル単体ではなく、エージェントシステム全体の性能を示します
- 計算コストは実装方法により大きく異なります
- データは2026年2月12日時点の最新公式情報に基づいています

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

- **2026-02-12**: GLM-5（77.8%）、Claude Opus 4.6（80.8%）、GPT-5.3 Codex（SWE-bench Pro 56.8%）を追加。GLM-5は4位にランクイン、オープンソース最強モデル。Claude Opus 4.6はARC-AGI-2で68.8%達成。GPT-5.3 CodexはTerminal-Bench 2.0で77.3%の全モデル最高スコアを達成
- **2026-01-28**: SWE-bench Proスコアを完全ランキングテーブルに追加。GPT-5.2 Thinking（55.6%）がPro SOTAを達成
- **2026-01-28**: Kimi K2.5（76.8%）をREADMEに追加。4位にランクイン、オープンソースマルチモーダルエージェントモデル
- **2026-01-24**: GPT-5.2 Thinking（80.0%）を追加。SWE-bench Pro 55.6%で新記録達成、400Kコンテキストウィンドウ、ARC-AGI 91.4%
- **2026-01-23**: GLM-4.7（73.8%）、MiniMax M2.1（74.0%）、MiniMax M2（69.4%）を追加。最新のオープンソース/オープンウェイトモデルのベンチマークを反映
- **2025-11-25**: Claude Opus 4.5を追加（80.9%）、SWE-bench Verified初の80%超えを達成。全ランキングを更新
- **2025-11-23 (更新3)**: API料金情報を最新データに更新。OpenAI o3（80%値下げで$0.40/$1.60）、o4-mini（$1.10/$4.40）、Grok 4（$3.00/$15.00）、GLM-4.5（$0.60/$2.20）、Gemini 2.5 Pro（$1.25/$10.00）、Claude 3.7 Sonnet（$3.00/$15.00）の価格を更新
- **2025-11-23 (更新2)**: 追加メトリクスを大幅更新 - Codeforces ELO、AIME 2025、Terminal-Bench 2.0の最新スコアを反映。Claude Sonnet 4.5（100% AIME）、Gemini 3 Pro（2,439 ELO、100% AIME）、GPT-5.1（94.0% AIME）の最新ベンチマークを追加
- **2025-11-23**: Claude Sonnet 4.5を追加、新たな世界最高スコア（77.2%）を反映。GPT-5.1とGemini 3 Proも追加
- **2025-08-21**: DeepSeek V3.1追加、OpenAI o3/o4-mini最新公式情報でアップデート
- **2025-08-07**: 初版作成、最新のSWE-benchランキングを収集・整理