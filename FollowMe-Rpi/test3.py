from math import radians, cos, sin, asin, sqrt,pi,atan2

import RPi.GPIO as io

import time

io.setmode(io.BCM)

# Define GPIO to use on Pi

GPIO_TRIGGER = 8

GPIO_ECHO    = 7

in1_pin = 23

in2_pin = 24

in3_pin = 27

in4_pin = 10

io.setup(in1_pin, io.OUT)

io.setup(in2_pin, io.OUT)

io.setup(in3_pin, io.OUT)

io.setup(in4_pin, io.OUT)

io.setup(26,io.OUT) #Green

io.setup(21,io.OUT) #Red

maxx=0


maxy=0

minx=0

miny=0

cellx=0

celly=0

goal=[0,0]

robotDirection=2

xcoordinate=0

ycoordinate=0

isAFrontEmpty=0

#ultrasonic

#waypoint

#read file

z=list(map(str.split, open('a2.txt')))

wayPoint=[['' for row in range(len(z[0]))] for col in range(len(z))]

for i in range(len(z)):
    
    for j in range(len(z[0])):
        
        wayPoint[i][j]=float(z[i][j])

#read file end
        

#read start and goal from file

p=list(map(str.split, open('sg2.txt')))

point=[['' for row in range(len(p[0]))] for col in range(len(p))]

for i in range(len(p)):
    
    for j in range(len(p[0])):
        
        point[i][j]=float(p[i][j])
        
start=[point[0]]

destination=point[1]

print(destination)

#end sg



def checkFrontEmpty(distance):
    
    global isAFrontEmpty
    
    if (distance > 10) :
        
        isAFrontEmpty = 0
        
        io.output(21,False)
        
        io.output(26,True)
        
        time.sleep(0.1)
        
       
        print('Front Empty')
        
        moveForward()
        
    elif(distance < 10):
        
        isAFrontEmpty = 1
        
        stop()
        
        io.output(26,False)
        
        io.output(21,True)
        
        time.sleep(0.1)
        
        io.output(21,False)
        
        time.sleep(0.1)
        
        print(isAFrontEmpty)
        
        print('Obstacle ')
        
        turnAround()
        
        


def updateWorld(q,w):
    
    global isAFrontEmpty
    
    global world
    
    a=0#ultrasonic()
    
    #checkFrontEmpty(a)
    
    #print(a)
    
    if(isAFrontEmpty==1):
        
        stop()
        
        time.sleep(3)
        

        
    elif(isAFrontEmpty==0):
        
        search()
        
    #global update
        
    #update=isAFrontEmpty
        
    print("update")
    
    #print(world)


def ultrasonic():
    
    print "Ultrasonic Measurement"
    
    # Set pins as output and input
    
    io.setup(GPIO_TRIGGER,io.OUT)  # Trigger
    
    io.setup(GPIO_ECHO,io.IN)      # Echo
    
    # Set trigger to False (Low)
    
    io.output(GPIO_TRIGGER, False)
    
    # Allow module to settle
    
    time.sleep(0.5)
    
    p=(0,0)
    
    # Send 10us pulse to trigger
    
    io.output(GPIO_TRIGGER, True)
    
    time.sleep(0.00001)
    
    io.output(GPIO_TRIGGER, False)
    
    start = time.time()
    
    #while True:
    
    io.output(GPIO_TRIGGER, True)
    
    time.sleep(0.00001)
    
    io.output(GPIO_TRIGGER, False)
    
    start = time.time()
    
    while io.input(GPIO_ECHO)==0:
        
        start = time.time()

    while io.input(GPIO_ECHO)==1:
        
        stop = time.time()

    # Calculate pulse length
    
    elapsed = stop-start
    
    # Distance pulse travelled in that time is time
    
    # multiplied by the speed of sound (cm/s)
    
    distance = elapsed * 34300
    
    # That was the distance there and back so halve the value
    
    distance = distance / 2
    print(distance)
    
    return distance

    


    #0 no obstacle
    
    #1 obstacle


