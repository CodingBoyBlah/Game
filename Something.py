import pygame, math

yellow = 245, 242, 86

screen_width = 600
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Clicker")
font = pygame.font.SysFont('Calibri', 35)

class Circle(object):
    def __init__(self):
        self.c_size = 40
        self.width = self.c_size * 2
        self.height = self.c_size * 2
        self.shape = pygame.Surface([self.width, self.height])
        self.shape.fill(yellow)
        self.rect = self.shape.get_rect()
        self.center_point = (0, 0)


    def draw(self, win):
        self.center_point = (win.get_width()/2, win.get_height()/2)
        pygame.draw.circle(self.shape, (255,0,0), 
                           (self.width/2, self.height/2), 
                           self.c_size)
        win.blit(self.shape, (win.get_width()/2 - self.width/2, 
                              win.get_height()/2 -  self.height/2))
        # print(self.rect)

    def distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        dist = x*x + y*y
        dist = math.sqrt(dist)
        return dist

    def isWithinCircle(self, mouse_point):
        dist = self.distance(mouse_point, self.center_point)
        if(dist < self.c_size):
            return True
        else:
            return False

def display_score(text, font, win):
    x = win.get_width() - 50
    y = 50
    textFrame = font.render(text, True, (0, 0, 0))
    textRect = textFrame.get_rect()
    textRect.center = (x, y)
    win.blit(textFrame, textRect)


Clicks = 0
print(Clicks)

run = True
c = Circle()

while run:
    # pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if c.isWithinCircle(pygame.mouse.get_pos()):
                    Clicks += 1
                    print(Clicks)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False 

    # if keys[pygame.K_SPACE]:
    #     Clicks += 1
    #     print(Clicks)

    screen.fill(yellow)
    c.draw(screen)
    display_score(str(Clicks), font, screen)
    pygame.display.flip()
    # pygame.display.update()

pygame.quit()