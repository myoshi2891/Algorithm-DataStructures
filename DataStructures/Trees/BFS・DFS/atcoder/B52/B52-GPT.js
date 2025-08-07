// 以下は、指定された問題を **Node.js (v18.16.1)** と `fs` モジュールを使って解く JavaScript のコードです。

// 要求されたポイントをすべて満たしています：

// * `fs` を用いた標準入力処理
// * ボールの状態管理を高速に行うために配列を使用
// * 幅優先探索（BFS）を用いた効率的な拡張
// * 実行時間制限（2秒）とメモリ制限（1024MiB）に収まるよう設計

// ---

// ### ✅ 解法概要（BFS）：

// * `X` 番目（1-indexed）からスタートして、隣に白ボールがあればキューに追加しながら青く塗っていく。
// * `O(N)` 時間・空間で処理可能。

// ---

// ```javascript
// 使用環境: Node.js 18.16.1

const fs = require('fs');

/**
 * @function simulateColoring
 * @description 与えられたボール列に対してシミュレーションを行い、最終的な状態を返す
 * @param {number} N - ボールの数（1 ≤ N ≤ 100000）
 * @param {number} X - 青く塗り始める位置（1-indexed）
 * @param {string} A - 初期状態の文字列（"#"=黒, "."=白）
 * @returns {string} - シミュレーション後の状態（"@"=青, "#"=黒, "."=白）
 */
function simulateColoring(N, X, A) {
    const balls = A.split('');
    const queue = [];

    // 0-indexed に変換
    const start = X - 1;
    balls[start] = '@';
    queue.push(start);

    while (queue.length > 0) {
        const pos = queue.shift();

        // 左隣
        const left = pos - 1;
        if (left >= 0 && balls[left] === '.') {
            balls[left] = '@';
            queue.push(left);
        }

        // 右隣
        const right = pos + 1;
        if (right < N && balls[right] === '.') {
            balls[right] = '@';
            queue.push(right);
        }
    }

    return balls.join('');
}

// 標準入力からのデータ取得と処理
(function main() {
    const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');
    const [N, X] = input[0].split(' ').map(Number);
    const A = input[1];

    const result = simulateColoring(N, X, A);
    console.log(result);
})();
// ```

// ---

// ### 💡 時間・メモリ計算

// * **時間計算量**: `O(N)`

//   * 各ボールは最大1回だけキューに入る。
// * **空間計算量**: `O(N)`

//   * `balls` 配列と `queue` は最大で `N` 要素。

// ---

// ### ✅ 注意点

// * 入力の位置 `X` は **1-indexed** で来るが、JavaScript 配列は **0-indexed** なので変換が必要。
// * 黒ボール（`#`）には影響を与えず、白（`.`）のみを青（`@`）に変える。

// ---

// 質問や別言語での解法希望があればお知らせください。
