#Guining 'Otoshuki' Pertin
#Python implementation of Chaos Game - Numberphile

#Import libraries
import cv2
import numpy as np

#Global mouse positions
clickX = 0
clickY = 0
change = 0

#Function to find mouse click location
def get_location(event, x, y, flags, param):
    global clickX, clickY, change
    #If left clicked, set click location
    if event == cv2.EVENT_LBUTTONDOWN:
        clickX = x
        clickY = y
        change = 1

#Main function
def main(size):
    #Global variable to detect change
    global change
    #Create empty background
    back = np.zeros((size, size))
    #Create window and bind function
    cv2.imshow("Select points", back)
    cv2.setMouseCallback("Select points", get_location)
    #Set up points
    points = []
    #Letters for polygon - max 10
    letters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    print("Select Points")
    while True:
        cv2.imshow("Select points", back)
        #If change occured, draw dot and append
        if change == 1:
            change = 0
            loc = (clickX, clickY)
            points.append(loc)
            cv2.circle(back, loc, 2, 255, -1)
            cv2.putText(back, letters[len(points)-1], loc, cv2.FONT_HERSHEY_SIMPLEX,
                        1, 255, 2, cv2.LINE_AA)
            print(letters[len(points)-1] + str(loc))
        if cv2.waitKey(1) == ord('q'): break
    cv2.destroyAllWindows()
    #Generate
    print("Generating")
    iter = 0
    while True:
        #Generate random number
        num = np.random.randint(len(points))
        #Draw the selected point
        loc = (int((points[num][0]+loc[0])/2), int((points[num][1]+loc[1])/2))
        cv2.circle(back, loc, 2, 255, -1)
        show = back.copy()
        cv2.putText(show, 'Iter : '+str(iter), (0,20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, 255, 1, cv2.LINE_AA)
        cv2.putText(show, 'tracepoint', loc, cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, 255, 1, cv2.LINE_AA)
        cv2.imshow('Draw', show)
        iter += 1
        if cv2.waitKey(1) == ord('q'): break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(800)
