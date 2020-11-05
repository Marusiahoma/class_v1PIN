class Button:
    def click(self):
        self.clc += 1

    def click_count(self):
        return self.clc

    def reset(self):
        self.clc = 0
