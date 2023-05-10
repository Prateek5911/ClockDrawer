# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:12:27 2022

@author: User
"""

import turtle 


#This draws the outline for the clock
def drawInitialCircle(alex,radius):
    alex.penup()
    alex.goto(0,(-radius))
    alex.pendown()
    alex.color("red")
    alex.circle(radius)
    alex.color("black")
# At completion of this comment, the arrowhead is at (0,-180), pointing right

#This function recenters the arrowhead at (0,0)
def recenter(alex):
    alex.penup()
    alex.goto(0,0)
    alex.pendown()

    
def drawClockTick(alex, radius, ticksize, angle):
    alex.penup()
    alex.forward((1-ticksize) * radius)
    alex.pendown()
    alex.forward(ticksize * radius)
    recenter(alex)
    alex.right(angle)
     
   

def drawClock(alex,radius):
    drawInitialCircle(alex,radius)
    recenter(alex)
    # This loop will draw the hour ticks
    for i in range(12):
        drawClockTick(alex,radius,0.15,30)
    
    # This loop will draw the minute ticks 
    for i in range(60):
        drawClockTick(alex,radius,0.05,6)
        
def drawMinuteHand(alex,radius,minutes):
    minuteAngle = 6*minutes 
    alex.setheading(90) 
    alex.right(minuteAngle)
    alex.forward(0.8 * radius)
    recenter(alex)
    
def drawHourHand(alex,radius,hour,minutes):
    hourAngle = 30*hour + (30 * (minutes/60))
    alex.setheading(90) 
    alex.right(hourAngle) 
    alex.forward(0.4 * radius)
    recenter(alex)
    
def main():
    hour = int(input("Please enter the hour: "))
    minutes = int(input("Please enter the minutes: "))
    radius = 180 
    
    wn = turtle.Screen()     # Pops up a window. 
    alex = turtle.Turtle()   # Arrowhead appears in window.
    
    alex.speed(0)
    drawClock(alex,radius)
    recenter(alex)
    drawMinuteHand(alex,radius,minutes)
    drawHourHand(alex,radius,hour,minutes)
    

    turtle.done()
    
main()