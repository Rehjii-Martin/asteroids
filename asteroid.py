from circleshape import *
from constants import *
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            vec_1 = self.velocity.rotate(random.uniform(20, 50))
            vec_2 = self.velocity.rotate(random.uniform(-20, -50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_1.velocity = vec_1 * 1.2
            split_2.velocity = vec_2