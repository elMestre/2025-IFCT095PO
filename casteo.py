def d(variable):
    print(variable, type(variable))

if __name__ == "__main__":
    a = float(3)
    x = int(1)
    y = int(2.8)
    z = int("3")
    w = int(float("3.0"))

    d(a)
    d(x)
    d(y)
    d(z)
