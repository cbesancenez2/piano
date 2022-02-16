class SimpleController(Controller):

    def __init__(self, num_lights, color_on, color_off):
        super().__init__(self,num_lights)
        self.color_on = color_on
        self.color_off = color_off
