import genesis as gs # type: ignore
import numpy as np
import time
import cv2
import math
import torch

gs.init()

import genesis.engine.solvers.rigid.rigid_solver as RigidSolver

scene = gs.Scene(
    show_viewer = True,
    viewer_options = gs.options.ViewerOptions(
        res           = (1280, 960),
        camera_pos    = (3.5, 0.0, 2.5),
        camera_lookat = (0.0, 0.0, 0.5),
        camera_fov    = 40,
        max_FPS       = 60,
    ),
    vis_options = gs.options.VisOptions(
        show_world_frame = True,
        world_frame_size = 1.0,
        show_link_frame  = False,
        show_cameras     = False,
        plane_reflection = True,
        ambient_light    = (0.1, 0.1, 0.1),
    ),
    renderer=gs.renderers.Rasterizer(),
)

plane = scene.add_entity(
    gs.morphs.Plane(),
)

# robot = scene.add_stage(
#     gs.morphs.USD(
#         file="assets/usd/robot.usd",
#         pos=(0, 0, 0.15)
#     )
# )
robot = scene.add_entity(
    # gs.morphs.MJCF(file="assets/mjcf/wbr_cod.xml",
    #     pos=(0.0, 0.0, 0.15)),
    gs.morphs.URDF(file="assets/urdf/urdf/nz.urdf",
    pos=(0.0, 0.0, 0.15)
    ),
    # vis_mode='collision'
)

# height_field = cv2.imread("assets/terrain/png/stairs.png", cv2.IMREAD_GRAYSCALE)
# terrain_height = torch.tensor(height_field) * 0.1
# print(terrain_height.size())
# terrain = scene.add_entity(
#         morph=gs.morphs.Terrain(
#         # pos = (0.0,0.0,0.0),
#         height_field = height_field,
#         horizontal_scale=0.1, 
#         vertical_scale=0.001,
#         ),
#     )

cam = scene.add_camera(
    res    = (640, 480),
    pos    = (3.5, 0.0, 2.5),
    lookat = (0, 0, 0.5),
    fov    = 30,
    GUI    = False,
)
scene.build(n_envs=1)
scene.step()
while True:
    scene.step()
    cam.render()