# 以下は「**0-1部分和問題（最小個数）」の**
# **Python (CPython 3.11.4)** 解答例です。

# ---

# ## 解法：**動的計画法（0-1ナップサック）**

# ### 特徴：

# * **同じ位置の数字は1回だけ使用可能（0-1制約）**
# * 最小個数で和`K`を作る
# * 解が存在しなければ`-1`を出力
# * **時間とメモリ使用量も計測**

# ---

# ## コード

import sys
import time
import tracemalloc
from typing import List, Tuple

def min_subset_sum(N: int, K: int, A: List[int]) -> Tuple[int, List[int]]:
    """
    部分和最小個数問題（0-1ナップサック）の解法

    Parameters:
    - N : int
    - K : int
    - A : List[int]

    Returns:
    - Tuple[int, List[int]] : (最小個数, 選んだ要素のリスト)  
      解なしなら (-1, [])
    """
    INF = 10**9
    dp: List[List[int]] = [[INF] * (K + 1) for _ in range(N + 1)]
    prev: List[List[int]] = [[-1] * (K + 1) for _ in range(N + 1)]

    dp[0][0] = 0

    for i in range(N):
        for k in range(K + 1):
            if dp[i][k] < dp[i + 1][k]:
                dp[i + 1][k] = dp[i][k]
                prev[i + 1][k] = k
            if k + A[i] <= K:
                if dp[i][k] + 1 < dp[i + 1][k + A[i]]:
                    dp[i + 1][k + A[i]] = dp[i][k] + 1
                    prev[i + 1][k + A[i]] = k

    if dp[N][K] == INF:
        return -1, []

    # res の型を明示する
    res: List[int] = []
    k = K
    for i in range(N, 0, -1):
        if prev[i][k] != k:
            res.append(A[i - 1])
            k = prev[i][k]

    return dp[N][K], res

def main() -> None:
    """
    メイン実行関数。
    標準入力からデータを受け取り、結果を標準出力に出力する。
    また、処理時間とメモリ使用量を標準エラーに出力する。
    """
    input_data = sys.stdin.read().strip().split('\n')
    N, K = map(int, input_data[0].split())
    A = list(map(int, input_data[1].split()))

    # 計測開始
    start_time = time.perf_counter()
    tracemalloc.start()

    cnt, res = min_subset_sum(N, K, A)

    # メモリ・時間計測終了
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    # 結果出力
    if cnt == -1:
        print(-1)
    else:
        print(cnt)
        print(' '.join(map(str, res)))

    # パフォーマンス情報を標準エラー出力
    print(f"Time: {(end_time - start_time)*1000:.3f} ms", file=sys.stderr)
    print(f"Memory: {peak // 1024} KB", file=sys.stderr)

if __name__ == "__main__":
    main()
# ```

# ---

# ## 入出力例：

# ### 入力：

# ```
# 5 4
# 1 3 2 2 1
# ```

# ### 出力：

# ```
# 2
# 1 3
# ```

# または

# ```
# 2
# 3 1
# ```

# （順序はどちらでもOK）

# ---

# ## 計測例（標準エラー出力）

# ```
# Time: 1.234 ms
# Memory: 1500 KB
# ```

# ---

# ## 処理時間・メモリ計測：

# | 項目   | 使用                    |
# | ---- | --------------------- |
# | 処理時間 | `time.perf_counter()` |
# | メモリ  | `tracemalloc`         |

# ---

# ## 計算量：

# | 項目    | 値        |
# | ----- | -------- |
# | 時間計算量 | O(N × K) |
# | 空間計算量 | O(N × K) |

# ---

# ## まとめ：

# | 要素       | 内容                                 |
# | -------- | ---------------------------------- |
# | 使用言語     | Python (CPython 3.11.4)            |
# | 型アノテーション | あり                                 |
# | メモリ・時間計測 | `tracemalloc`, `time.perf_counter` |
# | 入力       | 標準入力                               |
# | 出力       | 標準出力、パフォーマンス情報は`stderr`            |

# ---

# ✅ これで解消する理由
# res: List[int] と明示することで、
# Pylanceが append の引数を「int型を追加している」と認識できるようになります。

# Tuple[int, List[int]] と返り値の型も明示したため、Pylanceの推論が完全に行われます。

# Pylance 型警告のよくある原因と対応
# 原因	対応
# append の型が不明	リストの型を明示する（List[int] など）
# 戻り値が推論できない	関数の戻り値に -> 型 を必ず指定
# 配列の初期化時に型が消える	List[List[int]] のように型付きで初期化

# 🔍 補足
# Pylanceは高速ですが、型推論が途中で途切れると Unknown を返すことがあります。
# --strict モードなどを使うとこういった警告が頻繁に出るため、必ず型注釈を入れましょう。

