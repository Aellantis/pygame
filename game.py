import pygame
from random import randint, choice
from files.Confusion import Explosion
from files.Bomb import Bomb
from files.Fish import Fish
from files.Milk import Milk
from files.Player import Player
from files.Sparkle import Sparkle
from files.Yarn import Yarn
from files.ScoreBoard import ScoreBoard
from files.Points import PointsSprite

pygame.init()
pygame.mixer.init()

meow_sound = pygame.mixer.Sound("audio/meow.mp3")
bark_sound = pygame.mixer.Sound("audio/bark.mp3")
confused_dog_sound = pygame.mixer.Sound("audio/confused_dog.mp3")
sparkle_sound = pygame.mixer.Sound("audio/sparkle.mp3")

lives = 3

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Load the background image
background = pygame.image.load('images/background.jpg') 
background = pygame.transform.scale(background, (500, 500))
# ----------------------------------------------
def display_lives(screen, lives):
    for i in range(lives):
        screen.blit(pygame.image.load('images/lives.png'), (480 - (i + 1) * 40, 10))  # Adjust the position if needed

# Making Groups
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
explosion_sprites = pygame.sprite.Group()
yarn_sprite = pygame.sprite.Group()

# Make Fruit instances
for n in range(1, 2):
  fish = Fish()
  milk = Milk()
  yarn = Yarn()
  fruit_sprites.add(fish)
  fruit_sprites.add(milk)
  yarn_sprite.add(yarn)
  all_sprites.add(fish)
  all_sprites.add(milk)
  all_sprites.add(yarn)

    

# Instance of Player
player = Player()

# Make bomb
bomb = Bomb()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(bomb)

# Score
score = ScoreBoard(30, 30, 0)
all_sprites.add(score)

# Get the clock
clock = pygame.time.Clock()

def make_explosion(x, y):
  explosion = Explosion(x, y)
  explosion_sprites.add(explosion)

def make_pop(x, y):
  explosion = Sparkle(x, y)
  explosion_sprites.add(explosion)

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
        
# Check for the stun event (when the timer finishes)
    if event.type == pygame.USEREVENT:
        player.un_stun()  
        pygame.time.set_timer(pygame.USEREVENT, 0)  

  # Clear screen and draw background
  screen.blit(background, (0, 0))  

  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
    if entity != player: 
      pass

  # Displaying lives
  display_lives(screen, lives)

  # Check Colisions
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    make_pop(fruit.x, fruit.y)
    meow_sound.play()  
    points = PointsSprite(fruit.x, fruit.y, 100)
    score.update(50)
    all_sprites.add(points)
    fruit.reset()

  yarn = pygame.sprite.spritecollideany(player, yarn_sprite)
  if yarn: 
    make_pop(yarn.x, yarn.y)
    points = PointsSprite(yarn.x, yarn.y, 100)
    score.update(100)
    all_sprites.add(points)
    sparkle_sound.play()
    player.stun()
    yarn.reset()

# Fruit bomb collisions
  fruit = pygame.sprite.spritecollideany(bomb, fruit_sprites)
  if fruit:
    make_explosion(fruit.x, fruit.y)
    confused_dog_sound.play()
    points = PointsSprite(fruit.x, fruit.y, 100)
    score.update(-25)
    all_sprites.add(points)
    fruit.reset()

  fruit = pygame.sprite.spritecollideany(bomb, yarn_sprite)
  if fruit:
    make_explosion(fruit.x, fruit.y)
    confused_dog_sound.play()
    points = PointsSprite(fruit.x, fruit.y, 100)
    score.update(-75)
    all_sprites.add(points)
    fruit.reset()

  # Check collision player and bomb
  if pygame.sprite.collide_rect(player, bomb):
    bark_sound.play() 
    player.reset() 
    bomb.reset()  
    lives -=1
    if (lives <= 0):
      pygame.quit()

  # Animate the explosions
  for explosion in explosion_sprites:
    explosion.render(screen)
    if explosion.playing == False: 
      explosion.kill()

  # Update the window
  pygame.display.flip()

  # Tick the clock!
  clock.tick(30)
