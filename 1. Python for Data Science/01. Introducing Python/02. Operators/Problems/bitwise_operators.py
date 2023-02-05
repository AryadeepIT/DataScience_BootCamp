# Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
# 1. d = a ^ a
# 2. e = c ^ b
# 3. f = a & b
# 4. g = c | (a ^ a)
# 5. e = ~ e
# Note: ^ is for xor.
# The output is d e f g


a = int(input())
b = int(input())
c = int(input())

# Do a^a below
d = a ^ a
# Do c^b below
e = c ^ b
# Do a&b below
f = a & b
# Do c|(a^a) below
g = c | (a ^ a)
# Do ~e below
e = ~e

# The line below prints the output. Don't change it!
print(d, e, f, g)
