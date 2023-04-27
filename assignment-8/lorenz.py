from numpy import *
from mayavi import mlab
import sys
import os
from mayavi.api import Engine

START = (0.1, 0.1, 0.1)
EPSILON = 0.5
START_FRAME = 0
START_TIME = 1
STOP_TIME = 10
NUM_FRAMES = 300

if __name__ == "__main__":

    if not os.path.exists('img'):
        os.makedirs('img')
    
    n = len(sys.argv)

    if(n != 2):
        print("incorrect input format")
        sys.exit(0)
    
    filename = sys.argv[1]

    if(filename.split('.')[1] != "webm"):
        print("only webm format allowed")
        sys.exit(0)

    def lorenz(k, t, s=10., r=28., b=8./3):
        x, y, z = k
        derivative = [s*(y - x), r*x - y - x*z, x*y -b*z]
        return derivative

    from scipy.integrate import odeint

    s1 = array(START, dtype=float)
    s2 = array(START, dtype=float)

    s2[0] += EPSILON

    t = linspace(START_TIME, STOP_TIME, NUM_FRAMES)

    sol1 = odeint(lorenz, s1, t, args=(10., 28., 8./3))
    sol2 = odeint(lorenz, s2, t, args=(10., 28., 8./3))

    x0, y0, z0 = sol1.T
    x1, y1, z1 = sol2.T

    engine = Engine()
    engine.start()
    engine.new_scene()

    surface1 = mlab.plot3d(x0, y0, z0, tube_radius=0.01)
    surface1.actor.property.color = (0.8, 0.0, 0.0)

    surface2 = mlab.plot3d(x1, y1, z1, tube_radius=0.01)
    surface2.actor.property.color = (0.45098039215686275, 0.8235294117647058, 0.08627450980392157)

    scene = engine.scenes[0]

    def move_cam():
        scene.scene.camera.position = [-22.391771307189305, -13.800262998244234, 17.406961679144878]
        scene.scene.camera.focal_point = [0.17962832405011153, -2.2852168482470767, 33.04746364361828]
        scene.scene.camera.view_angle = 30.0
        scene.scene.camera.view_up = [0.5008500983301954, 0.1707680945833417, -0.8485207344991685]
        scene.scene.camera.clipping_range = [0.11237050268363391, 112.3705026836339]
        scene.scene.camera.compute_view_plane_normal()
        scene.scene.render()
    
    w = 0
    for i in range(START_FRAME, len(x0)):
        point = mlab.points3d(x0[i],y0[i], z0[i])
        point.glyph.glyph.scale_factor = 0.4
        point.actor.property.color = (0.8, 0.0, 0.0)

        point1 = mlab.points3d(x1[i],y1[i], z1[i])
        point1.glyph.glyph.scale_factor = 0.4
        point1.actor.property.color = (0.45098039215686275, 0.8235294117647058, 0.08627450980392157)
        
        move_cam()

        scene.scene.save(f'img/image{w}.png')
        w += 1
        point.parent.children = []
        point1.parent.children = []

    os.system(f"ffmpeg -r 1 -i img/image%01d.png -vcodec libvpx -y {filename}")