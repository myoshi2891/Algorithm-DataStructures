
## **問題の概要**

「配列の中から、**和が0になる3つ組**を全て見つける。ただし**重複は禁止**」

---

## **アルゴリズム図解**

### ① ソート（`O(NlogN)`）

#### 例：

入力 `nums = [-1, 0, 1, 2, -1, -4]`
まず**昇順にソート**します。

```
元配列:   [-1, 0, 1, 2, -1, -4]

ソート後: [-4, -1, -1, 0, 1, 2]
```

---

### ② forループで1つ目の要素`nums[i]`を決める

```
for i = 0 から n-3までループ
```

各`i`について、残り2つを**2ポインタで探索**します。

---

## **③ 2ポインタ法**

#### 考え方：

* `left` ポインタ: `i+1`（左から順に）
* `right` ポインタ: 配列の最後

**和が0になるか判定**します。

---

### **図解：1回目のループ**

```
i = 0  (nums[i] = -4)

left  -> index 1 (nums[left] = -1)
right -> index 5 (nums[right] = 2)
```

#### 計算：

```
sum = -4 + (-1) + 2 = -3
```

→ **小さいのでleftを右に移動**

---

次：

```
i = 0

left  -> index 2 (nums[left] = -1)
right -> index 5 (nums[right] = 2)

sum = -4 + (-1) + 2 = -3
```

→ また**小さいのでleft++**

---

次：

```
i = 0

left  -> index 3 (nums[left] = 0)
right -> index 5 (nums[right] = 2)

sum = -4 + 0 + 2 = -2
```

→ 小さいのでleft++

---

次：

```
i = 0

left  -> index 4 (nums[left] = 1)
right -> index 5 (nums[right] = 2)

sum = -4 + 1 + 2 = -1
```

→ 小さいのでleft++

---

`left >= right` になったのでループ終了
→ **解なし**

---

## **④ 次の`i`に進む**

```
i = 1 (nums[i] = -1)

left  -> index 2 (nums[left] = -1)
right -> index 5 (nums[right] = 2)

sum = -1 + (-1) + 2 = 0
```

#### → 解発見！

```
[-1, -1, 2]
```

---

### **図：結果**

```
[-4, -1, -1, 0, 1, 2]
   ^    ^           ^
   i   left       right

   sum = -1 + -1 + 2 = 0
```

---

## **⑤ 重複回避**

解を追加したら、
**同じ数字はスキップ**します。

```
while left < right && nums[left] == nums[left+1]:
    left++

while left < right && nums[right] == nums[right-1]:
    right--
```

---

## **⑥ 次の探索**

次の組み合わせを探します。

```
left -> index 3 (nums[left] = 0)
right -> index 4 (nums[right] = 1)

sum = -1 + 0 + 1 = 0
```

#### 解発見！

```
[-1, 0, 1]
```

---

## **⑦ 全探索終了**

他の`i`についても同様に探索。
重複を避けながら、**すべての3つ組を見つける**。

---

## **最終結果**

```
[[-1, -1, 2],
 [-1, 0, 1]]
```

---

# **全体フロー図**

```plaintext
      ┌──────────────┐
      │   配列をソート │
      └──────┬───────┘
             │
     ┌───────▼────────┐
     │  i を 0～n-3まで │
     └───────┬────────┘
             │
      ┌─────▼─────┐
      │ left=i+1   │
      │ right=n-1  │
      └─────┬─────┘
            │
 ┌──────────▼──────────┐
 │ sum=nums[i]+nums[left]+nums[right] │
 └──────────┬──────────┘
            │
     ┌──────┴──────┐
 ┌───▼───┐   ┌────▼────┐
 │ sum=0 │   │ sum≠0   │
 └───┬───┘   └────┬────┘
     │            │
 ┌───▼───┐   ┌────▼────┐
 │ 解追加 │   │ ポインタ更新 │
 └───┬───┘   └─────────┘
     │
 ┌───▼───┐
 │ 重複除去 │
 └───┬───┘
     │
     ▼
  次の探索
```

---

## **計算量**

| 処理      | 計算量      |
| ------- | -------- |
| ソート     | O(NlogN) |
| 2ポインタ探索 | O(N²)    |

---

## **まとめ**

* **ソート**+**2ポインタ法**で効率的に3Sumを解決
* **重複除去**が重要（ソート後だから可能）
* **全探索O(N³)** ではなく **O(N²)** で解ける！

