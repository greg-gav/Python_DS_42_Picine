def data_types():
    i = int()
    s = str()
    f = float()
    b = bool()
    lt = list()
    d = dict()
    t = tuple()
    st = set()

    lst = map(type, [i, s, f, b, lt, d, t, st])
    print(f"[{', '.join(var.__name__ for var in lst)}]")


if __name__ == "__main__":
    data_types()
