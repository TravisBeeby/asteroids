from circleshape import CircleShape 
from constants import PLAYER_RADIUS
class Player(CircleShape): 
    def __init__(self, name, x, y): 
        super().__init__(PLAYER_RADIUS) # Initialize the CircleShape part 
        self.name = name 
        self.x = x
        self.y = y
        self.rotation = 0
        
    def display_info(self): 
        print(f"Player Name: {self.name}") 
        print(f"Radius: {self.radius}") 
        print(f"Area: {self.area()}")
        print(f"Position: ({self.x}, {self.y})")
        print(f"Rotation: {self.rotation}")

    # in the player class
    def triangle(self):
       forward = pygame.Vector2(0, 1).rotate(self.rotation)
       right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
       a = self.position + forward * self.radius
       b = self.position - forward * self.radius - right
       c = self.position - forward * self.radius + right
       return [a, b, c]