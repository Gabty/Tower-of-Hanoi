import pygame
import random


pygame.init()
pygame.display.set_caption("Tower of Hanoi")
WIDTH,HEIGHT = 1200,600


SKYBLUE = (46,191,255)
BLUE = (11, 156,218)
BLUE2 = (0,115,164)


class Hanoi:
    def __init__(self, screen, towers=3, rings=0):
        self.screen = screen
        self.towersList = []
        for i in range(towers):
            rect = pygame.Rect(i*WIDTH//towers+WIDTH/towers/2/2, 50, WIDTH/towers/2,HEIGHT)
            tower = Tower(self.screen, rect, SKYBLUE,[], number_of_rings=rings)
            self.towersList.append(tower)
        
        self.starting = [Ring(i, self.randomColor(), self.screen, self.towersList[0], rings) for i in range(rings,0,-1)]
        self.towersList[0].stacks = self.starting.copy()
        self.towersList[0].starting = True
        self.selected = None
    @staticmethod
    def randomColor():
        return (random.randint(155,255),random.randint(155,255),random.randint(155,255))
    def update(self):
        for tower in self.towersList:
            if tower.rect.collidepoint(pygame.mouse.get_pos()):
                tower.color = BLUE
            else:
                tower.color = SKYBLUE
            if tower == self.selected:
                tower.color = BLUE2
            tower.update()
    def event(self, event):
        for tower in self.towersList:
            if event.type == pygame.MOUSEBUTTONUP and tower.rect.collidepoint(pygame.mouse.get_pos()) and self.selected == None and len(tower.stacks) != 0:
                self.selected = tower
            
            elif event.type == pygame.MOUSEBUTTONUP and tower.rect.collidepoint(pygame.mouse.get_pos()) and self.selected != None and self.selected != tower:
                if len(tower.stacks) == 0:
                    ring = self.selected.stacks.pop()
                    ring.tower = tower
                    tower.stacks.append(ring)
                elif self.selected.stacks[-1].value < tower.stacks[-1].value:
                    ring = self.selected.stacks.pop()
                    ring.tower = tower
                    tower.stacks.append(ring)
                
                if tower.starting != True:
                    print(tower.stacks == self.starting)
                self.selected = None

class Tower:
    def __init__(self, screen, rect, color, stack=[], number_of_rings=0):
        self.screen = screen
        self.color = color
        self.stacks = stack
        self.rect = pygame.Rect(rect)
        self.number_of_rings = number_of_rings
        self.starting = False

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        for ring in self.stacks:
            ring.update()
    def hover(self):
        self.color = (0,0,0)
class Ring:
    def __init__(self, value, color,screen, tower, rings=0):
        self.value = value
        self.color = color
        self.screen = screen
        self.tower = tower
        self.rings = rings

        self.x_divider = self.tower.rect.w /self.rings
        self.y_divider = self.tower.rect.h /(self.rings+1)
        self.font = pygame.font.Font(None, 50)
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text=self.font.render(str(self.value), True, (0,0,0))
        self.screen.blit(text, (self.rect.centerx-text.get_width()//2, self.rect.centery-text.get_height()//2))
    
    def update(self):
        width_mid = self.tower.rect.centerx - (self.value*self.x_divider)/2
        level =  self.tower.rect.h - (self.tower.stacks.index(self)+1) * self.y_divider
        ring_width = self.value * self.x_divider
        ring_height = self.y_divider-10
        self.rect = pygame.Rect(width_mid, level, ring_width, ring_height)
        self.draw()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hanoi = Hanoi(self.screen,towers=10, rings=8)

    def mainloop(self):
        run = True
        while run:
            self.screen.fill((255,255,255))
            self.hanoi.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.hanoi.event(event)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.mainloop()