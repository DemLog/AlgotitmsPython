import random
from random import randint


class Sort:

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(len(arr) - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    @staticmethod
    def insertion_sort(arr, left=0, right=None):
        if right is None:
            right = len(arr) - 1

        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1

            while j >= left and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr

    @staticmethod
    def shaker_sort(arr):
        start = 0
        end = len(arr) - 1

        while start <= end:
            for i in range(start, end, +1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            end -= 1

            for i in range(end, start, -1):
                if arr[i - 1] > arr[i]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            start += 1

        return arr

    @staticmethod
    def quick_sort(arr):
        if len(arr) < 2:
            return arr

        low, same, high = [], [], []
        pivot = arr[randint(0, len(arr) - 1)]

        for item in arr:
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        return Sort.quick_sort(low) + same + Sort.quick_sort(high)

    @staticmethod
    def timsort(arr):
        min_run = 32
        n = len(arr)

        for i in range(0, n, min_run):
            Sort.insertion_sort(arr, i, min((i + min_run - 1), n - 1))

        size = min_run

        while size < n:
            for start in range(0, n, size * 2):
                midpoint = start + size - 1
                end = min((start + size * 2 - 1), (n - 1))
                merged_array = Sort.__merge(
                    left=arr[start:midpoint + 1],
                    right=arr[midpoint + 1:end + 1]
                )
                arr[start:start + len(merged_array)] = merged_array
            size *= 2

        return arr

    @staticmethod
    def tree_sort(arr):
        btree = BinaryTree()
        return btree.starting(arr)

    @staticmethod
    def shell_sort(arr):
        n = len(arr)
        gap = int(n / 2)

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap = int(gap / 2)

        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) < 2:
            return arr

        midpoint = len(arr) // 2

        return Sort.__merge(
            left=Sort.merge_sort(arr[:midpoint]),
            right=Sort.merge_sort(arr[midpoint:])
        )

    @staticmethod
    def comb_sort(arr):
        n = len(arr)
        gap = n
        swapped = True

        while gap != 1 or swapped == 1:
            gap = int((gap * 10) / 13)
            if gap < 1:
                gap = 1

            swapped = False

            for i in range(0, n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True

        return arr

    @staticmethod
    def gnome_sort(arr):
        n = len(arr)
        index = 0

        while index < n:
            if index == 0:
                index = index + 1
            if arr[index] >= arr[index - 1]:
                index = index + 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index = index - 1

        return arr

    @staticmethod
    def bogo_sort(arr):
        bsort = BogoSort()
        return bsort.bogo_sort(arr)

    @staticmethod
    def __merge(left, right):
        if len(left) == 0:
            return right

        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0

        while len(result) < len(left) + len(right):
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                result += left[index_left:]
                break
            if index_left == len(left):
                result += right[index_right:]
                break

        return result


class BinaryTree:
    class __TreeNode:
        def __init__(self, key, arr):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None
            self.arr = arr

        def insert(self, node):
            if self.key > node.key:
                if self.left is None:
                    self.left = node
                    node.parent = self
                else:
                    self.left.insert(node)
            elif self.key <= node.key:
                if self.right is None:
                    self.right = node
                    node.parent = self
                else:
                    self.right.insert(node)

        def inorder(self):
            if self.left is not None:
                self.left.inorder()
            self.arr.append(self.key)
            if self.right is not None:
                self.right.inorder()

    def __init__(self):
        self.root = None
        self.result = []

    def __inorder(self):
        if self.root is not None:
            self.root.inorder()

    def __add(self, key):
        new_node = self.__TreeNode(key, self.result)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

    def starting(self, arr):
        for x in arr:
            self.__add(x)
        self.__inorder()

        return self.result


class BogoSort:

    def bogo_sort(self, arr):
        while not self.__is_sorted(arr):
            self.__shuffle(arr)
        return arr

    @staticmethod
    def __is_sorted(arr):
        n = len(arr)
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    @staticmethod
    def __shuffle(arr):
        n = len(arr)
        for i in range(0, n):
            r = random.randint(0, n - 1)
            arr[i], arr[r] = arr[r], arr[i]