def maxi(waypoint):
    
    for row in range(len(waypoint)):
        
        tempx= [waypoint[row][0] for row in range(len(waypoint))]
        
        tempy=[waypoint[row][1] for row in range(len(waypoint))]
        
    #print(tempy)
        
    global maxx
    
    global maxy
    
    global minx
    
    global miny
    
    maxx= max(tempx)
    
    minx=min(tempx)
    
    maxy=max(tempy)
    
    miny=min(tempy)
    
def cellxy(y1,x1,y2,x2):           # find cell no.minx,xlong,ylat,ylong
    
     global start
     
     if(start[0][0]==y1 and start[0][1]==x1 ):
         
         return 0
        
     elif(x1==x2):
         
        a=distance(y1,x1,y2,x2)*100
        
        return (int(a)/10)
    
     elif(y1==y2):
         
        a=distance(y1,x1,y2,x2)*100
        
        return (int(a)/10)
  
def distance(lat1, lng1, lat2, lng2):
    
    #return distance as meter
    
    radius = 6371 * 1000 

    dLat = (lat2-lat1) * pi / 180
    
    dLng = (lng2-lng1) * pi / 180

    lat1 = lat1 * pi / 180
    
    lat2 = lat2 * pi / 180

    val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * sin(dLng/2) * cos(lat1) * cos(lat2)
    
    ang = 2 * atan2(sqrt(val), sqrt(1-val))
    
    #print(radius * ang)
    
    return radius * ang


def matrix():
    
    global cellx
    
    global celly
    
    #ax = distance(12.983787, 77.752376, 12.983797, 77.752376) #north up
    
    #bx = distance(12.983787, 77.752366, 12.983787, 77.752392)
    
    ax = distance(minx, miny, maxx, miny) #north up
    
    bx = distance(minx, miny, minx, maxy)
    
    acm = ax * 100
    
    bcm = bx * 100
    
    #print ( int(acm) )
    
    #print ( int(bcm) )
    
    celly = int(acm) / 10
    
    cellx = int(bcm) / 10
    
    #print ( celly )
    
    #print ( cellx )
    
    #world = [[1 for row in range(int(cellx))] for col in range(int(celly))]
    
    #print(world)

def put0(waypoint):
    
    x=0
    
    global world
    
    #read the co ordinate and decide which is changing
    
    for row in range(len(waypoint)-1):
        
                #for col in range(len(waypoint[0])):
        
            #print(waypoint[row][col])
        
        #print( x )
        
        a= waypoint[ x ][ 0 ]
        
        b= waypoint[ x ][ 1 ]
        
        c= waypoint[ x + 1 ][ 0 ]
        
        d= waypoint[ x + 1 ][ 1 ]
        
        temp1= min( b , d)
        
        temp2= min( a , c)
        
        # print(miny)
       
        #print(a)
        
        #print(b)
        
        #print(c)
        
        #print(d)
       
        nocelly= 0
        
        nocellx= 0

        nocelly=(int(cellxy(minx, temp2, a, temp2)))       # height
     
        nocellx=(int(cellxy(a, miny, a, temp1         ))) # length
        
        #print(miny)
        
        #print(temp1)
        
        #print(a)
        
        x = x + 1
        
        #print ( nocelly )
        
        #print ( nocellx )
        
        hello=int((distance(a, b, c, d)*100)/10)
        
        #print(hello)
        
        if(nocelly+hello<=20 and (b==d or a==c)):   #need changes
            
            if(a==c ):
                
                for i in range(hello):
                    
                  world[nocelly][nocellx+i]=0
        
            elif(a!=c and b==d):
                
                for i in range(hello):
                    
                    #print(nocelly+i)
                    
                    world[nocelly+i][nocellx]=0

        elif(nocelly+hello>20 and (b==d or a==c)):   #need changes
            
            if(a==c ):
                
                for i in range(hello):
                    
                  world[nocelly][nocellx+i]=0
        
            elif(a!=c and b==d):
                
                for i in range(hello):
                    
                   #print(nocelly+i)
                    
                   world[nocelly+i][nocellx]=0
                   
        elif(nocelly+hello>11 and b!=d and a!=c):   #need improvement
            
            ab=nocelly-hello
            
            #print(ab)
            
            for i in range(hello+1):
                
                #print(nocelly+i)
                
                world[ab+i][nocellx]=0
                

