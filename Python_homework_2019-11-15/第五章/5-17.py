def mymaxmin(iterable):
    tmax=tmin=iterable[0]
    for item in iterable[1:]:
        if item>tmax:
            tmax=item
        elif item<tmin:
            tmin=item
    return(tmax,tmin)