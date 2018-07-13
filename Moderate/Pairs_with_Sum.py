# 16.24 Pairs with Sum
# Design an algorithm to find all pairs of integers within an array which sum to a specified value.


# Brute Force approach -> for each element search through rest of the array to find compliment to sum up to target value
# Time Complexity -> O(N^2)
# Space Complexity -> O(1)
def find_all_pairs1(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            j_pointer = i + j + 1
            pair_sum = arr[i] + arr[j_pointer]
            if pair_sum == target:
                print arr[i], arr[j_pointer]


# Solution using dictionary to hold values for quick lookup of compliment.
# Time Complexity -> O(N)
# Space Complexity -> O(N)
def find_all_pairs2(arr, target):
    lookup_dict = {}
    for value in arr:
        if target - value in lookup_dict:
            print value, target - value
        lookup_dict[value] = None


# Solution when we receive sorted array as argument.
# Time Complexity -> O(N)
# Space Complexity -> O(1)
def find_all_pairs3(arr, target):
    start_pointer = 0
    end_pointer = len(arr) - 1

    while start_pointer < end_pointer:
        pair_sum = arr[start_pointer] + arr[end_pointer]
        if pair_sum == target:
            print arr[start_pointer], arr[end_pointer]
            start_pointer += 1
            end_pointer -= 1
        else:
            if pair_sum > target:
                end_pointer -= 1
            else:
                start_pointer += 1


# e.g arr = [-2,4,-3,2,5,8,9,12]
# target = 17
# ans -> (5, 12)
#        (8, 9)
if __name__ == '__main__':
    arr = [9, 8, 12, -2, 4, -3, 2, 5]
    target = 17
    sorted_arr = sorted(arr)

    print 'Brute Force solution:'
    find_all_pairs1(arr, target)

    print 'Dictionary solution:'
    find_all_pairs2(arr, target)

    print 'Solution with sorted array passed'
    find_all_pairs3(sorted_arr, target)
