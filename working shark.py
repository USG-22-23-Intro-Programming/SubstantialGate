from graphics import *
from Button import *
#from SharkClass import *
#from FishClass import *
# for random start of fish and shark
import random
# for Run button, we don't want everything to happen in one second
import time

def gridMap(win):
# making a grid with line
    x=0
    y=0
# square start at (80,80) and end at (480,480)
    for i in range (21):
        xaxis=Line(Point(80+x, 80),Point(80+x,480))
        xaxis.draw(win)
        x=x+20

    for i in range (21):
        yaxis=Line(Point(80, 80+y),Point(480,80+y))
        yaxis.draw(win)
        y=y+20

def main():
    auto_mode = False

    win = GraphWin("Shark Simulator", 600, 600)
    win.setBackground("lightsteelblue")
    Quit = Button(win, Point(500, 550), Point(580, 580), "white", "QUIT")
    Run = Button(win, Point(300, 500), Point(380, 550), "white", "Run")
    Move = Button(win, Point(200, 500), Point(280, 550), "white", "Move")
    Reset = Button(win, Point(20, 550), Point(100, 580), "white", "Reset")
    c=gridMap(win)
    B= Button(win, Point(100, 30), Point(460, 60), "lavender", "Welcome to Shark Simulator by Jaein and Lyzane")
 
    # this is number of fish and we will loop 3 times to have 3 fish total
    number_of_creatures = 1

    start_x = 80
    start_y = 80
    cell_size = 20
    cell_number = 20
    fish_number = 3
# to have 3 fish total 
    fish_image = [0]*fish_number
    fishlist = [0]*fish_number
# because we only have one shark
    shark_image = 0
    shark = 0
    
# fish_number is 3
    for i in range (fish_number):
        # xlist is our x coordinates , ylist is our y coordinates
        # using import random 
        # we want 20 list for x and y, so (0, cell_number - 1) will give (0,19) which is 20 positions

        xlist = random.randint(0, cell_number - 1)
        ylist = random.randint(0, cell_number - 1)

# this will randomly put images into middle of square(cell_size/2)
# because [0,0] start with (80,80), middle value is (90,90)
        x = start_x + cell_size/2 + xlist*cell_size
        y = start_y + cell_size/2 + ylist*cell_size
# using i gives 3 fishes
        fish_image[i] = Image(Point(x,y), "fish.png")
        fish_image[i].draw(win)

 # making a list for every fish   
        fishlist[i]=[xlist,ylist]

# same thing with shark but we don't use i, because we only need one shark             
    for p in range (number_of_creatures):
        xlist = random.randint(0, cell_number - 1)
        ylist = random.randint(0, cell_number - 1)

        x = start_x + cell_size/2 + xlist*cell_size
        y = start_y + cell_size/2 + ylist*cell_size
        shark_image = Image(Point(x,y), "shark.png")
        shark_image.draw(win)

# making a list for shark 
        shark = [xlist, ylist]

    while True:
    # automode means you clicked the run button
        if not auto_mode:
            m = win.getMouse()

# same thing happen when you click move or run(many moves until done)
        if auto_mode or Move.isClicked(m):
# because we have 3 fish i=0,1,2
            for i in range(2):
# when there is no more fish, stop moving the shark
                if(len(fishlist) == 0):
                    auto_mode = False
                    continue
            # just set minimum distance to large number for now
                min_distance = 9999999
                cur_fish = 0
                index = 0
                cur_index = 0
                old_shark_x = shark[0]
                old_shark_y = shark[1]

# there is 3 fishlist,  fishlist[i]=[xlist,ylist]
                for fish in fishlist:
# we are getting the manhattan distance between shark and all fishes
# manhattan distance is the distance between two points measured along axes at right angles
# which is easier to get distance between objects in the grid 
# formula for manhattan distance is |x1 - x2| + |y1 - y2|
# to find which fish has minimum distance to the shark
# [0] is x value of objects, [1] is y value of objects
                    dist = abs(fish[0] - shark[0]) + abs(fish[1] - shark[1])
# Check all the distances between fish(3) and shark and figure out the minimum
                    if dist < min_distance:
                        min_distance = dist
# when you have fish with minimum distance with shark, 
# set that fish as a current fish, set the index to current index
                        cur_fish = fish
                        cur_index = index
