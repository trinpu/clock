import turtle
import time
from random import randint

def create_clock(n_hour_marks, hour_mark_shape, turtle_min_shape_size, turtle_max_shape_size, pen_color, fill_color, hour_hand_size_min, hour_hand_size_max, hour_mark_heading):
    """Creates a clock of as a list of N hour marks - hour hand and mark size can be of different size"""
    hour_mark_angle_size = 360 / n_hour_marks
    hour_marks = []

    for mark in range(n_hour_marks):

        hour_hand_size = randint(hour_hand_size_min, hour_hand_size_max)
        turtle_shape_size = randint(turtle_min_shape_size, turtle_max_shape_size)

        a_turtle = turtle.Turtle()
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


def start_counting_orb(clock, starting_mark, n_counts, pen_color, fill_color, delete_color, jump_forward_count, delete_backward_count, time_lag, clockwise=True):
    colored_mark_index = starting_mark
    for second in range(n_counts):
        # delete logic
        # if clockwise:
        #     deleted_mark_index = (colored_mark_index - delete_backward_count) % n_hour_marks
        # else:
        #     deleted_mark_index = (colored_mark_index + delete_backward_count) % n_hour_marks

        # clock[deleted_mark_index].color(pen_color, delete_color)

        # color logic
        clock[colored_mark_index % n_hour_marks].color(pen_color, fill_color)
        if clockwise:
            colored_mark_index += jump_forward_count
        else:   
            colored_mark_index -= jump_forward_count

        time.sleep(time_lag)
    
    if clockwise:
        return colored_mark_index - 1
    else:
        return colored_mark_index + 1

## core behaviours
def bouncing_clock():
    """A colored hour mark counting forward and backwards"""
    colored_mark = start_counting_orb(clock, starting_mark, 12, pen_color, fill_color, delete_color, 1, 1, 0.3)
    colored_mark = start_counting_orb(clock, colored_mark, 12, pen_color, fill_color, delete_color, 1, 1, 0.3, False)
    colored_mark = start_counting_orb(clock, colored_mark, 12, pen_color, fill_color, delete_color, 1, 1, 0.3)


def walking_orbs(clock, orbs_colors, n_steps, step_forward, pulse_duration, coloring_lag=0, continuous=True):
    """Create three obs one by one. Orbs walk forward by 1 step lasting n seconds (pulse duration)"""

    # For this version I assume that the orb_colors < n_hour_marks
    n_hour_marks = len(clock)
    if len(orbs_colors) > n_hour_marks:
        return "too many colors"

    # orbs settings
    tail_indexes = [n_hour_marks - x for x in range(1, len(orbs_colors))]
    moving_flag_index = [0]
    moving_flag_index.extend(tail_indexes)

    # walking settings
    orbs_created = 0
    orbs_creation_cutoff = len(orbs_colors) - 1

    # walking behaviour
    for count in range(n_steps):

        if count < orbs_creation_cutoff:
            orbs_created += 1
        else:
            orbs_created = len(orbs_colors)

        delete_backward_count = orbs_created + 1
        # create orbs
        for orb in range(orbs_created):
            start_counting_orb(clock, moving_flag_index[orb], 1, pen_color, orbs_colors[orb], delete_color, step_forward, delete_backward_count, coloring_lag)
        
        # pause
        time.sleep(pulse_duration)

        # delete created orbs
        if continuous != True:
            for orb in range(n_hour_marks):
                clock[orb].fillcolor(delete_color)
        
        # update orb index
        for orb in range(len(orbs_colors)):
            moving_flag_index[orb] += 1
    
    return 1



# --- MAIN SCRIPT BEHAVIOUR (Could be placed on a separate file)

# note: with time_lag at 0, I create the stepping flag behaviour I wanted
# next feature: draw ("scia"), it could be approached as:
# - a longer train with more colors and transparency, max # colors < # hour marks

# setting colors of background and orbs
background_color = "#090c1f"
delete_color = background_color
pen_color = "#BFEDFF"
fill_color = "#6490CE"

canvas = turtle.Screen()
canvas.bgcolor(background_color)

# defining clock and hour mark sizing
n_hour_marks = 12
hour_mark_heading = 90

hour_hand_size_min = 100
hour_hand_size_max = hour_hand_size_min + 300

turtle_min_shape_size = 2
turtle_max_shape_size = turtle_min_shape_size + 3

starting_mark = 12

clock = create_clock(n_hour_marks, "circle", turtle_min_shape_size, turtle_max_shape_size, pen_color, background_color, hour_hand_size_min, hour_hand_size_max, hour_mark_heading)

# defining walking behaviour
step_forward = 1
orbs_colors = ["red"]
orbs_colors = ["red","white","green"]
orbs_colors = ["yellow", "white", "#faf6eb", "#efe5c2", "#e5d39a", "#dac271","#d0b049", "#b6972f", "#8e7525", "#65541a","#3d3210","#141105"]
n_steps = len(orbs_colors) * 3
pulse_duration = 1
time_lag = 0

assert walking_orbs(clock, range(30), n_steps, step_forward, pulse_duration, time_lag, continuous=False) == "too many colors"
assert walking_orbs(clock, orbs_colors, n_steps, step_forward, pulse_duration, time_lag, continuous=True) == 1    

canvas.mainloop()

    

