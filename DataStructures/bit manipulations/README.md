# **JavaScript におけるビット演算の基本**

JavaScript の数値は内部的には 64 ビット浮動小数点数（Number 型）ですが、ビット演算を行うときは 32 ビット符号付き整数（signed 32-bit integer） として扱われます。

例：

console.log(5 | 3);  // 5: 0101, 3: 0011 → 0111 = 7

# **🌟**

# **主なビット演算子**

| **演算子** | **名前** | **例** | **説明** |
| --- | --- | --- | --- |
| & | AND | a & b | 両方のビットが 1 のときだけ 1 |
| ` | ` | OR | `a |
| ^ | XOR（排他的 OR） | a ^ b | ビットが異なると 1 |
| ~ | NOT（ビット反転） | ~a | 全ビットを反転 |
| << | 左シフト | a << n | ビット列を左に n ビットずらす（末尾に 0 補完） |
| >> | 符号付き右シフト | a >> n | ビット列を右に n ビットずらす（符号ビットを補完） |
| >>> | 符号なし右シフト | a >>> n | ビット列を右に n ビットずらす（常に 0 補完） |

# **🔹**

# **具体例**

let a = 5;  // 00000000 00000000 00000000 00000101

let b = 3;  // 00000000 00000000 00000000 00000011

console.log(a & b); // 1   → 00000001

console.log(a | b); // 7   → 00000111

console.log(a ^ b); // 6   → 00000110

console.log(~a);    // -6  → 11111111 11111111 11111111 11111010

console.log(a << 1);// 10  → 00001010

console.log(a >> 1);// 2   → 00000010

console.log(a >>> 1);// 2  → 00000010

# **⚠️**

# **ビット演算の注意点**

✅ 小数は整数に変換される

console.log(5.7 | 0); // 5 （小数点以下切り捨て）

✅ 32 ビット符号付き整数として扱われる

console.log(2147483647 | 0);  // 2147483647 （32ビットの最大値）

console.log(2147483648 | 0);  // -2147483648 （符号ビットが立つ）

✅ >>> は負の値を正の値に変換することがある

console.log(-1 >>> 1); // 2147483647

# **🚀**

# **応用例**

**1️⃣ ビットマスクによるフラグ管理**

const FLAG_READ = 1 << 0;  // 0001

const FLAG_WRITE = 1 << 1; // 0010

const FLAG_EXEC = 1 << 2;  // 0100

let permission = FLAG_READ | FLAG_WRITE;  // 0011

console.log((permission & FLAG_READ) !== 0);  // true

console.log((permission & FLAG_EXEC) !== 0);  // false

**2️⃣ 符号の確認**

function isNegative(n) {

return (n >> 31) !== 0;

}

console.log(isNegative(-10)); // true

console.log(isNegative(10));  // false

**3️⃣ 簡易的な整数の floor 処理（高速化のためのテクニック）**

console.log(5.9 | 0); // 5

# **💡**

# **まとめ**

- ビット演算は数値を 32 ビット整数として扱います。
- AND, OR, XOR, NOT、シフト演算が基本。
- ビットマスクやフラグ管理、パフォーマンスチューニングで役立ちます。
- ただし、大きな整数や浮動小数点演算には注意。