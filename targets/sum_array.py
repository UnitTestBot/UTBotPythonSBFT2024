def sum_(a_and_n):
    (a, n) = a_and_n
    result = 0
    for i in range(n):
        result += a[i]
    return result
