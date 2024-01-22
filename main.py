import pygame
from random import randrange

# Introducing all variables
window = 1 #variable for window size
tile_size = 20 #
range = (tile_size // 2, window - tile_size // 2, tile_size) #creates the rangefor where you'll randomly start
get_random_position = lambda:[randrange(*range), randrange(*range)]  # Generating a random position for anything
snake = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2]) #creates the snake
snake.center = get_random_position() 
length = 1 #beginning length of the snake
segments = [snake.copy()] 
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position() # randomizing food random
screen = pygame.display.set_mode([window] * 2) # displaying screen
clock = pygame.time.Clock() # setting a time/clock
dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1} # dirs is the controls, we are using WASD on the keyboardto move our snake
score = 0

# Creating a score text on window
label = Label(window, text="Score:{}".format(score), font=('ariel', 35), fill='white')
label.pack()

#controls of the snake
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			#controls for snake to go up with w
			if event.key == pygame.K_w and dirs[pygame.K_w]:
				snake_dir = (0, -tile_size)
				dirs = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}
			#controls for snake to go right with d
			if event.key == pygame.K_s and dirs[pygame.K_s]:
				snake_dir = (0, tile_size)
				dirs = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
			#controls for snake to go left with wa
			if event.key == pygame.K_a and dirs[pygame.K_a]:
				snake_dir = (-tile_size, 0)
				dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}
			#controls for snake to go down with d
			if event.key == pygame.K_d and dirs[pygame.K_d]:
				snake_dir = (tile_size, 0)
				dirs = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}
 
	screen.fill('black')
	# check borders and selfeating
	self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1 # making the snake not allowed to hit it's own body or else it restarts
	if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eating: # setting the tiles for selfeating
		snake.center, food.center = get_random_position(), get_random_position()
		length, snake_dir = 1, (0, 0) # setting the length of the amount of tiles you move when using WASD controls
		segments = [snake.copy()]
	# randomizing where the food spawns each time
	if snake.center == food.center: # randomizes food using the randomizing snake
		food.center = get_random_position() # setting food to equal random area
		length += 1 # making the food one tile in length
	# food
	pygame.draw.rect(screen, 'red', food) # creating food as a red rectangle
	# snake
	[pygame.draw.rect(screen, 'green', segment) for segment in segments] # creating the snake as a green rectangle
	# move snake
	time_now = pygame.time.get_ticks()
	if time_now - time > time_step:
		time = time_now
		snake.move_ip(snake_dir)
		segments.append(snake.copy())
		segments = segments[-length:]
	pygame.display.flip()
	clock.tick(60) # making a timer for 60 seconds in the game
