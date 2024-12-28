import pygame
import random
from circleshape import CircleShape
from constants import *
import pygame
class Asteroid(CircleShape):
    

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(random.uniform(-1,1), random.uniform(-1,1)).normalize() * ASTEROID_SPEED

    def update(self,dt):
        self.position += self.velocity * dt

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)),self.radius, 2)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)

        new_velocity1 = self.velocity.rotate(random_angle)*1.2
        new_velocity2 = self.velocity.rotate(-random_angle)*1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = new_velocity1
        new_asteroid2.velocity = new_velocity2

        for container in self.containers:
            container.add(new_asteroid1)
            container.add(new_asteroid2)

    def set_velocity(self,vx,vy):
        self.velocity = pygame.Vector2(vx, vy)