class Computer:
    def __init__(self, gpu):
       self.gpu = gpu

    def show_gpu_name(self):
        print(f"You have{self.guru} GPU processor")

class Mobile:
    def __init__(self, has_flash, model):
        self.has_flash = has_flash
        self.model = model

m1 = Mobile(has_flash = True, model = 'iphone')
m1.show_gpu_name()