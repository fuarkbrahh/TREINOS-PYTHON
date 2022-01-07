print('Treino def! ')


def sum(n1, n2=3):
    return n1+n2


s1 = sum(4)
s2 = sum(5, 350)
s3 = sum(5, 21)

print(s1, s2, s3)


print('______________________________ ')


def num(x):
    def num1(y):
        return x*y
    return num1


result = num(10)(3)
print(result)