# it's adress for fish in fishlist, you have to update everytime you by index+1
                    index = index + 1

# move shark method
                move_shark(shark, cur_fish)

# to move shark, undraw shark with old position, and redraw shark with new position
                shark_image.undraw()
                shark_image.move(cell_size*(shark[0] - old_shark_x), cell_size*(shark[1] - old_shark_y))
                shark_image.draw(win)

# shark ate fish by checking shark position overlaps to fish(current) position
# if true use .pop to erase the image and the list
                if(shark[0] == cur_fish[0] and shark[1] == cur_fish[1]):
                    fish_image.pop(cur_index).undraw()
                    fishlist.pop(cur_index)

# checking if the distance between shark and fish is within 6 pixels
# so fish can move away from shark when distance is within 6 pixels            
            distance=7
            index = 0
# fishlist[i]=[xlist,ylist]
# checking all 3 fish
            for fish in fishlist:
# distance should be absolute value and by doing fish(x,y) - shark (x,y) 
# we can tell the distance(dist)
                    dist = abs(fish[0] - shark[0]) + abs(fish[1] - shark[1])
# all possible move for fish (up, down, right, left for one pixel)
                    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# make to list, one for every possible move and one for the actual possible move 
                    allowed_directions = []

# dist is distance between shark and fish, distance is distance is 7 
# so dist <distance is checking if fish is to the shark in within 6 pixel
                    
                    if dist <distance:

# checking all possible directions(move), directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                        for direction in directions:
# checks that when the fish moves it’s not going out of the grid 
# This is for fish that is running away from the shark
# abs(fish[0] + direction[0] - shark[0]) + abs(fish[1] + direction[1] - shark[1]) < dist this line 
# checks if fish is eaten by shark by doing 
# ( new fish x value - shark’s x value + new fish y value - shark’s y value) 
# < distance between shark and fish
# continues to skip what is not possible for fish to move (out of the grid, eaten by shark)


                            if fish[0] + direction[0] < 0 or fish[0] + direction[0] > 19 or fish[1] + direction[1] < 0 or fish[1] + direction[1] > 19 or abs(fish[0] + direction[0] - shark[0]) + abs(fish[1] + direction[1] - shark[1]) < dist:
                                continue

# when you are done with checking all possible moves, 
# put all actual possible moves to new list which is allowed_directions
                            allowed_directions.append(direction)
# Now, you have direction that fish can move and can’t move
# this is for fish that is not running away from shark,
# so we only have to check if it’s inside of the grid
# everything else is same with before
                    else:
                        for direction in directions:
                            if fish[0] + direction[0] < 0 or fish[0] + direction[0] > 19 or fish[1] + direction[1] < 0 or fish[1] + direction[1] > 19:
                                continue
                            allowed_directions.append(direction)
# this is random choice that will randomly choose between all actual possible move,
# aka allowd_direction list                      
                    choice = random.randint(0, len(allowed_directions) - 1)

                    fishlist[index] = [fish[0] + allowed_directions[choice][0], fish[1] + allowed_directions[choice][1]];
                    fish_image[index].undraw()
                    fish_image[index].move(cell_size*allowed_directions[choice][0], cell_size*allowed_directions[choice][1])
                    fish_image[index].draw(win)
                    index = index + 1
            if auto_mode:
                # we import time for this, when we click run, move will happen every one second
                time.sleep(1)
                continue
                
        elif Run.isClicked(m):
            auto_mode = True
           # if fishlist==0:
                # B= Button(win, Point(100, 30), Point(460, 60), "darkslategray1", "Fish are all eaten by a shark")

# when you click restart botton
        elif Reset.isClicked(m):
            main()

# when you click quit button
        elif Quit.isClicked(m):
            break
    win.close()


def move_shark(shark, fish):
    if(abs(shark[0] - fish[0]) > 0):
        if(shark[0] - fish[0] > 0):
            shark[0] = shark[0] - 1
        else:
            shark[0] = shark[0] + 1
    else:
        if(shark[1] - fish[1] > 0):
            shark[1] = shark[1] - 1
        else:
            shark[1] = shark[1] + 1
       

if __name__ == "__main__":
    main()
