import pygame
from random import randint
from Linked_list import DLElem
from Linked_list import DLList

#Forklar hvordan der gives point i spillet, og tegn et tilstandsdiagram over variablen "state"
#Udvid programmet, så der tegnes en linjes tekst på skærmen, der viser hvor mange points man fik sidste gang man klikkede med musen
#Hvordan kunne spillet ellers udvides? Giv et par eksempler, og lav evt. en demo.


# Setup pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
myfont = pygame.font.SysFont("monospace", 12)
clock = pygame.time.Clock()


def draw_game():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,800,600))
    #pygame.draw.circle(screen, (200,200,50), (cx,cy), radius)
    #screen.blit(myfont.render("{} points".format(points), 0, (255,255,255)), (50,50))
    e = circle_list.head
    if e != None:
        while e.next != None:
            pygame.draw.circle(screen, (50,200,50), (e.key[0],e.key[1]), e.key[2])
            e = e.next
        pygame.draw.circle(screen, (50,200,50), (e.key[0],e.key[1]), e.key[2])

points = 0

circle_list = DLList(None)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        #Håndtering af input fra mus
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            c = DLElem([pos[0],pos[1],randint(10,200)])
            circle_list.insert(c)

    #Opdater radius
    if circle_list.head != None:
        e = circle_list.head
        while e.next != None:
            e.key[2] -= 1
            e = e.next
        e.key[2] -= 1
        #Remove negatives
        e = circle_list.head
        while e.next != None:
            if e.key[2] <= 0:
                circle_list.delete(e)
            e = e.next
        if e.key[2] <= 0:
            circle_list.delete(e)

    #if randint(1,50) < 2:
    #for i in range(3):
#        x = randint(100,700)
#        y = randint(100,500)
#        r = randint(20,50)
#        circle_list.insert(DLElem([x,y,r]))

    draw_game()

    pygame.display.flip()
    clock.tick(60)
