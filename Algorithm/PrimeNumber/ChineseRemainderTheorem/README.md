## **方針**

- 0 以上 m1 × m2 未満の全ての数について m1 , m2 で割った余りが b1 , b2 かどうかを調べると、制約より計算回数が最悪ケースで 10,000,000,000 回となってしまい実行時間制限に間に合いません。
- 0 以上 m1 × m2 未満の整数のうち、 m1 で割った余りが b1 になるような整数 Z は `Z = m1 * i + b1 (0 ≦ i < m2)`という形で表すことができ、その個数は m2 個です。この m2 個の各整数について m2 で割った余りが b2 になるかどうかを調べることでこの問題を最大 100,000　回程度の計算で解くことができます。

---

## 📌 ステップ1: 拡張ユークリッド互除法（`extendedGCD`）

### 目的

2つの整数 `a`, `b` に対して、次の関係を満たす整数 `x`, `y` を求める：

```
a * x + b * y = gcd(a, b)
```

これは「aのmod bにおける逆元（modInverse）」を求めるために使います。

### 例: `extendedGCD(5, 3)`

```
extendedGCD(5, 3)
 ↓
extendedGCD(3, 2)
 ↓
extendedGCD(2, 1)
 ↓
extendedGCD(1, 0) → [1, 0, 1]  ← gcd = 1
```

戻りながら、x, y を再帰的に復元：

```
[1, 0, 1] → [0, 1, 1]
→ [1, -1, 1]
→ [-1, 2, 1]
```

### 🧠 イメージ図

```
a = 5, b = 3
  ┌────────────┐
  ↓ recursion  ↓
gcd(5, 3) = gcd(3, 2)
          = gcd(2, 1)
          = gcd(1, 0) = 1

戻るときに：
1 = 2 - 1*1 → x = -1, y = 2
```

---

## 📌 ステップ2: 逆元を求める（`modInverse`）

### 目的

ある数 `a` に対して、`a * x ≡ 1 (mod m)` を満たす `x` を探す。

### 使い方

```ts
const inv = modInverse(5, 6); // = 5 (5*5 = 25 ≡ 1 mod 6)
```

### イメージ図

```
modInverse(a, m)
  ↳ extendedGCD(a, m) = [x, y, gcd]

  → x が逆元になる！（mod m）

例: modInverse(5, 6)
→ extendedGCD(5, 6) = [-1, 1, 1]
→ x = -1 → -1 mod 6 = 5（負の数もmod補正）
```

---

## 📌 ステップ3: 中国剰余定理の合成（`chineseRemainder`）

### 目的

次の連立合同式を解く：

```
Z ≡ b1 (mod m1)
Z ≡ b2 (mod m2)
```

### 手順

1. 全体の積 `M = m1 * m2`
2. `m1` の `mod m2` における逆元 `m1_inv` を求める
3. `m2` の `mod m1` における逆元 `m2_inv` を求める
4. 合成式：

```
Z = (b1 * m2 * m2_inv + b2 * m1 * m1_inv) mod M
```

### 🎯 例：`m1=5, m2=6, b1=2, b2=3`

```
M = 5 * 6 = 30
m1_inv = modInverse(5, 6) = 5
m2_inv = modInverse(6, 5) = 1

term1 = 2 * 6 * 1 = 12
term2 = 3 * 5 * 5 = 75

Z = (12 + 75) % 30 = 87 % 30 = 27
```

---

## 🎨 全体イメージ図

```
┌──────────────┐
│ Inputs       │
│ m1, m2, b1, b2│
└────┬─────────┘
     ↓
┌──────────────────────────┐
│ Step 1: Inverses         │
│ m1_inv = modInverse(m1,m2)│
│ m2_inv = modInverse(m2,m1)│
└────┬─────────────────────┘
     ↓
┌──────────────────────────────────────┐
│ Step 2: Compute Z                    │
│ Z = (b1*m2*m2_inv + b2*m1*m1_inv) % M│
│ M = m1 * m2                          │
└────┬─────────────────────────────────┘
     ↓
┌──────────────┐
│ Output Z     │
└──────────────┘
```

---

## ✅ TypeScript化コード（型付き）

```ts
function extendedGCD(a: number, b: number): [number, number, number] {
    if (b === 0) return [1, 0, a];
    const [x1, y1, gcd] = extendedGCD(b, a % b);
    const x = y1;
    const y = x1 - Math.floor(a / b) * y1;
    return [x, y, gcd];
}

function modInverse(a: number, m: number): number {
    const [x, , gcd] = extendedGCD(a, m);
    if (gcd !== 1) throw new Error("mod inverse does not exist");
    return (x % m + m) % m;
}

function chineseRemainder(m1: number, m2: number, b1: number, b2: number): number {
    const M = m1 * m2;
    const m1_inv = modInverse(m1, m2);
    const m2_inv = modInverse(m2, m1);
    const term1 = b1 * m2 * m2_inv;
    const term2 = b2 * m1 * m1_inv;
    return (term1 + term2) % M;
}
```

