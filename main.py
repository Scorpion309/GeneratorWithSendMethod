def generator():
    x = 0
    while True:
        flag = yield x
        if flag is not None:
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
