import bpy
import os
import numpy as np
import random as rnd
import time
import re

# CONSTANTS
# Positions of camera
positions = [[[0,-7.7,3], [90,0,0]],
            [[7.7,-7.7,3],[90,0,45]],
            [[7.7, 0, 3],[90,0,90]],
            [[7.7,7.7,3],[90,0,135]],
            [[0,7.7,3],[90,0,180]],
            [[-7.7,7.7,3],[90,0,225]],
            [[-7.7,0,3],[90,0,270]],
            [[-7.7,-7.7,3],[90,0,315]]]

# need = 3
sun_var = np.arange(-10, 11, 5)
tdelta = np.arange(-2,2, 0.5)
name_n = 0
timestart = time.clock()

# Path for background images
bip = "/home/jan/Documents/autovision/blender/backgrounds/bckgrnds_edited/"
r = re.compile(".*png")
imgs = list(filter(r.match, [f for f in os.listdir(bip)]))

need = 10 # number of needed samples
fov = 90.0 # camera field of view
pi = 3.14159265
scene = bpy.data.scenes["Scene"]
########################################

def light_chngn(str):
    bpy.data.lamps['Sun'].node_tree.nodes['Emission'].inputs[1].default_value = str

def rnd_sample(samples_num, needed):
    if rnd.randint(0, samples_num) < needed:
        return True
    else:
        return False

# Changing background
def back_chngn(img):
    img = bpy.data.images.load(img)
    tree = bpy.context.scene.node_tree
    tree.nodes["Image"].image = img


# def cam_rotation(rx, ry, rz):
#     scene.camera.rotation_mode = 'XYZ'
#     scene.camera.rotation_euler[0] = rx*(pi/180.0)
#     scene.camera.rotation_euler[1] = ry*(pi/180.0)
#     scene.camera.rotation_euler[2] = rz*(pi/180.0)

def cam_translation(tx, ty, tz):
    scene.camera.location.x = tx
    scene.camera.location.y = ty
    scene.camera.location.z = tz

def capture(position,i):
    cam_move(position)
    file = os.path.join("/home/jan/Documents/autovision/blender/images/excavator",\
    ob.name + str(i) )
    bpy.context.scene.render.filepath = file
    bpy.ops.render.render( write_still=True )


# Set render resolution
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080

# Set camera fov in degrees
scene.camera.data.angle = fov*(pi/180.0)

def cam_move(pos):
    # cam_rotation(pos[1][0],pos[1][1],pos[1][2])
    cam_translation(pos[0][0],pos[0][1],pos[0][2])

variations = len(positions) * 2 * len(sun_var) * len(tdelta) * len(imgs)

for ob in scene.objects:
    if ob.type == 'CAMERA':
        bpy.context.scene.camera = ob
        print('variations', variations)
        for i, position in enumerate(positions):
            print('len', len(imgs))
            print('imgs',imgs)
            for img in imgs:
                print(img)
                back_chngn(bip + img)
                for n in range(0,2):
                    for t in tdelta:
                        tmp_t = position[0][n]
                        position[0][n] += t
                        for sun in sun_var:
                            light_chngn(sun)
                            # print('lol2')
                            if rnd_sample(variations, need):
                                capture(position, name_n)
                                # print('lol1')
                            name_n += 1
                        position[0][n] = tmp_t
print('blended time = ', time.clock() - timestart)
