# Count Good Triplets in an Array (LeetCode 2179)

## 🧠 Problem Statement

You are given two `0-indexed` arrays `nums1` and `nums2` of length `n`, both of which are **permutations of** `[0, 1, ..., n - 1]`.

A **good triplet** is a set of 3 distinct values which are **in increasing order by position** in both `nums1` and `nums2`.

In other words, for a triplet `(x, y, z)`, let:

- `pos1x` = index of x in `nums1`
- `pos2x` = index of x in `nums2`

Then a **good triplet** must satisfy:

+ pos1[x] < pos1[y] < pos1[z] AND pos2[x] < pos2[y] < pos2[z]

  
---

## ✨ Example 1

**Input:**
```python
nums1 = [2, 0, 1, 3]
nums2 = [0, 1, 2, 3]
```
### Output: 1

### Explanation: There are 4 valid triplets in nums1 by position:

+ (2,0,1), (2,0,3), (2,1,3), (0,1,3)

+ Only (0,1,3) keeps the increasing order in both arrays. ✅

## ✅ Constraints
+ n == nums1.length == nums2.length

+ 3 <= n <= 10⁵

+ 0 <= nums1[i], nums2[i] <= n - 1

+ nums1 and nums2 are permutations of [0, ..., n - 1]

  
## 🧮 Time & Space Complexity
### Time Complexity: O(n log n) due to BIT queries and updates.

#### Space Complexity: O(n) for BIT and arrays.

## 📚 Topics Covered
+ Binary Indexed Tree (Fenwick Tree)

+ Coordinate Transformation

+ Permutations

+ Counting with Prefix Sums

## 🏁 Conclusion
This problem demonstrates how we can turn a brute-force O(n³) approach into a highly optimized O(n log n) solution using smart data structures and transformations. 💡

