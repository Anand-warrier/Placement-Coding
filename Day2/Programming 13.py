rows, cols = map(int, input().split())
matrix1 = []
matrix2 = []
result = []
for i in range(rows):
    matrix1.append(list(map(int, input().split())))
for i in range(rows):
    matrix2.append(list(map(int, input().split())))
print("First Matrix:")
for row in matrix1:
    print(*row)
print("Second Matrix:")
for row in matrix2:
    print(*row)
print("Sum of the two matrices is:")
for i in range(rows):
    row_result = []
    for j in range(cols):
        row_result.append(matrix1[i][j] + matrix2[i][j])
    print(*row_result)
