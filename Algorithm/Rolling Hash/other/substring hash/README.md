承知しました。以下では、**Pythonによる部分文字列ハッシュ計算**について、**各処理を図解で丁寧に解析・説明**していきます。

---

## 🧩 問題の本質

与えられた英大文字列 `S` に対し、複数の部分列 `S[L..R]` に関して、以下のような **数値ハッシュ** を計算する：

$$
H(S[L..R]) = T_L \cdot X^{R-L} + T_{L+1} \cdot X^{R-L-1} + \dots + T_R \cdot X^0 \mod P
$$

* `T_i` は `S[i]` のアルファベット順（A=1, B=2, ..., Z=26）
* `X` は基数（例えば 77777）
* `P` は素数モジュロ

---

## 📌 処理の流れ（図付き）

### 🔹 Step 1: 入力の受け取りと変換

```python
P, X, N, Q = map(int, data[0].split())
S = data[1]
```

#### 例：

```
S = "HELLOWORLD"
```

| 位置   | 1 | 2 | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
| ---- | - | - | -- | -- | -- | -- | -- | -- | -- | -- |
| 文字   | H | E | L  | L  | O  | W  | O  | R  | L  | D  |
| T\_i | 8 | 5 | 12 | 12 | 15 | 23 | 15 | 18 | 12 | 4  |

---

### 🔹 Step 2: 累積べき乗配列 powX\[i] の構築

```python
powX[i] = (powX[i-1] * X) % P
```

* 目的： $X^i \mod P$ をすばやく参照可能にするため

#### 例（X=10, P=1000000007）：

| i    | 0 | 1  | 2   | 3    |
| ---- | - | -- | --- | ---- |
| powX | 1 | 10 | 100 | 1000 |

→ クエリの長さ `(R - L + 1)` の指数参照に使用

---

### 🔹 Step 3: ハッシュ配列 h\[i] の構築（ローリングハッシュ）

```python
h[i] = (h[i - 1] * X + T[i - 1]) % P
```

ここでは、**先頭からi文字までのハッシュ値**を求めます。

#### 計算例（X=10, S="HEL"）

```
T = [8, 5, 12]   # "HEL"
h[0] = 0
h[1] = 0 * 10 + 8 = 8
h[2] = 8 * 10 + 5 = 85
h[3] = 85 * 10 + 12 = 862 → ハッシュ("HEL")
```

#### 図：hの構築

```
S = H  E  L  L  O ...
T = 8  5 12 12 15 ...
h[1] =    8
h[2] =    8*X + 5
h[3] = (8*X + 5)*X + 12
```

---

### 🔹 Step 4: クエリ処理（ハッシュ抽出）

#### クエリ `(L=2, R=4)` → `S[2..4] = "ELL"`

* `h[R] = h[4] = ハッシュ("HELL")`
* `h[L-1] = h[1] = ハッシュ("H")`
* `powX[R - L + 1] = powX[3] = X³`

$$
H(V) = (h[R] - h[L-1] \cdot X^{R-L+1}) \mod P
$$

#### 図：部分ハッシュ抽出

```
完全ハッシュ（h[4]）:       ハッシュ("HELL")
不要な先頭ハッシュ(h[1]):   ハッシュ("H")
                   削除指数: X^3
        ↓
部分列ハッシュ(V):           ハッシュ("ELL")
```

#### なぜ機能するか？

`h[i]` は次の形式：

$$
h[i] = T_1 \cdot X^{i-1} + T_2 \cdot X^{i-2} + \dots + T_i \cdot X^0
$$

つまり、

$$
h[R] = h[L-1] \cdot X^{R-L+1} + ハッシュ(S[L..R])
$$

逆にすれば：

$$
H(S[L..R]) = h[R] - h[L-1] \cdot X^{R-L+1}
$$

---

### 🔹 Step 5: 出力

```python
for res in results:
    print(res)
```

→ 各クエリに対して計算したハッシュを出力します。

---

## 🧠 補足：逆元を使わない理由

一般的な Rolling Hash では `X^(N - R)` で割る必要がありますが、

この実装では「**指数方向を固定（左から右）**」にしているため、**引き算と掛け算**だけで目的の部分列ハッシュが得られ、**逆元計算は不要**になります。

---

## 📊 時間・空間の観点

| 項目     | 分析                        |
| ------ | ------------------------- |
| 前処理    | O(N)（powX, ハッシュの構築）       |
| クエリ処理  | O(1) × Q（定数時間で抽出）         |
| 空間使用量  | O(N)（powX\[], h\[]） 約 2MB |
| ハッシュ衝突 | XとPの選択により衝突は実用上無視可        |

---

## ✅ まとめ図（全体の流れ）

```text
[S] --> [文字 → 数値変換: T[]]
     --> [べき乗配列 powX[]: O(N)]
     --> [累積ハッシュ配列 h[]: O(N)]

queries: [(L1,R1), (L2,R2), ...]
        ↓
  各クエリ:
    H(V) = (h[R] - h[L-1]*X^{R-L+1}) % P

     ↓

  [結果出力]
```
