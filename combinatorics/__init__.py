def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return int(fact)


def combination(n, k):
    comb = (factorial(n)/(factorial(k)*factorial(n-k)))
    return int(comb)


def permutation(n, k):
    perm = (factorial(n)/factorial(n-k))
    return int(perm)


# test cases -
# print(factorial(5))
# print(combination(5, 3))
# print(permutation(5, 2))
