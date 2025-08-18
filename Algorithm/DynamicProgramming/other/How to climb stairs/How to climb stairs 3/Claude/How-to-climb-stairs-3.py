# Python版の階段上り問題のDP解法を実装しました。主な特徴は以下の通りです：

# ## 🔍 実装の特徴

# ### 1. **型アノテーションの活用**
# - すべての関数に型ヒントを明示
# - `List[int]`, `tuple[int, int, int, int]`などで明確な型指定
# - Python 3.8.10対応の型システム使用

# ### 2. **メモリ効率を考慮した設計**
# - **基本版**: `O(n)`空間計算量でシンプルな実装
# - **最適化版**: `O(max(a,b,c))`空間計算量でメモリ効率向上

# ### 3. **処理時間の最適化**
# - 単純なループで`O(n)`時間計算量を実現
# - 条件分岐を最小限に抑制
# - 不要な計算を回避

# ### 4. **関数分割による保守性**
# ```python
# parse_input()     # 入力処理
# count_ways_to_climb_stairs()  # メインロジック  
# solve()          # 全体制御
# optimized_count_ways()  # メモリ最適化版
# ```

# ## ⚡ 計算量解析

# ### **基本実装**
# - **時間計算量**: `O(n)` - 各段を1回ずつ処理
# - **空間計算量**: `O(n)` - DPテーブルサイズ

# ### **最適化実装**  
# - **時間計算量**: `O(n)` - 同様の処理時間
# - **空間計算量**: `O(max(a,b,c))` - 最大7要素のウィンドウ

# ## 🎯 メモリ効率の改善点

# 制約条件（n ≤ 30, a,b,c ≤ 7）では基本実装で十分ですが、より大きなnに対しては最適化版が有効です：

# ```python
# # 基本版: 31要素の配列 (n=30の場合)
# dp = [0] * (n + 1)

# # 最適化版: 最大8要素の配列 (max(a,b,c)=7の場合)  
# window = [0] * (max_step + 1)
# ```

# ## 📝 使用方法

# 標準入力から `n a b c` を読み取り、結果を標準出力に出力：

# ```
# 入力例: 10 2 3 4
# 出力: 17
# ```

# この実装は制約条件に対して十分高速で、メモリ使用量も最適化されています。型安全性も確保されており、保守性の高いコードとなっています。

# Python 3.8.10では`tuple[int, int, int, int]`の記法がサポートされていないため、エラーが発生しています。Python 3.8では`typing`モジュールの型を使用する必要があります。修正完了しました！主な変更点は以下の通りです：

# ## 🔧 修正内容

# ### **Python 3.8.10対応の型アノテーション**
# ```python
# # 修正前（Python 3.9+の記法）
# from typing import List
# def parse_input() -> tuple[int, int, int, int]:

# # 修正後（Python 3.8対応）
# from typing import List, Tuple  
# def parse_input() -> Tuple[int, int, int, int]:
# ```

# ## 📋 Python バージョン別の型アノテーション対応

# | Python バージョン | タプル型の記法 | 必要なimport |
# |------------------|----------------|--------------|
# | Python 3.8 | `Tuple[int, int, int, int]` | `from typing import Tuple` |
# | Python 3.9+ | `tuple[int, int, int, int]` | 不要（組み込み型） |

# ## ✅ 修正により解決される問題

# 1. **TypeError: 'type' object is not subscriptable** - Python 3.8では組み込みの`tuple`型に角括弧記法`[]`を直接使用できない
# 2. **実行時エラーの回避** - `typing.Tuple`を使用することで正しく型チェックが動作
# 3. **後方互換性** - Python 3.8.10環境でも正常に動作

# この修正により、Python 3.8.10環境でランタイムエラーなく実行できるようになります。他の部分のロジックや計算量は変更していないため、パフォーマンスに影響はありません。

from typing import List, Tuple
import sys

