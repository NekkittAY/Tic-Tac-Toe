import pygame
from tkinter import *
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

def empty_cells(board):
    cells = []
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell=="#":
                cells.append([i,j])
    return cells
def check_score():
    if win1==True:
        score = 1
        return score
    elif win==True:
        score = -1
        return score
    else:
        score = 0
        return score
def ai_engine(board,player):
    global moves
    global board1
    board1 = board
    if hod==8:
        score = check_score()
    else:
        moves = []
        for cell in empty_cells(board):
            move = []
            if player == "O":
                board1[cell[0]][cell[1]] = "O"
                state = board1
                result = ai_engine(state,"X")
                result1 = check_win(state)
                move.append(result1)
            else:
                board1[cell[0]][cell[1]] = "X"
                state = board1
                result = ai_engine(state,"O")
                result1 = check_win(state)
                move.append(result1)
            moves.append(move)
    best_move = None
    if player == "O":
        best = -10
        for move in moves:
            if move>best:
                best = move
                best_move = move
    else:
        best = 10
        for move in moves:
            if move<best:
                best = move
                best_move = move
    return best_move
def not_ai():
    random_moves = empty_cells(board)
    rand_mass = random.choice(random_moves)
    i,j = rand_mass[0],rand_mass[1]
    board[i][j] = "O"
    return i,j

def check_win(board):
    global win
    global win1
    global Draw
    Draw = False
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
    
    if hod==9 and win==False and win1==False:
        Draw=True
        return Draw

def Click1():
    global click
    click = 0
    click+=1
def Click2():
    global click
    click = 0
    click+=2
    return click
def Destroy():
    root.destroy()
def call_func1():
    Click1()
    Destroy()
def call_func2():
    Click2()
    Destroy()

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
root = Tk()
root.geometry("300x250")
btn1 = Button(text="1 player",command=call_func1).pack()
btn2 = Button(text="2 players",command=call_func2).pack()
root.mainloop()
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
        if check_win(board)==True:
            running=False
            if win==True:
                print("player1 won, Game Over")
            elif win1==True:
                print("player2 won, Game Over")
        if hod==9:
            if win==True or win1==True:
                pass
            else:
                running=False
                print("draw, Game Over")
        if click==2:
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
                        check_win(board)
                    else:
                        player = "O"
                        player_2 = Move(x,y,player)
                        players.add(player_2)
                        hod+=1
                        print(board)
                        check_win(board)
                    all_sprites.update()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if hod%2==0:
                        player = "X"
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
                        player_1 = Move(x,y,player)
                        players.add(player_1)
                        hod+=1
                        print(board)
                        check_win(board)
                    else:
                        player_ai = "O"
                        #move_ai = ai_engine(board,player_ai)
                        #print(move_ai)
                        #x1,y1 = move_ai[0], move_ai[1]
                        x1,y1 = not_ai()
                        if x1==0 and y1==0:
                            x_ai=540
                            y_ai=240
                        elif x1==1 and y==0:
                            x_ai=540
                            y_ai=300
                        elif x1==2 and y==0:
                            x_ai=540
                            y_ai=360
                        elif x1==0 and y1==1:
                            x_ai=600
                            y_ai=240
                        elif x1==1 and y1==1:
                            x_ai=600
                            y_ai=300
                        elif x1==2 and y1==1:
                            x_ai=600
                            y_ai=360
                        elif x1==0 and y1==2:
                            x_ai=660
                            y_ai=240
                        elif x1==1 and y1==2:
                            x_ai=660
                            y_ai=300
                        elif x1==2 and y1==2:
                            x_ai=660
                            y_ai=360
                        player_2 = Move(x_ai,y_ai,player_ai)
                        players.add(player_2)
                        hod+=1
                        print(board)
                        check_win(board)
                    all_sprites.update()
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    players.draw(screen)
    pygame.display.flip()
    pygame.display.set_caption("Mун лох, TIC-TAC-TOE")
pygame.quit()
