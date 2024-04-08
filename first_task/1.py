def e():
    e = 1.0
    counter = 0
    while (1 + e != 1):
        counter += 1
        e /= 2

    return (e, counter)


print(e())