''' Given an array of numbers, print the min, max, and average '''

arr_1 = [29, 73, 51, 16, 42, 5]
arr_2 = [70, 84, 38, 84, 11, 57, 42, 34, 15, 1, 72, 23, 76, 67, 19, 20, 1]
arr_3 = []
arr_4 = [25, 23, 26, 31, 23, 21, 30, 6, 12, 12, 31, 32, 22, 31, 61, 26, 26, 30]

def min_max_avg(sample):
    if len(sample) == 0:
        print('Empty array. No minimum, maximum, or average.')
    else:
        minimum = sample[0]
        maximum = sample[0]
        total = sample[0]

        for x, i in enumerate(sample):
            if x > 0:
                if i < minimum:
                    minimum = i
                if i > maximum:
                    maximum = i
                total = total + i

        print(f'Min: {minimum} Max: {maximum} Total: {total} Avg: {total/len(sample)}')

list(map(min_max_avg, [arr_1, arr_2, arr_3, arr_4]))
