Linked List（リンクドリスト）は、データを線形に管理するデータ構造の一つで、動的なメモリ管理を行う必要がある場合や、頻繁にデータの挿入・削除を行うアプリケーションに適しています。配列と異なり、要素は連続したメモリ領域に格納されていませんが、それぞれの要素が次の要素への参照（ポインタ）を持つことで連続的にアクセス可能となっています。

以下では、Linked Listの基本構造、種類、利点と欠点について説明します。

---

## **1. 基本構造**
Linked Listは複数のノード（Node）で構成されます。各ノードは以下の2つの部分から成ります：
1. **データ部**: 実際の値を保持する。
2. **ポインタ部**: 次のノードを指すポインタ（アドレス）。

例:
```
[データ|ポインタ] -> [データ|ポインタ] -> [データ|ポインタ] -> NULL
```
- 最初のノードを**ヘッド（Head）**と呼びます。
- 最後のノードはポインタとして`NULL`を持ちます。

---

## **2. Linked Listの種類**
### **a. Singly Linked List (単方向リスト)**
- 各ノードが次のノードを指します。
- ノードを1方向にしかたどれません。
  
例:
```
Head -> [10|次] -> [20|次] -> [30|NULL]
```

### **b. Doubly Linked List (双方向リスト)**
- 各ノードが「次のノード」と「前のノード」の2つのポインタを持ちます。
- 前後にノードをたどることが可能です。

例:
```
NULL <- [10|次, 前] <-> [20|次, 前] <-> [30|NULL, 前]
```

### **c. Circular Linked List (循環リスト)**
- リストの最後のノードが、最初のノードを指すことでリストが循環します。
- 単方向または双方向で実装できます。

例:
```
[10|次] -> [20|次] -> [30|次] --+
         ^----------------------+
```

---

## **3. Linked Listの操作**
### **a. 挿入 (Insertion)**
- リストの先頭、末尾、または指定位置に新しいノードを追加。
- 時間計算量は挿入位置により異なり、通常は`O(1)`または`O(n)`。

### **b. 削除 (Deletion)**
- 指定したノードを削除。
- 時間計算量は`O(1)`（先頭削除）または`O(n)`（末尾や指定位置）。

### **c. 検索 (Search)**
- リスト内に特定のデータが存在するかを確認。
- 時間計算量は`O(n)`。

---

## **4. Linked Listの利点**
1. **動的なサイズ変更が可能**:
   - 配列のようにサイズを固定する必要がない。
2. **高速な挿入・削除**:
   - 要素の移動が不要（特に先頭や末尾での操作が効率的）。
3. **メモリ効率**:
   - 必要な分だけメモリを割り当てる。

---

## **5. Linked Listの欠点**
1. **ランダムアクセスが非効率**:
   - 配列のようにインデックスを指定して即座にアクセスできない（逐次アクセスのみ）。
2. **オーバーヘッド**:
   - 各ノードがポインタを持つため、配列に比べてメモリ使用量が多い。
3. **検索コストが高い**:
   - 必要な要素を探すのに線形時間`O(n)`が必要。

---

## **6. 用途と応用例**
- 実装の柔軟性が求められる場合やデータ構造が動的に変化する場合に使用されます。  
具体例:
1. **スタック**や**キュー**の実装。
2. **グラフ**の隣接リスト表現。
3. メモリ管理（フリーリストなど）。
4. テキストエディタのアンドゥ機能（双方向リスト）。

---
