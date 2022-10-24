def solution(A, K):
    n = 0
    x = 0
    for x in range(0, K, 1):
        for y in range(0, len(A), 1):
            A[n + 1] = A[n]
            A[-1] = A[0]

solution()