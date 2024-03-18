''' Create an array of all odd integers between 1 and 1028 '''

result = []
for i in range(1028):
    if i%2:
        result.append(i)
print(result)