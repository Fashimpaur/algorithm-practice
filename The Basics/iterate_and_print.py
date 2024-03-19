''' Iterate through a given array and print each value '''

arr_1 = [547, 230, 981, 64, 756, 312, 849, 173, 625, 408]
arr_2 = ["apple", "banana", "orange", "grape", "kiwi", "mango", "pineapple", "strawberry", "blueberry", "watermelon"]
arr_3 = [True, False, True, True, False]

def iterate_and_print(samples):
    for i in samples:
        print(i)
    print()

list(map(iterate_and_print, [arr_1, arr_2, arr_3]))