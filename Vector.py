class Vector:

    @staticmethod
    def return_one(arr):
        for i in range(0, len(arr)):
            arr[i] = 1

    @staticmethod
    def return_sum(arr):
        sum_vector = 0
        for i in range(0, len(arr)):
            sum_vector += arr[i]
        return sum_vector

    @staticmethod
    def return_mult(arr):
        mult_vector = 0
        for i in range(0, len(arr)):
            mult_vector *= arr[i]
        return mult_vector

    @staticmethod
    def polinom(arr):
        X = 1.5
        sum = 0
        for i in range(1, len(arr)):
            sum += arr[i] * pow(X, i - 1)
