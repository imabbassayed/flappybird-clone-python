#Shappy Bird
#Recommended Screen Resolution : 1280x720



import random
import os
import sys
import time
import re
from tkinter import *
from tkinter import messagebox as tkmb






def get_leaderboard(): #Function that reads and converts the leaderboard.dat data into a sorted list
        with open('data/leaderboard.dat') as leaderboarddat:
            lin = [i.strip().split(',') for i in leaderboarddat.readlines()]
            lin.sort(key=lambda x: int(x[0]), reverse=True)
            leaderboarddat.close()
            return lin




def set_movebirdup_key(key): #Function that saves the user setting for moving the bird
    defkey = open('data/defkey.dat','w')
    defkey.write(str(key))
    defkey.close()
    mainmenu_object()
    

def get_movebirdup_key(): #Function that returns the move bird key
    defkey = open('data/defkey.dat')
    key = defkey.read(1)
    defkey.close()
    return key

def quit_game(): #Function that confirms if the user want to quit the game
    confirmation = tkmb.askquestion ('Shappy Bird','Are you sure you want to exit the game ?!', icon='warning')
    if confirmation == 'yes':
       root.destroy()


def gameleave_conf(): #Function that confirms if the user want to exit the game without saving 
    confirmation = tkmb.askquestion ('Shappy Bird','Are you sure you want to leave without saving ?!', icon='warning')
    if confirmation == 'yes':
        root.unbind("p") #Unbinds the keys binded as the user is exiting the game now 
        root.unbind("b")
        root.unbind("f")
        root.unbind("u")

        key = get_movebirdup_key() 
        if int(key) == 1:
            root.unbind("w")
        elif int(key) == 2:
            root.unbind("<space>")
        elif int(key) == 3:
            root.unbind("x")
        mainmenu_object()


    
def setting(): #Tkinter Setting Window 

    maincanvas.delete("all")

    bg = PhotoImage(file = "assets/background/1.png") # Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg = bg
    bg_window = maincanvas.create_image(640, 100, image=bg)
    
    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label)


    label = Label(root, text="----------------------------------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 300, window=label)
    
    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1)

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2)

    img3 = PhotoImage(file = "assets/sprites/3.png")#Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3)

    img4 = PhotoImage(file = "assets/sprites/4.png")#Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4)

    label = Label(root, text="Setting", font=("Courier", 40),bg="#42f584")
    label_window = maincanvas.create_window(640, 350, window=label)

    label = Label(root, text="Choose the key you want to move the bird ?!", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 400, window=label)

    keyw = Button(root, text="W", command= lambda :set_movebirdup_key(1),width=5, height=5)
    w_window = maincanvas.create_window(450, 500, window=keyw)

    keyspace = Button(root, text="SPACE", command=lambda :set_movebirdup_key(2),width=20, height=5)
    space_window = maincanvas.create_window(640, 500, window=keyspace)

    keyx = Button(root, text="X", command=lambda :set_movebirdup_key(3),width=5, height=5)
    x_window = maincanvas.create_window(850, 500, window=keyx)
    
    
    backbtnimg = PhotoImage(file = "assets/images/back.png") # Downloaded from www.freeicons.io
    backbtn = Button(root, image = backbtnimg, command=mainmenu_object,width=64, height=64)
    backbtn.image = backbtnimg
    back_window = maincanvas.create_window(40, 40, window=backbtn)
    
