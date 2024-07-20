import pygame
import random

from stack import Stack


pygame.init()
pygame.display.set_caption("Tower of Hanoi")
WIDTH,HEIGHT = 1200,600


SKYBLUE = (46,191,255)
BLUE = (11, 156,218)
BLUE2 = (0,115,164)


class Hanoi:
    def __init__(self, screen, towers=3, rings=0):
        self.screen = screen
        self.towersList = Stack()
        for i in range(towers):
            rect = pygame.Rect(i*WIDTH//towers+WIDTH/towers/2/2, 50, WIDTH/towers/2,HEIGHT)
            tower = Tower(self.screen, rect, SKYBLUE, Stack(), number_of_rings=rings)
            self.towersList.insert(tower)
        
        self.starting = Stack()
        for i in range(rings,0,-1):
            ring = Ring(i, self.randomColor(), self.screen, self.towersList.index(0), rings)
            self.starting.insert(ring)
        self.towersList.index(0).stacks = self.starting.copy()
        self.towersList.index(0).starting = True
        self.selected = None
    @staticmethod
    def randomColor():
        return (random.randint(155,255),random.randint(155,255),random.randint(155,255))
    def update(self):
        for tower in self.towersList:
            if tower.data.rect.collidepoint(pygame.mouse.get_pos()):
                tower.data.color = BLUE
            else:
                tower.data.color = SKYBLUE
            if tower.data == self.selected:
                tower.data.color = BLUE2
            tower.data.update()
    def event(self, event):
        for tower in self.towersList:
            if event.type == pygame.MOUSEBUTTONUP and tower.data.rect.collidepoint(pygame.mouse.get_pos()) and self.selected == None and tower.data.stacks.length() != 0:
                self.selected = tower.data
            elif event.type == pygame.MOUSEBUTTONUP and tower.data.rect.collidepoint(pygame.mouse.get_pos()) and self.selected != None and self.selected != tower.data:
                if tower.data.stacks.length() == 0:
                    ring = self.selected.stacks.pop()
                    ring.tower = tower.data
                    tower.data.stacks.insert(ring)
                elif self.selected.stacks.getLast().value < tower.data.stacks.getLast().value:
                    ring = self.selected.stacks.pop()
                    ring.tower = tower.data
                    tower.data.stacks.insert(ring)
                
                if tower.data.starting != True:
                    print(tower.data.stacks == self.starting)
                
                self.starting.show('value')
                tower.data.stacks.show('value')
                self.selected = None

class Tower:
    def __init__(self, screen, rect, color, stack=Stack(), number_of_rings=0):
        self.screen = screen
        self.color = color
        self.stacks = stack
        self.rect = pygame.Rect(rect)
        self.number_of_rings = number_of_rings
        self.starting = False

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        for ring in self.stacks:
            ring.data.update()
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
        level =  self.tower.rect.h - (self.tower.stacks.getIndex(self)+1) * self.y_divider
        ring_width = self.value * self.x_divider
        ring_height = self.y_divider-10
        self.rect = pygame.Rect(width_mid, level, ring_width, ring_height)
        self.draw()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.hanoi = Hanoi(self.screen,towers=3, rings=4)

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