import numpy as np
import random
import matplotlib.pyplot as plt
import os

SIZE = 20
# TAUX_INS = 0.35
TIME = 50000
# DENS = ((SIZE*SIZE)//2) - 23


def insat(world,i,j):
    u = 0
    
    if world[(i+1)%SIZE,(j+1)%SIZE] !=0 and  world[(i+1)%SIZE,(j+1)%SIZE] != world[i,j] : u+=1
    if world[(i+1)%SIZE,(j  )%SIZE] !=0 and  world[(i+1)%SIZE,(j  )%SIZE] != world[i,j] : u+=1
    if world[(i+1)%SIZE,(j-1)%SIZE] !=0 and  world[(i+1)%SIZE,(j-1)%SIZE] != world[i,j] : u+=1
    if world[(i  )%SIZE,(j+1)%SIZE] !=0 and  world[(i  )%SIZE,(j+1)%SIZE] != world[i,j] : u+=1
    if world[(i  )%SIZE,(j-1)%SIZE] !=0 and  world[(i  )%SIZE,(j-1)%SIZE] != world[i,j] : u+=1
    if world[(i-1)%SIZE,(j+1)%SIZE] !=0 and  world[(i-1)%SIZE,(j+1)%SIZE] != world[i,j] : u+=1
    if world[(i-1)%SIZE,(j  )%SIZE] !=0 and  world[(i-1)%SIZE,(j  )%SIZE] != world[i,j] : u+=1
    if world[(i-1)%SIZE,(j-1)%SIZE] !=0 and  world[(i-1)%SIZE,(j-1)%SIZE] != world[i,j] : u+=1

    return u/8;   

def getOpen(world):
    L = []
    for i in range(SIZE):
        for j in range(SIZE):
            if world[i][j] == 0 :
                L.append((i,j))
    return L

def getInsat(world, ins):
    L = []
    for i in range(SIZE):
        for j in range(SIZE):
            if world[i,j] != 0 and insat(world,i,j) > ins :
                L.append((i,j))
    return L

for ins in np.arange(0.0, 1, 0.1):
    print("insat : ", ins)
    print("\n")

    Etude01X = []
    Etude01Y = []
    for j in range(15, 25):

        world = np.array([[0]*SIZE]*SIZE)
        DENS = ((SIZE*SIZE)//2) - j
        
        print("DENS : ", DENS)

        i=0
        while i<DENS:
            x = random.randrange(SIZE)
            y = random.randrange(SIZE)
            if world[x,y] == 0 :
                world[x,y] = 1
                i += 1

        i=0
        while i<DENS:
            x = random.randrange(SIZE)
            y = random.randrange(SIZE)
            if world[x,y] == 0 :
                world[x,y] = -1
                i += 1

        init = plt.imshow(world, interpolation='none')
        # plt.show()

        if not os.path.exists("./resultats/worlds/Init/INS_{}/initial_{}.png".format(ins, j)):
            os.makedirs("./resultats/worlds/Init/INS_{}/".format(ins), exist_ok=True)

        plt.savefig("./resultats/worlds/Init/INS_{}/initial_{}.png".format(ins, j))

        plt.close()

        for t in range(TIME):

            # if t%1000 == 0 :
                # print("{}/{}".format(t,TIME), end="      \r")

            insatL = list(getInsat(world, ins))
            if len(insatL) > 0 :
                x1,y1 = random.choice(insatL)
                x2,y2 = random.choice(getOpen(world))

                world[x2,y2] = world[x1,y1]
                world[x1,y1] = 0
            else : 
                print('break',t)        
                break

        Etude01X.append(DENS)
        Etude01Y.append(t)           

        plt.imshow(world, interpolation='none')

        if not os.path.exists("./resultats/worlds/Sorted/INS_{}/sorted_{}.png".format(ins, j)):
            os.makedirs("./resultats/worlds/Sorted/INS_{}/".format(ins), exist_ok=True)

        plt.savefig('./resultats/worlds/Sorted/INS_{}/sorted_{}.png'.format(ins, j))
        plt.close()

    print(Etude01X)
    print(Etude01Y)

    print("Courbe")
    plt.plot(Etude01X,Etude01Y)
    plt.title("Time evolution as function of density")
    plt.xlabel("Density")
    plt.ylabel("Time")
    plt.savefig('./resultats/Curves/time_as_function_DENS_{}_INS_{}.png'.format(j, ins))
    plt.close()