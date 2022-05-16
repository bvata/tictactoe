counts=0
user=[" "," "," "," "," "," "," "," "," "]   
i=0
j=0
pointer_location=0
win=False
vl=False

def initial_print():

    print("---------\n",end="",)
    for i in range(0,9,3):
        print("|       |")
    print("---------\n",end="",)

def input_user():
          global user
          #print("kalon funksioni input")
          user = input("Enter cell: ")
          it_is = False
          while it_is==False:
           try:
            str(user)
            it_is = True
           except ValueError:
            it_is = False
            #print("Invralid input. Please try again.")
            user = input("Enter cell: ")
          
          user=str(user)
          '''ktu ngec te afishimi pasi thot qe jane fut gabim kordinatat ose qe eshte e zene'''
          if len(user)==9:
                afishimi_lojes() 
          else:
                user = input("Enter cell: ")
def enter_cordintates():
          global x,y
          x,y = (input("Enter the coordinates:").split())
          it_is=False
          while it_is==False:
           try:
            int(x)
            int(y)
            it_is=True
            #print("true")
           except ValueError:
            it_is=False
            #print("false")
            x,y = (input("You should enter numbers!").split())
          x,y=int(x),int(y)
          #while 0>=x or x>3 or 0>=y or y>3: # alternative way of while. both work
          if (0< x <4) == False or (0< y <4) == False:
              print("Coordinates should be from 1 to 3!",end="\n")
              enter_cordintates()
              #x,y=int(x),int(y)
def afishimi_lojes():
    #mbushja_fillestare_pa_user()
    print("---------\n",end="",)
    for i in range(0,9,3):
        print("|",user[i],user[i+1],user[i+2],"|")
    print("---------\n",end="",)
    kontrolli_lojes()

def loja_ne_fund():
    global types,user,counts,win,vl
    while win==False: # eshte gabim sepse duhet derisa te fitoje njeri ose te dale barazim loja
        
        counts+=1
        if counts%2==0:        
            types='O'
            enter_cordintates()
        else:
            enter_cordintates()
            types='X'
        butoni=user[(x-1)*3+(y-1)]
        pointer_location = (x-1)*3+(y-1)
        while butoni!=' ':
            print("This cell is occupied! Choose another one!")
            enter_cordintates()
            butoni=user[(x-1)*3+(y-1)]
            pointer_location = (x-1)*3+(y-1)
        user[pointer_location]=types
        afishimi_lojes()

def kontrolli_lojes():
    global win,vl,user
    element_X,element_O,element__,numri=0,0,0,0
    for element in user:
        if element=="X":
            element_X+=1
        if element=="O":
            element_O+=1
        if element==" ":
            element__+=1
    if element_O>element_X+1 or element_X>element_O+1:
        print("Impossible 1")
        print(element_O,element_X)
        return 0

    vlera_kontrollit={
        "rreshtat":rreshtat(),
        "shtyllat":shtyllat(),
        "diagonalja":diagonalja()
    }
    sum=vlera_kontrollit["rreshtat"][1]+vlera_kontrollit["shtyllat"][1]+vlera_kontrollit["diagonalja"][1]
    if sum>1:
        print("Impossible 2",vlera_kontrollit["rreshtat"]) # Problemi, bug 
        
    elif sum==1:
        if vlera_kontrollit["rreshtat"][1]==1:
            print(vlera_kontrollit["rreshtat"][0],"wins")
            win,vl=True,True

        if vlera_kontrollit["shtyllat"][1]==1:
            print(vlera_kontrollit["shtyllat"][0],"wins")
            win,vl=True,True

        if vlera_kontrollit["diagonalja"][1]==1:
            print(vlera_kontrollit["diagonalja"][0],"wins")
            win,vl=True,True
    else:
        for element in user:
            if element== ' ':
                numri+=1
        #print(user)
        #print("numri eshte",numri,"counts eshte:",counts)
        if numri==0:
            if win==True and vl==True:
                pass
            else:
                win=True
                print("---------\n",end="",)
                for i in range(0,9,3):
                    print("|",user[i],user[i+1],user[i+2],"|")
                print("---------\n",end="",)
                print("Draw")
        loja_ne_fund()
def rreshtat():
    control,vlera=0,''
    for i in range(0,9,3):
                if user[i] == user[i+1] and user[i] == user[i+2]:
                  if user[i]==' ':
                        pass
                  else:
                        vlera+=user[i]
                        control+=1
    return vlera,control
def shtyllat():
    control,vlera=0,''
    for i in range(3):
                if user[i] == user[i+3] and user[i] == user[i+6]:
                  if user[i]==' ':
                        pass
                  else:
                        vlera+=user[i]
                        control+=1
    return vlera,control

def diagonalja():
    control,vlera=0,''
    if user[4]==' ':
        pass
    elif (user[4] == user[0] and user[4] == user[8]) and (user[4] == user[6] and user[4] == user[2]):
            control=2
    elif (user[4] == user[0] and user[4] == user[8]) or (user[4] == user[6] and user[4] == user[2]):
        vlera=user[4]
        control=1
    return vlera,control

if __name__ == '__main__':
    initial_print()
    loja_ne_fund()