def leader_board(): #Tkinter Leaderboard Window 
    
    maincanvas.delete("all")

    bg = PhotoImage(file = "assets/background/1.png") # Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg = bg
    bg_window = maincanvas.create_image(640, 100, image=bg)
    
    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label)

    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1)

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2)

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3)

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4)

    label = Label(root, text="Leader Board", font=("Courier", 30),bg="#42f584")
    label_window = maincanvas.create_window(640, 320, window=label)

    label = Label(root, text="RANK       NAME       SCORE", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 370, window=label)

    label = Label(root, text="---------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 400, window=label)


    y_pos = 430
    rank = 1
    lin = get_leaderboard() #Gets the leaderboard sorted list and prints to screen using Tkinter labels 
    for players in lin:
        if rank > 10:
            break
        x_pos = 810
        count = 0
        
        for details in players:
             count+=1
             label = Label(root, text=details, font=("Courier", 15),bg="#42f584")
             label_window = maincanvas.create_window(x_pos, y_pos, window=label)
             x_pos-= 175

             if count == 2:
                 label = Label(root, text=rank, font=("Courier", 15),bg="#42f584")
                 label_window = maincanvas.create_window(x_pos, y_pos, window=label)
                 x_pos-= 175
                 rank +=1
        y_pos+= 30
        
        
    
    backbtnimg = PhotoImage(file = "assets/images/back.png")# Downloaded from www.freeicons.io
    backbtn = Button(root, image = backbtnimg, command=mainmenu_object,width=64, height=64)
    backbtn.image = backbtnimg
    back_window = maincanvas.create_window(40, 40, window=backbtn)


def get_name(): #Tkinter Window that gets user's name
    maincanvas.delete("all")

    bg = PhotoImage(file = "assets/background/1.png") # Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg = bg
    bg_window = maincanvas.create_image(640, 100, image=bg)
    
    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label)

    label = Label(root, text="----------------------------------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 300, window=label)

   


    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1)

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2)

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3)

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4)


    label = Label(root, text="Tell me, What's your good name ?!", font=("Courier", 40),bg="#42f584")
    label_window = maincanvas.create_window(640, 350, window=label)

    name = Entry(root, width=50, highlightbackground="red" )
    name_window = maincanvas.create_window(640, 400, window=name)

    label = Label(root, text="------>", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(270, 400, window=label)
 
    label = Label(root, text="-----------------------------------------", font=("Courier", 30),bg="#42f584")
    label_window = maincanvas.create_window(640, 500, window=label)

    key = get_movebirdup_key()
    
    if int(key) == 1:
        keybtn = Button(root, text="W",width=3, height=3)
    elif int(key) == 2:
        keybtn = Button(root, text="SPACE",width=12, height=3)
    elif int(key) == 3:
        keybtn = Button(root, text="X",width=3, height=3)

    key_window = maincanvas.create_window(350, 550, window=keybtn)
    
    label = Label(root, text="Bird Movement (Change?! -> Settings)", font=("Courier", 12),bg="#42f584")
    label_window = maincanvas.create_window(640, 550, window=label)
    
    pausebtn = Button(root, text="P",width=3, height=3)
    pause_window = maincanvas.create_window(350, 620, window=pausebtn)
    
    label = Label(root, text="Pause Key", font=("Courier", 12),bg="#42f584")
    label_window = maincanvas.create_window(540, 620, window=label)

    helpbtn = Button(root, text="?",width=3, height=3, command=game_help)
    help_window = maincanvas.create_window(750, 620, window=helpbtn)
    
    label = Label(root, text="Want to score higher ?! -> Help", font=("Courier", 12),bg="#42f584")
    label_window = maincanvas.create_window(1000, 620, window=label)

    bossbtn = Button(root, text="B",width=3, height=3)
    boss_window = maincanvas.create_window(350, 690, window=bossbtn)
    
    label = Label(root, text="Boss Key", font=("Courier", 12),bg="#42f584")
    label_window = maincanvas.create_window(540, 690, window=label)
    
    
    backbtnimg = PhotoImage(file = "assets/images/back.png") # Downloaded from www.freeicons.io
    backbtn = Button(root, image = backbtnimg, command=mainmenu_object,width=64, height=64)
    backbtn.image = backbtnimg
    back_window = maincanvas.create_window(40, 40, window=backbtn)

    nextbtnimg = PhotoImage(file = "assets/images/next.png") # Downloaded from www.freeicons.io
    nextbtn = Button(root, image = nextbtnimg, command=lambda : sprite_selection(name),width=64, height=64)
    nextbtn.image = nextbtnimg
    next_window = maincanvas.create_window(1240, 680, window=nextbtn)

    
    

    
def sprite_selection(name): #Tkinter Bird Selection Window 
    global name1
    namenore = name.get() #Gets the name from Tkiner entry on the last Tkinter window and then removes all characters except the alphabets
    name1 = re.sub('[^a-zA-Z]+', '', namenore)
    
    maincanvas.delete("all")

    bg = PhotoImage(file = "assets/background/1.png") # Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg = bg
    bg_window = maincanvas.create_image(640, 100, image=bg)
    
    backbtnimg = PhotoImage(file = "assets/images/back.png") # Downloaded from www.freeicons.io
    backbtn = Button(root, image = backbtnimg, command=get_name,width=64, height=64)
    backbtn.image = backbtnimg
    back_window = maincanvas.create_window(40, 40, window=backbtn)

    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label)

    label = Label(root, text="----------------------------------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 300, window=label)

   


    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1)

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2)

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3)

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4)
    
    
    
    label = Label(root, text=str(name1)+", Which bird you like ?!", font=("Courier", 40),bg="#42f584")
    label_window = maincanvas.create_window(640, 350, window=label)


    #Buttons that get the user's bird choice and pass it to the start game function
    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    sprite1 = Button(root, image = img1, height=130, width=130, command= lambda: start_game(1,False))
    sprite1.image = img1
    sprite1_window = maincanvas.create_window(540, 450, window=sprite1)

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    sprite2 = Button(root, image = img2, height=130, width=130, command= lambda: start_game(2,False))
    sprite2.image = img2
    sprite2_window = maincanvas.create_window(740, 450, window=sprite2)

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    sprite3 = Button(root, image = img3, height=130, width=130, command= lambda: start_game(3,False))
    sprite3.image = img3
    sprite3_window = maincanvas.create_window(540, 600, window=sprite3)

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    sprite4 = Button(root, image = img4, height=130, width=130,command= lambda: start_game(4,False))
    sprite4.image = img4
    sprite4_window = maincanvas.create_window(740, 600, window=sprite4)


