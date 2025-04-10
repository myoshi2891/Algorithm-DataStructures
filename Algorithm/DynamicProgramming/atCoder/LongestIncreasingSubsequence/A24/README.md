最長増加部分列（LIS: Longest Increasing Subsequence）を求めるアルゴリズム（O(N log N)) の流れを、**図付き**でわかりやすく解説します。

---

## 💡 アルゴリズムの概要

- `dp[i]` は「長さが `i+1` の増加部分列の**末尾の最小値**」を保持します。
- 各要素 `A[i]` を見ながら、
  - `dp` の中で `A[i]` より**初めて大きい or 等しい値**を**二分探索**で探し、
  - その位置を `A[i]` で**置き換え**ます。
- 最終的な `dp` の長さが答えになります。

---

## 📘 例で解説（A = [2, 3, 1, 6, 4, 5]）

初期状態：`dp = []`（空）

### 1️⃣ A[0] = 2
- dp は空 → `2` を追加
```
dp = [2]
```

### 2️⃣ A[1] = 3
- `3` は `dp` の最後の要素より大きい → 末尾に追加
```
dp = [2, 3]
```

### 3️⃣ A[2] = 1
- `1` は `dp[0] (=2)` より小さい → 先頭を置き換える
```
dp = [1, 3]
```

### 4️⃣ A[3] = 6
- `6` は `dp` の最後より大きい → 末尾に追加
```
dp = [1, 3, 6]
```

### 5️⃣ A[4] = 4
- `4` は `dp[2] (=6)` より小さいが、`dp[1] (=3)` より大きい
- → `dp[2] (=6)` を `4` に置き換える
```
dp = [1, 3, 4]
```

### 6️⃣ A[5] = 5
- `5` は `dp[2] (=4)` より大きい → 末尾に追加
```
dp = [1, 3, 4, 5]
```

---

## ✅ 結果

- `dp.length = 4`
- よって、**最長増加部分列の長さは 4**

---

## 🖼️ イメージ図

```
A = [2, 3, 1, 6, 4, 5]
      ↓   ↓   ↓   ↓   ↓
dp = [1, 3, 4, 5] ← 各ステップで更新
        ↑
   長さ4のLIS
```

---

## 🔍 注意点

- `dp` 配列そのものは「実際の LIS を構成する部分列」とは限らない（あくまで長さを求めるための補助）。
- 実際の増加部分列を求めたい場合は、トラッキングが必要（別途インデックス配列を持つ）。
---

## ✅ アルゴリズムの**処理自体は正しい**ですが、  
## ❗️ `dp = [1, 3, 4, 5]` は **実際の LIS と一致するとは限りません**。

---

### 🔁 おさらい

入力：
```
A = [2, 3, 1, 6, 4, 5]
```

この配列に対して最長増加部分列（LIS）の**長さ**は `4` で、  
実際の LIS としては `**[2, 3, 4, 5]**` がありえます。

でも、アルゴリズムで途中生成される `dp = [1, 3, 4, 5]` なので混乱しがちです。

---

### 🤔 なぜ `dp` は `[2, 3, 4, 5]` ではないのか？

この `dp` は **最長増加部分列を構成する「候補の末尾の最小値」**を管理していて、  
「**最長増加部分列そのものではない**」からです。

---

### 🔍 例：A = [2, 3, 1, 6, 4, 5]

| i | A[i] | dpの更新 | dp |
|--:|------|-----------|-----|
| 0 | 2    | 追加       | [2] |
| 1 | 3    | 追加       | [2, 3] |
| 2 | 1    | dp[0]更新 | [1, 3] |
| 3 | 6    | 追加       | [1, 3, 6] |
| 4 | 4    | dp[2]更新 | [1, 3, 4] |
| 5 | 5    | 追加       | [1, 3, 4, 5] |

→ この最終 `dp` は「長さ4の増加列が存在する」という情報を持っているだけで、  
実際の列 `[2, 3, 4, 5]` の構成順序ではありません。

