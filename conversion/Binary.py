num = int(input("Enter a number: "))

def num2bin(n, bits = 8):
    bin = ""
    for i in range(bits):
        bin = ("1" if (2**i & n) else "0") + bin
    return bin

def num2bin_neg(n, bits = 8):
    return num2bin(~n + 1, bits)

print(num2bin(num, 8))      # n -> bin
print(num2bin_neg(num, 8))  # (-n) -> bin

























# num = int(input("Enter a number: "))

# def dec2bin(n):
#     bin = ""

#     bit = 2 ** (8 - 1) # bit = 128
#     bit >>= 1 # bit = 128

#     while bit > 0:
#         bin += "1" if (n & bit) else "0"
#         bit >>= 1 # bit = bit >> 1

#     return bin

# print(dec2bin(num))
# print(dec2bin(~int(dec2bin(num), 2) + 1)) # flipped