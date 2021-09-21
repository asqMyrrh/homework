class Field():
    __pos_hare = 0
    __pos_tort = 0
    def __init__(self, n, m, x):
        if n <= m:
            print("нееее, не прокатит")
            return
        self.__step_hare = n
        self.__step_tort = m
        self.__length = x
    def get_pos_hare(self):
        return self.__pos_hare
    def get_pos_tort(self):
        return self.__pos_tort
    def get_age(self):
        return self.__age
    def step(self):
        hare_new_pos = self.__pos_hare + self.__step_hare
        if hare_new_pos > self.__length:
            hare_new_pos -= self.__length
        self.__pos_hare = hare_new_pos
        
        tort_new_pos = self.__pos_tort + self.__step_tort
        if tort_new_pos > self.__length:
            tort_new_pos -= self.__length
        self.__pos_tort = tort_new_pos
f = Field(5, 2, 11)
i = 0
first_meet = 0
while (i < 100):
    f.step()
    i += 1
    if f.get_pos_hare() ==f.get_pos_tort():
        print("oh, shit, here we go again...", i - first_meet)
        first_meet = i
    