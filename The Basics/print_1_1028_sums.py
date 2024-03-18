''' Print every integer from 1 to 1027 following each with the sum of all integers to that point '''

sum = 0

for i in range(1, 1028):
    sum += i
    print(i, sum)
