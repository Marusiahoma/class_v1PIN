class Button:
    def __init__(self):
        self.clc = 0

    def click(self, n):
        self.clc += n

    def click_count(self):
        return self.clc

    def reset(self):
        self.clc = 0
