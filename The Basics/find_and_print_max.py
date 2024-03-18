''' Find and print the largest element in a given array '''

arr_1 = [547, 230, 981, 64, 756, 312, 849, 173, 625, 408]
arr_2 = [279, 531, 647, 182, 814, 390, 703, 58, 965, 376, 125, 845, 612, 238, 739]
arr_3 = [47, 18, 92, 56, 63, 85, 12, 37, 72, 29, 41, 5, 88, 76, 24, 9, 61, 53, 98, 14]

def find_max_value(sample):
    max = 0
    for num in sample:
        if num > max:
            max = num
    return max

print(find_max_value(arr_1))
print(find_max_value(arr_2))
print(find_max_value(arr_3))