---

中国剰余定理（Chinese Remainder Theorem, CRT）は、**複数の異なる法（modulus）に関する同時合同式**の解を見つけるための強力な数学的定理です。ここでは、**定理の概要 → 直感的なイメージ → 数式の導出 → 計算手順 → 応用例**の順に、詳しく解説します。

---

## 🧠 1. 中国剰余定理とは？

### 📜 定理の内容（2つの式の場合）

> **m₁ と m₂ を互いに素な正の整数**とする。
> 任意の整数 b₁, b₂ に対して、
>
> ```
> Z ≡ b₁ (mod m₁)
> Z ≡ b₂ (mod m₂)
> ```
>
> をともに満たす整数 Z は、
> **0 ≦ Z < m₁ × m₂ の範囲にただ一つ存在する。**

### ✅ 互いに素とは？

`gcd(m₁, m₂) = 1`（最大公約数が1）であること。

---

## 🔍 2. 直感的な例

### 例：

```
Z ≡ 2 (mod 5)
Z ≡ 3 (mod 6)
```

このとき、Z を 0 〜 29（5×6−1）の範囲で探すと…

|  Z | Z mod 5 | Z mod 6 |
| -: | ------: | ------: |
| 27 |       2 |       3 |

→ ✅ 条件を満たす `Z = 27` がただ1つ存在！

---

## 🔧 3. 一般的な解法の導出（2式版）

### 与えられた：

```
Z ≡ b₁ (mod m₁)
Z ≡ b₂ (mod m₂)
```

### ステップ：

1. 全体の積：`M = m₁ * m₂`

2. 他方の法の積：`M₁ = m₂`, `M₂ = m₁`

3. 各 `Mᵢ` に対して、次を求める：

   * `y₁ = M₁⁻¹ mod m₁`
   * `y₂ = M₂⁻¹ mod m₂`

4. 解は次の形で得られる：

```
Z = (b₁ * M₁ * y₁ + b₂ * M₂ * y₂) mod M
```

---

## 🔁 4. 実際の計算方法

### 入力：

```
m₁ = 5, m₂ = 6, b₁ = 2, b₂ = 3
```

### 計算：

* `M = 5 × 6 = 30`
* `M₁ = 6`, `M₂ = 5`
* `y₁ = 6⁻¹ mod 5 = 1`（なぜなら 6≡1 mod 5 → 1\*1 ≡ 1 mod 5）
* `y₂ = 5⁻¹ mod 6 = 5`（5\*5 = 25 ≡ 1 mod 6）

```
Z = (2 * 6 * 1 + 3 * 5 * 5) mod 30
  = (12 + 75) mod 30
  = 87 mod 30
  = 27
```

---

## 📘 5. 定理の拡張（n本の式）

複数の法 `m₁, m₂, ..., mₙ` がすべて **互いに素**であるとき、

```
Z ≡ b₁ (mod m₁)
Z ≡ b₂ (mod m₂)
...
Z ≡ bₙ (mod mₙ)
```

これらをすべて同時に満たす Z は `M = m₁×m₂×...×mₙ` の範囲に1つだけ存在します。

解は次の形：

```
Z = ∑ (bᵢ * Mᵢ * yᵢ) mod M
  ※ Mᵢ = M / mᵢ, yᵢ = Mᵢ⁻¹ mod mᵢ
```

---

## 💡 6. 応用分野

| 分野    | 応用内容                |
| ----- | ------------------- |
| 暗号理論  | RSA暗号での計算高速化（秘密鍵計算） |
| 数値計算  | 大きな整数の分解と再構築        |
| 計算最適化 | モジュロ演算の分割処理         |
| 整数問題  | カレンダー・周期的なスケジュールの調整 |

---

## 🧩 7. 図によるイメージ（2式版）

```
数直線：mod 5 の世界と mod 6 の世界が交差する点

mod 5:   ...  2   7  12  17  22  27  ...
mod 6:   ...  3   9  15  21  27  33  ...

交点 → ✅ 27 が両方に一致
```

---

## ✅ まとめ

| 特徴   | 内容                           |
| ---- | ---------------------------- |
| 条件   | 各法が互いに素                      |
| 解の個数 | 0 ≤ Z < m₁×m₂×...×mₙ にちょうど1つ |
| 手法   | モジュロ逆元を使って合成                 |
| 応用   | 暗号・周期計算・分散演算 など              |

---