def game_help(): #Tkinter Help Window where the cheat keys are displayed
    maincanvas.delete("all")

    bg = PhotoImage(file = "assets/background/1.png") # Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg = bg
    bg_window = maincanvas.create_image(640, 100, image=bg)
    
    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label)

    label = Label(root, text="----------------------------------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 300, window=label)


    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1)

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2)

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3)

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4)

    label = Label(root, text="Help", font=("Courier", 40),bg="#42f584")
    label_window = maincanvas.create_window(640, 350, window=label)

    label = Label(root, text="-----------------------------------------", font=("Courier", 30),bg="#42f584")
    label_window = maincanvas.create_window(640, 450, window=label)

    fencebtn = Button(root, text="F",width=3, height=3)
    fence_window = maincanvas.create_window(350, 520, window=fencebtn)
    
    label = Label(root, text="Removes the Upper and Lower black fences !!!", font=("Courier", 12),bg="#42f584")
    label_window = maincanvas.create_window(740, 520, window=label)

    movebackbtn = Button(root, text="U",width=3, height=3) 
    moveback_window = maincanvas.create_window(350, 590, window=movebackbtn)
    
    label = Label(root, text="Pushes the green pipes back !!!", font=("Courier", 12),bg="#42f584")
    label_window = maincanvas.create_window(740, 590, window=label)
    
    backbtnimg = PhotoImage(file = "assets/images/back.png") # Downloaded from www.freeicons.io
    backbtn = Button(root, image = backbtnimg, command=mainmenu_object,width=64, height=64)
    backbtn.image = backbtnimg
    back_window = maincanvas.create_window(40, 40, window=backbtn)



