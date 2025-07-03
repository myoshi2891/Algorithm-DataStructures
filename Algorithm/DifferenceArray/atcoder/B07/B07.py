# この問題では、**いもす法（差分配列）＋累積和**を用いて、最大入力でも高速に処理できます。
# ## ✅ Pythonコード（型付き・高速対応）
from typing import List
import sys

def main() -> None:
    input = sys.stdin.readline

    T: int = int(input())
    N: int = int(input())

    # 差分配列の初期化（サイズ T+1）
    cnt: List[int] = [0] * (T + 1)

    # 差分の更新
    for _ in range(N):
        L_str, R_str = input().split()
        L: int = int(L_str)
        R: int = int(R_str)
        cnt[L] += 1
        cnt[R] -= 1

    # 累積和を計算して出力
    current: int = 0
    output: List[str] = []
    for t in range(T):
        current += cnt[t]
        output.append(str(current))

    # 出力（高速化のため一括）
    print("\n".join(output))


if __name__ == "__main__":
    main()
# 
# 📥 入力例
# 
# ```
# 10
# 7
# 0 3
# 2 4
# 1 3
# 0 3
# 5 6
# 5 6
# 5 6
# ```
# 
# ---
# 
# 📤 出力例
# 
# ```
# 2
# 3
# 4
# 1
# 0
# 3
# 0
# 0
# 0
# 0
# ```
# 
# ---
# 
# 🧠 補足
# 
## 型アノテーション解説
# 
# | 変数        | 型           | 説明                 |
# | --------- | ----------- | ------------------ |
# | `T`       | `int`       | 開店から閉店までの時間（0〜T-1） |
# | `N`       | `int`       | 従業員数               |
# | `cnt`     | `List[int]` | 差分配列               |
# | `current` | `int`       | 現在の従業員数（累積用）       |
# | `output`  | `List[str]` | 出力行のバッファ（高速出力用）    |
# 
# ---
# 
# 🧮 計算量
# 
# * 差分更新：O(N)
# * 累積和＋出力：O(T)
# * 合計：O(N + T) → 最大でも 10⁶ 程度、余裕で間に合います。
# 
# ---
# 
# ✅ 実行方法（例）
# 
# ファイル名を `main.py` にして、以下のように標準入力から実行できます：
# 
# ```bash
# python3 main.py < input.txt
# ```
# 
