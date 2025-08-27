# Python版の背の順区間アルゴリズムを作成します。このPythonコードは以下の特徴を持っています：

# ## 🐍 Python版の最適化ポイント

# ### **型アノテーション**
# - すべての関数に引数・戻り値の型を明示
# - `List[int]`, `str`, `int` など具体的な型を指定
# - コードの可読性と保守性を向上

# ### **メモリ効率の配慮**
# ```python
# # リスト内包表記でメモリ効率を向上
# heights = [int(lines[i]) for i in range(1, n + 1)]

# # 事前にサイズを指定してメモリ確保
# dp = [0] * n
# ```

# ### **処理時間の最適化**
# - **O(n)の線形時間**: 各要素を一度だけ処理
# - **max()関数**: 内部でC実装を使用し高速
# - **インデックス直接アクセス**: リストの要素に直接アクセス

# ### **エラーハンドリング**
# ```python
# try:
#     # メイン処理
# except (ValueError, IndexError) as e:
#     # 入力形式エラー
# except Exception as e:
#     # その他の予期しないエラー
# ```

# ## 📊 計算量分析

# **時間計算量: O(n)**
# - 入力読み取り: O(n)
# - DP配列計算: O(n)
# - 最大値取得: O(n)

# **空間計算量: O(n)**
# - `heights`配列: O(n)
# - `dp`配列: O(n)
# - その他の変数: O(1)

# ## 🔄 アルゴリズムの動作

# **入力例**: n=5, [160, 178, 170, 190, 190]

# 1. **初期化**: `dp[0] = 1`
# 2. **i=1**: 160 ≤ 178 → `dp[1] = dp[0] + 1 = 2`
# 3. **i=2**: 178 > 170 → `dp[2] = 1` (新区間)
# 4. **i=3**: 170 ≤ 190 → `dp[3] = dp[2] + 1 = 2`
# 5. **i=4**: 190 ≤ 190 → `dp[4] = dp[3] + 1 = 3`
# 6. **結果**: `max([1, 2, 1, 2, 3]) = 3`

# このPython実装は、型安全性とパフォーマンスを両立し、制約条件（n ≤ 200,000）下でも効率的に動作します。

import sys
from typing import List


def find_longest_non_decreasing_sequence(input_data: str) -> int:
    """
    標準入力から文字列を読み取り、背の順区間の最長長さを計算する

    Args:
        input_data (str): 標準入力の文字列（改行区切り）

    Returns:
        int: 背の順であるような区間のうち、最長であるものの長さ

    Time Complexity: O(n) - 配列を一度だけ走査
    Space Complexity: O(n) - heights配列とdp配列を使用
    """
    lines: List[str] = input_data.strip().split("\n")
    n: int = int(lines[0])

    # 身長データを配列に格納（メモリ効率を考慮してリスト内包表記を使用）
    heights: List[int] = [int(lines[i]) for i in range(1, n + 1)]

    # dp[i] = i番目の人が右端となる背の順区間の最長長さ
    # 初期化時にサイズを指定してメモリ効率を向上
    dp: List[int] = [0] * n
    dp[0] = 1  # 最初の人は長さ1の区間

    # 動的プログラミングでdp配列を計算
    # インデックスは0-basedで処理
    for i in range(1, n):
        if heights[i - 1] <= heights[i]:
            # 前の人の身長以上なら、前の区間に追加できる
            dp[i] = dp[i - 1] + 1
        else:
            # 前の人より身長が低いなら、新しい区間の開始
            dp[i] = 1

    # dp配列の最大値を求める（max関数を使用して効率的に取得）
    return max(dp)


def process_input() -> str:
    """
    標準入力を読み取る

    Returns:
        str: 標準入力の全体文字列

    Note:
        sys.stdin.read()を使用してメモリ効率を重視
    """
    return sys.stdin.read()


def main() -> None:
    """
    メイン処理関数
    標準入力を読み取り、結果を標準出力に出力する

    Returns:
        None

    Raises:
        SystemExit: 入力読み取りエラー時に終了コード1で終了
    """
    try:
        # 標準入力を読み取り
        input_data: str = process_input()

        # 最長の背の順区間の長さを計算
        result: int = find_longest_non_decreasing_sequence(input_data)

        # 結果を出力
        print(result)

    except (ValueError, IndexError) as e:
        print(f"Error processing input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
