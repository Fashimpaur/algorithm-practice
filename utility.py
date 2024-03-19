from random import randint


def generate_int_list(total, count, min_value_allowed, max_value_allowed):
    ''' This is buggy at this time but multiple attempts can generate a list '''
    if total < count:
        raise ValueError("Total must be greater than or equal to count")

    integer_list = [1] * count

    while(sum(integer_list) < total):
        for i in range(len(integer_list)):
            if sum(integer_list) == total:
                break
            current_diff = total - sum(integer_list)
            if current_diff < max_value_allowed:
                integer_list[i] = integer_list[i] + randint(integer_list[i] + 1 , current_diff)
            else:
                integer_list[i] = randint(min_value_allowed, max_value_allowed)

    print(integer_list)
    print(sum(integer_list))


# generate_int_list(468, 18, 1, 32)

def generate_rand_list(lowest, highest, length):
    output_list = []
    for i in range(length):
        output_list.append(randint(lowest, highest))
    print(output_list)

generate_rand_list(0, 20, 15)


