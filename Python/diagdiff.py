#Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonalDifference(arr):
    arr2 = arr[::-1]
    return abs(sum([arr[x][x] for x in range(len(arr))])-sum([arr2[y][y] for y in range(len(arr2))])
