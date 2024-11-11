import pygame
from random import randint, choice
pygame.init()
pygame.mixer.init()

meow_sound = pygame.mixer.Sound("audio/meow.mp3")
bark_sound = pygame.mixer.Sound("audio/bark.mp3")

lives = 3

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Lanes
lanes = [50, 150, 250, 350, 400]  

# Load the background image
background = pygame.image.load('images/background.jpg') 
background = pygame.transform.scale(background, (500, 500))


# ----------------------------------------------
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

# ----------------------------------------------
class Fish(GameObject):
  def __init__(self):
    super(Fish, self).__init__(0, 0, 'images/fish.png')
    self.original_image = pygame.image.load('images/fish.png')
    self.flipped_image = pygame.transform.flip(self.original_image, True, False)  # Flip horizontally
    self.surf = self.original_image  
    self.dx = 0 
    self.dy = 0  
    self.reset()

  def move(self):
    super().move()
    if self.dy > 0: 
      self.surf = self.flipped_image
    else:  
      self.surf = self.original_image

    if self.y > 500 or self.y < -64: 
      self.reset()

  def reset(self):
    self.x = choice(lanes)
    direction = randint(0, 1) 
    
    if direction == 0: 
      self.y = 500  
      self.dy = -((randint(0, 200) / 100) + 1)  
    else: 
      self.y = -64 
      self.dy = (randint(0, 200) / 100) + 1  
    
    self.surf = self.original_image 
# ----------------------------------------------
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
class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'images/doggo_enemy.png')
    self.original_image = pygame.image.load('images/doggo_enemy.png')
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

# -------------------------------------------
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
# ---------------------------------------
def display_lives(screen, lives):
    for i in range(lives):
        screen.blit(pygame.image.load('images/lives.png'), (480 - (i + 1) * 40, 10))  # Adjust the position if needed

# Making Groups
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

# Make 'Fruit' instances
fish = Fish()
milk = Milk()
fruit_sprites.add(fish)
fruit_sprites.add(milk)

# Instance of Player
player = Player()

# Make bomb
bomb = Bomb()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(fish)
all_sprites.add(milk)
all_sprites.add(bomb)

# Get the clock
clock = pygame.time.Clock()


# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()

  # Clear screen and draw background
  screen.blit(background, (0, 0))  

  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)

  
  # Displaying lives
  display_lives(screen, lives)

  # Check Colisions
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    meow_sound.play()  
    fruit.reset()

  # Check collision player and bomb
  if pygame.sprite.collide_rect(player, bomb):
    bark_sound.play() 
    player.reset() 
    bomb.reset()  
    lives -=1
    if (lives <= 0):
      pygame.quit()

  # Update the window
  pygame.display.flip()

  # tick the clock!
  clock.tick(30)
