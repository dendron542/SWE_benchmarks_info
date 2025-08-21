#!/usr/bin/env python3
"""
SWE-bench ランキング表示ツール
"""

import json
import csv
from pathlib import Path
from typing import Dict, List, Any
import argparse


def load_json_data(file_path: str) -> Dict[str, Any]:
    """JSONファイルからデータを読み込む"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_csv_data(file_path: str) -> List[Dict[str, str]]:
    """CSVファイルからデータを読み込む"""
    with open(file_path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def display_ranking_table(
    ranking_data: List[Dict[str, Any]], benchmark_name: str
) -> None:
    """ランキングテーブルを表示"""
    print(f"\n{'=' * 100}")
    print(f"[RANKING] {benchmark_name} ランキング (APIコスト含む)")
    print(f"{'=' * 100}")

    # ヘッダー
    print(
        f"{'順位':<4} {'モデル名':<30} {'スコア':<8} {'組織':<12} {'入力コスト':<12} {'出力コスト':<12} {'備考':<20}"
    )
    print(f"{'-' * 4} {'-' * 30} {'-' * 8} {'-' * 12} {'-' * 12} {'-' * 12} {'-' * 20}")

    # データ行
    for item in ranking_data:
        rank = str(item.get("rank", "N/A"))
        model = item.get("model_name", "N/A")
        score = f"{item.get('score', 0):.1f}%"
        org = item.get("organization", "N/A")
        input_cost = item.get("api_cost_input", "N/A")[:10] + (
            "..." if len(item.get("api_cost_input", "")) > 10 else ""
        )
        output_cost = item.get("api_cost_output", "N/A")[:10] + (
            "..." if len(item.get("api_cost_output", "")) > 10 else ""
        )
        notes = item.get("notes", "N/A")[:18] + (
            "..." if len(item.get("notes", "")) > 18 else ""
        )

        print(
            f"{rank:<4} {model:<30} {score:<8} {org:<12} {input_cost:<12} {output_cost:<12} {notes:<20}"
        )


def display_performance_trends(trends_data: Dict[str, Any]) -> None:
    """パフォーマンストレンドを表示"""
    print(f"\n{'=' * 80}")
    print("[TRENDS] SWE-bench パフォーマンストレンド")
    print(f"{'=' * 80}")

    for year, data in trends_data.items():
        success_rate = data["swe_bench_success_rate"]
        description = data["description"]
        print(f"{year}: {success_rate}% - {description}")


def display_coding_metrics(metrics_data: Dict[str, Any]) -> None:
    """コーディングメトリクスを表示"""
    print(f"\n{'=' * 80}")
    print("[CODING] コーディング競技スコア")
    print(f"{'=' * 80}")

    # Codeforces ELO
    print("\n[ELO] Codeforces ELO ランキング:")
    print(f"{'モデル名':<25} {'ELO':<6} {'パーセンタイル':<10}")
    print(f"{'-' * 25} {'-' * 6} {'-' * 10}")

    for item in metrics_data.get("codeforces_elo", []):
        model = item["model_name"]
        elo = item["elo_rating"]
        percentile = f"{item['percentile']:.1f}%"
        print(f"{model:<25} {elo:<6} {percentile:<10}")

    # AIME Scores
    print("\n[AIME] AIME スコア:")
    print(f"{'モデル名':<25} {'スコア':<8} {'年度':<6}")
    print(f"{'-' * 25} {'-' * 8} {'-' * 6}")

    for item in metrics_data.get("aime_scores", []):
        model = item["model_name"]
        score = f"{item['score']:.1f}%"
        year = item["year"]
        print(f"{model:<25} {score:<8} {year:<6}")


def display_top_models_summary() -> None:
    """トップモデルの簡潔なサマリーを表示"""
    print(f"\n{'=' * 100}")
    print("[TOP3] 2025年 SWE-bench 最優秀モデル（トップ3）- APIコスト比較")
    print(f"{'=' * 100}")

    top_models = [
        {
            "name": "Claude 4 Sonnet",
            "score": 72.7,
            "input_cost": "$3.00",
            "output_cost": "$15.00",
            "status": "2025年5月リリース",
        },
        {
            "name": "Claude 4 Opus",
            "score": 72.5,
            "input_cost": "$15.00",
            "output_cost": "$75.00",
            "status": "高計算時79.4%",
        },
        {
            "name": "OpenAI o3",
            "score": 72.0,
            "input_cost": "$1.00",
            "output_cost": "$4.00",
            "status": "未公開",
        },
    ]

    print(
        f"{'順位':<4} {'モデル名':<20} {'スコア':<8} {'入力コスト/1M':<12} {'出力コスト/1M':<12} {'ステータス':<20}"
    )
    print(f"{'-' * 4} {'-' * 20} {'-' * 8} {'-' * 12} {'-' * 12} {'-' * 20}")

    for i, model in enumerate(top_models, 1):
        print(
            f"{i:<4} {model['name']:<20} {model['score']:.1f}%{'':<3} {model['input_cost']:<12} {model['output_cost']:<12} {model['status']:<20}"
        )


def main():
    parser = argparse.ArgumentParser(description="SWE-bench ランキング表示ツール")
    parser.add_argument(
        "--format",
        choices=["summary", "full", "json"],
        default="summary",
        help="表示形式",
    )
    parser.add_argument(
        "--benchmark",
        choices=["verified", "full", "lite", "all"],
        default="verified",
        help="ベンチマークタイプ",
    )

    args = parser.parse_args()

    # データファイルのパス
    json_path = Path(__file__).parent / "swe_bench_ranking.json"

    try:
        data = load_json_data(json_path)

        if args.format == "summary":
            display_top_models_summary()
            display_performance_trends(data["performance_trends"])

        elif args.format == "full":
            if args.benchmark == "verified" or args.benchmark == "all":
                verified_data = data["swe_bench_verified_ranking"]
                display_ranking_table(verified_data["ranking"], "SWE-bench Verified")

            if args.benchmark == "full" or args.benchmark == "all":
                full_data = data["swe_bench_full_ranking"]
                display_ranking_table(full_data["ranking"], "SWE-bench Full")

            if args.benchmark == "lite" or args.benchmark == "all":
                lite_data = data["swe_bench_lite_ranking"]
                display_ranking_table(lite_data["ranking"], "SWE-bench Lite")

            display_coding_metrics(data["coding_performance_metrics"])
            display_performance_trends(data["performance_trends"])

        elif args.format == "json":
            print(json.dumps(data, indent=2, ensure_ascii=False))

    except FileNotFoundError:
        print(f"[ERROR] データファイルが見つかりません: {json_path}")
    except json.JSONDecodeError:
        print(f"[ERROR] JSONファイルの読み込みに失敗しました: {json_path}")
    except Exception as e:
        print(f"[ERROR] エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
