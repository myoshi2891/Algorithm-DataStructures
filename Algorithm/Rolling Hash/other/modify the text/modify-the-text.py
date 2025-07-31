
# 以下は、**Python (CPython 3.11.4)** を用いた効率的な解法です。
# 時間計算量・メモリ効率を最大限意識し、すべての演算を `mod P` 下で **差分更新** によって高速に処理しています。

# ---

# ### ✅ 特徴：

# * 型アノテーション（PEP 484）対応済み
# * `pow()`を使った事前累乗計算（O(N)）
# * 差分のみを扱い `O(1)` クエリ処理
# * 入力は `sys.stdin` 経由で高速読み込み

# ---

# ### ✅ 実装コード（Python）:

# ```python
import sys
from typing import List, Tuple

# 標準入力の高速化
input = sys.stdin.readline

def solve(P: int, X: int, N: int, Q: int, S: str, queries: List[Tuple[int, str]]) -> List[int]:
    """
    文字列の一文字更新によるハッシュ再計算を高速に処理する。
    
    Parameters:
    - P (int): 素数（modの法）
    - X (int): 基数
    - N (int): 文字列長
    - Q (int): クエリ数
    - S (str): 初期文字列
    - queries (List[Tuple[int, str]]): クエリ (位置, 変更後文字)
    
    Returns:
    - List[int]: 各クエリ後のハッシュ値のリスト
    """

    MOD = P
    base = X

    # A=1, B=2, ..., Z=26 へ変換する関数
    def char_to_val(c: str) -> int:
        return ord(c) - ord('A') + 1

    # pow_table[i] = X^(N-i-1) mod P
    pow_table: List[int] = [1] * N
    for i in range(N - 2, -1, -1):
        pow_table[i] = (pow_table[i + 1] * base) % MOD

    # 初期ハッシュの計算
    hash_val = 0
    S_list: List[str] = list(S)
    for i in range(N):
        hash_val = (hash_val + char_to_val(S_list[i]) * pow_table[i]) % MOD

    results: List[int] = []

    for i, c in queries:
        old_val = char_to_val(S_list[i])
        new_val = char_to_val(c)
        diff = (new_val - old_val) % MOD
        hash_val = (hash_val + diff * pow_table[i]) % MOD
        S_list[i] = c
        results.append(hash_val)

    return results

# 実行部分（標準入力読み込み）
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    P, X, N, Q = map(int, input().split())
    S = input().strip()
    # queries = []
    # 明示的な型指定（Pylance対策）
    queries: List[Tuple[int, str]] = []
    for _ in range(Q):
        idx, ch = input().split()
        queries.append((int(idx) - 1, ch))  # 0-indexed に変換

    result = solve(P, X, N, Q, S, queries)
    for val in result:
        print(val)

if __name__ == "__main__":
    main()
# ```

# ---

# ### ✅ 入力例（stdin）:

# ```
# 1000000007 77777 14 7
# HELLOWORLDNANA
# 1 G
# 4 O
# 7 O
# 2 D
# 14 B
# 13 Y
# 7 E
# ```

# ### ✅ 出力:

# ```
# 792612268
# 411858279
# 411858279
# 311466064
# 311466065
# 312321612
# 686941116
# ```

# ---

# ### 📊 計算量とメモリ

# | 処理内容     | 時間計算量            | メモリ消費量                       |
# | -------- | ---------------- | ---------------------------- |
# | 累乗の事前計算  | O(N)             | O(N) ≒ 約1.6MB (int × 200000) |
# | 初期ハッシュ計算 | O(N)             | -                            |
# | 各クエリ処理   | O(1) × Q         | O(Q) ≒ 約1.6MB (int × 200000) |
# | 合計       | O(N + Q) ≤ 4×10⁵ | 総メモリ ≒ 数MB程度                 |

# ---

# ### 🔍 備考

# * Python の `pow(a, b, mod)` を使えば都度の累乗計算も可能ですが、全てのクエリに対応するために事前計算方式を採用しています（高速＆安全）。
# * ハッシュ値は負にならないよう `% MOD` を逐次適用。

# ---

# 他の形式（例：ファイル読み込み、差分検証、部分更新テストなど）をご希望の場合も対応できます。お気軽にお知らせください。

# Pylance（VS Codeの静的型チェッカー）からの警告メッセージに対応するために、**型注釈が不明確な部分を明示的に指定**する必要があります。

# ---

# ### 🔧 **問題の本質：**

# * `queries: list[Unknown]` の原因は、以下の行で型が推論できないためです：

# ```python
# queries = []
# ```

# この時点では、空リストに型が指定されていないため、Pylance が `Unknown` 型と推論してしまいます。

# ---

# ### ✅ **修正方法（型を明示）**

# ```python
# from typing import List, Tuple

# queries: List[Tuple[int, str]] = []
# ```

# これにより、**Pylance の型エラー**は解消されます。

# ---

# ### 🔁 修正済み `main()` 関数：

# ```python
# def main():
#     import sys
#     sys.setrecursionlimit(1 << 25)
#     P, X, N, Q = map(int, input().split())
#     S = input().strip()

#     # 明示的な型指定（Pylance対策）
#     queries: List[Tuple[int, str]] = []

#     for _ in range(Q):
#         idx, ch = input().split()
#         queries.append((int(idx) - 1, ch))  # 0-indexed に変換

#     result = solve(P, X, N, Q, S, queries)
#     for val in result:
#         print(val)
# ```

# ---

# ### 📌 補足（appendについて）

# `list.append()` の型も `list[Unknown]` に対して使うと以下のような警告が出ます：

# > `"append" の型は "(object: Unknown, /) -> None" です`

# →これは、リストの要素型が不明（`Unknown`）のため、何を追加しているか判断できないという意味です。

# ---

# ### 💡 補足（Pylanceが賢く型推論するには）

# * 空のリストには必ず型注釈をつける。
# * 関数の引数も、リストやタプルであれば具体的に `List[Tuple[int, str]]` などにする。

# ---

# ### ✅ まとめ

# | 対処              | 方法                                     |
# | --------------- | -------------------------------------- |
# | `list[Unknown]` | 明示的に `List[Tuple[int, str]]` を指定       |
# | `.append()`     | リストに対する型注釈を与えれば解消                      |
# | 関数引数の型          | `queries: List[Tuple[int, str]]` などを使う |

# ---

# 必要であれば `solve` 側の戻り値の型アノテーションなどもさらに強化できます。続けて修正を希望される箇所があれば、お知らせください。
