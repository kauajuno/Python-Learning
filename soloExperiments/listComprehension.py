"""
# LIST COMPREHENSION

squares = [x**2 for x in range(1, 30) if x**2 < 500]
print(squares)


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vecsep = [num for elem in vec for num in elem]
print(vec)
print(vecsep)
"""

# NESTED LIST COMPREHENSION

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transposed_matrix = [[row[i] for row in matrix] for i in range(4)]

for i in range(4):
    for j in range(3):
        print(transposed_matrix[i][j], end=" ")
    print()

print(transposed_matrix)
print(matrix)
print(*matrix)
print(list(zip(matrix)))
print(list(zip(*matrix)))

