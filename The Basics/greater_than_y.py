''' Given an array and a value Y, print the number of values greater than Y '''

arr_1 = [6, 27, 22, 4, 18, 40, 3, 8, 23, 15, 13, 9, 2, 20, 32, 31, 30, 35, 47, 48]
arr_2 = [8, 33, 16, 2, 19, 28, 5, 12, 21, 7, 25, 10, 30, 23, 3, 35, 38, 13, 31, 18]
arr_3 = [23, 9, 14, 20, 16, 18, 4, 25, 6, 22, 21, 11, 3, 12, 8, 19, 17, 24, 28, 27]

def greater_than_y(sample, y):
    matches = []
    count = 0

    for i in sample:
        if i > y:
            matches.append(i)
            count += 1

    print(count, matches)

greater_than_y(arr_1, 28)
greater_than_y(arr_2, 35)
greater_than_y(arr_3, 16)
greater_than_y(arr_3, 49)
