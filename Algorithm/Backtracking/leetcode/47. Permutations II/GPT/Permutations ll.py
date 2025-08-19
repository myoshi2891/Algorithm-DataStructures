# ```python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        パラメータ:
            nums: List[int] - 重複を含む可能性がある整数配列
        返却値:
            List[List[int]] - 一意な順列の全パターン

        処理概要:
        1. 入力配列をソートすることで重複処理を容易にする。
        2. バックトラッキングにより順列を生成。
        3. 直前の要素と同じで、かつ未使用の場合はスキップすることで重複順列を防ぐ。

        計算量:
            - 時間計算量: O(n * n!) （順列生成の特性上。ただし重複を排除するため平均的には少し軽減される）
            - 空間計算量: O(n) （再帰スタック + 使用中フラグ配列）
        
        実行環境:
            Python (CPython 3.11.4), LeetCode想定
        """
        nums.sort()  # ソートで重複管理を容易にする
        res: List[List[int]] = []
        used: List[bool] = [False] * len(nums)
        path: List[int] = []

        def backtrack() -> None:
            if len(path) == len(nums):
                res.append(path[:])  # 完成した順列を追加
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # 直前と同じ値で、かつ前が未使用ならスキップ（重複防止）
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])

                backtrack()

                # 戻す処理（バックトラッキング）
                path.pop()
                used[i] = False

        backtrack()
        return res
# ```

# ---

# ### 🔎 処理時間・メモリの消費量について

# * **時間計算量**:

#   * 最悪ケース: `O(n * n!)` （順列生成の特性）
#   * ただし `n <= 8` の制約なので、計算可能範囲。
# * **空間計算量**:

#   * `O(n)` （`used` 配列, `path` 一時リスト, 再帰スタック）
#   * `res` のサイズは結果の順列数に比例するため、理論上最大 `O(n * n!)` 要素を保持する。

# ---

# 👉 この後は「**実行時の再帰スタックの流れを図解**」して、Python 実装に合わせて可視化してみましょうか？
