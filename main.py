import pygame

#@author Aaron Guyett
#@date 8/31/19
#@version .02

#Set screen size and display it
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

#Import background and planets
background = pygame.image.load('background.png')
planets = ['Earth.png', 'Jupiter.png', 'DPlanet.png']
p_index = 0
planet = pygame.image.load(planets[p_index])

#Define starting position and set the initial horizontal move direction
planet_x = 140
move_direction = 'right'

#Import spaceship and bullet images
spaceship = pygame.image.load('spaceship.png')
bullet = pygame.image.load('bullet.png')

#Define vertical bullet
bullet_y = 500
fired = False

#Define loop for the game and set the clock
run_game = True
clock = pygame.time.Clock()

#Start the game loop
while run_game:

  #Call the get_pressed function
  pygame.event.get()
  keys = pygame.key.get_pressed()

  #If the user presses space to fire
  if keys[pygame.K_SPACE] == True:
    fired = True

  #Control the movement of the bullet when fired
  if fired is True:
    bullet_y = bullet_y - 5
    if bullet_y == 50:
      fired == False
      bullet_y = 500
      
  #Import Images
  screen.blit(background, [0, 0])
  screen.blit(bullet, [180, bullet_y])
  screen.blit(spaceship, [160, 500])

  #Control movement of the planet
  if move_direction == 'right':
    planet_x = planet_x + 5
    if planet_x == 300:
      move_direction = 'left'
  else:
    planet_x = planet_x - 5
    if planet_x == 0:
      move_direction = 'right'

  screen.blit(planet, [planet_x, 50])

  #Control the collision of the bullet and the planet
  if bullet_y < 80 and planet_x > 120 and planet_x < 180:
    p_index = p_index + 1
    if p_index < len(planets):
      planet = pygame.image.load(planets[p_index])
      planet_x = 10
    else:
      print('YOU WIN')
      keep_alive = False

  #Update the display based on the clock
  pygame.display.update()
  clock.tick(60)