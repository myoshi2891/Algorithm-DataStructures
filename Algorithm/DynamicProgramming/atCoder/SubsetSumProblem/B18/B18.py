
# ---

# ## ✅ 想定される誤答の原因

# ### 1. **複数のカードに同じ値がある場合の経路復元の誤り**

# * たとえば、`A = [2, 2, 3]` のように同じ値が複数ある場合に、

#   * `dp[i][s] = j` のような「A\[j]を使った」という記録方法だけでは、
#   * **どの「2」を使ったのか曖昧になり、復元に失敗**することがあります。

# ### 2. **和を構成するカードが一意に決まらない場合の復元ミス**

# * 同じ `curr_sum` を複数のパスから構成できる場合、

#   * 現在のコードでは **直前のインデックス `i` の記録**しかしていないため、
#   * 結果的に `curr_sum - A[i]` が `dp[i]` に存在しないパスをたどる可能性があります。

# ---

# ## ✅ 修正方針：より堅牢な「どのカードを使ったか」を記録

# ### 🔁 修正点（配列の添え字を保存して復元可能にする）

# ```python
from typing import List, Optional
import sys

def main() -> None:
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    N: int = data[0]
    S: int = data[1]
    A: List[int] = data[2:]
    
    # dp[s] = (i, prev_s) => カードiを使って s を構成、直前の合計は prev_s
    dp: dict[int, Optional[tuple[int, int]]] = {0: None}

    for i in range(N):
        next_dp = dp.copy()
        for s in dp:
            new_sum = s + A[i]
            if new_sum <= S and new_sum not in next_dp:
                next_dp[new_sum] = (i, s)
        dp = next_dp

    if S not in dp:
        print(-1)
        return
    
    # 経路復元
    res: List[int] = []
    curr_sum: int = S
    while curr_sum != 0:
        value = dp.get(curr_sum)
        if value is None:
            raise ValueError(f"dp[{curr_sum}] is None")
        i: int
        prev_sum: int
        i, prev_sum = value
        res.append(i + 1)  # 1-indexed
        curr_sum = prev_sum

    res.reverse()
    print(len(res))
    print(*res)

if __name__ == "__main__":
    main()
# ```

# ---

# ## ✅ 修正内容のポイント

# | 修正前                     | 修正後                          |
# | ----------------------- | ---------------------------- |
# | `dp[i][s] = index`（不完全） | `dp[s] = (index, 前の合計値)`（完全） |
# | `dp`を2次元配列で記録           | `dp`を1次元辞書で記録（合計値ごと）         |
# | 経路復元が不正確                | 正確にどのカードを使ったか復元可能            |

# ---

# ## ✅ 動作確認例

# ### 入力例 1

# ```
# 3 7
# 2 2 3
# ```

# ### 出力例 1

# ```
# 3
# 1 2 3
# ```

# ---

# ## ✅ 計算量（変化なし）

# * 時間: `O(N*S)`
# * 空間: `O(S)`（1次元辞書に改善）

# ---

# ## ✅ 期待される効果

# * 同じ値のカードが複数あっても **個別に追跡**できる
# * 複数のルートが存在しても **正確なパス復元**が可能
# * これにより、**誤答の2件が解消される可能性が高い**です