def putStar(destination):
    
    global goal
    
    nocelly=(int(cellxy(minx, destination[1], destination[0], destination[1])))       # height
    
    nocellx=(int(cellxy(destination[0], miny, destination[0], destination[1] )))
    
    goal[0]=nocelly
    
    goal[1]=nocellx-1
    
    #print(goal)


def startH(start):
    
    global init
    
    nocelly=(int(cellxy(minx, start[0][1], start[0][0], start[0][1])))       # height
    
    nocellx=(int(cellxy(start[0][0], miny, start[0][0], start[0][1] )))
    
    init[0]=nocelly

    init[1]=nocellx-1
    
    #print(goal)
       

#print(wayPoint)
    
    
maxi(wayPoint)


#print(maxx)

#print(maxy)

#print(minx)

#print(miny)

#end

init=[0,0]


move=[]


matrix()


world = [[1 for row in range(int(cellx)+2)] for col in range(int(celly)+2)]


optimize =[[1 for row in range(int(cellx)+2)] for col in range(int(celly)+2)]


print(world)

maxi(wayPoint)


put0(wayPoint)


startH(start)


world[5][7]=0 # adjustment


world[5][8]=0 #adjustment


putStar(destination)


#print(goal)

delta = [[-1,0],  #up
       [0,-1],  #left
       [1,0],   #down
       [0,1]]   #right

delta_name=['^','<','v','>']

cost=1

print(world)

def search():
    
   global goal
   
   global init
   
   closed=[[0 for row in range(len(world[0]))] for col in range(len(world))]
   
   closed[init[0]][init[1]]=1
   
   expand=[[-1 for row in range(len(world[0]))] for col in range(len(world))]
   
   action=[[-1 for row in range(len(world[0]))] for col in range(len(world))]
   
   x=init[0]
   
   y=init[1]
   
   g=0
   
   count=0
   
   open1=[[g,x,y]]
   
   #print(open1)
   
   #print(len(open1))
   
   found=False
   
   resign=False
   
   while not found and not resign:
    
          if len(open1)==0:
              
              resign=True
              
              return "Fail"
            
          else:
              
              open1.sort()
              
              open1.reverse()
              
              next=open1.pop()
              
              x=next[1]
              
              y=next[2]
              
              g=next[0]
              
              expand[x][y]=count
              
              count+=1
              
          if x==goal[0] and y==goal[1]:
              
              found=True
              
          else:
              for i in range(len(delta)):
                  
                   x2=x+delta[i][0]
                   
                   y2=y+delta[i][1]
                   
                   if x2>=0 and x2<len(world) and y2>=0 and y2<len(world[0]):
                       
                        if closed[x2][y2]==0 and world[x2][y2]==0:
                            
                             g2=g+cost
                             
                             open1.append([g2,x2,y2])
                             
                             closed[x2][y2]=1
                             
                             action[x2][y2]=i
                             
   policy=[[' ' for row in range(len(world[0]))] for col in range(len(world))]
   
   x=goal[0]
   
   length=0
   
   y=goal[1]
   
   policy[x][y]='*'
   
   while x!=init[0] or y!=init[1]:
       
       x2=x-delta[action[x][y]][0]
       
       y2=y-delta[action[x][y]][1]
       
       policy[x2][y2]=delta_name[action[x][y]]
       
       x=x2
       
       y=y2
       
   for i in range(len(action)):
       
          print ('', policy[i])
   #for i in range(len(action)):
    #  if policy[i][i]=='>':
     #    print(policy[i])

              
#print(world)

   for col in range(len(world)):
       
       for i in range(len(world[0])):
           
           if policy[col][i]=='v' or policy[col][i]=='<' or policy[col][i]=='>' or policy[col][i]=='*' or policy[col][i]=='^':
               optimize[col][i]=0

               #print(policy[col][i])
               #print(col)
               #print(i)
               length=length+1
