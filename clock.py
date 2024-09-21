import turtle
import time
import math

# Setup the window
ws = turtle.Screen()
ws.bgcolor("black")
ws.setup(width=500, height=500)
ws.tracer(0)

# Setup the turtle
tur = turtle.Turtle()
tur.hideturtle()
tur.speed(0)
tur.pensize(3)

def draw_clock(hour, min, second, tur):
    # Draw the clock face
    tur.up()
    tur.goto(0, 210)
    tur.setheading(180)
    tur.color("red")
    tur.pendown()
    tur.circle(210)
    tur.up()
    tur.goto(0, 0)
    tur.setheading(90)

    # Draw clock ticks
    for _ in range(12):
        tur.fd(190)
        tur.pendown()
        tur.fd(20)
        tur.penup()
        tur.goto(0, 0)
        tur.rt(30)

def draw_hand(length, angle, color, tur):
    tur.penup()
    tur.goto(0, 0)
    tur.color(color)
    tur.setheading(90)
    tur.rt(angle)
    tur.pendown()
    tur.fd(length)

while True:
    # Get the current time
    hour = int(time.strftime("%I"))
    min = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    
    tur.clear()  # Clear only the clock hands
    
    draw_clock(hour, min, second, tur)  # Draw the clock face

    # Calculate the angles for the clock hands
    second_angle = (second / 60) * 360
    min_angle = (min / 60) * 360 + (second / 60) * 6
    hour_angle = (hour / 12) * 360 + (min / 60) * 30

    # Draw the clock hands
    draw_hand(150, second_angle, "blue", tur)   # Second hand
    draw_hand(110, min_angle, "green", tur)     # Minute hand
    draw_hand(80, hour_angle, "yellow", tur)    # Hour hand

    ws.update()  # Update the screen
    time.sleep(1)
