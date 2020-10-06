import pygame
from game import Game

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))#, pygame.FULLSCREEN)
myfont = pygame.font.SysFont("monospace", 12)
clock = pygame.time.Clock()

# Initialize game variables
done = False
game = Game()
current_tile = (3,3)
<<<<<<< HEAD
effects = []
=======
>>>>>>> f314dcff790fc02ee1c0e057a4dc27f1714cabce

# tile vars
tile_colors = [(0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255)]
tile_offset = [280,530]
tile_size = [50,50]
<<<<<<< HEAD

def draw_game():
=======
mario = pygame.image.load('mario.jpg')

# Sprites
class Orb_sprite():
    def __init__(self):
        self.sprite_images = []
        self.frames = 6
        image = pygame.image.load('orbs_small.png')
        image = image.convert_alpha()
        spriteWidth = image.get_width() // self.frames
        spriteHeight = image.get_height()
        x = 0
        for i in range(self.frames):
            frameSurf = pygame.Surface((spriteWidth, spriteHeight), pygame.SRCALPHA, 32)
            frameSurf.blit(image, (x, 0))
            self.sprite_images.append(frameSurf.copy())
            x -= spriteWidth
        self.anim_count = 0
        self.anim_frame = 0

    def update(self):
        self.anim_count += 1
        if self.anim_count >= 7:
            self.anim_count = 0
            self.anim_frame = (self.anim_frame + 1) % self.frames

    def get_current_image(self):
        return self.sprite_images[self.anim_frame]

orb_sprite = Orb_sprite()

def draw_game():
    orb_sprite.update()

>>>>>>> f314dcff790fc02ee1c0e057a4dc27f1714cabce
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,800,600))
    if current_tile is not None:
        t = abs((pygame.time.get_ticks() % 512) - 256) % 256
        c = (t,t,t)
        pygame.draw.rect(screen, c, pygame.Rect(tile_offset[0] + current_tile[0]*tile_size[0] - 3, tile_offset[1] - (current_tile[1]+1)*tile_size[1] - 3, tile_size[0], tile_size[1]))
<<<<<<< HEAD
    screen.blit(myfont.render("{} points".format(game.points), 0, (255,255,255)), (50,50))
=======
>>>>>>> f314dcff790fc02ee1c0e057a4dc27f1714cabce
    for y in range(0,len(game.grid)):
        for x in range(0,len(game.grid[y])):
            if game.anim[x][y] > 0:
                game.anim[x][y] -= 1
                if game.anim[x][y] == 0:
<<<<<<< HEAD
                    dp = game.detect_matches(True)
                    if dp > 0:
                        effects.append(["+{}".format(dp), 100, cell_to_pixels(x,y)])
            pygame.draw.rect(screen, tile_colors[game.grid[x][y]], pygame.Rect(tile_offset[0] + x*tile_size[0], tile_offset[1] - (y+1)*tile_size[1] - game.anim[x][y], tile_size[0]-5, tile_size[1]-5))
    for e in effects:
        if e[1] > 0:
            e[1] -= 1
            pygame.draw.rect(screen, (200,200,200),pygame.Rect(e[2][0],e[2][1], 20,20))
            screen.blit(myfont.render(e[0], 0, (255,255,255)), (e[2][0],e[2][1]))
=======
                    game.detect_matches(True)
            if game.grid[x][y] == 1:
                screen.blit(mario, [tile_offset[0] + x*tile_size[0], tile_offset[1] - (y+1)*tile_size[1] - game.anim[x][y]])
            elif game.grid[x][y] == 4:
                screen.blit(orb_sprite.get_current_image(), [tile_offset[0] + x*tile_size[0] + 7, tile_offset[1] - (y+1)*tile_size[1] - game.anim[x][y] + 7])
            else:
                pygame.draw.rect(screen, tile_colors[game.grid[x][y]], pygame.Rect(tile_offset[0] + x*tile_size[0], tile_offset[1] - (y+1)*tile_size[1] - game.anim[x][y], tile_size[0]-5, tile_size[1]-5))
>>>>>>> f314dcff790fc02ee1c0e057a4dc27f1714cabce

def pixels_to_cell(x,y):
    x1 = int((x - tile_offset[0])/tile_size[0])
    y1 = int((-y + tile_offset[1])/tile_size[1])
    return x1,y1

def cell_to_pixels(x,y):
    x1 = int(tile_offset[0] + x * tile_size[0])
    y1 = int(tile_offset[1] - y * tile_size[1])
    return x1,y1

def output_logic(tilstand):
    if tilstand == 1:
        draw_game()
    elif tilstand == 0:
        draw_menu()
<<<<<<< HEAD
    elif tilstand == -1:
        draw_splash()

def draw_menu():
    s = pygame.Surface((200,200))
    s.blit(pygame.Rect(0,0,200,200), (0,0,200,200))
    s.blit(myfont.render("Tryk p for at fortsætte", 0, (255,255,255)), (30,170))


tilstand = 0
=======

def draw_menu():
    pass

tilstand = 1

if not pygame.mixer.get_init():
    pygame.mixer.init()
>>>>>>> f314dcff790fc02ee1c0e057a4dc27f1714cabce

#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if tilstand == 0:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                tilstand = 1
        elif tilstand == 1:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                tilstand = 0



        #Håndtering af input fra mus
<<<<<<< HEAD
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_cell, y_cell = pixels_to_cell(pos[0],pos[1])
            print(pos, cell_to_pixels(x_cell,y_cell))
            if 0 <= x_cell < len(game.grid) and 0 <= y_cell < len(game.grid[0]):
                if current_tile is None:
                    current_tile = (x_cell, y_cell)
                else:
                    game.swap_tiles(x_cell, y_cell, current_tile[0], current_tile[1])

                    #Når der er byttet brikker, kan vi kontrollere om der er lavet et match
                    dp = game.detect_matches()
                    if dp > 0:
                        effects.append(["+{}".format(dp), 100, cell_to_pixels(current_tile[0], current_tile[1])])
                    current_tile = None
=======
        if tilstand == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x_cell, y_cell = pixels_to_cell(pos[0],pos[1])
                print(pos, cell_to_pixels(x_cell,y_cell))
                if 0 <= x_cell < len(game.grid) and 0 <= y_cell < len(game.grid[0]):
                    if current_tile is None:
                        current_tile = (x_cell, y_cell)
                    else:
                        game.swap_tiles(x_cell, y_cell, current_tile[0], current_tile[1])

                        #Når der er byttet brikker, kan vi kontrollere om der er lavet et match
                        game.detect_matches()
                        current_tile = None
>>>>>>> f314dcff790fc02ee1c0e057a4dc27f1714cabce

    output_logic(tilstand)

    #pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.flip()
    clock.tick(60)
