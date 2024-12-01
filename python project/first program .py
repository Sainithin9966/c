class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class And:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"And({', '.join(map(str, self.args))})"


class Or:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"Or({', '.join(map(str, self.args))})"


class Not:
    def __init__(self, arg):
        self.arg = arg

    def __repr__(self):
        return f"Not({self.arg})"