def count_ways_to_climb_stairs(n: int, a: int, b: int, c: int) -> int:
    """
    階段を上る方法の数を動的プログラミングで計算する関数
    
    Args:
        n (int): 階段の段数 (1 <= n <= 30)
        a (int): 1歩で上れる段数1 (1 <= a <= 7)
        b (int): 1歩で上れる段数2 (1 <= b <= 7)
        c (int): 1歩で上れる段数3 (1 <= c <= 7)
    
    Returns:
        int: n段の階段を上る方法の数
    
    Time Complexity: O(n) - 各段を1回ずつ処理
    Space Complexity: O(n) - DPテーブル分のメモリ使用
    """
    # DPテーブルを初期化（0で埋める）
    # dp[i] = i段目に到達する方法の数
    dp: List[int] = [0] * (n + 1)
    
    # 初期条件：0段目（スタート地点）に到達する方法は1通り
    dp[0] = 1
    
    # 各段について計算
    for i in range(1, n + 1):
        # a段前から来る場合
        if i >= a:
            dp[i] += dp[i - a]
        
        # b段前から来る場合
        if i >= b:
            dp[i] += dp[i - b]
        
        # c段前から来る場合
        if i >= c:
            dp[i] += dp[i - c]
    
    return dp[n]

def parse_input() -> Tuple[int, int, int, int]:
    """
    標準入力から値を読み取る関数
    
    Returns:
        Tuple[int, int, int, int]: (n, a, b, c) のタプル
    
    Time Complexity: O(1) - 定数時間
    Space Complexity: O(1) - 定数メモリ
    """
    # 標準入力から1行読み取り、末尾の改行を除去
    line: str = sys.stdin.readline().strip()
    
    # スペースで分割して整数に変換
    values: List[str] = line.split()
    n: int = int(values[0])
    a: int = int(values[1])
    b: int = int(values[2])
    c: int = int(values[3])
    
    return n, a, b, c

def solve() -> None:
    """
    メイン処理を実行する関数
    標準入力から値を読み取り、問題を解いて結果を出力する
    
    Time Complexity: O(n) - count_ways_to_climb_stairs関数の計算量に依存
    Space Complexity: O(n) - DPテーブル分のメモリ使用
    """
    # 標準入力から値を読み取り
    n, a, b, c = parse_input()
    
    # 階段を上る方法の数を計算
    result: int = count_ways_to_climb_stairs(n, a, b, c)
    
    # 結果を標準出力に出力（末尾に改行あり）
    print(result)

def optimized_count_ways(n: int, a: int, b: int, c: int) -> int:
    """
    メモリ最適化版：スライディングウィンドウを使用したDP解法
    （参考実装：より高いnに対してメモリ効率を向上）
    
    Args:
        n (int): 階段の段数
        a (int): 1歩で上れる段数1
        b (int): 1歩で上れる段数2  
        c (int): 1歩で上れる段数3
    
    Returns:
        int: n段の階段を上る方法の数
    
    Time Complexity: O(n)
    Space Complexity: O(max(a, b, c)) - 必要最小限のメモリ使用
    """
    # 最大ステップサイズを取得
    max_step: int = max(a, b, c)
    
    # スライディングウィンドウ用の配列
    # インデックス i % (max_step + 1) に dp[i] の値を格納
    window: List[int] = [0] * (max_step + 1)
    window[0] = 1  # dp[0] = 1
    
    for i in range(1, n + 1):
        current_ways: int = 0
        
        # a段前から来る場合
        if i >= a:
            current_ways += window[(i - a) % (max_step + 1)]
        
        # b段前から来る場合  
        if i >= b:
            current_ways += window[(i - b) % (max_step + 1)]
        
        # c段前から来る場合
        if i >= c:
            current_ways += window[(i - c) % (max_step + 1)]
        
        # 現在の値を更新
        window[i % (max_step + 1)] = current_ways
    
    return window[n % (max_step + 1)]

# メイン処理の実行
if __name__ == "__main__":
    solve()