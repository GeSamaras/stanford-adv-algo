def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        m = n // 2
        a = x // 10**m
        b = x % 10**m
        c = y // 10**m
        d = y % 10**m
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        return ac * 10**(2*m) + (ad_plus_bc * 10**m) + bd
    
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba(num1, num2))
