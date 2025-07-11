<!-- 以下は、**PHP 8.2.8** での「カエルの最小コスト移動経路」問題の解法です。

* **型アノテーション対応**（PHP 8.2 準拠）
* **処理時間 O(N)**、**メモリ使用量 O(N)** に抑えた動的計画法（DP）
* **標準入力（STDIN）対応**
* 実行制限：**時間 1秒以内、メモリ 1024MiB以下**

---

## ✅ PHP 実装（`Main.php`）

```php -->
<?php

declare(strict_types=1);

function main(): void {
    $input = trim(stream_get_contents(STDIN));
    $lines = explode("\n", $input);
    
    $N = intval($lines[0]);
    $h = array_map('intval', preg_split('/\s+/', $lines[1]));

    /** @var int[] $dp 最小コスト配列 */
    $dp = array_fill(0, $N, INF);
    /** @var int[] $prev 経路復元用配列 */
    $prev = array_fill(0, $N, -1);

    $dp[0] = 0;

    for ($i = 1; $i < $N; $i++) {
        $cost1 = $dp[$i - 1] + abs($h[$i] - $h[$i - 1]);
        if ($cost1 < $dp[$i]) {
            $dp[$i] = $cost1;
            $prev[$i] = $i - 1;
        }

        if ($i > 1) {
            $cost2 = $dp[$i - 2] + abs($h[$i] - $h[$i - 2]);
            if ($cost2 < $dp[$i]) {
                $dp[$i] = $cost2;
                $prev[$i] = $i - 2;
            }
        }
    }

    /** @var int[] $path 経路復元 */
    $path = [];
    $current = $N - 1;
    while ($current !== -1) {
        $path[] = $current + 1; // 1-indexed
        $current = $prev[$current];
    }

    $path = array_reverse($path);

    echo count($path) . "\n";
    echo implode(' ', $path) . "\n";
}

main();
// ```

// ---

// ## ⏱️ 計算量・メモリ使用量

// | 項目     | 内容                    |
// | ------ | --------------------- |
// | 時間計算量  | O(N)                  |
// | 空間計算量  | O(N)                  |
// | メモリ使用量 | 約 1MB（N ≦ 100000 の場合） |

// ---

// ## 📥 入力例

// ```
// 6
// 30 10 60 10 60 50
// ```

// ---

// ## 📤 出力例

// ```
// 4
// 1 3 5 6
// ```

// ---

// ## ✅ 実行方法

// ```bash
// php Main.php < input.txt
// ```

// ---

// ## 💡 補足

// * `dp[i]` は i 番目の足場にたどり着くまでの最小コスト
// * `prev[i]` はどの足場から来たか（経路復元用）
// * 経路は逆順にたどってから `array_reverse()` で正順に戻す

// ---