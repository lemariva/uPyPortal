type_gen = type((lambda: (yield))())


def conv(it):
    yield '"'
    #yield from it
    for i in it:
        yield i.replace('"', "'").replace("\n", "\\n")
    yield '"'


def idumps(obj):
    if isinstance(obj, str):
        yield '"'
        yield obj
        yield '"'
    elif isinstance(obj, int):
        yield str(obj)
    elif isinstance(obj, dict):
        comma = False
        yield '{'
        for k, v in obj.items():
            if comma:
                yield ',\n'
            yield from idumps(k)
            yield ': '
            yield from idumps(v)
            comma = True
        yield '}'
    elif isinstance(obj, type_gen):
        yield from conv(obj)
    else:
        assert 0, repr(obj)


if __name__ == "__main__":
    def templ():
        yield from ["1", "2", "3"]
    print(list(idumps({"foo": templ()})))
