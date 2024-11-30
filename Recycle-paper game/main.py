import random
import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Recycle paper game"
center_x = WIDTH// 2
center_y = HEIGHT// 2
center = (center_x, center_y)
final_level = 8
start_speed = 10
ITEMS = ["bag", "battery", "bottle", "chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def select_items(num_of_extra_items):
    items_to_create = ["paper"]
    for i in range(num_of_extra_items):
        random_items = random.choice(ITEMS)
        items_to_create.append(random_items)
    return items_to_create

def create_actors(items_to_create):
    new_items = []
    for item in items_to_create:
        new_actor = Actor(item + "img")
        new_items.append(new_actor)
    return new_items

def layout_actors(items_to_layout):
    num_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH // num_of_gaps
    random.shuffle(items_to_layout)

def make_items(num_of_extra_items):
    items_to_create = select_items(num_of_extra_items)
    new_items = create_actors(items_to_create)
    layout_actors(new_items)




def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("Game over", "Try again next time.")
    elif game_complete:
        display_message("You win!", "Good job:)")
    else:
        for item in items:
            item.draw()

def display_message(main_msg, sub_msg):
    screen.draw.text(main_msg, fontsize = 60, color = "black", center = (center_x, center_y))
    screen.draw.text(sub_msg, fontsize = 30, color = "black", center = (center_x, center_y + 30))
    

def update():
    global items
    if len (items) == 0 :
        items = make_items(current_level)
    




pgzrun.go()

