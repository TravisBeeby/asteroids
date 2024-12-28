import pygame
from circleshape import CircleShape 
from constants import *
from shot import Shot

class Player(CircleShape): 
    def __init__(self, name, x, y): 
        super().__init__(x, y, PLAYER_RADIUS) # Initialize the CircleShape part 
        self.name = name 
        self.rotation = 0
        self.velocity = pygame.Vector2(0,0)
        self.shoot_cooldown = 0
        
    def display_info(self): 
        print(f"Player Name: {self.name}") 
        print(f"Radius: {self.radius}") 
        print(f"Area: {self.area()}")
        print(f"Position: ({self.position.x}, {self.position.y})")
        print(f"Rotation: {self.rotation}")

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot()
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        movement = forward * PLAYER_SPEED * dt
        self.position += movement

    # in the player class
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0,-1).rotate(self.rotation)
        shot.set_velocity(direction.x * 300, direction.y * 300)
        for container in self.containers:
            container.add(shot)
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation) 
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 
      a = pygame.Vector2(self.position.x, self.position.y) + forward * self.radius 
      b = pygame.Vector2(self.position.x, self.position.y) - forward * self.radius - right 
      c = pygame.Vector2(self.position.x, self.position.y) - forward * self.radius + right 
      return [a, b, c]
    
    def draw(self, screen): 
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle())