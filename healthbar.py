def __init__(self):
    self.current_health=200
    self.maximum_health=1000
    self.health_bar_lenght=400
    self.health_ratio=self.maximum_health/self.health_bar_lenght
def update(self):
    pass
def get_damage(self,amount):
    if self.current_health>0:
        self.current_health-=amount
    if self.current.health<=0:
        self.current_health=0
def basic_health(self):
    pygame.graw.rect(win,(255,0,0),(10,10,self.current_health,25))