// 以下は、LeetCodeの仕様に従って `val` を取り除き、配列 `nums` をインプレース（in-place）で変更し、変更後の長さ `k` を返すJavaScript関数です。クラスを使用せず、関数として実装しています。

// ```javascript
/**
 * 配列 nums から val のすべての出現をインプレースで削除し、
 * val 以外の要素数 k を返します。
 *
 * @param {number[]} nums - 入力配列（参照渡しで変更される）
 * @param {number} val - 削除する値
 * @returns {number} - val 以外の要素の個数（k）
 *
 * 時間計算量: O(n)  — 配列を一度走査する
 * 空間計算量: O(1)  — 追加メモリは使用しない
 */
function removeElementJs(nums, val) {
  let k = 0; // val 以外の値を書き込む位置

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[k] = nums[i]; // val でない場合、前方に詰める
      k++;
    }
  }

  // nums の k 以降の値は問題により重要ではない（そのままでOK）
  return k;
}
// ```

// ---

// ### ✅ 使用例（LeetCode Judge テストケースに相当）

// ```javascript
// const nums = [0,1,2,2,3,0,4,2];
// const val = 2;

// const k = removeElement(nums, val);
// console.log("k:", k); // 出力: 5
// console.log("modified nums (first k elements):", nums.slice(0, k)); 
// 出力例: [0,1,3,0,4] のような順不同の val ≠ 2 の要素たち
// ```

// ---

// ### ✅ 解説と図解

// #### 入力:

// ```
// nums = [0,1,2,2,3,0,4,2]
// val = 2
// ```

// #### ループ処理:

// | i | nums\[i] | nums (途中経過)      | k |
// | - | -------- | ---------------- | - |
// | 0 | 0        | \[0,...]         | 1 |
// | 1 | 1        | \[0,1,...]       | 2 |
// | 2 | 2        | (スキップ)           | 2 |
// | 3 | 2        | (スキップ)           | 2 |
// | 4 | 3        | \[0,1,3,...]     | 3 |
// | 5 | 0        | \[0,1,3,0,...]   | 4 |
// | 6 | 4        | \[0,1,3,0,4,...] | 5 |
// | 7 | 2        | (スキップ)           | 5 |

// ---

// ### ✅ 処理性能（最大100要素において）

// * **時間計算量:** O(n) （最大で100回ループ）
// * **空間計算量:** O(1) （インプレースで処理、追加メモリなし）
// * **メモリ使用:** 元の配列以外に追加配列を使わず、省メモリ

// ---

// 必要であれば、以下のように要素の先頭 `k` 件をソートして `expectedNums` と比較できます：

// ```javascript
// nums.sort((a, b) => a - b); // 全体ソート
// console.log(nums.slice(0, k)); // => expectedNums と比較対象に
// ```

// 他に図やパフォーマンス検証が必要でしたら、お知らせください。
