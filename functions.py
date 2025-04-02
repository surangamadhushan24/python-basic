def sayHello():
    print("hellooooo")


sayHello()


def getsum(x, y):
    print(x + y)


getsum(2, 4)


def returnSum(x, y):

    return x + y


tot = returnSum(4, 6)
print(tot)


def getAnswer(num1,num2):
    tot = num1 + num2
    mul = num1 * num2
    return tot, mul


total , multipication = getAnswer(2,6)
print(total,multipication)