class PQueue:
    def __init__(self):
        self.__values = []
        self.__descending = False
        self.__custom_sort_key = None

    def __sort(self):
        if self.__custom_sort_key != None:
            self.__values.sort(
                reverse=not self.__descending,
                key=self.__custom_sort_key
            )
            return
        self.__values.sort(reverse=not self.__descending)

    def change_sort_key(self, key):
        if key == 'default':
            self.__custom_sort_key = None
            return
        self.__custom_sort_key = key

    def make_ascending(self):
        self.__descending = False
        self.__sort()

    def make_descending(self):
        self.__descending = True
        self.__sort()

    def insert(self, value):
        self.__values.append(value)
        self.__sort()

    def tail(self):
        return self.__values[len(self.__values)-1]

    def head(self):
        return self.__values[0]

    def pop(self):
        return self.__values.pop()

    def length(self):
        return len(self.__values)
