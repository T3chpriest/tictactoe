class Cell:
    def __init__(self, value = 0):
        self.value = value


    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    SIZE = 3
    def __init__(self):
        self.__pole = tuple([tuple([Cell() for _ in range(self.SIZE)]) for _ in range(self.SIZE)])

    @staticmethod
    def index_check(idx):
        max_index = 2
        min_index = 0
        for _ in idx:
            if not type(_) is int or _ < min_index or _ > max_index:
                raise IndexError('некорректно указанные индексы')


    def __setitem__(self, key, value):
        self.index_check(key)
        i, j = key
        self.__pole[i][j] = value


    def __getitem__(self, key):
        self.index_check(key)
        i, j = key
        return self.__pole[i][j]


    def show(self):
        print(self.__pole)


    def human_go(self):
        self[input()] = self.HUMAN_X



