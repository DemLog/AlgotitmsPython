import random
import copy

from testing import AlgorithmTest
from SortAlgorithm import Sort


def insertion_test(iter):
    test = AlgorithmTest('InsertionSort', 'C:/Users/DemLoveSky/Desktop/lab1-2.xlsx', 2)
    arr = []
    for x in range(1, iter+1):
        arr.append(random.randint(1, 100000))
        arrtest = copy.copy(arr)
        test.start_test()
        Sort.insertion_sort(arrtest)
        test.end_test()
    test.save_result()


def bogosort_test(iter):
    test = AlgorithmTest('BogoSort', 'C:/Users/DemLoveSky/Desktop/lab1-2.xlsx', 1)
    arr = []
    for x in range(1, iter+1):
        arr.append(random.randint(1, 100000))
        arrtest = copy.copy(arr)
        print(test.start_test())
        Sort.bogo_sort(arrtest)
        test.end_test()
    test.save_result()

def quick_test(iter):
    test = AlgorithmTest('QuickSort', 'C:/Users/DemLoveSky/Desktop/lab1-2.xlsx', 3)
    arr = []
    for x in range(1, iter+1):
        arr.append(random.randint(1, 100000))
        arrtest = copy.copy(arr)
        print(test.start_test())
        Sort.quick_sort(arrtest)
        test.end_test()
    test.save_result()

def binarysort_test(iter):
    test = AlgorithmTest('BinarySort', 'C:/Users/DemLoveSky/Desktop/lab1-2.xlsx', 4)
    arr = []
    for x in range(1, iter+1):
        arr.append(random.randint(1, 100000))
        arrtest = copy.copy(arr)
        print(test.start_test())
        Sort.tree_sort(arrtest)
        test.end_test()
    test.save_result()


# insertion_test(2000)
# bogosort_test(10)
# quick_test(2000)
binarysort_test(2000)
