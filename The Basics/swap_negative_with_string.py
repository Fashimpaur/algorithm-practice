''' Given a list of numbers, change any negative numbers to 'Whoops!' '''

arr_1 = [-19, 3, 19, -7, 5, -9, -11, 4, -5, -4, 1, -7, 1, 14, -7]
arr_2 = []
arr_3 = [14, 1, 7, 4, 18, 19, 8, 1, 6, 9, 13, 13, 0, 4, 18]

def swap_negative_with_string(sample):
    updated_list = [i  if i >= 0 else "Whoops!" for i in sample]
    print(updated_list)

list(map(swap_negative_with_string, [arr_1, arr_2, arr_3]))
