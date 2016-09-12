def first_4(iterable):
    return iterable[:4]

def odds(iterable):
    return iterable[1::2]

def first_and_last_4(iterable):
    last_4 = iterable[(len(iterable)-4):]
    first_and_last = first_4(iterable).extend(last_4(iterable))
    return first_and_last

