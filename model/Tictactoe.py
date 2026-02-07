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
        if not type(idx) is int or idx < min_index or idx > max_index:
            raise IndexError('некорректно указанные индексы')


    def __setitem__(self, key, value):
        i, j = key
        self.__pole[i][j] = value


