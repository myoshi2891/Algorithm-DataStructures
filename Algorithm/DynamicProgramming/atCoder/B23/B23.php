<!-- 以下は、**PHP 8.2.8** を用いた「巡回セールスマン問題（TSP）」の解法です。
ビットDP（状態：訪問済み都市集合×現在地）により、**全都市を訪問して出発地に戻る最短距離**を求めます。

---

## ✅ 実装（PHP 8.2.8、型・コメント付き）

<?php

declare(strict_types=1);

/**
 * 距離行列を計算する
 *
 * @param array<int, array{int, int}> $coords 各都市の座標 [(x1, y1), ..., (xN, yN)]
 * @return array<int, array<int, float>> 距離行列 dist[i][j] = 都市iからjへの距離
 */
function computeDistances(array $coords): array {
    $N = count($coords);
    $dist = array_fill(0, $N, array_fill(0, $N, 0.0));
    for ($i = 0; $i < $N; $i++) {
        for ($j = 0; $j < $N; $j++) {
            $dx = $coords[$i][0] - $coords[$j][0];
            $dy = $coords[$i][1] - $coords[$j][1];
            $dist[$i][$j] = hypot($dx, $dy);
        }
    }
    return $dist;
}

/**
 * 巡回セールスマン問題を解く
 *
 * @param int $N 都市の数 (2 <= N <= 15)
 * @param array<int, array{int, int}> $coords 各都市の座標
 * @return float 最短距離（誤差1e-3以内）
 */
function solveTSP(int $N, array $coords): float {
    $dist = computeDistances($coords);
    $INF = INF;

    // dp[s][u] := 訪問済み集合s, 現在地u のときの最短距離
    $dp = array_fill(0, 1 << $N, array_fill(0, $N, $INF));
    $dp[1][0] = 0.0;

    for ($s = 1; $s < (1 << $N); $s++) {
        for ($u = 0; $u < $N; $u++) {
            if (!(($s >> $u) & 1)) continue;
            for ($v = 0; $v < $N; $v++) {
                if (($s >> $v) & 1) continue;
                $ns = $s | (1 << $v);
                $dp[$ns][$v] = min($dp[$ns][$v], $dp[$s][$u] + $dist[$u][$v]);
            }
        }
    }

    $res = $INF;
    for ($u = 1; $u < $N; $u++) {
        $res = min($res, $dp[(1 << $N) - 1][$u] + $dist[$u][0]);
    }

    return $res;
}

/**
 * 標準入力から座標情報を読み取り、solveTSP を呼び出すメイン関数
 */
function main(): void {
    [$N] = sscanf(trim(fgets(STDIN)), "%d");
    $coords = [];

    for ($i = 0; $i < $N; $i++) {
        [$x, $y] = sscanf(trim(fgets(STDIN)), "%d %d");
        $coords[] = [$x, $y];
    }

    $result = solveTSP($N, $coords);

    // 小数点以下12桁で出力（誤差1e-3対策）
    printf("%.12f\n", $result);
}

main();

// ## 🧪 実行方法

// ```bash
// php main.php < input.txt
// ```

// 例: `input.txt`

// ```
// 4
// 0 0
// 0 1
// 1 0
// 1 1
// ```

// 出力:

// ```
// 4.000000000000
// ```

// ---

// ## 📊 計算量と制約への対応

// | 項目       | 内容                             |
// | -------- | ------------------------------ |
// | 時間計算量    | `O(N^2 * 2^N)`（N≦15で約50万）      |
// | 空間使用量    | `N * 2^N * float` ≒ 約4MiB      |
// | 精度       | `hypot` + `printf("%.12f")` 使用 |
// | PHPバージョン | 8.2.8（型指定、INF、hypot利用可）        |

// ---

// ## ✅ 特徴

// * 型コメント・戻り値明示（`array{int, int}` 型タプル風）
// * 安全で高速な `hypot()` による距離計算
// * 浮動小数誤差に強い出力形式（12桁）
// * 計算量・メモリ制限に完全準拠（N ≦ 15）

// ---

// ご希望があれば、**経路復元付き実装** や **部分メモ化付きDFS版** なども提供可能です。お気軽にどうぞ！