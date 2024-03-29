from functools import reduce
from random import randint, shuffle


def generate_int_list(total, count, min_value_allowed, max_value_allowed):
    if total < count:
        raise ValueError("Total must be greater than or equal to count")

    if max_value_allowed < min_value_allowed:
        raise ValueError("max_value_allowed must be greater than min_value_allowed")

    expected_average = total / count

    integer_list = []

    numbers = list(range(min_value_allowed, max_value_allowed))


    shuffle(numbers)
    integer_list = numbers[:count]
    list_total = sum(integer_list)

    while list_total != total:
        if list_total < total:
            balance = total - list_total

            for i, v in enumerate(integer_list):
                if v + balance < max_value_allowed:
                    integer_list[i] = v + balance
                    break

                diff = max_value_allowed - v
                if v + balance > max_value_allowed:
                    integer_list[i] = max_value_allowed
                    balance = balance - diff
                else:
                    integer_list[i] = v + diff
                    break

        if list_total > total:
            balance = list_total - total

            for i, v in enumerate(integer_list):
                if v - balance > min_value_allowed:
                    integer_list[i] = v - balance
                    break
                if v > min_value_allowed and v - balance < max_value_allowed:
                    diff = v - min_value_allowed
                    integer_list[i] = min_value_allowed
                    balance = balance - diff

        list_total = sum(integer_list)

        if list_total != total:
            shuffle(numbers)
            integer_list = numbers[:count]
            list_total = sum(integer_list)

    return integer_list





    # while True:
    #     integer_list = [randint(min_value_allowed, max_value_allowed) for i in range(count)]
    #     avg = reduce(lambda x, y: x + y, integer_list) / len(integer_list)
    #
    #     if avg == expected_average:
    #         return integer_list


def generate_rand_list(lowest, highest, length):
    output_list = []
    for i in range(length):
        output_list.append(randint(lowest, highest))
    print(output_list)


if __name__ == '__main__':
    int_list = generate_int_list(468, 18, 1, 32)
    print(int_list),
    print(len(int_list))

    int_list = generate_int_list(714, 17, 1, 50)
    print(int_list),
    print(len(int_list))
