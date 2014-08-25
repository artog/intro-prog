__author__ = 'Adam'

"""
 Show how to fire bullets.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/PpdJjaiLX6A
"""
import pygame
import random
import math

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)

screen_width = 700
screen_height = 400

# --- Classes

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    xMotion = 0
    yMotion = 0
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([20, 15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):

        self.rect.x += self.xMotion
        self.rect.y += self.yMotion

        if self.rect.x > screen_width:
            self.rect.x = 0

        if self.rect.x < 0:
            self.rect.x = screen_width

        if self.rect.y > screen_height:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = screen_height

class Player(pygame.sprite.Sprite):

    moving = False
    lat_moving = False

    angle = 0
    lat_move = 0

    position = [screen_width/2,screen_height/2]

    shooting = False
    previousShotTime = 0

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # self.source_image = pygame.Surface([20, 20])
        self.source_image = pygame.image.load('Assets/player.png')
        self.source_image.fill(RED)
        self.rect = self.source_image.get_rect()

    def update(self):

        rotated_image = pygame.transform.rotate(self.source_image, self.angle)

        new_rect = rotated_image.get_rect()

        self.position[0] += self.moving*2*math.sin(math.radians(self.angle))
        self.position[1] += self.moving*2*math.cos(math.radians(self.angle))

        self.position[0] += self.lat_move*2*math.sin(math.radians(self.angle-90))
        self.position[1] += self.lat_move*2*math.cos(math.radians(self.angle-90))

        new_rect.centerx = self.position[0]
        new_rect.centery = self.position[1]

        self.rect = new_rect
        self.image = rotated_image

    def shoot(self,bullet_list,all_sprites_list):

        bullet = Bullet(self.angle)

        # Set the bullet so it is where the player is
        bullet.position[0] = self.rect.centerx
        bullet.position[1] = self.rect.centery

        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)

class Bullet(pygame.sprite.Sprite):

    angle = 0
    position = [0.0,0.0]

    def __init__(self,angle=0):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([4, 4])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.angle = angle

    def update(self):
        """ Move the bullet. """
        modX = 5*math.sin(math.radians(self.angle))
        modY = 5*math.cos(math.radians(self.angle))
        print(self.position)
        self.position[0] -= modX
        self.position[1] -= modY
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]


# --- Create the window

# Initialize Pygame
pygame.init()


screen = pygame.display.set_mode([screen_width, screen_height])

# --- Sprite lists

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# List of each block in the game
block_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# --- Create the sprites
def makeBlock():
    i = random.randrange(4)
    # This represents a block
    block = Block((0,100+50*int(i/5),0))

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)

    if int(i) == 0:
        block.rect.x = 0
        block.xMotion = 1

    if int(i) == 1:
        block.rect.x = screen_width
        block.xMotion = -1

    if int(i) == 2:
        block.rect.y = 0
        block.yMotion = 1

    if int(i) == 3:
        block.rect.y = screen_height
        block.yMotion = -1

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

for i in range(20):
    makeBlock()

# Create a red player block
player = Player()
all_sprites_list.add(player)

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
player.rect.y = 0
player.rect.x = 0

gameOver = False

font = pygame.font.SysFont('Verdana',14)


# -------- Main Program Loop -----------
while not done:


    if len(pygame.sprite.spritecollide(player,block_list,False)) > 0 or gameOver:
        # done = True
        pass

    pos = pygame.mouse.get_pos()

    # vec = pygame.math.Vector2(
    # )

    angleRad = math.atan2(

        -(pos[0]-player.rect.centerx),
        -(pos[1]-player.rect.centery)
        # -vec.x,
        # -vec.y
    )

    angle = math.degrees(angleRad)
    player.angle = angle
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.shooting = True
        elif event.type == pygame.MOUSEBUTTONUP:
            player.shooting = False
        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                player.lat_move = 0

            if event.key == pygame.K_d:
                player.lat_move = 0


            if event.key == pygame.K_w:
                player.moving = 0
            if event.key == pygame.K_s:
                player.moving = 0

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                player.lat_move = 1

            if event.key == pygame.K_d:
                player.lat_move = -1

            if event.key == pygame.K_w:
                player.moving = -1
            if event.key == pygame.K_s:
                player.moving = 1

    # --- Game logic
    if player.shooting and player.previousShotTime+200 < pygame.time.get_ticks():
        print(player.previousShotTime)
        player.shoot(bullet_list,all_sprites_list)
        player.previousShotTime = pygame.time.get_ticks()
    # Call the update() method on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:

        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            makeBlock()
            if score % 10 == 0:
                makeBlock()

        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)




    # Clear the screen
    screen.fill(WHITE)

    scoreSurface = font.render("Score: "+str(score),True,BLACK)
    numBlocksSurface = font.render("Blocks: "+str(len(block_list)),True,BLACK)
    screen.blit(scoreSurface,(10, 10))
    screen.blit(numBlocksSurface,(screen_width-150,10))

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)

pygame.quit()
