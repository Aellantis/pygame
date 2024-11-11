import pygame

# ----------------------------------------------
# Sequence image 

class SequenceImage():
  def __init__(self, image, duration):
    self.surf = pygame.image.load(image)
    self.duration = duration

  def get_rect(self):
    return self.surf.get_rect()

# ----------------------------------------------
# Game Object

class Animation(pygame.sprite.Sprite):
  def __init__(self, x, y, sequence):
    super(Animation, self).__init__()
    self.x = x
    self.y = y
    self.images = []
    self.init(sequence)
    self.next_image_count = 0
    self.index = 0
    self.rect = self.get_current_image().get_rect()
    self.play_mode = 'loop'
    self.playing = True

  def get_current_image(self):
    return self.images[self.index]

  def init(self, sequence):
    for image in sequence:
      self.images.append(SequenceImage(image[0], image[1]))

  def next_frame(self):
    self.index += 1
    if self.index == len(self.images):
      if self.play_mode == 'loop':
        self.reset_index()
      else:
        self.index = len(self.images) - 1
        self.playing = False

  def reset_index(self):
    self.index = 0

  def render(self, screen):
    self.next_image_count += 1
    if self.next_image_count >= self.images[self.index].duration: 
      self.next_image_count = 0
      self.next_frame()
    self.rect.x = self.x
    self.rect.y = self.y
    screen.blit(self.get_current_image().surf, (self.x, self.y))