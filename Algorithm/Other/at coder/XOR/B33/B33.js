// 入力: 標準入力を受け取り、勝者を標準出力に出力する
// Node.js用: fsモジュールを用いて高速に入力を読み込む

const fs = require('fs');

/**
 * ゲームにおける勝者を判定して出力する
 * @param {number} N - コマの数
 * @param {number} H - マス目の高さ
 * @param {number} W - マス目の幅
 * @param {[number, number][]} positions - 各コマの位置 (A_i, B_i)
 * @returns {void} - 標準出力に "First" または "Second" を出力
 */
function determineWinner(N, H, W, positions) {
    let xorSum = 0;
    for (let i = 0; i < N; i++) {
        const [a, b] = positions[i];
        xorSum ^= (a - 1) ^ (b - 1); // 正しい Grundy 数
    }
    console.log(xorSum === 0 ? 'Second' : 'First');
}

// メイン処理
function main() {
    const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');
    const [N, H, W] = input[0].split(' ').map(Number);
    const positions = input.slice(1).map((line) => line.split(' ').map(Number));
    determineWinner(N, H, W, positions);
}

main();

// この問題は **各コマの位置に対して Grundy 数を求めて XOR を取る** という典型的な「Nim型ゲーム理論」の問題です。

// ---

// ### 🧠 問題の本質

// 各コマは左か上に何マスでも動かせます。これは「(a, b) → (a’, b’)（a’ < a または b’ < b）」のように、**(a, b) から左または上への移動が可能**ということを意味します。

// 各コマの位置 `(a, b)` の Grundy 数は `a ^ b` になります。
// （※なぜなら、それぞれの方向に独立して1以上動かせる Nim 山に等しい）

// * **Grundy 数の総 XOR = 0** → **後手必勝**
// * **Grundy 数の総 XOR ≠ 0** → **先手必勝**

// ---

// ### ✅ 実装方針

// * 各位置の `a ^ b` を XOR で全て合計
// * 最終的な XOR 値を見て勝者を決定

// ---

// ### ✅ JavaScript (Node.js 18.16.1) 解答コード

// ```javascript
// // 入力: 標準入力を受け取り、勝者を標準出力に出力する
// // Node.js用: fsモジュールを用いて高速に入力を読み込む

// const fs = require("fs");

// /**
//  * ゲームにおける勝者を判定して出力する
//  * @param {number} N - コマの数
//  * @param {number} H - マス目の高さ
//  * @param {number} W - マス目の幅
//  * @param {[number, number][]} positions - 各コマの位置 (A_i, B_i)
//  * @returns {void} - 標準出力に "First" または "Second" を出力
//  */
// function determineWinner(N, H, W, positions) {
//   let xorSum = 0;
//   for (let i = 0; i < N; i++) {
//     const [a, b] = positions[i];
//     xorSum ^= (a ^ b); // 各コマの Grundy 数 (a ^ b) を XOR
//   }
//   console.log(xorSum === 0 ? "Second" : "First");
// }

// // メイン処理
// function main() {
//   const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
//   const [N, H, W] = input[0].split(" ").map(Number);
//   const positions = input.slice(1).map(line => line.split(" ").map(Number));
//   determineWinner(N, H, W, positions);
// }

// main();
// ```

// ---

// ### ✅ 時間・メモリ計算

// * **計算量**: `O(N)`（最大10⁵個の位置を1回ずつ処理）
// * **メモリ使用量**: 約 `N * 8` バイト程度（各位置に `2 * 4 byte`）

//   * 最大でも約 `800KB` → メモリ制限1024MBに対して十分余裕あり
// * **実行時間**: `~20ms` 程度（Node.js 18基準）

// ---

// ### ✅ 入力例での動作確認

// #### 入力例1:

// ```
// 1 3 5
// 2 4
// ```

// * Grundy 数: `2 ^ 4 = 6`
// * XOR: `6 ≠ 0` → **First 勝ち**

// #### 入力例2:

// ```
// 2 8 4
// 6 4
// 7 1
// ```

// * Grundy 数: `6^4 = 2`, `7^1 = 6` → `2^6 = 4 ≠ 0` → **First 勝ち**

// → ん？例と異なる…

// #### 🚨 実は、**(a - 1) ^ (b - 1)** が正しい！

// → 左または上に1マス以上移動 = 座標は1ではなく**0-indexed**で評価すべき！

// ---

// ### ✅ 修正コード（正しく0-indexed）

// ```javascript
// function determineWinner(N, H, W, positions) {
//   let xorSum = 0;
//   for (let i = 0; i < N; i++) {
//     const [a, b] = positions[i];
//     xorSum ^= ((a - 1) ^ (b - 1)); // 正しい Grundy 数
//   }
//   console.log(xorSum === 0 ? "Second" : "First");
// }
// ```

// ---

// ### ✅ 最終まとめ

// * 各コマ `(a, b)` の Grundy 数 = `(a - 1) ^ (b - 1)`
// * 全コマに対して XOR を計算
// * XOR = 0 → Second（後手）勝ち、≠ 0 → First（先手）勝ち

// ---

// 必要であれば、手元で動かすテストコードも提供可能です。
