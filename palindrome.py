n = int(input("Enter a number: "))
rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10
print("Number palindrome" if n == rev else "Not palindrome")