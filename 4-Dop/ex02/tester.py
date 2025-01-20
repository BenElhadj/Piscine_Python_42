# tester.py


from callLimit import callLimit


@callLimit(5)
def f(i):
    print(f"f({i})")


@callLimit(2)
def g(i):
    print(f"g({i})")


for i in range(10):
    f(i + 1)
    g(i + 1)
