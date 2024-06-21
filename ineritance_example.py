class Computer:
    def __init__(self, gpu):
        self.gpu = gpu
    def show_gpu_name(self):
        print(f"You have {self.gpu} GPU processor")

class Mobile(Computer):
    def __init__(self, has_flash, model, gpu):
        self.has_flash = has_flash
        self.model = model
        super().__init__(gpu = gpu)

m1 = Mobile(has_flash = True, model = 'iphone', gpu = 'M1')
m1.show_gpu_name()