from ursina import *

app = Ursina()

cube1 = Entity(model='cube', texture='white_cube', color=color.blue, scale_x=4, collider='box')
cube2 = Entity(model='cube', texture='white_cube', color=color.green, scale_y=6, collider='box')

def spin():
        i = 0
        while i < 10:
                cube1.animate('rotation_y', cube1.rotation_y+360, duration=2)
                cube2.animate('rotation_x', cube1.rotation_y+360, duration=2)
                i=i+1


EditorCamera()
spin()

app.run()




# from ursina import *
#
# app = Ursina()
#
# player = Entity(model='cube', color=color.orange, scale_y=2)
#
# def update():   # update gets automatically called.
#     player.x += held_keys['d'] * .1
#     player.x -= held_keys['a'] * .1
#     player.y += held_keys['w'] * .1
#     player.y -= held_keys['s'] * .1
#
# app.run()

