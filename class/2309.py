class Counter():
    __hidden_counter = 0
    def count(self):
        self.__hiden_counter += 1
    def counter_to_zero(self):
        self.__hidden_counter = 0
    def get(self):
        return self.__hidden_counter
    def set(self,n):
        self.__hidden_counter = n
c = Counter()
c.count()
print(c.get())