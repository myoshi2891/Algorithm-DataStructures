<!-- 以下は、**PHP 8.2.8** を使用した `N 以下の素数を列挙する` 問題の解法です。
エラトステネスの篩アルゴリズムを使い、**高速化のために標準出力をまとめて出力**する形式とし、**関数化＋型指定**＋**処理時間・メモリ使用量の計測**を含めています。

---

## ✅ PHPコード（`Main.php`）

<?php
declare(strict_types=1);

/**
 * エラトステネスの篩で N 以下の素数を列挙する関数
 *
 * @param int $n 素数の上限（2 <= $n <= 10^6）
 * @return array<int> 昇順の素数リスト
 */
function sieve_of_eratosthenes(int $n): array {
    if ($n < 2) return [];

    $isPrime = array_fill(0, $n + 1, true);
    $isPrime[0] = $isPrime[1] = false;

    for ($i = 2; $i * $i <= $n; $i++) {
        if ($isPrime[$i]) {
            for ($j = $i * $i; $j <= $n; $j += $i) {
                $isPrime[$j] = false;
            }
        }
    }

    $primes = [];
    for ($i = 2; $i <= $n; $i++) {
        if ($isPrime[$i]) {
            $primes[] = $i;
        }
    }

    return $primes;
}

// 入力の読み込み
fscanf(STDIN, "%d", $N);

// 計測開始
$start = hrtime(true);

// 素数の列挙
$primes = sieve_of_eratosthenes($N);

// 出力を高速化（implodeでまとめて表示）
echo implode("\n", $primes) . "\n";

// 計測終了と時間・メモリ表示（stderrへ）
$end = hrtime(true);
$time = ($end - $start) / 1e6; // ミリ秒

fwrite(STDERR, sprintf("Execution Time: %.3f ms\n", $time));
fwrite(STDERR, sprintf("Memory Usage: %.2f MB\n", memory_get_peak_usage(true) / 1024 / 1024));

// ## ✅ 実行方法

// ```bash
// php Main.php < input.txt
// ```

// ---

// ## 🧪 入力例

// ```txt
// 20
// ```

// ### ✅ 出力

// ```txt
// 2
// 3
// 5
// 7
// 11
// 13
// 17
// 19
// ```

// ### ✅ stderr（参考）

// ```
// Execution Time: 1.230 ms
// Memory Usage: 1.00 MB
// ```

// ---

// ## 🧠 解説ポイント

// | 項目     | 内容                                       |
// | ------ | ---------------------------------------- |
// | アルゴリズム | エラトステネスの篩：O(N log log N)                 |
// | メモリ使用量 | `O(N)`（`$isPrime` 配列）                    |
// | 高速化策   | 出力を `implode("\n", $primes)` で一括出力       |
// | 時間計測   | `hrtime(true)` で高精度に処理時間をミリ秒単位で計測        |
// | メモリ計測  | `memory_get_peak_usage(true)` を使用（バイト単位） |

// ---

// ## 💬 補足

// * `declare(strict_types=1)` により、型の厳格さを保っています。
// * 出力は `echo` でまとめて表示 → `print` より高速。
// * メモリ削減の余地は小さいですが、必要なら `bitset` 的表現も可能です。

