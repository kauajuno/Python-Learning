from animal import Animal


class Snake(Animal):
    def __init__(self, entry):
        super().__init__(entry)
        self.skin = "green"

    def bite(self):
        print("Nhac!")
