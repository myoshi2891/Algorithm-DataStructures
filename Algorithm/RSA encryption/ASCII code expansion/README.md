
---

## 🔐 問題の背景と目的

RSA暗号では以下の数式に基づいて **秘密の数字 M** を安全にやりとりできます。

* 暗号化：`E ≡ M^e mod n`
* 復号化：`M ≡ E^d mod n`

さらに今回は、`M`（28ビット）を **7ビットごとに区切ってASCII文字に復元**します。

---

## 🧩 入力例

```
n = 3995747143  
e = 3007  
E = 602607029
```

---

## 🪜 処理ステップ図解（全体）

```mermaid
flowchart TD
    A[入力: n, e, E] --> B[素因数分解 n = p × q]
    B --> C[φ(n) = (p-1)(q-1)]
    C --> D[d = e⁻¹ mod φ(n)]
    D --> E[M = E^d mod n]
    E --> F[28ビット → 7ビット×4 に分割]
    F --> G[ASCIIコード → 文字列]
```

---

## 🔹 ステップ①：n の素因数分解（p, q）

```
n = 3995747143 = p × q
```

調べると、

```
p = 59359  
q = 67309
```

#### 図：

```
+-----------------------------+
|         素因数分解         |
+-----------------------------+
|          n = pq             |
|   p = 59359 , q = 67309     |
+-----------------------------+
```

---

## 🔹 ステップ②：φ(n) の計算

```
φ(n) = (p - 1) × (q - 1)
     = 59358 × 67308 = 3995620776
```

#### 図：

```
+--------------------------------+
|      オイラー関数 φ(n)         |
+--------------------------------+
| φ(n) = (p - 1)(q - 1)          |
|      = 59358 × 67308           |
|      = 3995620776              |
+--------------------------------+
```

---

## 🔹 ステップ③：秘密鍵 d の計算

秘密鍵 `d` は以下を満たす逆元：

```
d ≡ e⁻¹ mod φ(n)
```

`e = 3007`、`φ(n) = 3995620776` に対して、

```
d = 1899220895
```

これは拡張ユークリッド互除法で求めます。

#### 図：

```
+---------------------------------------------------+
|              秘密鍵 d の計算（逆元）              |
+---------------------------------------------------+
|     e × d ≡ 1 mod φ(n)                            |
| → 3007 × d ≡ 1 mod 3995620776                     |
| → d = 1899220895                                  |
+---------------------------------------------------+
```

---

## 🔹 ステップ④：復号 `M = E^d mod n`

与えられた `E = 602607029` を復号します：

```
M = E^d mod n
  = 602607029^1899220895 mod 3995747143
  = 1347701416
```

（繰り返し二乗法を使って効率的に計算）

#### 図：

```
+-----------------------------------------+
|       復号処理：M = E^d mod n           |
+-----------------------------------------+
|   E = 602607029                          |
|   d = 1899220895                         |
|   n = 3995747143                         |
| → M = 1347701416                         |
+-----------------------------------------+
```

---

## 🔹 ステップ⑤：28ビット → 7ビット × 4 分割

28ビット表現の `M = 1347701416` は 2進数で：

```
M = 01010000 01000001 01001001 01011010
        P        A       I       Z
```

上位から7ビットずつ分割：

| S\[0] | S\[1] | S\[2] | S\[3] |
| ----- | ----- | ----- | ----- |
| 80    | 65    | 73    | 90    |
| 'P'   | 'A'   | 'I'   | 'Z'   |

#### 図：

```
+-----------------------------------------------------+
|   28ビット分解： 1347701416                         |
+-----------------------------------------------------+
| 2進数：01010000 01000001 01001001 01011010          |
|         ^        ^        ^        ^                |
|       S[0]     S[1]     S[2]     S[3]               |
|       80        65       73        90               |
|       'P'       'A'      'I'       'Z'              |
+-----------------------------------------------------+
```

---

## ✅ 最終出力

```txt
PAIZ
```

---

## 🧠 処理全体まとめ（再掲）

```mermaid
graph LR
  A1[n, e, E 入力] --> A2[素因数分解 → p, q]
  A2 --> A3[φ(n) 計算]
  A3 --> A4[秘密鍵 d 計算（mod逆元）]
  A4 --> A5[復号 M = E^d mod n]
  A5 --> A6[28ビットを 7ビット × 4 分割]
  A6 --> A7[ASCIIコード → 文字列]
  A7 --> A8[出力：PAIZ]
```

---
