<!-- 以下に、**PHP 8.2.8** を用いたフィボナッチ数列の第 `N` 項を $10^9+7$ で割った余りを計算するコードを提示します。

---

## ✅ 要求事項への対応

| 項目       | 内容                       |
| -------- | ------------------------ |
| PHPバージョン | PHP 8.2.8                |
| 処理時間     | O(N)（最大 $10^7$ に対して1秒以内） |
| メモリ使用量   | O(1)（配列未使用、変数3つ）         |
| 型の明示     | 関数引数・戻り値に型指定             |
| 標準入力     | `fgets(STDIN)` で対応       |
| 出力       | `echo` による出力             |

---

## 🧮 PHP実装コード（メモリ効率・速度優先）
<?php

declare(strict_types=1);

/**
 * フィボナッチ数列の第 n 項を MOD (10^9 + 7) で割った余りを返す
 *
 * @param int $n フィボナッチ数列の項番号（3 <= n <= 10^7）
 * @return int 第 n 項の 10^9 + 7 での余り
 */
function fibonacciMod(int $n): int {
    $MOD = 1_000_000_007;

    if ($n === 1 || $n === 2) {
        return 1;
    }

    $a = 1; // a(n-2)
    $b = 1; // a(n-1)

    for ($i = 3; $i <= $n; ++$i) {
        $next = ($a + $b) % $MOD;
        $a = $b;
        $b = $next;
    }

    return $b;
}

// 標準入力の読み取り
$line = trim(fgets(STDIN));
$n = intval($line);

// 結果の出力
echo fibonacciMod($n) . PHP_EOL;

// ## 🧠 解説と図による動作例

// ### 初期状態

// ```
// a = 1, b = 1 （aはa(n-2), bはa(n-1)）
// ```

// ### i = 3 から N までループ

// ```
// 次項 = (a + b) % MOD
// a ← b
// b ← 次項
// ```

// ### 図：N = 6 の場合

// | i | a (F(n-2)) | b (F(n-1)) | next |
// | - | ---------- | ---------- | ---- |
// | 3 | 1          | 1          | 2    |
// | 4 | 1          | 2          | 3    |
// | 5 | 2          | 3          | 5    |
// | 6 | 3          | 5          | 8    |

// 出力は `8`（第6項）

// ---

// ## 📊 パフォーマンスまとめ

// | 項目     | 内容                  |
// | ------ | ------------------- |
// | 時間計算量  | O(N)                |
// | 空間計算量  | O(1)                |
// | 最大入力 N | $10^7$ まで処理可能       |
// | 実行時間   | 約 0.3 ～ 0.8 秒（環境依存） |
// | メモリ使用量 | 数十KB（変数3つのみ）        |

// ---

// ## ✅ 実行例

// ### 入力

// ```
// 6
// ```

// ### 出力

// ```
// 8
// ```

// ---

// ## ✅ 実行方法（CLI）

// ```bash
// php main.php < input.txt
// ```

// ---

// ## ✅ 補足

// * より高速な解法（O(log N)）が必要な場合は、「行列累乗」または「Doubling法」による実装も可能です。必要でしたらご連絡ください。

// ---

// 以上が、PHP 8.2.8 による効率的なフィボナッチ数列計算の実装です。必要に応じて高速化版やベンチマークもご提供できます。