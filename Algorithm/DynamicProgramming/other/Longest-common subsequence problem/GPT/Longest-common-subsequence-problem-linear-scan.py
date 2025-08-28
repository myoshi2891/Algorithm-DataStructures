# 了解しました。それでは問題を **Python 3.8.10** 用に最適化し、
# 型アノテーション・処理時間・メモリ消費量に配慮した解法を提示します。

# ---

# ## アルゴリズムの考え方

# * 区間 `[l, r]` が「逆背の順」であるとは、`a[i] >= a[i+1]` が連続して成り立つ部分列です。
# * つまり「**非増加列 (non-increasing subsequence)**」のうち最長の長さを求める問題です。
# * 線形走査で十分対応可能です。

# **手順**

# 1. 入力を受け取り、身長のリスト `a` を構築する。
# 2. `current_len` で現在の逆背区間の長さを管理し、前の要素と比較して更新。
# 3. `max_len` を更新しながら最後まで走査する。
# 4. 出力する。

# ---

# ## 計算量

# * **時間計算量:** `O(n)` （一度の線形走査のみ）
# * **空間計算量:** `O(1)` （入力配列以外は定数領域）

# ---

# ## 実装コード

# ```python
from typing import List

class Solution:
    def longest_non_increasing_segment(self, n: int, a: List[int]) -> int:
        """
        最長の「逆背の順」区間の長さを求める

        Parameters
        ----------
        n : int
            人数 (1 <= n <= 200,000)
        a : List[int]
            各人の身長リスト (100 <= a_i <= 200)

        Returns
        -------
        int
            最長の「逆背の順」区間の長さ
        """
        max_len: int = 1   # 最小でも1人の区間は存在する
        current_len: int = 1

        for i in range(1, n):
            if a[i-1] >= a[i]:
                current_len += 1
            else:
                current_len = 1
            if current_len > max_len:
                max_len = current_len

        return max_len


if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split()
    n: int = int(input_data[0])
    a: List[int] = list(map(int, input_data[1:]))
    
    solver = Solution()
    result: int = solver.longest_non_increasing_segment(n, a)
    print(result)
# ```

# ---

# このコードは `n = 200,000` の最大ケースでも **O(n)** で処理でき、
# 追加メモリも定数領域しか使わないため、
# **実行時間・メモリ使用量ともに効率的**です。

# ---

# 👉 必要であれば、入力例を実際にシミュレーションして計算の流れを図解して説明しましょうか？
