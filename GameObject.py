import pygame

# Game Object
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
    self.dx = 0
    self.dy = 0
    self.rect = self.surf.get_rect()

  def move(self):
    self.x += self.dx
    self.y += self.dy

  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
    screen.blit(self.surf, (self.x, self.y))
