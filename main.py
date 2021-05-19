def generator():
    x = 0
    while True:
        h = yield x
        if h == False or h == True:
            x += 1
            yield x
        else:
            x += 2


if __name__ == '__main__':
    gen = generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    gen.send(False)
    print(next(gen))
    print(next(gen))
    gen.send(True)
    print(next(gen))
