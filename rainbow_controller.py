class RainbowController(Controller):

    def __init__(self, num_lights):
       super().__init__(self,num_lights)
        self.color_on = (255,255,255)
        self.color_off = (0,0,0)


    def process_event(self, event):
        super().process_event(self,event)
        self.color_off = self.color_on
        if self.next_light % (self.num_lights * 2) == 0:
            self.next_light = 0

        # pick the next color to turn on
        self.color_on = wheel(self.next_light * 256 // self.num_lights )

        # Only turn on one light for a chord
        if deltatime < 0.02:
            print('chord')
            return

##Funtion that makes each light a different rainbow color
def wheel(pos):
    if pos<0 or pos > 255:
        red = green = blue = 0
    elif pos<85:
        red = int(pos*3)
        green = int(255-pos*3)
        blue =0
    elif pos<170:
        pos -=85
        red = int(255 -pos*3)
        green = 0
        blue = int(pos*3)
    else:
        pos-= 170
        red = 0
        green = int(pos*3)
        blue = int(255-pos*3)
    return (red,green,blue)
