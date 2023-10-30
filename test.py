import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 50), (90, 50), (80, 50)]
        self.direction = "RIGHT"

    def move(self, food_pos):
        # Move the snake
        new_head = self.get_new_head()
        self.body.insert(0, new_head)

        # Check for collisions
        if self.check_collision(food_pos):
            return True
        else:
            self.body.pop()
            return False

    def change_direction(self, new_direction):
        if new_direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if new_direction == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if new_direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if new_direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def get_new_head(self):
        # Calculate new head position based on the current direction
        if self.direction == "RIGHT":
            new_head = (self.body[0][0] + 10, self.body[0][1])
        if self.direction == "LEFT":
            new_head = (self.body[0][0] - 10, self.body[0][1])
        if self.direction == "UP":
            new_head = (self.body[0][0], self.body[0][1] - 10)
        if self.direction == "DOWN":
            new_head = (self.body[0][0], self.body[0][1] + 10)
        return new_head

    def check_collision(self, food_pos):
        # Check if the snake collides with itself or the boundaries
        if (
            self.body[0] in self.body[1:]
            or self.body[0][0] < 0
            or self.body[0][0] >= screen_width
            or self.body[0][1] < 0
            or self.body[0][1] >= screen_height
        ):
            return True
        # Check if the snake eats the food
        if self.body[0] == food_pos:
            return True
        return False

# Define the Food class
class Food:
    def __init__(self):
        self.position = (random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10)

    def spawn_food(self):
        self.position = (random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10)
        return self.position

# Create the Snake and Food instances
snake = Snake()
food = Food()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            if event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            if event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            if event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    food_pos = food.position
    game_over = snake.move(food_pos)

    if game_over:
        break

    screen.fill(black)
    for pos in snake.body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    pygame.display.update()

    pygame.time.Clock().tick(15)

# Game over
pygame.quit()
quit()
