def solution(A, B, C):
    # write your code in Python 3.6
    bit_list = [0] * 32
    bit_A = [0] * 32
    bit_B = [0] * 32
    bit_C = [0] * 32
    for i in range(0, 30):
        test_num = 1 << i
        if test_num & A:
            bit_A[i] = 1
        if test_num & B:
            bit_B[i] = 1
        if test_num & C:
            bit_C[i] = 1
    a1 = 1 << (30 - sum(bit_A))
    b1 = 1 << (30 - sum(bit_B))
    c1 = 1 << (30 - sum(bit_C))

    for i in range(0, 30):
        if bit_A[i] or bit_B[i]:
            bit_list[i] = 1
    ab = (1 << (30 - sum(bit_list))) if sum(bit_list) else 0
    bit_list = [0] * 32
    for i in range(0, 30):
        if bit_A[i] or bit_C[i]:
            bit_list[i] = 1
    ac = (1 << (30 - sum(bit_list))) if sum(bit_list) else 0
    bit_list = [0] * 32
    for i in range(0, 30):
        if bit_B[i] or bit_C[i]:
            bit_list[i] = 1
    bc = (1 << (30 - sum(bit_list))) if sum(bit_list) else 0
    bit_list = [0] * 32
    for i in range(0, 30):
        if bit_A[i] or bit_B[i] or bit_C[i]:
            bit_list[i] = 1
    abc = (1 << (30 - sum(bit_list))) if sum(bit_list) else 0
    if A == B == 0 or A == C == 0:
        a1 = 0
    if B == C == 0:
        b1 = 0
    # print("a1:", a1, "b1:", b1, "c1:", c1, "ab:", ab, "ac:", ac, "bc:", bc, "abc:", abc)
    sum_count = a1 + b1 + c1 - ab - ac - bc + abc

    return sum_count


if __name__ == '__main__':
    # A = 8
    A = 1073741727
    B = 1073741631
    C = 1073741679
    lea_count = solution(A, B, C)
    print(lea_count)

    # A = 1073741824
    A = 0
    B = 0
    C = 0
    lea_count = solution(A, B, C)
    print(lea_count)

    # A = 1
    A = 1073741823
    B = 1073741823
    C = 1073741823
    lea_count = solution(A, B, C)
    print(lea_count)