---

## ✅ 結論

- `dp` は **実際の LIS ではなく、その長さを得るための道具**。
- `[2, 3, 4, 5]` のように、**正しい LIS は他のルートで得られます**。
- もし **実際の LIS を出力したい**場合は、別の配列でパスを記録するようにします。

---

図解付きで「**実際のLIS（列）を復元する処理**」を分かりやすく解説します！  
流れを追いつつ、`dp`, `dpIndex`, `prevIndex` の3つの配列がどう変化していくかを**ステップごとに図解**していきます。

---

## 🎯 問題の例

```txt
A = [2, 3, 1, 6, 4, 5]
```

---

## 🧩 用語整理

| 配列        | 意味 |
|-------------|------|
| `dp`        | 各長さのLISの末尾の最小値 |
| `dpIndex`   | `dp[i]` が A の何番目だったか |
| `prevIndex` | A[i] の直前のLIS要素のインデックス（たどると元の列がわかる） |

---

## 🔁 各ステップを図で追う！

---

### 🟢 Step 0：i = 0, A[i] = 2

- `dp` は空 → 追加
- `dp = [2]`
- `dpIndex = [0]`
- `prevIndex[0] = -1`

```
dp:        [2]
dpIndex:   [0]
prevIndex: [-1, _, _, _, _, _]
```

---

### 🟢 Step 1：i = 1, A[i] = 3

- 3 > dp[0] → 追加
- `dp = [2, 3]`
- `dpIndex = [0, 1]`
- `prevIndex[1] = dpIndex[0] = 0`

```
dp:        [2, 3]
dpIndex:   [0, 1]
prevIndex: [-1, 0, _, _, _, _]
```

---

### 🟢 Step 2：i = 2, A[i] = 1

- 1 < dp[0] → dp[0] を更新
- `dp = [1, 3]`
- `dpIndex = [2, 1]`
- `prevIndex[2] = -1`（先頭なので）

```
dp:        [1, 3]
dpIndex:   [2, 1]
prevIndex: [-1, 0, -1, _, _, _]
```

---

### 🟢 Step 3：i = 3, A[i] = 6

- 6 > dp[1] → 追加
- `dp = [1, 3, 6]`
- `dpIndex = [2, 1, 3]`
- `prevIndex[3] = dpIndex[1] = 1`

```
dp:        [1, 3, 6]
dpIndex:   [2, 1, 3]
prevIndex: [-1, 0, -1, 1, _, _]
```

---

### 🟢 Step 4：i = 4, A[i] = 4

- 4 < dp[2] (=6) → dp[2] を更新
- `dp = [1, 3, 4]`
- `dpIndex = [2, 1, 4]`
- `prevIndex[4] = dpIndex[1] = 1`

```
dp:        [1, 3, 4]
dpIndex:   [2, 1, 4]
prevIndex: [-1, 0, -1, 1, 1, _]
```

---

### 🟢 Step 5：i = 5, A[i] = 5

- 5 > dp[2] (=4) → 追加
- `dp = [1, 3, 4, 5]`
- `dpIndex = [2, 1, 4, 5]`
- `prevIndex[5] = dpIndex[2] = 4`

```
dp:        [1, 3, 4, 5]
dpIndex:   [2, 1, 4, 5]
prevIndex: [-1, 0, -1, 1, 1, 4]
```

---

## 🧱 LIS の復元（逆順にたどる）

最後の LIS の末尾は `dpIndex[3] = 5` → A[5] = 5  
そこから `prevIndex` をたどっていく：

```
index = 5 → 4 → 1 → 0
A[index] = 5 → 4 → 3 → 2
```

→ 逆順なので **LIS = [2, 3, 4, 5]**

---

## ✅ 出力結果

```txt
4
2 3 4 5
```

---

## 💬 補足

- `dp` は LIS の長さを求めるための道具
- `dpIndex` + `prevIndex` を使えば、**実際の列も完全復元できる！**

---
