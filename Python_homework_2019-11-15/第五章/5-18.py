def myall(iterable):
    for item in iterable:
        if not item:
            return False
    return True

def myany(iterable):
    for item in iterable:
        if item:
            return True
    return False

def myzip(*iterables):
    min_length=min(map(len,iterables))
    for i in range(min_length):
        yield tuple((it[i] for it in iterables))