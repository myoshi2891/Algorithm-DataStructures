動的計画法（DP）を使って、ナップザック問題を解きます。以下のコードは、JavaScriptで実装された典型的な0-1ナップザック問題の解法です。

### 解説
1. **入力のパース**  
   - `fs.readFileSync('/dev/stdin', 'utf8')` を使用して標準入力からデータを読み込む。
   - 入力データを行ごとに分割し、最初の行で `N`（アイテム数）と `W`（ナップザックの容量）を取得。
   - 残りの行をアイテムの `(weight, value)` ペアに変換。

2. **DPテーブルの初期化**  
   - `dp[w]` はナップザックの容量が `w` のときに得られる最大価値を保持する。
   - 初期状態ではすべて `0`。

3. **DP更新処理**  
   - 各アイテム `(weight, value)` を順番に処理。
   - `for (let w = W; w >= weight; w--)` のように**大きい容量から更新**することで、1つの配列を使いながら状態遷移を実装。
   - `dp[w] = Math.max(dp[w], dp[w - weight] + value)` により、現在の価値と新しいアイテムを加えた場合の価値を比較し、大きい方を採用。

4. **出力**  
   - `Math.max(...dp)` で `dp` 配列の最大値を出力。

### 計算量
- **O(NW)** の動的計画法に基づく実装。
- `N ≤ 100` かつ `W ≤ 100000` なので、`10^7` 回程度の計算となり、JavaScriptでも十分に実行可能。

この方法で、制約内で最適な解を求められます。

ナップザック問題（0-1 Knapsack Problem）を **動的計画法（DP）** を用いて解く方法を詳しく解説します。  
JavaScriptでの実装も交えながら、理論とコードを説明します。

---

## 🔹 ナップザック問題とは？
### 問題の概要
- `N` 個の品物があり、それぞれ **重さ `w[i]`** と **価値 `v[i]`** を持つ。
- **ナップザック（バッグ）** の容量は `W` であり、**合計の重さが `W` を超えないように品物を選ぶ**。
- 選んだ品物の価値の合計の **最大値を求める**。

### 制約
- 1 ≤ `N` ≤ 100
- 1 ≤ `W` ≤ 100000
- 1 ≤ `w[i]` ≤ `W`
- 1 ≤ `v[i]` ≤ 10⁹

### 例題
#### **入力**
```
4 7
3 13
3 17
5 29
1 10
```
（4個の品物、ナップザックの容量 7）

| 品物 | 重さ (`w[i]`) | 価値 (`v[i]`) |
|------|--------------|--------------|
| 1    | 3           | 13           |
| 2    | 3           | 17           |
| 3    | 5           | 29           |
| 4    | 1           | 10           |

#### **出力**
```
40
```
（品物 **1, 2, 4** を選ぶと 13 + 17 + 10 = 40 ）

---

## 🔹 動的計画法（DP）とは？
### **考え方**
DP（Dynamic Programming）は、**部分問題を解いて、それを組み合わせて全体の解を求める**手法です。  
ナップザック問題では、「ある容量 `w` で得られる最大の価値」を**小さい容量から順に求めていく**ことで解きます。

---

## 🔹 DPの状態設計
### **DPテーブルの定義**
- `dp[w]`: **重さ `w` のときに得られる最大の価値**を格納する配列

### **遷移方程式**
1. 品物 `i` を **選ばない** → `dp[w]` は変化なし
2. 品物 `i` を **選ぶ** → `dp[w] = dp[w - w[i]] + v[i]` に更新

\[
dp[w] = \max(dp[w], dp[w - w[i]] + v[i])
\]

（ただし、品物 `i` の重さ `w[i]` が `w` 以下の場合のみ）

---

## 🔹 JavaScriptの実装
**DPを1次元配列で実装する（O(NW)）**
```javascript
const fs = require('fs');

function knapsack(input) {
    const lines = input.trim().split('\n');
    const [N, W] = lines[0].split(' ').map(Number);
    const items = lines.slice(1).map(line => line.split(' ').map(Number));

    // DPテーブル（0 から W までの最大価値を管理）
    const dp = new Array(W + 1).fill(0);

    // 各アイテムについてDPテーブルを更新
    for (let i = 0; i < N; i++) {
        const [weight, value] = items[i];

        // 大きい容量から更新する（逆順ループ）
        for (let w = W; w >= weight; w--) {
            dp[w] = Math.max(dp[w], dp[w - weight] + value);
        }
    }

    // 最大価値を出力
    console.log(Math.max(...dp));
}

// 標準入力から読み込む
const input = fs.readFileSync('/dev/stdin', 'utf8');
knapsack(input);
```

---

## 🔹 実装のポイント
### **1. 配列 `dp` の使い方**
- `dp[w]` は「重さ `w` のときに得られる最大価値」
- 初期値は `0`（何も選ばないときの価値）

### **2. 逆順ループの理由**
- `for (let w = W; w >= weight; w--)`
- **「前の状態を使って次の状態を更新する」**ため、**後ろから更新**する必要がある。
- 順方向にループすると、同じ品物を**複数回選ぶ可能性**が出てしまう。

### **3. 計算量**
- **時間計算量**: `O(NW)`（100 × 100000 = 約 10⁷ → 許容範囲）
- **空間計算量**: `O(W)`（1次元配列を使用）

---

## 🔹 具体例でのシミュレーション
入力：
```
4 7
3 13
3 17
5 29
1 10
```
### **ステップ 1: 初期 DP テーブル**
```
dp = [0, 0, 0, 0, 0, 0, 0, 0]
```

### **ステップ 2: 品物 1（重さ 3, 価値 13）**
- `w = 7` から `w = 3` まで更新
```
dp = [0, 0, 0, 13, 13, 13, 13, 13]
```

### **ステップ 3: 品物 2（重さ 3, 価値 17）**
- `w = 7` から `w = 3` まで更新
```
dp = [0, 0, 0, 17, 17, 17, 17, 30]
```

### **ステップ 4: 品物 3（重さ 5, 価値 29）**
- `w = 7` から `w = 5` まで更新
```
dp = [0, 0, 0, 17, 17, 29, 29, 30]
```

### **ステップ 5: 品物 4（重さ 1, 価値 10）**
- `w = 7` から `w = 1` まで更新
```
dp = [0, 10, 10, 17, 27, 29, 39, 40]
```

### **最終解答**
```
40
```

---

## 🔹 まとめ
✅ **DP配列 `dp[w]` を用意し、重さ `w` ごとの最大価値を求める。**  
✅ **アイテムごとに、逆順ループで `dp` 配列を更新する。**  
✅ **計算量 `O(NW)` で解けるため、制約内で実行可能。**  
✅ **ナップザック問題の典型的なDP解法として、競技プログラミングでよく出る！**  

この方法をしっかり理解すれば、より高度な **部分和問題** や **応用的なナップザック問題** も解けるようになります！💪