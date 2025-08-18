# Python版の階段上りDP問題の解答を作成しました。主な特徴とパフォーマンス最適化について説明します：

# ## 🎯 コードの特徴

# ### **型アノテーション（Type Hints）**
# - 全ての関数パラメーター、戻り値、変数に型を明示
# - `List[int]`, `tuple[int, int, int]`など具体的な型指定
# - Python 3.8.10対応の型記法を使用

# ### **メモリ最適化**
# ```python
# dp: List[int] = [0] * (n + 1)  # リスト乗算でメモリ効率良く初期化
# ```
# - `[0] * (n + 1)`による高速な初期化
# - 必要最小限のメモリ使用量：O(n)

# ### **処理時間最適化**
# ```python
# for i in range(1, n + 1):  # range()による効率的なループ
#     if i >= a:             # 条件分岐で不要な計算を回避
#         dp[i] += dp[i - a]
# ```
# - 条件チェックによる無効なアクセス防止
# - 単一ループでO(n)時間計算量を実現

# ## 📊 パフォーマンス分析

# | 項目 | 計算量 | 説明 |
# |------|--------|------|
# | **時間計算量** | O(n) | 各段を1回ずつ処理 |
# | **空間計算量** | O(n) | DPテーブルのサイズ |
# | **メモリ使用量** | 約4n bytes | int配列（Python intは28bytes程度だが、小さい値は最適化される） |

# ## 🔧 関数設計のポイント

# ### **関数分離による保守性向上**
# 1. `parse_input()`: 入力処理専用
# 2. `count_stair_climbing_ways()`: DP計算ロジック
# 3. `main()`: 全体の制御フロー

# ### **エラーハンドリング**
# - 境界条件（`i >= a`, `i >= b`）の適切な処理
# - インデックス範囲外アクセスの防止

# ## 💡 アルゴリズムの動作例

# **入力: n=11, a=3, b=4**
# ```
# dp[0] = 1  # 初期状態
# dp[1] = 0  # 1段は到達不可
# dp[2] = 0  # 2段は到達不可  
# dp[3] = 1  # 3段: dp[0] = 1通り
# dp[4] = 1  # 4段: dp[0] = 1通り
# dp[7] = 2  # 7段: dp[3] + dp[4] = 1 + 1 = 2通り
# ...
# dp[11] = 3 # 最終答え
# ```

# このPython実装は、制約条件（n≤40）に対して十分高速で、メモリ効率も良好です。型安全性も確保されており、保守性の高いコードとなっています。

# このエラーはPython 3.8.10での型アノテーションの問題です。Python 3.9未満では `tuple[int, int, int]` の記法が使用できません。## 🐛 エラーの原因と解決策

# ### **エラーの詳細**
# ```bash
# TypeError: 'type' object is not subscriptable
# ```

# **原因:**
# - Python 3.8では `tuple[int, int, int]` の記法が **サポートされていない**
# - この記法はPython 3.9で導入された新しい型アノテーション機能
# - Python 3.8では `typing.Tuple` を使用する必要がある

# ### **修正内容**
# ```python
# # ❌ Python 3.8では使用不可
# def parse_input() -> tuple[int, int, int]:

# # ✅ Python 3.8で正しい記法  
# def parse_input() -> Tuple[int, int, int]:
# ```

# ### **Python バージョン別対応表**

# | Python版 | 型アノテーション | 例 |
# |----------|----------------|-----|
# | **3.8以前** | `typing.Tuple` | `Tuple[int, str]` |
# | **3.9以降** | 組み込み `tuple` | `tuple[int, str]` |
# | **3.10以降** | Union記法も変更 | `int \| str` |

# ### **他の潜在的な互換性問題**

# もし他にもエラーが発生する場合は、以下もチェックしてください：

# ```python
# # Python 3.8で確実に動作する記法
# from typing import List, Tuple, Optional

# # ❌ Python 3.9以降の記法
# def func() -> list[int]: pass
# def func() -> dict[str, int]: pass

# # ✅ Python 3.8互換の記法  
# def func() -> List[int]: pass
# def func() -> Dict[str, int]: pass
# ```

# 修正されたコードは**Python 3.8.10で正常に動作**するはずです！

import sys
from typing import List, Tuple


def count_stair_climbing_ways(n: int, a: int, b: int) -> int:
    """
    階段を上る方法の数を動的プログラミングで計算する関数
    
    Parameters:
    -----------
    n : int
        上る階段の段数 (1 <= n <= 40)
    a : int
        1歩で上れる段数1 (1 <= a <= 5, a != b)
    b : int
        1歩で上れる段数2 (1 <= b <= 5, a != b)
    
    Returns:
    --------
    int
        n段の階段を上る方法の数
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # DPテーブルを初期化（メモリ効率を考慮してリスト内包表記使用）
    dp: List[int] = [0] * (n + 1)
    
    # ベースケース：0段目に到達する方法は1通り（何もしない）
    dp[0] = 1
    
    # DPテーブルを埋める処理
    for i in range(1, n + 1):
        # i段目に到達する方法を計算
        # (i-a)段目からa段上る場合
        if i >= a:
            dp[i] += dp[i - a]
        
        # (i-b)段目からb段上る場合    
        if i >= b:
            dp[i] += dp[i - b]
    
    return dp[n]


def parse_input() -> Tuple[int, int, int]:
    """
    標準入力から値を読み取り、パースする関数
    
    Returns:
    --------
    Tuple[int, int, int]
        (n, a, b)のタプル
        n: 階段の段数
        a: 1歩で上れる段数1  
        b: 1歩で上れる段数2
    """
    # 標準入力から1行読み取り、末尾の改行を除去
    line: str = sys.stdin.readline().strip()
    
    # スペースで分割して整数に変換
    values: List[str] = line.split()
    n: int = int(values[0])
    a: int = int(values[1]) 
    b: int = int(values[2])
    
    return n, a, b


def main() -> None:
    """
    メイン処理関数
    標準入力から値を読み取り、階段を上る方法の数を計算して出力する
    
    Parameters:
    -----------
    None
    
    Returns:
    --------
    None
    """
    # 標準入力から値を読み取る
    n, a, b = parse_input()
    
    # 階段を上る方法の数を計算
    result: int = count_stair_climbing_ways(n, a, b)
    
    # 結果を出力（末尾に改行付き）
    print(result)


# メイン処理を実行
if __name__ == "__main__":
    main()