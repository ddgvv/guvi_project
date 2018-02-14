

class RobotGame:
    def format_row(row):
        return '|' + '|'.join('{0:^3s}'.format(x) for x in row) + '|'

    def format_board(board):
        return '\n\n'.join(RobotGame.format_row(row) for row in board)

    def move(direction,x,y,row,col):
        if direction=='n' and x-1!=-1:
            x-=1
        elif direction=='s' and x+1<row:
            x+=1
        elif direction=='w' and y-1!=-1:
            y-=1
        elif direction=='e' and y+1<col:
            y+=1
        return x,y

    def rotate(direction):
        if direction=='e':
            direction='s'
        elif direction=='s':
            direction='w'
        elif direction=='w':
            direction='n'
        elif direction=='n':
            direction='e'
        return direction
f=RobotGame
row,col=map(int,input("Enter grid x&y:").split(' '))
direction=input("Enter e/w/n/s:")
x,y=map(int,input("Enter initial position x&y:").split(' '))
l= [['' for i in range(col)] for j in range(row)]
l[x][y]='R'+direction
print (f.format_board(l))
l[x][y]=''
while True:
    i=input("Enter Process:(m/r) or enter any key to exit:")
    if i=='m':
        x,y=f.move(direction,x,y,row,col)
    elif i=='r':
        direction=f.rotate(direction)
    else:
        break
    print('\n'*10)
    l[x][y]='R'+ direction
    print (f.format_board(l))

    l[x][y]=''
