##############################################################
#For the "Point in Polygon Test"

# Copyright 2001, softSurfer (www.softsurfer.com)
# This code may be freely used and modified for any purpose
# providing that this copyright notice is included with it.
# SoftSurfer makes no warranty for this code, and cannot be held
# liable for any real or imagined damage resulting from its use.
# Users of this code must verify correctness for their application.
##############################################################

#Guining 'Otoshuki' Pertin
#Not the most efficient code though
#Import necessary modules
import cv2
import numpy as np

#First try with three points
def three_points():
    #Create background
    back = np.zeros((500,500))
    #Select points
    a = (250, 20)
    b = (400, 400)
    c = (20, 450)
    #Initial point
    loc = (200,200)
    #Show once
    cv2.circle(back, a, 2, 255, -1)
    cv2.circle(back, b, 2, 255, -1)
    cv2.circle(back, c, 2, 255, -1)
    cv2.circle(back, loc, 2, 255, -1)
    cv2.putText(back, 'A', a, cv2.FONT_HERSHEY_SIMPLEX,
                1, 255, 2, cv2.LINE_AA)
    cv2.putText(back, 'B', b, cv2.FONT_HERSHEY_SIMPLEX,
                1, 255, 2, cv2.LINE_AA)
    cv2.putText(back, 'C', c, cv2.FONT_HERSHEY_SIMPLEX,
                1, 255, 2, cv2.LINE_AA)
    show = back.copy()
    cv2.putText(show, 'tracepoint', loc, cv2.FONT_HERSHEY_SIMPLEX,
                0.5, 255, 1, cv2.LINE_AA)
    cv2.imshow('Init', show)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Run
    iter = 0
    while True:
        #Generate random number
        num = np.random.randint(3)
        #Conditions
        if num == 0:    #Move halfway to A
            loc = (int((a[0]+loc[0])/2), int((a[1]+loc[1])/2))
            cv2.circle(back, loc, 2, 255, -1)
        elif num == 1:  #Move halfway to B
            loc = (int((b[0]+loc[0])/2), int((b[1]+loc[1])/2))
            cv2.circle(back, loc, 2, 255, -1)
        elif num == 2:  #Move halfway to C
            loc = (int((c[0]+loc[0])/2), int((c[1]+loc[1])/2))
            cv2.circle(back, loc, 2, 255, -1)
        show = back.copy()
        cv2.putText(show, 'Iter : '+str(iter), (0,20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, 255, 1, cv2.LINE_AA)
        cv2.putText(show, 'tracepoint', loc, cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, 255, 1, cv2.LINE_AA)
        iter += 1
        cv2.imshow('Draw', show)
        if cv2.waitKey(1) == ord('q'): break

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Crossing number algorithm - Maciej Kalisiak <mac@dgp.toronto.edu>
def convexity(P,V):
    cn = 0    # the crossing number counter
    # repeat the first vertex at end
    V = tuple(V[:])+(V[0],)
    # loop through all edges of the polygon
    for i in range(len(V)-1):   # edge from V[i] to V[i+1]
        if ((V[i][1] <= P[1] and V[i+1][1] > P[1])   # an upward crossing
            or (V[i][1] > P[1] and V[i+1][1] <= P[1])):  # a downward crossing
            # compute the actual edge-ray intersect x-coordinate
            vt = (P[1] - V[i][1]) / float(V[i+1][1] - V[i][1])
            if P[0] < V[i][0] + vt * (V[i+1][0] - V[i][0]): # P[0] < intersect
                cn += 1  # a valid crossing of y=P[1] right of P[0]

    return cn % 2   # 0 if even (out), and 1 if odd (in)

#Generate for an n sided convex polygon
def n_points(n):
    #Create background
    back = np.zeros((800,800))
    size = 800
    #Points and initials
    points = []
    tester = []
    letters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    #Generate a convex polygon
    i = 0
    while i < n:
        point = (np.random.randint(0, size), np.random.randint(0, size))
        tester.append(point)
        #If inside, skip the point
        if convexity(point, tester.copy()): continue
        cv2.circle(back, point, 2, 255, -1)
        cv2.putText(back, letters[i], point, cv2.FONT_HERSHEY_SIMPLEX,
                    1, 255, 2, cv2.LINE_AA)
        points.append(point)
        tester = points.copy()
        i += 1
    #Set random initial point
    loc = (np.random.randint(0, size), np.random.randint(0, size))
    cv2.circle(back, loc, 2, 255, -1)
    show = back.copy()
    cv2.putText(show, 'tracepoint', loc, cv2.FONT_HERSHEY_SIMPLEX,
                0.5, 255, 1, cv2.LINE_AA)
    cv2.imshow('Init', show)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Generate
    iter = 0
    while True:
        #Generate random number
        num = np.random.randint(n)
        #Draw the selected point
        loc = (int((points[num][0]+loc[0])/2), int((points[num][1]+loc[1])/2))
        cv2.circle(back, loc, 2, 255, -1)
        show = back.copy()
        cv2.putText(show, 'Iter : '+str(iter), (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255, 1, cv2.LINE_AA)
        cv2.putText(show, 'tracepoint', loc, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1, cv2.LINE_AA)
        iter += 1
        cv2.imshow('Draw', show)
        if cv2.waitKey(1) == ord('q'): break

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #three_points()
    number = input("Select the number of sides : ")
    n_points(int(number))
