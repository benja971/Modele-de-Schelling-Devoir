import numpy as np
import random
import matplotlib.pyplot as plt
SIZE = 15
TIME = 25000


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

def initWorld(world, DENS):
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
            
    return world

def moove(world, ins, t):
    insatL = list(getInsat(world, ins))
    if len(insatL) > 0 :
        x1,y1 = random.choice(insatL)
        x2,y2 = random.choice(getOpen(world))

        world[x2,y2] = world[x1,y1]
        world[x1,y1] = 0
        return -1
    else : 
        # print('break',t)        
        return t

def etude1(curves_etude1):
    for ins in [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]:
        curves_etude1[ins] = []
        for libre in range(15, 26):
            tmax = 0 
            for test in range(5):
                tmp = 0
                DENS = ((SIZE*SIZE)//2) - libre
                world = initWorld(np.array([[0]*SIZE]*SIZE), DENS)
                for t in range(TIME):
                    tmp = t
                    if moove(world, ins, t) == t :
                        break
                tmax += tmp/5   
            curves_etude1[ins].append(tmax)

    # print(curves_etude1)

    for ins in curves_etude1.keys():
        plt.plot([x for x in range(15, 26)], curves_etude1[ins])
        plt.title("Time evolution as a function of the desatisfaction rate")
        plt.xlabel("Desatisfaction rate")
        plt.ylabel("Time")
        plt.savefig("./resultats/Curves/POP_evolution/time_evolution_as_a_function_of_libre_INS_{}.png".format(ins))
        plt.close()

def etude2(curves_etude2):
    for pop in range(15, 26):
        # INS_rates = np.arange(0.1, 0.9, 0.1)
        INS_rates = [ 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
        curves_etude2[pop] = []

        for ins in INS_rates:
            tmax = 0
            tmp = 0
            print("INS_rate : {}".format(ins))
            for test in range(5):
                DENS = ((SIZE*SIZE)//2) - pop
                world = initWorld(np.array([[0]*SIZE]*SIZE), DENS)

                for t in range(TIME):
                    tmp = t
                    if moove(world, ins, t) == t :
                        break

                tmax += tmp/5
            curves_etude2[pop].append(tmax)


    for pop in curves_etude2.keys():
        plt.plot(INS_rates, curves_etude2[pop])
        plt.title("Time evolution as a function of the desatisfaction rate")
        plt.xlabel("Desatisfaction rate")
        plt.ylabel("Time")
        plt.savefig("./resultats/Curves/INS_evolution/INS_evolution_as_function_of_time_at_DENS_{}_for_POP_{}.png".format(((SIZE*SIZE)//2) - pop, pop))
        plt.close()


if __name__ == "__main__":
    curves_etude1 = {}
    curves_etude2 = {}
    etude1(curves_etude1)
    etude2(curves_etude2)