n = input("Enter first number: ")
m = input("Enter second number: ")
n = int(n)
m = int(m)
n_last_digit = n % 10
m_last_digit = m % 10
if n_last_digit > m_last_digit:
    print(n)
elif n_last_digit < m_last_digit:
    print(m)
else:
    if n > m:
        print(n)
    elif m > n:
        print(m)
    else:
        print(n, " = ",m)
