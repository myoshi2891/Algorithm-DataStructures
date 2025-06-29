## **方針**

- 問題文にある通り、A の mod 逆元を求めるには拡張ユークリッドの互除法を用いて x , y についての 1 次方程式 Ax + My = 1 の 解 x を求めれば良いです。
- 拡張ユークリッドの互除法では、解が負の値となる場合があるので、問題文にしたがって x の値を 1 以上 M 未満にすることを忘れないでください。
- 拡張ユークリッドの互除法がわからない方は、この問題集の「拡張ユークリッドの互除法」に取り組んでみてください。
---

## 🧮 問題設定の復習

A と M が互いに素（gcd(A, M) = 1）であるとき、

> $A \times x \equiv 1 \pmod{M}$

となる `x`（**A の mod M における逆元**）を求める。

---

## 📘 例題

```
入力: M = 7, A = 11
求めたい: 11^(-1) mod 7
```

---

## 🔧 アルゴリズム：拡張ユークリッドの互除法

方程式：

$$
11x + 7y = 1
$$

この x が `11 の 7 における逆元` になる！

---

## 🔢 ステップごとの計算の様子

### ステップ 0: 初期化

| 変数   | 意味     | 初期値 |
| ---- | ------ | --- |
| `a`  | A（変動）  | 11  |
| `m`  | M（変動）  | 7   |
| `x1` | 1つ前の x | 1   |
| `x0` | 2つ前の x | 0   |

---

### ステップ 1: ユークリッドの互除法 + 係数追跡

```
a = 11, m = 7
q = ⌊11 / 7⌋ = 1
→ a = 7, m = 11 % 7 = 4
→ x0 = x1 - q * x0 = 1 - 1*0 = 1, x1 = 0
```

📘 状態: a=7, m=4, x0=1, x1=0

---

```
a = 7, m = 4
q = ⌊7 / 4⌋ = 1
→ a = 4, m = 7 % 4 = 3
→ x0 = x1 - q * x0 = 0 - 1*1 = -1, x1 = 1
```

📘 状態: a=4, m=3, x0=-1, x1=1

---

```
a = 4, m = 3
q = ⌊4 / 3⌋ = 1
→ a = 3, m = 4 % 3 = 1
→ x0 = x1 - q * x0 = 1 - 1*(-1) = 2, x1 = -1
```

📘 状態: a=3, m=1, x0=2, x1=-1

---

```
a = 3, m = 1
q = ⌊3 / 1⌋ = 3
→ a = 1, m = 0（終了）
→ x0 = x1 - q * x0 = -1 - 3*2 = -7, x1 = 2
```

📘 終了: 逆元 = x1 = 2

---

## 🎯 最終的に得られる答え

```
11 × 2 ≡ 22 ≡ 1 mod 7 → ✅
```

よって、答えは `2`

---

## 📈 図での流れイメージ

```
  A = 11, M = 7

  ┌──────────────┐
  │   11 * x + 7 * y = 1   │
  └──────────────┘
         ↓
  ユークリッドの互除法で gcd(11, 7)
         ↓
  11 = 1×7 + 4
   7 = 1×4 + 3
   4 = 1×3 + 1
   3 = 3×1 + 0 ←終了
         ↓
  逆に戻って、
  1 = 4 - 1×3
    = 4 - 1×(7 - 1×4)
    = 2×4 - 1×7
    = 2×(11 - 1×7) - 1×7
    = 2×11 - 3×7

⇒ x = 2（mod 逆元！）
```

---

## ✅ JavaScript コードのおさらい

```js
function modInverse(a, m) {
  let m0 = m;
  let x0 = 0, x1 = 1;

  while (a > 1) {
    const q = Math.floor(a / m);
    [a, m] = [m, a % m];
    [x0, x1] = [x1 - q * x0, x0];
  }

  return x1 < 0 ? x1 + m0 : x1;
}
```

---

## ✍ 補足（負になるケース）

mod 逆元 x が負になった場合でも、`x + M` で正の範囲に戻せば問題ありません。

---
