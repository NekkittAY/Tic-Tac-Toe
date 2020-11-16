import pygame
import random
from os import path
class Move(pygame.sprite.Sprite):
    def __init__(self,x,y,player):
        pygame.sprite.Sprite.__init__(self)
        black = (0,0,0)
        self.x = x
        self.y = y
        if player == "O":
            self.image = pygame.transform.scale(O_img,((55,55)))
        elif player == "X":
            self.image = pygame.transform.scale(X_img,((55,55)))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    
class Line(pygame.sprite.Sprite):
    def __init__(self,pos,x,y):
        pygame.sprite.Sprite.__init__(self)
        if pos=="x":
            self.image=pygame.Surface((1,y))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        elif pos=="y":
            self.image=pygame.Surface((y,1))
            self.image.fill((0,0,0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            
class Cell(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.surface.Surface((60,60))
        self.image.fill((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y

def chek_win(board):
    global win
    global win1
    win = False
    win1 = False
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        win=True
        return win
    elif board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
        win=True
        return win
    elif board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
        win=True
        return win
    elif board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        win=True
        return win
    elif board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        win=True
        return win
    elif board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        win=True
        return win
    elif board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        win=True
        return win
    elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        win=True
        return win
        
    if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        win1=True
        return win1
    elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
        win1=True
        return win1
    elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        win1=True
        return win1
    elif board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
        win1=True
        return win1
    elif board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
        win1=True
        return win1
    elif board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
        win1=True
        return win1
    elif board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        win1=True
        return win1
    elif board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
        win1=True
        return win1

pygame.init()
screen=pygame.display.set_mode((1200,600))
running=True
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()
img_dir = path.join(path.dirname(__file__),'tic_tac_toe')
X_img = pygame.image.load(path.join(img_dir,'X.png')).convert()
O_img = pygame.image.load(path.join(img_dir,'O.png')).convert()
players = pygame.sprite.Group()
board = []
for k in range(0,3):
    board1 = []
    for l in range(0,3):
        board1.append("#")
    board.append(board1)
print(board)
x=540
y=240
for i in range(0,3):
    for j in range(0,3):
        cell=Cell(x+60*i,y+60*j)
        all_sprites.add(cell)
q = 30
w = 30
for n in range(0,2):
    line = Line("y",x+q,y+q)
    all_sprites.add(line)
    q*=3
for m in range(0,2):
    line1 = Line("x",x+w,y+w)
    all_sprites.add(line1)
    w*=3    
hod=0     
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if chek_win(board)==True:
            running=False
            if win==True:
                print("player1 won, Game Over")
            else:
                print("player2 won, Game Over")
        if hod==9:
            if win==True or win1==True:
                pass
            else:
                running=False
                print("draw, Game Over")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if hod%2==0:
                    player = "X"
                else:
                    player = "O"
                x,y = pygame.mouse.get_pos()
                if x>=510 and x<=570 and y<=270:
                    if board[0][0] == "X" or board[0][0] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 540
                    y = 240
                    board[0][0] = player
                elif x>=510 and x<=570 and y>270 and y<=330:
                    if board[1][0] == "X" or board[1][0] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 540
                    y = 300
                    board[1][0] = player
                elif x>=510 and x<=570 and y>330 and y<=390:
                    if board[2][0] == "X" or board[2][0] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 540
                    y = 360
                    board[2][0] = player
                elif x>570 and x<=630 and y<=270:
                    if board[0][1] == "X" or board[0][1] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 600
                    y = 240
                    board[0][1] = player
                elif x>570 and x<=630 and y>270 and y<=330:
                    if board[1][1] == "X" or board[1][1] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 600
                    y = 300
                    board[1][1] = player
                elif x>570 and x<=630 and y>330 and y<=390:
                    if board[2][1] == "X" or board[2][1] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 600
                    y = 360
                    board[2][1] = player
                elif x>630 and x<=690 and y<=270:
                    if board[0][2] == "X" or board[0][2] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 660
                    y = 240
                    board[0][2] = player
                elif x>630 and x<=690 and y>270 and y<=330:
                    if board[1][2] == "X" or board[1][2] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 660
                    y = 300
                    board[1][2] = player
                elif x>630 and x<=690 and y>330 and y<=390:
                    if board[2][2] == "X" or board[2][2] == "O":
                        running=False
                        print("Ты дурак?")
                    x = 660
                    y = 360
                    board[2][2] = player
                else:
                    running=False
                    print("Ты дурак?")
                if hod%2==0:
                    player = "X"
                    player_1 = Move(x,y,player)
                    players.add(player_1)
                    hod+=1
                    print(board)
                    chek_win(board)
                else:
                    player = "O"
                    player_2 = Move(x,y,player)
                    players.add(player_2)
                    hod+=1
                    print(board)
                    chek_win(board)
                all_sprites.update()
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    players.draw(screen)
    pygame.display.flip()
    pygame.display.set_caption("Mун лох, TIC-TAC-TOE")
pygame.quit()