#print(policy)
               #print(length)
               
   move1=['' for row in range(length)]
   
   for col in range(len(world)):
       
       for i in range(len(world[0])):
           
           if policy[col][i]=='v' or policy[col][i]=='<' or policy[col][i]=='>' or policy[col][i]=='^' or policy[col][i]=='*' :

               #for x in range(length):
               
               move1[x]=policy[col][i]
               
               x+=1
               
   
               
print(search())

print(optimize)





                         #movement


def clockwise():
    
    io.output(in1_pin, False)
    
    io.output(in2_pin, True)
    
    io.output(in3_pin, False)
    
    io.output(in4_pin, True)

def counter_clockwise():
    
    io.output(in1_pin, True)
    
    io.output(in2_pin, False)
    
    io.output(in3_pin, True)
    
    io.output(in4_pin, False)
    
def right():
    
    io.output(in1_pin, True)
    
    io.output(in2_pin, False)
    
    io.output(in3_pin, False)
    
    io.output(in4_pin, True)
    
def left():
    
    io.output(in1_pin, False)
    
    io.output(in2_pin, True)
    
    io.output(in3_pin, True)
    
    io.output(in4_pin, False)
    
def around():
    
    io.output(in1_pin, False)
    
    io.output(in2_pin, True)
    
    io.output(in3_pin, True)
    
    io.output(in4_pin, False)
    
def stop():
    
    io.output(in1_pin, False)
    
    io.output(in2_pin, False)
    
    io.output(in3_pin, False)
    
    io.output(in4_pin, False)

                              #movement end



# Gets the number on the Grid of the space right in front of it.

def getFrontNumber():
    
    global robotDirection
    
    global xcoordinate
    
    global ycoordinate
    
    #global optimize
    
    if (robotDirection == 0):
        
        #updateWorld(ycoordinate - 1,xcoordinate)
        
        return optimize  [ycoordinate - 1][xcoordinate]

    if (robotDirection == 1):
        
        #updateWorld(ycoordinate,xcoordinate+1)
        
        return optimize  [ycoordinate][xcoordinate + 1]
  
    if (robotDirection == 2) :
        
        #updateWorld(ycoordinate + 1,xcoordinate)
        
        return optimize [ycoordinate + 1][xcoordinate] 
  
    if (robotDirection == 3) :
        
        #updateWorld(ycoordinate,xcoordinate-1)
        
        return optimize  [ycoordinate][xcoordinate - 1]



# Gets the number on the Grid of the space to the Right of it.


def getRightNumber() :
    
    global robotDirection
    
    global xcoordinate
    
    global ycoordinate
    
    if (robotDirection == 0):
        
        return optimize [ycoordinate][xcoordinate + 1]

  
    if (robotDirection == 1)  :
        
        return optimize  [ycoordinate + 1][xcoordinate]

  
    if (robotDirection == 2) :
        
        return optimize  [ycoordinate][xcoordinate - 1]
  
    if (robotDirection == 3) :
        
        return optimize  [ycoordinate - 1][xcoordinate]
  


# Gets the number on the Grid of the Space to the Left of it.


def getLeftNumber() :
    
    global robotDirection
    
    global xcoordinate
    
    global ycoordinate
    
    global optimize
    
    if (robotDirection == 0) :
        
        return optimize [ycoordinate][xcoordinate - 1] 
  
    if (robotDirection == 1)  :
        
        return optimize  [ycoordinate - 1][xcoordinate]
 
    if (robotDirection == 2) :
        
        return optimize [ycoordinate][xcoordinate + 1] 
  
    if (robotDirection == 3) :
        
        return optimize  [ycoordinate + 1][xcoordinate]
    
    
