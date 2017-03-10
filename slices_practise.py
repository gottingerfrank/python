def first_4(iterable):
    return iterable[:4]

def first_and_last_4(iterable):
    return iterable[:4]+iterable[-4:]

def odds(iterable):
    odds = []
    for i in range(len(iterable)):
        if i % 2 == 0:
            pass
        else:
            odds.append(iterable[i])
    return odds

def reverse_evens(iterable):
    evens = []
    for i in range(len(iterable)):
        if i % 2 == 0:
            evens.append(iterable[i])
        else:
            pass
    evens = evens[::-1]
    return evens


    “