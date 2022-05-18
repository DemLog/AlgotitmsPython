class BinarySearchTask:

    @staticmethod
    def rec_bin_search(arr, key, left, right):
        if right >= left:
            mid = left + (right - left) // 2

            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return BinarySearchTask.rec_bin_search(arr, key, left, mid - 1)
            else:
                return BinarySearchTask.rec_bin_search(arr, key, mid + 1, right)
        else:
            return -1