def checksavedgame(): #Checks if there is a saved game session 

        if os.path.getsize('data/savegame.dat') > 0: #Checks if the savegame.dat datafile is not empty and asks user if they want to continue the saved game or start again
                confirmation = tkmb.askquestion ('Shappy Bird','You have a saved game, do you want to continue ?!', icon='warning',parent=root)
                if confirmation == 'yes':
                        savegame = open('data/savegame.dat')
                        lines = savegame.readlines()
                        print(lines[6])
                        start_game(int(lines[6]),True) #Starts the saved game
                else:
                        open('data/savegame.dat', 'w').close() # If user chooses not to the play the saved game then the data in the save game will be deleted
                        get_name()
        else:
                        get_name()
                  

                
                
    
def mainmenu_object(): #Tkinter Main Menu Window 
    maincanvas.delete("all")


    bg = PhotoImage(file = "assets/background/1.png") # Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg = bg
    bg_window = maincanvas.create_image(640, 100, image=bg)
    
    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label)

    label = Label(root, text="----------------------------------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 300, window=label)


    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1)

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2)

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3)

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4)

 
  

    startbtnimg = PhotoImage(file = "assets/images/start.png") # Downloaded from www.freeicons.io
    startbtn = Button(root, image = startbtnimg, command=checksavedgame,width=300, height=140)
    startbtn.image = startbtnimg
    start_window = maincanvas.create_window(390, 500, window=startbtn)
  
    lbbtnimg = PhotoImage(file = "assets/images/leaderboard.png") # Downloaded from www.freeicons.io
    lbbtn = Button(root, image = lbbtnimg, command=leader_board,width=300, height=140)
    lbbtn.image = lbbtnimg
    lb_window = maincanvas.create_window(890, 500, window=lbbtn)

    exitbtnimg = PhotoImage(file = "assets/images/exit.png") # Downloaded from www.freeicons.io
    exitbtn = Button(root, image = exitbtnimg, command=quit_game,width=64, height=64)
    exitbtn.image = exitbtnimg
    exit_window = maincanvas.create_window(40, 40, window=exitbtn)

    helpbtnimg = PhotoImage(file = "assets/images/help.png") # Downloaded from www.freeicons.io
    helpbtn = Button(root, image = helpbtnimg, command=game_help)
    helpbtn.image = helpbtnimg
    help_window = maincanvas.create_window(640, 650, window=helpbtn)
    
    settingbtnimg = PhotoImage(file = "assets/images/setting.png") # Downloaded from www.freeicons.io
    settingbtn = Button(root, image = settingbtnimg, command=setting,width=64, height=64)
    settingbtn.image = settingbtnimg
    setting_window = maincanvas.create_window(1240, 40, window=settingbtn)

  

