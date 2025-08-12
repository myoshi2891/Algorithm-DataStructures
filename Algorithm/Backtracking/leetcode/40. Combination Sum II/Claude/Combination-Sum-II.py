# このPythonソリューションの特徴とLeetCode用の最適化ポイント：

# ## 🔧 型安全性とPylance対応
# - `from typing import List` でリスト型を明示的にインポート
# - 全ての変数・パラメータ・戻り値に型ヒントを追加
# - `result: List[List[int]]` で結果リストの型を明確に定義
# - Pylanceの型チェックを完全にクリア

# ## ⚡ パフォーマンス最適化
# 1. **メモリ効率**：
#    - `current_combination.copy()` でリストの浅いコピーを作成（深いコピーより高速）
#    - バックトラッキングで `pop()` 操作により状態を効率的に復元

# 2. **時間効率**：
#    - `candidates.sort()` による事前ソートで剪定効果を最大化
#    - 早期終了条件 `current_sum > target` で不要な探索を回避
#    - インデックス範囲を `range(start_index, len(candidates))` で最小化

# ## 🎯 重複排除の最適化
# ```python
# if i > start_index and candidates[i] == candidates[i - 1]:
#     continue
# ```
# - O(1)時間での重複検出
# - ハッシュセットを使わずメモリ効率を維持
# - 同一レベルでの重複要素スキップを保証

# ## 📊 計算量
# - **時間計算量**: O(2^n) - 最悪ケースで各要素の選択/非選択
# - **空間計算量**: O(target) - 再帰スタックの深さ
# - **実用的な効率**: ソートと剪定により実際の実行時間は大幅に短縮

# このソリューションはLeetCodeのPython環境で最適なパフォーマンスを発揮し、Pylanceの型チェックも完全に通過する設計になっています。

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        重複要素を含む配列から、各要素を最大1回使用して目標値に達する全ての組み合わせを見つける
        
        Args:
            candidates: 候補数値のリスト（重複要素を含む可能性がある）
            target: 目標となる合計値
            
        Returns:
            目標値に達する全ての一意な組み合わせのリスト
        """
        result: List[List[int]] = []
        
        # ソートして重複要素を隣接させ、効率的な剪定を可能にする
        candidates.sort()
        
        def backtrack(start_index: int, current_sum: int, current_combination: List[int]) -> None:
            """
            バックトラッキングによる組み合わせ探索
            
            Args:
                start_index: 探索開始インデックス
                current_sum: 現在の合計値
                current_combination: 現在の組み合わせ
            """
            # 目標値に達した場合、結果に追加（リストのコピーを作成）
            if current_sum == target:
                result.append(current_combination.copy())
                return
            
            # 目標値を超えた場合は探索を打ち切り（ソート済みなので以降も超える）
            if current_sum > target:
                return
            
            for i in range(start_index, len(candidates)):
                # 同じレベルで重複要素をスキップ（重複組み合わせを防ぐ）
                # start_indexより大きいインデックスで同じ値の場合はスキップ
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # 現在の数値を組み合わせに追加
                current_combination.append(candidates[i])
                
                # 再帰的に探索（次のインデックスから開始、各要素は1回のみ使用）
                backtrack(i + 1, current_sum + candidates[i], current_combination)
                
                # バックトラック：現在の数値を組み合わせから削除
                current_combination.pop()
        
        backtrack(0, 0, [])
        return result