class OddEvenSeparator:
    def __init__(self):
        self.odd = []
        self.up = []
        self.over = []

    def add_number(self, n):
        self.odd.append(n)

    def even(self):
        for i in range(len(self.odd)):
            if i % 2 == 0:
                self.up.append(i)
        return self.up

    def odd(self):
        for i in range(len(self.odd)):
            if i % 2 != 0:
                self.over.append(i)
        return self.over
