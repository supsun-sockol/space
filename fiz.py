class object:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def tick(self):
        self.x = self.x+self.vx
        self.y = self.y+self.vy
    def print(self):
        print(self.x, self.y, self.vx, self.vy)



apple = object(247, 458, 34, -12)


for i in range(100):
    apple.tick()
    apple.print()
