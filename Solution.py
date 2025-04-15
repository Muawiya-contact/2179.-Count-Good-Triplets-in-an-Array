# By Coding Moves
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.n = size

    def update(self, index, value):
        index += 1
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)

        # Map value to index in nums2
        pos_in_nums2 = {val: i for i, val in enumerate(nums2)}

        # Convert nums1 values into their positions in nums2
        transformed = [pos_in_nums2[val] for val in nums1]

        # Count left smaller
        left_tree = FenwickTree(n)
        left_smaller = [0] * n
        for i in range(n):
            left_smaller[i] = left_tree.query(transformed[i] - 1)
            left_tree.update(transformed[i], 1)

        # Count right larger
        right_tree = FenwickTree(n)
        right_larger = [0] * n
        for i in range(n - 1, -1, -1):
            right_larger[i] = right_tree.query(n - 1) - right_tree.query(transformed[i])
            right_tree.update(transformed[i], 1)

        # Multiply left and right counts
        count = 0
        for i in range(n):
            count += left_smaller[i] * right_larger[i]

        return count
