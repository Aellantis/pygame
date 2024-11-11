import pygame
from random import randint, choice
from GameObject import GameObject
from Lanes import lanes

# Milk
class Milk(GameObject):
  def __init__(self):
    super(Milk, self).__init__(0, 0, 'images/milk.png')
    self.original_image = pygame.image.load('images/milk.png')
    self.flipped_image = pygame.transform.flip(self.original_image, True, False)  # Flip horizontally
    self.surf = self.original_image 
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    super().move()
    if self.x > 500 or self.x < -64:
        self.reset()

  def reset(self):
    if randint(0, 1) == 0:
      self.x = -64
      self.dx = (randint(0, 200) / 100) + 1 
      self.surf = self.original_image 
    else:
      self.x = 500
      self.dx = ((randint(0, 200) / 100) + 1) * -1 
      self.surf = self.flipped_image 
    self.y = choice(lanes)
# -------------------------------------------