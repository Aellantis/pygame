from Lanes import lanes
from GameObject import GameObject
import pygame

# Player

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'images/cat_player.png')
    self.original_image = pygame.image.load('images/cat_player.png')
    self.flipped_image = pygame.transform.flip(self.original_image, True, False)
    self.surf = self.original_image  
    self.dx = 0
    self.dy = 0
    self.pos_x = 2
    self.pos_y = 2
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()
      self.surf= self.original_image

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()
      self.surf= self.flipped_image  

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[len(lanes) // 2] 
    self.y = 250  
    self.dx = self.x
    self.dy = self.y


  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]