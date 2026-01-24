import pgzrun, pyautogui, random
WIDTH, HEIGHT= pyautogui.size()
TITLE="Connect the Power Ups(From 1)"
mario_powers = [
    "star",
    "star",
    "star",
    "star",
    "star",
    "star",
    "star"
]
nextpower=0
lines=[]
powers=[]
totalpower=len(mario_powers)
for i in range(totalpower):
    A=Actor(mario_powers[i])
    A.pos=random.randint(50, WIDTH-50 ), random.randint(50, HEIGHT-50)
    powers.append(A)


def draw():
    screen.clear()
    screen.blit("space.jpg", (0,0))
    for i,v in enumerate (powers):
        v.draw()
        screen.draw.text(str(i+1), (v.pos[0], v.pos[1]+50), fontsize=50)
    for i in lines:
        print(i)
        screen.draw.line(i[0], i[1], 'white')
        
def update():
    pass
def on_mouse_down(pos):
    global nextpower, lines
    if nextpower<totalpower:
        if powers[nextpower].collidepoint(pos):
            if nextpower:
                lines.append((powers[nextpower-1].pos, powers[nextpower].pos))
            nextpower=nextpower+1
        else:
            lines=[]
            nextpower=0
pgzrun.go()