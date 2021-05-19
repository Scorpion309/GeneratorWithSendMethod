def generator():
    x = 0
    while True:
        try:
            flag = yield x
            if flag is not None:
                x += 1
                yield x
            else:
                x += 2
        except ValueError:
            x = 0
            yield x
            print('Сброс генератора')



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
    gen.throw(ValueError, "To zero!")
    print(next(gen))
    print(next(gen))
    print(next(gen))
    gen.send(False)
    print(next(gen))
    print(next(gen))
    gen.send(True)
    print(next(gen))
