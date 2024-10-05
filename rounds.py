class Cartridge:
    def __init__(self, is_live):
        self.is_live = is_live

    def show_cartridge_specs(self):
        print(str(self.is_live))