root = Tk()
root.title("Shappy Bird")
root.geometry('1280x720')
root.resizable(False,False)
maincanvas = Canvas(root, height=720, width=1280,highlightthickness=0, bg="#42f584")
maincanvas.pack()


    
mainmenu_object()


 
def start_game(spritechoice,savedgame): # Start Game function 
    
    global scorelabel
    global pipeUp
    global pipeDown
    global sprite
    global complexety
    global xcor_pipe
    global ycor_sprite
    global presscount
    global score
    global pausegame
    global fenceremove
    global spritechoice1
    global name1
    
    spritechoice1 = spritechoice

    #Checks if the user chose to continue the saved game or wanted to start new game

    
    if savedgame == True: # If saved game, then it loads the main gameplay parameters from the savegame.dat
         savefile = open('data/savegame.dat')
         lines = savefile.readlines()
         complexety = int(lines[0])
         xcor_pipe = int(lines[1])
         ycor_sprite = int(lines[2])
         presscount=int(lines[3])
         score = int(lines[4])-1
         name1 = lines[7][:-1]
         pausegame = False
         fenceremove = False
         
    else: # Else starts new game with default gameplay parameters
         open('data/savegame.dat', 'w').close()
         complexety = 50
         xcor_pipe = 1040
         ycor_sprite = 200
         presscount=0
         score = -1
         pausegame = False
         fenceremove = False


                        
    
    
    maincanvas.delete("all")

    gamerectangle= maincanvas.create_rectangle(0,0,1280,1280, fill="#71bec7",outline="#71bec7")


    pipeUp = maincanvas.create_rectangle(550,0,650,0, fill="#74BF2E", outline="#74BF2E")
    pipeDown = maincanvas.create_rectangle(550,200,650,720, fill="#74BF2E", outline="#74BF2E")

  

    bg = PhotoImage(file = "assets/background/2.png") # Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg = bg
    bg_window = maincanvas.create_image(1110, 360, image=bg)
    
    bg1 = PhotoImage(file = "assets/background/2.png")# Downloaded from https://weeklyhow.com/flappy-bird-unity-tutorial/
    root.bg1 = bg1
    bg1_window = maincanvas.create_image(170, 360, image=bg1)


    x = 0
    while x<1280: # Prints the fences (Black Triangles) to the screen
        maincanvas.create_polygon((x, 0, x+15, 45, x+30, 0), fill="black", tag="upfence")
        maincanvas.create_polygon((x, 720, x+15, 675, x+30, 720), fill="black",tag="downfence")
        x+=30
    
    if spritechoice == 1: # Prints the bird depending on the user choice
        spritepng = PhotoImage(file="assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    elif spritechoice == 2:
        spritepng = PhotoImage(file="assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    elif spritechoice == 3:
        spritepng = PhotoImage(file="assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    elif spritechoice == 4:
        spritepng = PhotoImage(file="assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
        
    root.spritepng = spritepng 
    sprite = maincanvas.create_image(0, 0, image=spritepng)
    

    
    #Calls the gameplay functions and binds the keys
    random_space()
    pipemovement()
    movedownSprite()
    
    key = get_movebirdup_key()
    if int(key) == 1:
        root.bind("w", moveupSprite)
    elif int(key) == 2:
        root.bind("<space>", moveupSprite)
    elif int(key) == 3:
        root.bind("x", moveupSprite)
        
    root.bind("p", gamepause)
    root.bind("b", gamebosskey)
    root.bind("f", cheat_removefence)
    root.bind("u", cheat_movepipeback)
    collision()

def random_space(): # Function that randomly generates the space between the upper and lower pipe
    global score
    global complexety
    global spacebetweenpipes
    global scorelabel

    
    score +=1
    maincanvas.delete("score")
    scorelabel = maincanvas.create_text(640, 80, text=score,font=("Academy Engraved LET", 60), tag="score") # Upadates and prints the users score
    
    spacebetweenpipes = random.randint(75,500)  #Random spaces between the pipes

    if (score % 3 == 0 and score != 0): # Increases the gameplay complexety everytime the user reaches multiples of 3
        if complexety == 5:
            complexety =5
        else:
            complexety -=5

   

def pipemovement(): # Function that moves the upper and lower pipe
    global xcor_pipe
    global pausegame
    global spacebetweenpipes
    global pipeUp
    global pipeDown
    

   
    #Moves the cordinate of pipe 
    xcor_pipe -=7
    maincanvas.coords(pipeUp, xcor_pipe, 0, xcor_pipe + 100, spacebetweenpipes)
    maincanvas.coords(pipeDown, xcor_pipe, spacebetweenpipes + 200, xcor_pipe + 100, 720)


    #If the pipe reached the end of the gameplay screen it moves it back with another random space between them
    if xcor_pipe <= 240:
        xcor_pipe = 1040
        random_space()
        
    if not pausegame: root.after(complexety, pipemovement)


def movedownSprite(): 
    global sprite
    global ycor_sprite
    global pausegame

    if not pausegame:
        ycor_sprite +=10 # Changes the sprite y Value to move it 
        maincanvas.coords(sprite, 640, ycor_sprite)
        root.after(complexety, movedownSprite)
    

def moveupSprite(event= None):
    global sprite
    global ycor_sprite
    global pausegame
    global presscount

    if not pausegame:
        ycor_sprite -=25 # Changes the sprite y Value to move it 
        maincanvas.coords(sprite, 640, ycor_sprite)
        if presscount < 4:
            presscount +=1
            root.after(complexety, moveupSprite)
        else :
            presscount = 0
    


def collision(): # Function that dectects the bird collision 
    global pausegame
    global ycor_sprite
    global xcor_pipe
    global spacebetweenpipes
    global complexety
    global fenceremove

    if fenceremove == False: # Detects bird collision with fences (Black Triangles) and ends game
        if (ycor_sprite >= 653 or ycor_sprite <= 67 ):
            pausegame = True
            gameend()
    if (xcor_pipe < 660 and xcor_pipe + 100 >= 590) and (ycor_sprite < spacebetweenpipes + 45 or ycor_sprite > spacebetweenpipes + 175): # Detects the bird collision with upper and lower pipes 
        pausegame = True
        gameend()
    if pausegame == False: root.after(complexety, collision)
    
def gameend(): # Tkinter End Game Window
    global score
    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label, tag="a1")

    label = Label(root, text="----------------------------------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 300, window=label, tag="a2")

    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1, tag="a3")

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2, tag="a4")

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3, tag="a6")

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4, tag="a7")

    label = Label(root, text="Game Over !!!", font=("Courier", 40),bg="#42f584")
    label_window = maincanvas.create_window(640, 350, window=label, tag="a8")

    ldfile= open('data/leaderboard.dat','a') # Writes the user's score to the leaderboard.dat file
    ldfile.write(str(score)+","+name1+"\n")
    ldfile.close()
    
    lin = get_leaderboard()
    rank = str((lin.index([str(score),name1]))+1) # Gets the sorted leaderboard list and finds the index of current user in the list to calculate the rank
    
    label = Label(root, text=name1+", Your rank is "+rank+" with the score of "+str(score), font=("Courier", 20),bg="#42f584") 
    label_window = maincanvas.create_window(640, 420, window=label, tag="a8")

    rebtnimg = PhotoImage(file = "assets/images/replay.png")# Downloaded from www.freeicons.io
    rebtn = Button(root, image = rebtnimg, command=replay_conf,width=200, height=140)
    rebtn.image = rebtnimg
    re_window = maincanvas.create_window(340, 550, window=rebtn, tag="a11")

    backbtnimg = PhotoImage(file = "assets/images/back.png")# Downloaded from www.freeicons.io
    backbtn = Button(root, image = backbtnimg, command=mainmenu_object,width=64, height=64)
    backbtn.image = backbtnimg
    back_window = maincanvas.create_window(40, 40, window=backbtn, tag="a9")

    lbbtnimg = PhotoImage(file = "assets/images/leaderboard.png")# Downloaded from www.freeicons.io
    lbbtn = Button(root, image = lbbtnimg, command=leader_board,width=200, height=140)
    lbbtn.image = lbbtnimg
    lb_window = maincanvas.create_window(890, 550, window=lbbtn)

    #Unbinds the keys as the game has ended now
    root.unbind("p")
    root.unbind("b")
    root.unbind("f")
    root.unbind("u")

    key = get_movebirdup_key()
    if int(key) == 1:
        root.unbind("w")
    elif int(key) == 2:
        root.unbind("<space>")
    elif int(key) == 3:
        root.unbind("x")

    #Clears the savegame.dat datafile 
    open('data/savegame.dat', 'w').close()
    
    
