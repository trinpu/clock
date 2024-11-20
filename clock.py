from turtle import Screen, Turtle
import time
from random import randint

def create_clock(n_hour_marks, hour_mark_shape, turtle_min_shape_size, turtle_max_shape_size, pen_color, fill_color, hour_hand_size_min, hour_hand_size_max, hour_mark_heading):
    """Creates a clock of as a list of N hour marks - hour hand and mark size can be of different size"""
    hour_mark_angle_size = 360 / n_hour_marks
    hour_marks = []

    for mark in range(n_hour_marks):

        hour_hand_size = randint(hour_hand_size_min, hour_hand_size_max)
        turtle_shape_size = randint(turtle_min_shape_size, turtle_max_shape_size)

        a_turtle = Turtle()
        a_turtle.speed(8)
        a_turtle.shape(hour_mark_shape)
        a_turtle.setheading(hour_mark_heading)
        a_turtle.shapesize(turtle_shape_size)
        a_turtle.color(pen_color, fill_color)
        a_turtle.penup()
        a_turtle.forward(hour_hand_size)
        hour_mark_heading -= hour_mark_angle_size
        hour_marks.append(a_turtle)

    return hour_marks


def color_orb(clock, orb_index, pen_color, fill_color, time_lag):
    """Color orb in a clock at orb_index"""
    n_hour_marks = len(clock)
    clock[orb_index % n_hour_marks].color(pen_color, fill_color)
    time.sleep(time_lag)


def walking_orbs(clock, orbs_colors, delete_color, n_steps, pulse_duration, coloring_lag=0, continuous=True):
    """Create obs one by one. Orbs walk forward by 1 step lasting n seconds (pulse duration)"""

    n_hour_marks = len(clock)
    n_orbs_colors = len(orbs_colors)

    if n_orbs_colors > n_hour_marks:
        n_orbs_colors = n_hour_marks

    colored_orbes_indexes = [0] + [n_hour_marks - x for x in range(1, n_orbs_colors)]

    orbs_created = 1
    for count in range(n_steps):

        for orb in range(orbs_created):
            color_orb(clock, colored_orbes_indexes[orb], pen_color, orbs_colors[orb], coloring_lag)
        
        time.sleep(pulse_duration)

        if orbs_created < n_orbs_colors:
            orbs_created += 1
            
        # (optional) delete created orbs
        if continuous != True:
             for orb_index in colored_orbes_indexes:
                clock[orb_index].fillcolor(delete_color)
        
        # update colored orbs state
        for index, orb_index in enumerate(colored_orbes_indexes):
            colored_orbes_indexes[index] = (orb_index + 1) % n_hour_marks
    
    return 1

def change_orb_outline_color(clock:list, pen_color:str):
    """Change the pen color of each orb in a clock"""
    for orb in clock:
        orb.pencolor(pen_color)
        
    return 1

# color settings
background_color = "#090c1f"
delete_color = background_color
pen_color = "#BFEDFF"
orbs_colors = ["yellow", "white", "#faf6eb", "#efe5c2"] #, "#e5d39a", "#dac271","#d0b049", "#b6972f", "#8e7525", "#65541a","#3d3210","#141105"]

# clock settings
n_hour_marks = 18
shape_size = 2
hour_hand_size = 100

# main
canvas = Screen()
canvas.bgcolor(background_color)

clock = create_clock(n_hour_marks, "circle", shape_size, shape_size, pen_color, background_color, hour_hand_size, hour_hand_size, 90)
assert walking_orbs(clock, orbs_colors, delete_color, n_hour_marks, 0.5, continuous=False) == 1
assert change_orb_outline_color(clock, "#2a3891") == 1

clock = create_clock(n_hour_marks, "circle", shape_size, shape_size, pen_color, background_color, hour_hand_size, hour_hand_size * 3, 90)
assert walking_orbs(clock, orbs_colors, delete_color, n_hour_marks, 0.5, continuous=False) == 1
assert change_orb_outline_color(clock, "#2a3891") == 1

clock = create_clock(n_hour_marks, "circle", shape_size, shape_size * 3, pen_color, background_color, hour_hand_size, hour_hand_size * 3, 90)
assert walking_orbs(clock, orbs_colors, delete_color, n_hour_marks, 0.5, continuous=False) == 1

canvas.mainloop()