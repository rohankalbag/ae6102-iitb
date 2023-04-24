from numpy import *
import mayavi
from mayavi.sources.vtk_xml_file_reader import VTKXMLFileReader

src = VTKXMLFileReader()
src.initialize('file.xml')

from mayavi.api import Engine
engine = Engine()

engine.start()
engine.new_scene()
engine.add_source(src)

from mayavi.modules.vectors import Vectors

engine.add_module(Vectors())

# script obtained from recorder in mayavi

vectors = engine.scenes[0].children[0].children[0].children[0]
vectors.glyph.glyph.followed_camera_position = array([0., 0., 0.])
vectors.glyph.glyph.followed_camera_view_up = array([0., 1., 0.])
vectors.glyph.glyph.range = array([0.        , 3.82231318])
# vectors.glyph.glyph.input_connection = <tvtk.tvtk_classes.algorithm_output.AlgorithmOutput object at 0x7f87c80492c0>
vectors.glyph.mask_input_points = True
vectors.glyph.mask_points.on_ratio = 4
scene = engine.scenes[0]
scene.scene.camera.position = [-7.898444476736709, 2.9765540911521304, 11.78790380002067]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.040724877251047745, 0.9941347872219963, -0.10018737050129375]
scene.scene.camera.clipping_range = [8.172091759414796, 24.511172784522614]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-12.27936395936057, 1.506588690272146, 1.6211025570258553]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.0017883284457494435, 0.9859094826327564, -0.1672701226644521]
scene.scene.camera.clipping_range = [8.368035742295945, 24.32445276100183]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-12.193440433552636, 3.1169076343376587, 0.7888423471488014]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.11023744596374835, 0.9800800299016671, -0.1651993961712241]
scene.scene.camera.clipping_range = [8.137358553717506, 24.625215715070855]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-12.193440433552636, 3.1169076343376587, 0.7888423471488014]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1085359097867396, 0.9939170106128747, -0.01867972968571358]
scene.scene.camera.clipping_range = [8.137358553717506, 24.625215715070855]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-12.193440433552636, 3.1169076343376587, 0.7888423471488014]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1083396701739006, 0.9940737866324464, -0.008934349267847778]
scene.scene.camera.clipping_range = [8.137358553717506, 24.625215715070855]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-8.442819326951305, 2.70888194570679, 0.8709314029793152]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1083396701739006, 0.9940737866324464, -0.008934349267847778]
scene.scene.camera.clipping_range = [4.401451882779341, 20.79496796658375]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-8.129648438384562, 4.0346225033782535, 2.579411000735969]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.21879877498682107, 0.9749881549414726, -0.03905372950294887]
scene.scene.camera.clipping_range = [3.9653949834873714, 21.335411653977875]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-8.18827626474398, 3.2100940526889525, 3.216142794835335]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.14845080880146355, 0.9885053163119658, -0.028628604387423158]
scene.scene.camera.clipping_range = [3.980767749250843, 21.307294529433477]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-7.327772471500335, 3.076258583926626, 3.05705057234058]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.14845080880146355, 0.9885053163119658, -0.028628604387423158]
scene.scene.camera.clipping_range = [3.104358236451268, 20.40875346328038]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-7.3967291557111885, 2.690105049742641, 2.967025346697389]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1131065760033452, 0.9933298749334599, -0.022420125545504894]
scene.scene.camera.clipping_range = [3.1873615411702594, 20.303300612690947]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.save('vectors.png')
vectors.actor.mapper.scalar_range = array([0.        , 3.82231318])
module_manager = engine.scenes[0].children[0].children[0]
module_manager.children[0:1] = []
from mayavi.modules.streamline import Streamline
streamline = Streamline()
vtkxml_file_reader = engine.scenes[0].children[0]
engine.add_filter(streamline, vtkxml_file_reader)
streamline.seed.widget.center = array([3.02409729, 1.09026767, 1.445075  ])
streamline.seed.widget.handle_direction = array([1., 0., 0.])
scene.scene.camera.position = [-6.3684146894257765, 2.5689505016337058, 2.786950361112486]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1131065760033452, 0.9933298749334599, -0.022420125545504894]
scene.scene.camera.clipping_range = [3.072026225069331, 17.848746033542596]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-4.920563748176786, 1.2455040314408645, 6.543931471093107]
scene.scene.camera.focal_point = [3.1269367188215256, 1.4502217015251517, 1.1241562217473984]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.025019266634815608, 0.9996867824910751, 0.0006109089114712529]
scene.scene.camera.clipping_range = [3.3244270148995243, 17.527864302312487]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.save('streamline.png')
streamline.seed.widget.center = array([3.02409729, 1.09026767, 1.445075  ])
streamline.seed.widget.handle_direction = array([1., 0., 0.])
streamline.seed.widget.enabled = False
streamline.seed.widget.center = array([3.02409729, 1.09026767, 1.445075  ])
streamline.seed.widget.handle_direction = array([1., 0., 0.])
streamline.seed.widget.interactor = None
streamline.actor.mapper.scalar_range = array([298.38122559, 692.23968506])
module_manager.children[0:1] = []
from mayavi.modules.glyph import Glyph
glyph = Glyph()
engine.add_filter(glyph, vtkxml_file_reader)
scene.scene.camera.position = [-11.245082050676585, 3.5608183008701335, 0.8471220588038297]
scene.scene.camera.focal_point = [2.972866289317608, 1.3452532030642033, 1.1796342432498932]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1551330677112766, 0.9857312064144614, -0.0653277889047148]
scene.scene.camera.clipping_range = [7.537480403694304, 23.058259646263522]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-11.245082050676585, 3.5608183008701335, 0.8471220588038297]
scene.scene.camera.focal_point = [2.972866289317608, 1.3452532030642033, 1.1796342432498932]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.15387152058566744, 0.9880816117562656, 0.004275939872723594]
scene.scene.camera.clipping_range = [7.537480403694304, 23.058259646263522]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-8.087594434826823, 3.0687909569000498, 0.920965561354355]
scene.scene.camera.focal_point = [2.972866289317608, 1.3452532030642033, 1.1796342432498932]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.15387152058566744, 0.9880816117562656, 0.004275939872723594]
scene.scene.camera.clipping_range = [4.372998122937678, 19.813866196800916]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-8.173817041566014, 2.385569144076574, 1.3808226378194135]
scene.scene.camera.focal_point = [2.972866289317608, 1.3452532030642033, 1.1796342432498932]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.09287126956941365, 0.9956735318755877, -0.0030241049846946658]
scene.scene.camera.clipping_range = [4.510724169536388, 19.64049747985129]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
# glyph.glyph.mask_points.input_connection = <tvtk.tvtk_classes.algorithm_output.AlgorithmOutput object at 0x7f87ab134310>
glyph.glyph.glyph.followed_camera_position = array([0., 0., 0.])
glyph.glyph.glyph.followed_camera_view_up = array([0., 1., 0.])
glyph.glyph.glyph.range = array([298.38122559, 692.23968506])
# glyph.glyph.glyph.input_connection = <tvtk.tvtk_classes.algorithm_output.AlgorithmOutput object at 0x7f87ab134310>
glyph.glyph.mask_input_points = True
glyph.glyph.mask_points.on_ratio = 8
glyph.glyph.mask_points.on_ratio = 10
scene.scene.camera.position = [-7.204702991531391, 2.91239467996743, 5.576500676418076]
scene.scene.camera.focal_point = [2.972866289317608, 1.3452532030642033, 1.1796342432498932]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.13616433174668377, 0.9899700692285106, -0.03766346760027736]
scene.scene.camera.clipping_range = [4.084564320208895, 20.244037190226923]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.save('glyph.png')
glyph.actor.mapper.scalar_range = array([298.38122559, 692.23968506])
module_manager.children[0:1] = []
from mayavi.modules.volume import Volume
volume = Volume()
engine.add_filter(volume, vtkxml_file_reader)
scene.scene.camera.position = [-9.847209076075856, 3.4273419526702313, 4.263357185720508]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.1570519014985658, 0.986669186665504, -0.04264523795827602]
scene.scene.camera.clipping_range = [6.570819799968511, 21.996415203027198]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-9.934313408830551, 4.690684998731404, 1.4024353266554088]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.25616944941494046, 0.9656114644916562, -0.04440397311868991]
scene.scene.camera.clipping_range = [6.807588364955907, 21.698372361171195]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-10.153390594237258, 2.036417709141721, -1.1549140340653945]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.0735349717182245, 0.9941804750812068, -0.07872604970215401]
scene.scene.camera.clipping_range = [6.81912912123462, 21.683844926760052]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-8.911566527867208, 3.276403660130695, 6.960557867353989]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.14988788512238502, 0.9879873567652298, -0.03761123190741607]
scene.scene.camera.clipping_range = [6.5349851820552125, 22.041523603968308]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-7.188871802970631, 2.9833376819781714, 6.127444712123535]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.14988788512238502, 0.9879873567652298, -0.03761123190741607]
scene.scene.camera.clipping_range = [4.618461185298806, 20.07660253658674]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-6.793788248937933, 2.916125803668438, 5.936378180414265]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.14988788512238502, 0.9879873567652298, -0.03761123190741607]
scene.scene.camera.clipping_range = [4.178924742141165, 19.625966688298856]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-6.526380813886542, 2.870634272066228, 5.8070571528821695]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.14988788512238502, 0.9879873567652298, -0.03761123190741607]
scene.scene.camera.clipping_range = [3.881429916865121, 19.320959367435037]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-6.636787635783616, 1.4807880383683507, 5.856438918529271]
scene.scene.camera.focal_point = [3.0, 1.25, 1.1999999284744263]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.03315574841979513, 0.9992678479803156, 0.019090949151692085]
scene.scene.camera.clipping_range = [4.13179105796322, 19.00580627273618]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.save('volume.png')