def moveForward ():
    
    #motor1.write(180)
    
    #motor2.write(0)
    
    global robotDirection
    
    global xcoordinate
    
    global ycoordinate
    
    print("Forward")
    
    clockwise()
    
    #time.sleep(2)
    
    if (robotDirection == 0):
        
        ycoordinate = ycoordinate - 1
        
    if (robotDirection == 1):
        
        xcoordinate = xcoordinate + 1
        
    if (robotDirection == 2):
        
        ycoordinate = ycoordinate + 1
        
    if (robotDirection == 3):
        
        xcoordinate = xcoordinate - 1
        
    
    
    print("  xcoordinate " )
    
    print(xcoordinate)
    
    print(" ycoordinate ")
    
    print(ycoordinate)
    
    print("  robot direction: ")
    
    print(robotDirection)
    
    print ("   ")
    
  
    


# Turns 90 degrees to the Right


def turnRight () :
        
    global robotDirection
    
    global xcoordinate
    
    global ycoordinate
    
    print("Right")
    
    right()
    
    time.sleep(1.5)
    
    
    if (robotDirection == 0):
        
        robotDirection = 1
        
    elif (robotDirection == 1):
        
        robotDirection = 2
        
    elif (robotDirection == 2):
        
        robotDirection = 3
        
    elif (robotDirection == 3):
        
        robotDirection = 0
        
    print("  xcoordinate " )
    
    print(xcoordinate)
    
    print(" ycoordinate ")
    
    print(ycoordinate)
    
    print("  robot direction: ")
    
    print(robotDirection)
    
    print("  ")

    



# Turns 90 degrees to the Left


def turnLeft () :
    
    global robotDirection
    
    global xcoordinate
    
    global ycoordinate
    
    print("Left")
    
    left()
    
    time.sleep(1.5)
    
    
    if(robotDirection == 0):
        
        robotDirection = 3
        
    elif(robotDirection == 1):
        
        robotDirection = 0
        
    elif(robotDirection == 2):
        
        robotDirection = 1
        
    elif(robotDirection == 3):
        
        robotDirection = 2
    
    print("  xcoordinate " )
    
    print(xcoordinate)
    
    
    print(" ycoordinate ")
    
    print(ycoordinate)
    
    print("  robot direction: ")
    
    print(robotDirection)
    
    print("   ")
    



# Turns 180 degrees

def turnAround ():
    
    global robotDirection
    
    global xcoordinate
    
    global ycoordinate
    
    print("Around")
    
    stop()
    
    around()
    
    time.sleep(2.4)
    
    stop()
    
    if (robotDirection == 0):
        
        robotDirection = 2
        
    elif (robotDirection == 1):
        
        robotDirection = 3
        
    elif (robotDirection == 2):
        
        robotDirection = 0
        
    elif (robotDirection == 3):
        
        robotDirection = 1
    
    print("  xcoordinate " )
    
    print(xcoordinate)
    
    
    
    print(" ycoordinate ")
    
    print(ycoordinate)
    
    
    print("  robot direction: ")
    
    print(robotDirection)
    
    print("  ")

    



def isFrontOpen ():
    
    nextNumber = getFrontNumber()
    
    print(nextNumber)
    
    if (nextNumber == 0):
        
        return True
    
    else:
        
        return False

    

# Checks if there is something to the Right of it using Grids


def isRightOpen():
    
    nextNumber = getRightNumber()
    
    if (nextNumber == 0):
        
        return True
    
    else:
        
        return False
    

# Checks if there is something to the Left of it using Grids


def isLeftOpen():
    
    nextNumber = getLeftNumber()
    
    if (nextNumber == 0):
        
        return True
  
    else:
        
        return False

    

def loop():
    
    while (1==1):
        
        if(xcoordinate==goal[1] and ycoordinate==goal[0] and g==0):

            stop()
            
            print('stop')

            time.sleep(2)

            g=1
            
        else:
            if (isFrontOpen() == True) :
                
                #moveForward()
                
                a=ultrasonic()
                
                checkFrontEmpty(a)

                g=0

               
            elif (isRightOpen() == True):               

                turnRight()

                
            
            
            elif (isLeftOpen() == True) :
                turnLeft()
            
            
            else:
                turnAround()
            
        

loop()









