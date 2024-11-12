import pygame
from files.GameObject import GameObject
from random import randint, choice
from files.Lanes import lanes

class Yarn(GameObject):
  def __init__(self):
    super(Yarn, self).__init__(0, 0, 'images/yarn.png')
    self.original_image = pygame.image.load('images/yarn.png')
    self.flipped_image = pygame.transform.flip(self.original_image, True, False)
    self.surf = self.original_image  
    self.dx = 0
    self.dy = 0
    self.reset()

  def move(self):
    super().move()
    if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
      self.reset()

  def reset(self):
    direction = randint(1, 4)
    if direction == 1:  # left
      self.x = -64
      self.y = choice(lanes)
      self.dx = (randint(0, 200) / 100) + 1
      self.dy = 0
      self.surf = self.original_image  

    elif direction == 2:  # right
      self.x = 500
      self.y = choice(lanes)
      self.dx = ((randint(0, 200) / 100) + 1) * -1
      self.dy = 0
      self.surf = self.flipped_image  

    elif direction == 3:  # down
      self.x = choice(lanes)
      self.y = -64
      self.dx = 0
      self.dy = (randint(0, 200) / 100) + 1
      self.surf = self.original_image  

    else:  # up
      self.x = choice(lanes)
      self.y = 500
      self.dx = 0
      self.dy = ((randint(0, 200) / 100) + 1) * -1
      self.surf = self.flipped_image 