def gamepause(event = None): # Pause game function and Tkinter window 
    global pausegame
    label = Label(root, text="Shappy Bird" ,bg="#42f584",font=("Courier", 70))
    label_window = maincanvas.create_window(640, 250, window=label, tag="a1")

    label = Label(root, text="----------------------------------------------------", font=("Courier", 20),bg="#42f584")
    label_window = maincanvas.create_window(640, 300, window=label, tag="a2")

    img1 = PhotoImage(file = "assets/sprites/1.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img1 = img1
    sprite1_window = maincanvas.create_image(450, 150, image=img1, tag="a3")

    img2 = PhotoImage(file = "assets/sprites/2.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img2 = img2
    sprite2_window = maincanvas.create_image(550, 50, image=img2, tag="a4")

    img3 = PhotoImage(file = "assets/sprites/3.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img3 = img3
    sprite3_window = maincanvas.create_image(750, 50, image=img3, tag="a6")

    img4 = PhotoImage(file = "assets/sprites/4.png") #Downloaded from https://www.cleanpng.com/free/flappy-bird.html
    root.img4 = img4
    sprite4_window = maincanvas.create_image(830, 150, image=img4, tag="a7")

    label = Label(root, text="Wait, Why did u pause ?!", font=("Courier", 40),bg="#42f584")
    label_window = maincanvas.create_window(640, 350, window=label, tag="a8")

    backbtnimg = PhotoImage(file = "assets/images/back.png")# Downloaded from www.freeicons.io
    backbtn = Button(root, image = backbtnimg, command=gameleave_conf,width=64, height=64)
    backbtn.image = backbtnimg
    back_window = maincanvas.create_window(40, 40, window=backbtn, tag="a9")

    startbtnimg = PhotoImage(file = "assets/images/start.png")# Downloaded from www.freeicons.io
    startbtn = Button(root, image = startbtnimg, command=gamepause,width=200, height=140)
    startbtn.image = startbtnimg
    start_window = maincanvas.create_window(390, 500, window=startbtn, tag="a10")
  
    savebtnimg = PhotoImage(file = "assets/images/save.png")# Downloaded from www.freeicons.io
    savebtn = Button(root, image = savebtnimg, command=savegame,width=200, height=140)
    savebtn.image = savebtnimg
    save_window = maincanvas.create_window(890, 500, window=savebtn, tag="a11")

    label = Label(root, text="-----------------------------------------", font=("Courier", 30),bg="#42f584")
    label_window = maincanvas.create_window(640, 620, window=label, tag="a12")
        
    pausebtn = Button(root, text="P",width=3, height=3)
    pause_window = maincanvas.create_window(450, 670, window=pausebtn, tag="a13")
        
    label = Label(root, text="To continue playing", font=("Courier", 12),bg="#42f584")
    label_window = maincanvas.create_window(640, 670, window=label, tag="a14")

    rebtnimg = PhotoImage(file = "assets/images/replay.png")# Downloaded from www.freeicons.io
    rebtn = Button(root, image = rebtnimg, command=replay_conf,width=200, height=140)
    rebtn.image = rebtnimg
    re_window = maincanvas.create_window(640, 500, window=rebtn, tag="a11")



    #Unbinds all the keys except teh P key which user can use to unpause the game
    root.unbind("b")
    root.unbind("f")
    root.unbind("u")

    key = get_movebirdup_key()
    if int(key) == 1:
        root.unbind("w")
    elif int(key) == 2:
        root.unbind("<space>")
    elif int(key) == 3:
        root.unbind("x")
        
    if not pausegame: #Pauses the game
        pausegame = True

    
    else: #Unpauses the game and binds all the keys back
        pausegame = False
  
        for i in range (1,15): # Removes the Pause Tkinter window buttons and labels etc....
            tags = "a"+str(i)
            maincanvas.delete(tags)


        # Calls the gameplay functions and binds back the keys
        pipemovement()
        moveupSprite()
        movedownSprite()
        collision()

        key = get_movebirdup_key()
        if int(key) == 1:
            root.bind("w", moveupSprite)
        elif int(key) == 2:
            root.bind("<space>", moveupSprite)
        elif int(key) == 3:
            root.bind("x", moveupSprite)
        
        root.bind("p", gamepause)
        root.bind("b", gamebosskey)
        root.bind("f", cheat_removefence)
        root.bind("u", cheat_movepipeback)
        

def gamebosskey(event = None): # Function that shows a screenshot of the Microsoft Excel as the Boss key
    global pausegame
    img3 = PhotoImage(file = "assets/images/bosskey.png") # Personally Taken the screenshot
    root.img3 = img3
    sprite3_window = maincanvas.create_image(640, 360, image=img3, tag="a6")

        
    if not pausegame: # Pauses the game and unbinds all keys except B which will be used to remove the screenshot and continue the game
        pausegame = True

        root.unbind("p")
        root.unbind("f")
        root.unbind("u")

        key = get_movebirdup_key()
        if int(key) == 1:
            root.unbind("w")
        elif int(key) == 2:
            root.unbind("<space>")
        elif int(key) == 3:
            root.unbind("x")

    
    else: # unpauses the game and removes the Microsoft Excel Screenshot and binds the keys
        pausegame = False
        maincanvas.delete("a6")
        key = get_movebirdup_key()
        if int(key) == 1:
            root.bind("w", moveupSprite)
        elif int(key) == 2:
            root.bind("<space>", moveupSprite)
        elif int(key) == 3:
            root.bind("x", moveupSprite)
        
        root.bind("p", gamepause)
        root.bind("b", gamebosskey)
        root.bind("f", cheat_removefence)
        root.bind("u", cheat_movepipeback)
        
        pipemovement()
        moveupSprite()
        movedownSprite()
        collision()

def cheat_removefence(event = None): # Cheat function that removes the fences for 5000 ms
    global fenceremove

    if fenceremove == False: # Remove the fences and then call the function back in 5000ms
        maincanvas.delete("upfence")
        maincanvas.delete("downfence")
        fenceremove= True
        root.after(5000,cheat_removefence)

    else: # Prints the fences back to the screen
        x = 0
        while x<1280:
            maincanvas.create_polygon((x, 0, x+15, 45, x+30, 0), fill="black", tag="upfence")
            maincanvas.create_polygon((x, 720, x+15, 675, x+30, 720), fill="black",tag="downfence")
            x+=30
            fenceremove= False

def cheat_movepipeback(event = None): # Cheat function that moves the upper and lower pipe back
    global xcor_pipe
    global pausegame
    global spacebetweenpipes
    global pipeUp
    global pipeDown
    

   

    xcor_pipe +=120 # Changes the upper and lower pipe x cordinate to move them back
    maincanvas.coords(pipeUp, xcor_pipe, 0, xcor_pipe + 100, spacebetweenpipes)
    maincanvas.coords(pipeDown, xcor_pipe, spacebetweenpipes + 200, xcor_pipe + 100, 720)
    
    
def replay_conf(): # Asks the user if they want to restart the game
    confirmation = tkmb.askquestion ('Shappy Bird','Are you sure you want start again ?!', icon='warning',parent=root)
    if confirmation == 'yes':
        global spritechoice1
        
        start_game(spritechoice1,False)


def savegame(): # Saves the main gameplay parameters to the savegame.dat when the user wishes to save the game
        global complexety
        global xcor_pipe
        global ycor_sprite
        global presscount
        global score
        global pausegame
        global spritechoice1
        global name1

        savefile = open('data/savegame.dat','w')
        savefile.write(str(complexety)+"\n"+str(xcor_pipe)+"\n"+str(ycor_sprite)+"\n"+str(presscount)+"\n"+str(score)+"\n"+str(pausegame)+"\n"+str(spritechoice1)+"\n"+str(name1)+"\n")

        mainmenu_object()


        
root.mainloop()
