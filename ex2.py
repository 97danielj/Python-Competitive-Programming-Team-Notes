from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

result2 = list(combinations(data,2))
print(result2)


result3 = list(product(data, repeat = 3))

print(result3)

result4 = list(combinations_with_replacement(data, 2))
print(result4)