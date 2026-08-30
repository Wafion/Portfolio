import bpy
cameras = {}
scene = bpy.context.scene
frame = scene.frame_current - 1

data = bpy.data.cameras.new('Camera')
data.lens = 50.0
data.shift_x = 0.0
data.shift_y = 0.0
data.dof.focus_distance = 10.0
data.clip_start = 0.10000000149011612
data.clip_end = 1000.0
data.display_size = 1.0
obj = bpy.data.objects.new('Camera', data)
obj.hide_render = False
bpy.context.collection.objects.link(obj)
cameras['Camera'] = obj

# new frame
scene.frame_set(1 + frame)
obj = cameras['Camera']
obj.location = 7.823199272155762, -2.0844359397888184, 1.634231686592102
obj.scale = 0.9999999403953552, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.410224437713623, -4.000609692411672e-07, 1.2496581077575684
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(2 + frame)
obj = cameras['Camera']
obj.location = 7.8209028244018555, -2.093348979949951, 1.6297342777252197
obj.scale = 0.9999881982803345, 0.9999830722808838, 0.9999850392341614
obj.rotation_euler = 1.4091074466705322, 0.00194688665214926, 1.2453076839447021
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(3 + frame)
obj = cameras['Camera']
obj.location = 7.818644046783447, -2.102874279022217, 1.625834584236145
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.407228946685791, 0.00464803958311677, 1.2416342496871948
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(4 + frame)
obj = cameras['Camera']
obj.location = 7.815854549407959, -2.112277030944824, 1.6219549179077148
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4050008058547974, 0.008291542530059814, 1.2393414974212646
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(5 + frame)
obj = cameras['Camera']
obj.location = 7.811689853668213, -2.121110439300537, 1.6172144412994385
obj.scale = 1.0, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4028400182724, 0.012770356610417366, 1.2386319637298584
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(6 + frame)
obj = cameras['Camera']
obj.location = 7.807579040527344, -2.12911319732666, 1.6124926805496216
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.4003918170928955, 0.01730983331799507, 1.2386857271194458
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(7 + frame)
obj = cameras['Camera']
obj.location = 7.803990364074707, -2.135462522506714, 1.6070741415023804
obj.scale = 1.0, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3971015214920044, 0.021254727616906166, 1.2388224601745605
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(8 + frame)
obj = cameras['Camera']
obj.location = 7.799992561340332, -2.142509937286377, 1.6019560098648071
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3937745094299316, 0.024579327553510666, 1.2380565404891968
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(9 + frame)
obj = cameras['Camera']
obj.location = 7.795872688293457, -2.1477437019348145, 1.5967429876327515
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.390651822090149, 0.027329381555318832, 1.2374907732009888
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(10 + frame)
obj = cameras['Camera']
obj.location = 7.792079448699951, -2.1519951820373535, 1.5917398929595947
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3876900672912598, 0.029122721403837204, 1.2366061210632324
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(11 + frame)
obj = cameras['Camera']
obj.location = 7.788481712341309, -2.155738353729248, 1.5872223377227783
obj.scale = 1.0000003576278687, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3849331140518188, 0.0299500972032547, 1.2349516153335571
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(12 + frame)
obj = cameras['Camera']
obj.location = 7.784603118896484, -2.158992052078247, 1.5830936431884766
obj.scale = 0.9999999403953552, 1.0000007152557373, 1.0000005960464478
obj.rotation_euler = 1.3828171491622925, 0.03001289628446102, 1.2326545715332031
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(13 + frame)
obj = cameras['Camera']
obj.location = 7.779685974121094, -2.1632637977600098, 1.5798513889312744
obj.scale = 1.0, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.3811167478561401, 0.029511205852031708, 1.22970712184906
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(14 + frame)
obj = cameras['Camera']
obj.location = 7.776169776916504, -2.1666064262390137, 1.5772894620895386
obj.scale = 1.0, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3795875310897827, 0.02937321551144123, 1.2273943424224854
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(15 + frame)
obj = cameras['Camera']
obj.location = 7.770909309387207, -2.1706430912017822, 1.5756924152374268
obj.scale = 0.9999998807907104, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.3785697221755981, 0.029607709497213364, 1.2255580425262451
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(16 + frame)
obj = cameras['Camera']
obj.location = 7.764742374420166, -2.174396514892578, 1.574399709701538
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3778711557388306, 0.030145635828375816, 1.224498987197876
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(17 + frame)
obj = cameras['Camera']
obj.location = 7.7588324546813965, -2.177792549133301, 1.5731332302093506
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.377036452293396, 0.030872715637087822, 1.2239104509353638
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(18 + frame)
obj = cameras['Camera']
obj.location = 7.7523980140686035, -2.181138038635254, 1.5723568201065063
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3761779069900513, 0.03142092376947403, 1.2234991788864136
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(19 + frame)
obj = cameras['Camera']
obj.location = 7.745352268218994, -2.1842308044433594, 1.5719902515411377
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.375413179397583, 0.031502291560173035, 1.2231063842773438
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(20 + frame)
obj = cameras['Camera']
obj.location = 7.737678050994873, -2.1870360374450684, 1.5721503496170044
obj.scale = 0.9999997615814209, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3747022151947021, 0.03098839893937111, 1.2225829362869263
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(21 + frame)
obj = cameras['Camera']
obj.location = 7.729957103729248, -2.1897053718566895, 1.5727612972259521
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3739386796951294, 0.030350036919116974, 1.2219053506851196
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(22 + frame)
obj = cameras['Camera']
obj.location = 7.721888542175293, -2.1922192573547363, 1.573984146118164
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3731746673583984, 0.029696250334382057, 1.221107006072998
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(23 + frame)
obj = cameras['Camera']
obj.location = 7.713440895080566, -2.1946301460266113, 1.575904130935669
obj.scale = 0.9999999403953552, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3725746870040894, 0.029628615826368332, 1.2200185060501099
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(24 + frame)
obj = cameras['Camera']
obj.location = 7.705123424530029, -2.1976046562194824, 1.5786434412002563
obj.scale = 1.0000003576278687, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3717551231384277, 0.03052285499870777, 1.2190316915512085
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(25 + frame)
obj = cameras['Camera']
obj.location = 7.696200370788574, -2.19973087310791, 1.5815074443817139
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.3714025020599365, 0.0324753038585186, 1.218673586845398
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(26 + frame)
obj = cameras['Camera']
obj.location = 7.68710470199585, -2.201681613922119, 1.5847753286361694
obj.scale = 0.9999998807907104, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.371186375617981, 0.03491624444723129, 1.2185593843460083
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(27 + frame)
obj = cameras['Camera']
obj.location = 7.677488327026367, -2.2027764320373535, 1.5881128311157227
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3710849285125732, 0.037842828780412674, 1.218649983406067
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(28 + frame)
obj = cameras['Camera']
obj.location = 7.66710090637207, -2.2037811279296875, 1.5913875102996826
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3712425231933594, 0.040465112775564194, 1.2185108661651611
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(29 + frame)
obj = cameras['Camera']
obj.location = 7.657585620880127, -2.20408034324646, 1.59437894821167
obj.scale = 0.9999997615814209, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.3713891506195068, 0.04170990362763405, 1.2179239988327026
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(30 + frame)
obj = cameras['Camera']
obj.location = 7.646636962890625, -2.2019262313842773, 1.597489833831787
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.373022198677063, 0.041095104068517685, 1.2138402462005615
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(31 + frame)
obj = cameras['Camera']
obj.location = 7.6360015869140625, -2.201995849609375, 1.6009671688079834
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3732961416244507, 0.03815170377492905, 1.2065485715866089
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(32 + frame)
obj = cameras['Camera']
obj.location = 7.624207496643066, -2.2046144008636475, 1.6053962707519531
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.373421311378479, 0.03550717234611511, 1.198601245880127
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(33 + frame)
obj = cameras['Camera']
obj.location = 7.612700462341309, -2.2080960273742676, 1.610509991645813
obj.scale = 0.9999998211860657, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3735965490341187, 0.034863028675317764, 1.194138526916504
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(34 + frame)
obj = cameras['Camera']
obj.location = 7.600815296173096, -2.2121100425720215, 1.615450143814087
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3739651441574097, 0.03643212839961052, 1.193008542060852
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(35 + frame)
obj = cameras['Camera']
obj.location = 7.589086055755615, -2.214759111404419, 1.6199201345443726
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3746036291122437, 0.039111100137233734, 1.194362998008728
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(36 + frame)
obj = cameras['Camera']
obj.location = 7.577878952026367, -2.2156009674072266, 1.6237890720367432
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3753679990768433, 0.04155455157160759, 1.1961748600006104
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(37 + frame)
obj = cameras['Camera']
obj.location = 7.567639350891113, -2.215214967727661, 1.6271259784698486
obj.scale = 1.0000001192092896, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.3759801387786865, 0.04246680811047554, 1.196361780166626
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(38 + frame)
obj = cameras['Camera']
obj.location = 7.558189392089844, -2.214245557785034, 1.6310657262802124
obj.scale = 0.9999998807907104, 1.0, 0.9999998807907104
obj.rotation_euler = 1.376383900642395, 0.04193294048309326, 1.1943901777267456
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(39 + frame)
obj = cameras['Camera']
obj.location = 7.547913074493408, -2.214881420135498, 1.6354997158050537
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000004768371582
obj.rotation_euler = 1.3768882751464844, 0.0410013385117054, 1.1914334297180176
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(40 + frame)
obj = cameras['Camera']
obj.location = 7.538435459136963, -2.214521646499634, 1.6398980617523193
obj.scale = 0.9999998807907104, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.3774418830871582, 0.04056291654706001, 1.1893372535705566
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(41 + frame)
obj = cameras['Camera']
obj.location = 7.530040264129639, -2.2139248847961426, 1.6443145275115967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3777676820755005, 0.0395902656018734, 1.1873316764831543
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(42 + frame)
obj = cameras['Camera']
obj.location = 7.521649360656738, -2.213238000869751, 1.6490739583969116
obj.scale = 1.0, 0.9999999403953552, 1.0
obj.rotation_euler = 1.3780028820037842, 0.03839755430817604, 1.1851140260696411
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(43 + frame)
obj = cameras['Camera']
obj.location = 7.514070510864258, -2.2126808166503906, 1.6539270877838135
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.378119707107544, 0.0374782495200634, 1.183699607849121
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(44 + frame)
obj = cameras['Camera']
obj.location = 7.506799221038818, -2.2126662731170654, 1.6587613821029663
obj.scale = 0.9999998807907104, 1.0000004768371582, 1.0
obj.rotation_euler = 1.3781428337097168, 0.03771108016371727, 1.183518409729004
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(45 + frame)
obj = cameras['Camera']
obj.location = 7.500248908996582, -2.2121877670288086, 1.6632697582244873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3781450986862183, 0.03843818977475166, 1.184761643409729
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(46 + frame)
obj = cameras['Camera']
obj.location = 7.4943013191223145, -2.2119197845458984, 1.6677873134613037
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.378067135810852, 0.039514318108558655, 1.1871989965438843
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(47 + frame)
obj = cameras['Camera']
obj.location = 7.487865924835205, -2.2122418880462646, 1.6721585988998413
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.3781412839889526, 0.04136462137103081, 1.1906684637069702
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(48 + frame)
obj = cameras['Camera']
obj.location = 7.482579708099365, -2.212557554244995, 1.6746456623077393
obj.scale = 0.9999999403953552, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.3782507181167603, 0.044032566249370575, 1.1956244707107544
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(49 + frame)
obj = cameras['Camera']
obj.location = 7.476821422576904, -2.2121500968933105, 1.6781463623046875
obj.scale = 1.0, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3790301084518433, 0.04685179516673088, 1.2014232873916626
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(50 + frame)
obj = cameras['Camera']
obj.location = 7.471475124359131, -2.2115345001220703, 1.6809024810791016
obj.scale = 1.000000238418579, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.379930853843689, 0.04863813519477844, 1.2068631649017334
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(51 + frame)
obj = cameras['Camera']
obj.location = 7.466912269592285, -2.210566520690918, 1.6828486919403076
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3806393146514893, 0.04854418337345123, 1.2108879089355469
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(52 + frame)
obj = cameras['Camera']
obj.location = 7.4622483253479, -2.209956407546997, 1.6843154430389404
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.381211280822754, 0.04649175703525543, 1.2129817008972168
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(53 + frame)
obj = cameras['Camera']
obj.location = 7.458276271820068, -2.209812641143799, 1.685090184211731
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.3817211389541626, 0.04320722445845604, 1.2130316495895386
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(54 + frame)
obj = cameras['Camera']
obj.location = 7.453688621520996, -2.210336446762085, 1.6852141618728638
obj.scale = 0.9999999403953552, 0.9999997615814209, 1.0
obj.rotation_euler = 1.3823634386062622, 0.039116162806749344, 1.2115558385849
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(55 + frame)
obj = cameras['Camera']
obj.location = 7.448260307312012, -2.2130675315856934, 1.685208797454834
obj.scale = 1.0, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3832932710647583, 0.03540298715233803, 1.2103939056396484
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(56 + frame)
obj = cameras['Camera']
obj.location = 7.447020053863525, -2.216219902038574, 1.6847574710845947
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.383042335510254, 0.0324646420776844, 1.2112332582473755
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(57 + frame)
obj = cameras['Camera']
obj.location = 7.4440202713012695, -2.2201528549194336, 1.681726098060608
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3834556341171265, 0.029935693368315697, 1.2132760286331177
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(58 + frame)
obj = cameras['Camera']
obj.location = 7.441632270812988, -2.222421884536743, 1.6791203022003174
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.3838285207748413, 0.027459193021059036, 1.216237187385559
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(59 + frame)
obj = cameras['Camera']
obj.location = 7.440258502960205, -2.2252914905548096, 1.6764229536056519
obj.scale = 0.9999999403953552, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3835017681121826, 0.024100415408611298, 1.2179383039474487
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(60 + frame)
obj = cameras['Camera']
obj.location = 7.437801837921143, -2.2282609939575195, 1.6725035905838013
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3828833103179932, 0.018952302634716034, 1.2174979448318481
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(61 + frame)
obj = cameras['Camera']
obj.location = 7.436453819274902, -2.230548143386841, 1.6687833070755005
obj.scale = 1.0, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3816978931427002, 0.013399157673120499, 1.2155992984771729
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(62 + frame)
obj = cameras['Camera']
obj.location = 7.433608531951904, -2.2319111824035645, 1.6643832921981812
obj.scale = 1.000000238418579, 1.0, 1.000000238418579
obj.rotation_euler = 1.3811407089233398, 0.008151225745677948, 1.2135767936706543
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(63 + frame)
obj = cameras['Camera']
obj.location = 7.431446552276611, -2.232449531555176, 1.6611835956573486
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3805180788040161, 0.00404093973338604, 1.212300419807434
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(64 + frame)
obj = cameras['Camera']
obj.location = 7.4289350509643555, -2.233046054840088, 1.6577495336532593
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.3801774978637695, 0.0009900303557515144, 1.211242914199829
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(65 + frame)
obj = cameras['Camera']
obj.location = 7.425344944000244, -2.2324507236480713, 1.6542381048202515
obj.scale = 0.9999998807907104, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3801764249801636, -0.0018986535724252462, 1.2096065282821655
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(66 + frame)
obj = cameras['Camera']
obj.location = 7.422210693359375, -2.2303595542907715, 1.651124119758606
obj.scale = 1.000000238418579, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3801735639572144, -0.005022861994802952, 1.2061034440994263
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(67 + frame)
obj = cameras['Camera']
obj.location = 7.417760848999023, -2.22808837890625, 1.6482245922088623
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3804187774658203, -0.008908242918550968, 1.2000130414962769
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(68 + frame)
obj = cameras['Camera']
obj.location = 7.413482666015625, -2.2266182899475098, 1.6455470323562622
obj.scale = 0.9999999403953552, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.380570650100708, -0.012541508302092552, 1.1921486854553223
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(69 + frame)
obj = cameras['Camera']
obj.location = 7.408299446105957, -2.2251453399658203, 1.642896294593811
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.380734920501709, -0.014675884507596493, 1.184924840927124
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(70 + frame)
obj = cameras['Camera']
obj.location = 7.403708457946777, -2.224587917327881, 1.6399688720703125
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3804823160171509, -0.014154616743326187, 1.1795560121536255
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(71 + frame)
obj = cameras['Camera']
obj.location = 7.397828578948975, -2.22243070602417, 1.6376547813415527
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.380384922027588, -0.01058057602494955, 1.177647590637207
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(72 + frame)
obj = cameras['Camera']
obj.location = 7.393354892730713, -2.2215418815612793, 1.6356655359268188
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3796528577804565, -0.004879698157310486, 1.1776992082595825
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(73 + frame)
obj = cameras['Camera']
obj.location = 7.388384819030762, -2.217339515686035, 1.6344878673553467
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3794673681259155, 0.001000645337626338, 1.1794309616088867
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(74 + frame)
obj = cameras['Camera']
obj.location = 7.384489059448242, -2.2127599716186523, 1.6338083744049072
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3791295289993286, 0.005730551201850176, 1.1802725791931152
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(75 + frame)
obj = cameras['Camera']
obj.location = 7.380308151245117, -2.2075982093811035, 1.6331347227096558
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3788620233535767, 0.008363780565559864, 1.1801061630249023
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(76 + frame)
obj = cameras['Camera']
obj.location = 7.377065658569336, -2.2024080753326416, 1.6326204538345337
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3785006999969482, 0.009854874573647976, 1.1797746419906616
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(77 + frame)
obj = cameras['Camera']
obj.location = 7.3729729652404785, -2.1994667053222656, 1.632191777229309
obj.scale = 0.9999999403953552, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3783642053604126, 0.011316019110381603, 1.1801819801330566
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(78 + frame)
obj = cameras['Camera']
obj.location = 7.370057582855225, -2.1957781314849854, 1.6311304569244385
obj.scale = 0.9999998211860657, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.3780698776245117, 0.012835209257900715, 1.1824970245361328
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(79 + frame)
obj = cameras['Camera']
obj.location = 7.366511344909668, -2.1927874088287354, 1.629802942276001
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.3780018091201782, 0.013850510120391846, 1.1858022212982178
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(80 + frame)
obj = cameras['Camera']
obj.location = 7.364077568054199, -2.1881909370422363, 1.6277492046356201
obj.scale = 1.0000001192092896, 0.9999996423721313, 0.9999997615814209
obj.rotation_euler = 1.3771833181381226, 0.014505299739539623, 1.1895434856414795
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(81 + frame)
obj = cameras['Camera']
obj.location = 7.360440731048584, -2.1841204166412354, 1.6244338750839233
obj.scale = 0.9999998807907104, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3761218786239624, 0.01324473600834608, 1.1919679641723633
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(82 + frame)
obj = cameras['Camera']
obj.location = 7.357259273529053, -2.1787774562835693, 1.6207754611968994
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.3745204210281372, 0.011079230345785618, 1.1932764053344727
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(83 + frame)
obj = cameras['Camera']
obj.location = 7.35414457321167, -2.174525737762451, 1.6166727542877197
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3722196817398071, 0.008762612007558346, 1.1933459043502808
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(84 + frame)
obj = cameras['Camera']
obj.location = 7.350584030151367, -2.1706156730651855, 1.6117676496505737
obj.scale = 1.000000238418579, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3698660135269165, 0.007539371959865093, 1.1934202909469604
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(85 + frame)
obj = cameras['Camera']
obj.location = 7.346822261810303, -2.166102647781372, 1.6064813137054443
obj.scale = 1.0, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3675628900527954, 0.007274844218045473, 1.194362998008728
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(86 + frame)
obj = cameras['Camera']
obj.location = 7.342733860015869, -2.1612775325775146, 1.600708246231079
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3652260303497314, 0.008382302708923817, 1.1955156326293945
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(87 + frame)
obj = cameras['Camera']
obj.location = 7.33887243270874, -2.155447006225586, 1.595043420791626
obj.scale = 0.9999998807907104, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.362486481666565, 0.009549601934850216, 1.196486234664917
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(88 + frame)
obj = cameras['Camera']
obj.location = 7.335387706756592, -2.1496715545654297, 1.5891813039779663
obj.scale = 1.0, 0.9999997019767761, 0.9999997615814209
obj.rotation_euler = 1.3594441413879395, 0.010686631314456463, 1.1971266269683838
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(89 + frame)
obj = cameras['Camera']
obj.location = 7.332691192626953, -2.144834041595459, 1.5832208395004272
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3561944961547852, 0.014542175456881523, 1.198225498199463
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(90 + frame)
obj = cameras['Camera']
obj.location = 7.330065727233887, -2.140122652053833, 1.5776828527450562
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3540927171707153, 0.019001593813300133, 1.2016910314559937
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(91 + frame)
obj = cameras['Camera']
obj.location = 7.328937530517578, -2.1356587409973145, 1.572753667831421
obj.scale = 1.0, 0.9999997019767761, 0.9999997615814209
obj.rotation_euler = 1.3527518510818481, 0.025018543004989624, 1.207499623298645
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(92 + frame)
obj = cameras['Camera']
obj.location = 7.327949523925781, -2.1296911239624023, 1.567521095275879
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.352152705192566, 0.032008275389671326, 1.2147009372711182
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(93 + frame)
obj = cameras['Camera']
obj.location = 7.326770782470703, -2.1244494915008545, 1.5640138387680054
obj.scale = 1.0, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3518651723861694, 0.033886607736349106, 1.2211318016052246
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(94 + frame)
obj = cameras['Camera']
obj.location = 7.325248718261719, -2.1191060543060303, 1.5614893436431885
obj.scale = 1.000000238418579, 1.0000005960464478, 1.0000005960464478
obj.rotation_euler = 1.3508155345916748, 0.034882400184869766, 1.2263926267623901
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(95 + frame)
obj = cameras['Camera']
obj.location = 7.323465347290039, -2.112128257751465, 1.5592997074127197
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3491252660751343, 0.03283717855811119, 1.229556918144226
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(96 + frame)
obj = cameras['Camera']
obj.location = 7.320003986358643, -2.1079347133636475, 1.5566612482070923
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3478331565856934, 0.030302461236715317, 1.2299983501434326
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(97 + frame)
obj = cameras['Camera']
obj.location = 7.316195487976074, -2.105117082595825, 1.5556010007858276
obj.scale = 1.000000238418579, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.347116470336914, 0.030433036386966705, 1.2326245307922363
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(98 + frame)
obj = cameras['Camera']
obj.location = 7.311036586761475, -2.102416515350342, 1.5557119846343994
obj.scale = 0.9999998807907104, 1.0000005960464478, 1.0000004768371582
obj.rotation_euler = 1.3470786809921265, 0.03052717074751854, 1.2371306419372559
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(99 + frame)
obj = cameras['Camera']
obj.location = 7.305416107177734, -2.0975286960601807, 1.5559673309326172
obj.scale = 0.9999998807907104, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3469598293304443, 0.029589325189590454, 1.242540717124939
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(100 + frame)
obj = cameras['Camera']
obj.location = 7.298834800720215, -2.09253191947937, 1.5570292472839355
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3459159135818481, 0.02682078257203102, 1.2462564706802368
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(101 + frame)
obj = cameras['Camera']
obj.location = 7.292426109313965, -2.0880846977233887, 1.5579073429107666
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.343667984008789, 0.023709921166300774, 1.2481193542480469
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(102 + frame)
obj = cameras['Camera']
obj.location = 7.286901473999023, -2.084547519683838, 1.5586930513381958
obj.scale = 0.9999998807907104, 1.0000001192092896, 0.9999998211860657
obj.rotation_euler = 1.3407810926437378, 0.021372895687818527, 1.2498369216918945
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(103 + frame)
obj = cameras['Camera']
obj.location = 7.2803473472595215, -2.0813775062561035, 1.5592032670974731
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3385239839553833, 0.020724279806017876, 1.2528196573257446
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(104 + frame)
obj = cameras['Camera']
obj.location = 7.273563385009766, -2.078320026397705, 1.5593822002410889
obj.scale = 0.9999998807907104, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3370769023895264, 0.020993387326598167, 1.2577135562896729
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(105 + frame)
obj = cameras['Camera']
obj.location = 7.266793251037598, -2.075174331665039, 1.5594520568847656
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.0
obj.rotation_euler = 1.3364473581314087, 0.024750279262661934, 1.2640910148620605
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(106 + frame)
obj = cameras['Camera']
obj.location = 7.260485649108887, -2.070673704147339, 1.5596157312393188
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.3363786935806274, 0.025771550834178925, 1.2714520692825317
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(107 + frame)
obj = cameras['Camera']
obj.location = 7.253233909606934, -2.0658931732177734, 1.5589736700057983
obj.scale = 0.9999998211860657, 0.9999995231628418, 0.9999997019767761
obj.rotation_euler = 1.3369956016540527, 0.029065892100334167, 1.2783678770065308
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(108 + frame)
obj = cameras['Camera']
obj.location = 7.2466959953308105, -2.060765027999878, 1.5582560300827026
obj.scale = 1.0000001192092896, 1.000000238418579, 0.9999999403953552
obj.rotation_euler = 1.3374972343444824, 0.028198063373565674, 1.2846038341522217
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(109 + frame)
obj = cameras['Camera']
obj.location = 7.239524841308594, -2.05464768409729, 1.5558950901031494
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3379156589508057, 0.027113700285553932, 1.2892463207244873
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(110 + frame)
obj = cameras['Camera']
obj.location = 7.232180595397949, -2.048069715499878, 1.5542023181915283
obj.scale = 0.9999999403953552, 1.0, 0.9999998211860657
obj.rotation_euler = 1.337584376335144, 0.02245311439037323, 1.2915576696395874
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(111 + frame)
obj = cameras['Camera']
obj.location = 7.224733829498291, -2.041041612625122, 1.5515668392181396
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3366782665252686, 0.017959700897336006, 1.290395975112915
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(112 + frame)
obj = cameras['Camera']
obj.location = 7.217475414276123, -2.0352513790130615, 1.5480172634124756
obj.scale = 0.9999998211860657, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.335512638092041, 0.013266417197883129, 1.2864092588424683
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(113 + frame)
obj = cameras['Camera']
obj.location = 7.2107648849487305, -2.029641628265381, 1.5441535711288452
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3346030712127686, 0.008574114181101322, 1.2822329998016357
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(114 + frame)
obj = cameras['Camera']
obj.location = 7.204922676086426, -2.024383306503296, 1.5402857065200806
obj.scale = 1.000000238418579, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.3340260982513428, 0.004974261857569218, 1.2782886028289795
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(115 + frame)
obj = cameras['Camera']
obj.location = 7.198176860809326, -2.0182249546051025, 1.5363192558288574
obj.scale = 0.9999998807907104, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.3340121507644653, 0.0002495718072168529, 1.2740861177444458
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(116 + frame)
obj = cameras['Camera']
obj.location = 7.192440986633301, -2.013563394546509, 1.5319280624389648
obj.scale = 0.9999998807907104, 1.0, 1.0
obj.rotation_euler = 1.3338109254837036, -0.003916566260159016, 1.2684388160705566
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(117 + frame)
obj = cameras['Camera']
obj.location = 7.185969352722168, -2.0100953578948975, 1.5272983312606812
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3341501951217651, -0.0063377502374351025, 1.2625418901443481
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(118 + frame)
obj = cameras['Camera']
obj.location = 7.179452896118164, -2.0079071521759033, 1.5220410823822021
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.334930419921875, -0.007320282515138388, 1.2571344375610352
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(119 + frame)
obj = cameras['Camera']
obj.location = 7.172606468200684, -2.0068278312683105, 1.5162417888641357
obj.scale = 1.0000001192092896, 0.9999998211860657, 1.0
obj.rotation_euler = 1.3362480401992798, -0.0065402379259467125, 1.2528927326202393
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(120 + frame)
obj = cameras['Camera']
obj.location = 7.1650896072387695, -2.006342887878418, 1.5101159811019897
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3382314443588257, -0.004211890045553446, 1.2501161098480225
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(121 + frame)
obj = cameras['Camera']
obj.location = 7.157970905303955, -2.00563383102417, 1.5041477680206299
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3404768705368042, -0.0020812961738556623, 1.2491683959960938
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(122 + frame)
obj = cameras['Camera']
obj.location = 7.150659561157227, -2.004225730895996, 1.496517539024353
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.342670202255249, -0.0010116539197042584, 1.2486636638641357
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(123 + frame)
obj = cameras['Camera']
obj.location = 7.1438889503479, -2.002445697784424, 1.4907701015472412
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999997615814209
obj.rotation_euler = 1.3439990282058716, -0.001222335617057979, 1.247504711151123
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(124 + frame)
obj = cameras['Camera']
obj.location = 7.135485649108887, -2.0007781982421875, 1.485102653503418
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.345251202583313, -0.001834809547290206, 1.2453572750091553
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(125 + frame)
obj = cameras['Camera']
obj.location = 7.127207279205322, -2.0001697540283203, 1.479278802871704
obj.scale = 1.000000238418579, 1.0, 1.000000238418579
obj.rotation_euler = 1.3462618589401245, -0.002265356946736574, 1.2428194284439087
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(126 + frame)
obj = cameras['Camera']
obj.location = 7.117375373840332, -1.9997459650039673, 1.4733929634094238
obj.scale = 1.0, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3475379943847656, -0.002810888458043337, 1.2408472299575806
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(127 + frame)
obj = cameras['Camera']
obj.location = 7.108104228973389, -1.9993479251861572, 1.4679313898086548
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3486329317092896, -0.0033718827180564404, 1.2397379875183105
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(128 + frame)
obj = cameras['Camera']
obj.location = 7.098596096038818, -1.9999064207077026, 1.4624453783035278
obj.scale = 0.9999998211860657, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.3495886325836182, -0.0031133918091654778, 1.2389976978302002
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(129 + frame)
obj = cameras['Camera']
obj.location = 7.088519096374512, -2.000678062438965, 1.4571810960769653
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3506962060928345, -0.0032416661269962788, 1.2393804788589478
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(130 + frame)
obj = cameras['Camera']
obj.location = 7.077698230743408, -2.0016303062438965, 1.4519615173339844
obj.scale = 0.9999998807907104, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3519684076309204, -0.003582956502214074, 1.2405928373336792
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(131 + frame)
obj = cameras['Camera']
obj.location = 7.066742897033691, -2.0024659633636475, 1.4470961093902588
obj.scale = 0.9999999403953552, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3527032136917114, -0.003435845021158457, 1.2422549724578857
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(132 + frame)
obj = cameras['Camera']
obj.location = 7.055379867553711, -2.0036754608154297, 1.4420111179351807
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.35271418094635, -0.0030398734379559755, 1.243900179862976
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(133 + frame)
obj = cameras['Camera']
obj.location = 7.043402194976807, -2.004032611846924, 1.4373775720596313
obj.scale = 1.0000003576278687, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3519880771636963, -0.003138675121590495, 1.2459598779678345
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(134 + frame)
obj = cameras['Camera']
obj.location = 7.0317702293396, -2.003854274749756, 1.4328248500823975
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.3504992723464966, -0.002454785630106926, 1.2479369640350342
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(135 + frame)
obj = cameras['Camera']
obj.location = 7.019068241119385, -2.0032734870910645, 1.4271435737609863
obj.scale = 1.0, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.3488011360168457, -0.0010483101941645145, 1.24990713596344
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(136 + frame)
obj = cameras['Camera']
obj.location = 7.006494998931885, -2.0023627281188965, 1.4221926927566528
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3469880819320679, 0.00031074447906576097, 1.2523459196090698
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(137 + frame)
obj = cameras['Camera']
obj.location = 6.99387264251709, -2.001350164413452, 1.4178791046142578
obj.scale = 1.0, 1.000000238418579, 1.0
obj.rotation_euler = 1.3455692529678345, 0.0028656437061727047, 1.255279302597046
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(138 + frame)
obj = cameras['Camera']
obj.location = 6.9811906814575195, -1.9995262622833252, 1.4132612943649292
obj.scale = 1.0, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.344704508781433, 0.004614587407559156, 1.2588151693344116
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(139 + frame)
obj = cameras['Camera']
obj.location = 6.9683027267456055, -1.997420310974121, 1.409769892692566
obj.scale = 0.9999998807907104, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3444344997406006, 0.005381240509450436, 1.2629108428955078
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(140 + frame)
obj = cameras['Camera']
obj.location = 6.95651912689209, -1.9938615560531616, 1.4071487188339233
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3437252044677734, 0.005678506568074226, 1.2671595811843872
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(141 + frame)
obj = cameras['Camera']
obj.location = 6.945258617401123, -1.989849328994751, 1.4045779705047607
obj.scale = 1.0000003576278687, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3425875902175903, 0.005760116036981344, 1.269679069519043
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(142 + frame)
obj = cameras['Camera']
obj.location = 6.9342780113220215, -1.9851042032241821, 1.4027838706970215
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3417565822601318, 0.0053926026448607445, 1.271069049835205
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(143 + frame)
obj = cameras['Camera']
obj.location = 6.92431116104126, -1.9801945686340332, 1.401616096496582
obj.scale = 0.9999999403953552, 1.0, 0.9999998807907104
obj.rotation_euler = 1.341131567955017, 0.005241781007498503, 1.2716604471206665
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(144 + frame)
obj = cameras['Camera']
obj.location = 6.914729118347168, -1.9744216203689575, 1.4015581607818604
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999995231628418
obj.rotation_euler = 1.3411716222763062, 0.004481112584471703, 1.2718836069107056
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(145 + frame)
obj = cameras['Camera']
obj.location = 6.905093193054199, -1.968468427658081, 1.4007573127746582
obj.scale = 0.9999998807907104, 0.9999997019767761, 0.9999998211860657
obj.rotation_euler = 1.3420885801315308, 0.004019229672849178, 1.2707180976867676
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(146 + frame)
obj = cameras['Camera']
obj.location = 6.895326137542725, -1.9617092609405518, 1.4011337757110596
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.343015432357788, 0.004490229766815901, 1.2685528993606567
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(147 + frame)
obj = cameras['Camera']
obj.location = 6.885178565979004, -1.9557148218154907, 1.401362419128418
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.3443726301193237, 0.0046024564653635025, 1.2652356624603271
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(148 + frame)
obj = cameras['Camera']
obj.location = 6.875443935394287, -1.9492194652557373, 1.4022326469421387
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3464683294296265, 0.0030204809736460447, 1.2624541521072388
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(149 + frame)
obj = cameras['Camera']
obj.location = 6.864996433258057, -1.9439438581466675, 1.4026577472686768
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.349530577659607, 0.003265151521191001, 1.2595127820968628
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(150 + frame)
obj = cameras['Camera']
obj.location = 6.854240894317627, -1.9375803470611572, 1.402899146080017
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.353309154510498, 0.004875215236097574, 1.2575316429138184
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(151 + frame)
obj = cameras['Camera']
obj.location = 6.842153072357178, -1.9346466064453125, 1.4037492275238037
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999997615814209
obj.rotation_euler = 1.356664776802063, 0.006412219256162643, 1.2562975883483887
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(152 + frame)
obj = cameras['Camera']
obj.location = 6.83089542388916, -1.9322376251220703, 1.4043397903442383
obj.scale = 0.9999999403953552, 0.9999999403953552, 1.0
obj.rotation_euler = 1.359418511390686, 0.006722021382302046, 1.2574377059936523
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(153 + frame)
obj = cameras['Camera']
obj.location = 6.817828178405762, -1.9306777715682983, 1.4055092334747314
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.363317847251892, 0.005789096001535654, 1.2612959146499634
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(154 + frame)
obj = cameras['Camera']
obj.location = 6.806610107421875, -1.9272197484970093, 1.4075971841812134
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.3659337759017944, 0.003007198916748166, 1.266741156578064
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(155 + frame)
obj = cameras['Camera']
obj.location = 6.795261383056641, -1.9228020906448364, 1.4101495742797852
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.367376685142517, 0.0007175285718403757, 1.2713218927383423
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(156 + frame)
obj = cameras['Camera']
obj.location = 6.783932685852051, -1.9181277751922607, 1.4122838973999023
obj.scale = 0.9999998807907104, 1.0000005960464478, 1.000000238418579
obj.rotation_euler = 1.368032693862915, -0.001579398987814784, 1.273431420326233
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(157 + frame)
obj = cameras['Camera']
obj.location = 6.772405624389648, -1.913562536239624, 1.4142940044403076
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.368140697479248, -0.001963928807526827, 1.2732218503952026
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(158 + frame)
obj = cameras['Camera']
obj.location = 6.759969711303711, -1.9092999696731567, 1.416208267211914
obj.scale = 0.9999999403953552, 1.0000005960464478, 1.0000005960464478
obj.rotation_euler = 1.368328332901001, -0.000515670224558562, 1.2712610960006714
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(159 + frame)
obj = cameras['Camera']
obj.location = 6.748143672943115, -1.9043995141983032, 1.4179415702819824
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3684272766113281, 0.003281738143414259, 1.2694069147109985
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(160 + frame)
obj = cameras['Camera']
obj.location = 6.735154628753662, -1.9004367589950562, 1.4202690124511719
obj.scale = 0.9999997019767761, 0.9999996423721313, 0.9999995231628418
obj.rotation_euler = 1.3698055744171143, 0.00683577498421073, 1.2686668634414673
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(161 + frame)
obj = cameras['Camera']
obj.location = 6.721437931060791, -1.8951706886291504, 1.4231090545654297
obj.scale = 0.9999998807907104, 1.0, 1.0
obj.rotation_euler = 1.3721928596496582, 0.008471564389765263, 1.2703322172164917
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(162 + frame)
obj = cameras['Camera']
obj.location = 6.706855773925781, -1.8913520574569702, 1.4253853559494019
obj.scale = 1.0000001192092896, 1.0000007152557373, 1.0000005960464478
obj.rotation_euler = 1.375522255897522, 0.008947199210524559, 1.273643136024475
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(163 + frame)
obj = cameras['Camera']
obj.location = 6.694153308868408, -1.8853093385696411, 1.4293289184570312
obj.scale = 0.9999999403953552, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3774889707565308, 0.006720595061779022, 1.280504584312439
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(164 + frame)
obj = cameras['Camera']
obj.location = 6.680752754211426, -1.8774336576461792, 1.4331989288330078
obj.scale = 1.0, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.378798007965088, 0.005195680074393749, 1.2852163314819336
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(165 + frame)
obj = cameras['Camera']
obj.location = 6.666961669921875, -1.868366003036499, 1.4368146657943726
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3793140649795532, 0.002238611923530698, 1.2873588800430298
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(166 + frame)
obj = cameras['Camera']
obj.location = 6.652163028717041, -1.8585675954818726, 1.4399735927581787
obj.scale = 1.0000003576278687, 1.000000238418579, 1.0
obj.rotation_euler = 1.3791369199752808, -0.0020723494235426188, 1.2872178554534912
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(167 + frame)
obj = cameras['Camera']
obj.location = 6.6371002197265625, -1.8484930992126465, 1.4428431987762451
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3777031898498535, -0.006158608011901379, 1.2854969501495361
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(168 + frame)
obj = cameras['Camera']
obj.location = 6.622061252593994, -1.8383365869522095, 1.4456055164337158
obj.scale = 1.000000238418579, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.375322937965393, -0.007318529766052961, 1.2825353145599365
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(169 + frame)
obj = cameras['Camera']
obj.location = 6.6061601638793945, -1.8282960653305054, 1.4482409954071045
obj.scale = 1.0, 1.0000005960464478, 1.0000004768371582
obj.rotation_euler = 1.3728101253509521, -0.008056621067225933, 1.2792623043060303
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(170 + frame)
obj = cameras['Camera']
obj.location = 6.591573238372803, -1.8178694248199463, 1.4514085054397583
obj.scale = 0.9999999403953552, 1.0000007152557373, 1.0000003576278687
obj.rotation_euler = 1.3695411682128906, -0.007410064339637756, 1.276535153388977
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(171 + frame)
obj = cameras['Camera']
obj.location = 6.575932025909424, -1.8080161809921265, 1.4542174339294434
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3669016361236572, -0.006840361747890711, 1.2746952772140503
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(172 + frame)
obj = cameras['Camera']
obj.location = 6.566871166229248, -1.800498366355896, 1.4549777507781982
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3620332479476929, -0.007053686305880547, 1.2731870412826538
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(173 + frame)
obj = cameras['Camera']
obj.location = 6.550086498260498, -1.7900326251983643, 1.4580371379852295
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.359868049621582, -0.007018521893769503, 1.2744150161743164
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(174 + frame)
obj = cameras['Camera']
obj.location = 6.535531520843506, -1.7790734767913818, 1.460777759552002
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.356593370437622, -0.00642441725358367, 1.2758815288543701
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(175 + frame)
obj = cameras['Camera']
obj.location = 6.519600868225098, -1.768385648727417, 1.4628807306289673
obj.scale = 0.9999998211860657, 1.0, 1.0
obj.rotation_euler = 1.353785514831543, -0.007016359828412533, 1.276869773864746
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(176 + frame)
obj = cameras['Camera']
obj.location = 6.503598690032959, -1.7577844858169556, 1.4643571376800537
obj.scale = 0.9999999403953552, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.3506516218185425, -0.005541176535189152, 1.2772033214569092
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(177 + frame)
obj = cameras['Camera']
obj.location = 6.488085746765137, -1.746667504310608, 1.465914249420166
obj.scale = 0.9999998807907104, 1.0, 0.9999999403953552
obj.rotation_euler = 1.347540259361267, -0.000924576714169234, 1.2774778604507446
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(178 + frame)
obj = cameras['Camera']
obj.location = 6.47344446182251, -1.7375415563583374, 1.4663259983062744
obj.scale = 0.9999999403953552, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3451074361801147, 0.002417811658233404, 1.2772647142410278
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(179 + frame)
obj = cameras['Camera']
obj.location = 6.458433628082275, -1.7263433933258057, 1.468320608139038
obj.scale = 1.0, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3444253206253052, 0.005590907298028469, 1.2792019844055176
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(180 + frame)
obj = cameras['Camera']
obj.location = 6.4437432289123535, -1.7171909809112549, 1.4698965549468994
obj.scale = 0.9999999403953552, 1.0000007152557373, 1.0000007152557373
obj.rotation_euler = 1.3460291624069214, 0.006530946120619774, 1.2826358079910278
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(181 + frame)
obj = cameras['Camera']
obj.location = 6.430800437927246, -1.7081266641616821, 1.4724756479263306
obj.scale = 1.0, 1.0, 0.9999998211860657
obj.rotation_euler = 1.348414421081543, 0.005357170011848211, 1.2893285751342773
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(182 + frame)
obj = cameras['Camera']
obj.location = 6.4173054695129395, -1.7002174854278564, 1.475450038909912
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3525201082229614, 0.0033737244084477425, 1.2977184057235718
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(183 + frame)
obj = cameras['Camera']
obj.location = 6.406156063079834, -1.6923549175262451, 1.4787089824676514
obj.scale = 1.0000001192092896, 1.0, 0.9999998211860657
obj.rotation_euler = 1.3566054105758667, 0.00022008377709425986, 1.3050206899642944
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(184 + frame)
obj = cameras['Camera']
obj.location = 6.393674373626709, -1.6846907138824463, 1.48191237449646
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3619829416275024, -0.002590942196547985, 1.3095955848693848
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(185 + frame)
obj = cameras['Camera']
obj.location = 6.382170677185059, -1.676145315170288, 1.4852731227874756
obj.scale = 1.000000238418579, 1.0, 1.0000003576278687
obj.rotation_euler = 1.366803765296936, -0.0060349409468472, 1.3116259574890137
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(186 + frame)
obj = cameras['Camera']
obj.location = 6.370512962341309, -1.6678814888000488, 1.4883474111557007
obj.scale = 0.9999998807907104, 0.9999998807907104, 1.0
obj.rotation_euler = 1.3724907636642456, -0.005870520602911711, 1.3109652996063232
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(187 + frame)
obj = cameras['Camera']
obj.location = 6.359144687652588, -1.6598138809204102, 1.4912903308868408
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3778284788131714, -0.0062744808383286, 1.3086621761322021
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(188 + frame)
obj = cameras['Camera']
obj.location = 6.346391677856445, -1.652355670928955, 1.494625210762024
obj.scale = 1.000000238418579, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.3838496208190918, -0.0073579601012170315, 1.3065083026885986
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(189 + frame)
obj = cameras['Camera']
obj.location = 6.335328102111816, -1.645102858543396, 1.498311161994934
obj.scale = 0.9999999403953552, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3893465995788574, -0.007074416149407625, 1.3055545091629028
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(190 + frame)
obj = cameras['Camera']
obj.location = 6.323001861572266, -1.6375519037246704, 1.502124309539795
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3949862718582153, -0.006645686458796263, 1.3062468767166138
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(191 + frame)
obj = cameras['Camera']
obj.location = 6.309440612792969, -1.6321349143981934, 1.5045737028121948
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.4005597829818726, -0.007044858764857054, 1.306510329246521
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(192 + frame)
obj = cameras['Camera']
obj.location = 6.296255588531494, -1.62534761428833, 1.5078012943267822
obj.scale = 0.9999998807907104, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4050227403640747, -0.006120803765952587, 1.3069758415222168
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(193 + frame)
obj = cameras['Camera']
obj.location = 6.2826948165893555, -1.620355486869812, 1.5109779834747314
obj.scale = 0.9999996423721313, 1.000000238418579, 1.0
obj.rotation_euler = 1.4087817668914795, -0.004873431287705898, 1.3065005540847778
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(194 + frame)
obj = cameras['Camera']
obj.location = 6.268101215362549, -1.6149811744689941, 1.5141141414642334
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4121052026748657, -0.004107911605387926, 1.3062398433685303
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(195 + frame)
obj = cameras['Camera']
obj.location = 6.253283977508545, -1.6111334562301636, 1.517244577407837
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4146465063095093, -0.002827101619914174, 1.3054118156433105
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(196 + frame)
obj = cameras['Camera']
obj.location = 6.238189697265625, -1.607391357421875, 1.5202136039733887
obj.scale = 0.9999998807907104, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4163963794708252, -0.0014523917343467474, 1.304705262184143
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(197 + frame)
obj = cameras['Camera']
obj.location = 6.223167896270752, -1.603325366973877, 1.5230717658996582
obj.scale = 1.0, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4174093008041382, 0.0012225218815729022, 1.3039215803146362
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(198 + frame)
obj = cameras['Camera']
obj.location = 6.208019256591797, -1.5999177694320679, 1.5254698991775513
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4179961681365967, 0.004748981911689043, 1.3025671243667603
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(199 + frame)
obj = cameras['Camera']
obj.location = 6.19246244430542, -1.5967340469360352, 1.527238130569458
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4185222387313843, 0.008743997663259506, 1.300823450088501
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(200 + frame)
obj = cameras['Camera']
obj.location = 6.175480842590332, -1.5946533679962158, 1.5285431146621704
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.4195750951766968, 0.011607964523136616, 1.2989884614944458
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(201 + frame)
obj = cameras['Camera']
obj.location = 6.159449577331543, -1.592139720916748, 1.5294283628463745
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4203464984893799, 0.013188003562390804, 1.2984455823898315
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(202 + frame)
obj = cameras['Camera']
obj.location = 6.1433539390563965, -1.5897072553634644, 1.5299171209335327
obj.scale = 1.0, 0.9999998807907104, 1.0000001192092896
obj.rotation_euler = 1.4212956428527832, 0.014114822261035442, 1.2992392778396606
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(203 + frame)
obj = cameras['Camera']
obj.location = 6.126676559448242, -1.5869492292404175, 1.529484510421753
obj.scale = 0.9999999403953552, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.4226139783859253, 0.01462942361831665, 1.3006623983383179
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(204 + frame)
obj = cameras['Camera']
obj.location = 6.110565185546875, -1.5844330787658691, 1.5283886194229126
obj.scale = 0.9999998807907104, 0.9999998807907104, 1.0
obj.rotation_euler = 1.4235411882400513, 0.015108280815184116, 1.301638126373291
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(205 + frame)
obj = cameras['Camera']
obj.location = 6.09420919418335, -1.583234190940857, 1.5265543460845947
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.424200415611267, 0.017288455739617348, 1.300999641418457
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(206 + frame)
obj = cameras['Camera']
obj.location = 6.078210353851318, -1.582162857055664, 1.5239322185516357
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4244840145111084, 0.019775008782744408, 1.2992826700210571
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(207 + frame)
obj = cameras['Camera']
obj.location = 6.063065528869629, -1.5809873342514038, 1.5207592248916626
obj.scale = 0.9999998211860657, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.4235508441925049, 0.027073724195361137, 1.2951289415359497
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(208 + frame)
obj = cameras['Camera']
obj.location = 6.048218727111816, -1.5797864198684692, 1.517816424369812
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4229875802993774, 0.0310450941324234, 1.290757179260254
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(209 + frame)
obj = cameras['Camera']
obj.location = 6.03360652923584, -1.5789222717285156, 1.5139806270599365
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.423225998878479, 0.03457769379019737, 1.2880886793136597
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(210 + frame)
obj = cameras['Camera']
obj.location = 6.019510269165039, -1.5790330171585083, 1.5109264850616455
obj.scale = 0.9999998211860657, 0.9999997019767761, 0.9999997615814209
obj.rotation_euler = 1.424093246459961, 0.037625834345817566, 1.2876282930374146
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(211 + frame)
obj = cameras['Camera']
obj.location = 6.006059169769287, -1.5793237686157227, 1.5073530673980713
obj.scale = 0.9999996423721313, 0.9999997019767761, 0.9999996423721313
obj.rotation_euler = 1.4253654479980469, 0.03985932841897011, 1.2889740467071533
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(212 + frame)
obj = cameras['Camera']
obj.location = 5.9917521476745605, -1.5806376934051514, 1.5032432079315186
obj.scale = 1.0, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4274888038635254, 0.0412229523062706, 1.2911046743392944
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(213 + frame)
obj = cameras['Camera']
obj.location = 5.978789329528809, -1.580201506614685, 1.4987263679504395
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4291287660598755, 0.04291035607457161, 1.2943121194839478
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(214 + frame)
obj = cameras['Camera']
obj.location = 5.966052055358887, -1.5789039134979248, 1.4937286376953125
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4303045272827148, 0.045308127999305725, 1.2971649169921875
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(215 + frame)
obj = cameras['Camera']
obj.location = 5.952914237976074, -1.5786628723144531, 1.4882609844207764
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.4311964511871338, 0.0475885272026062, 1.2984395027160645
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(216 + frame)
obj = cameras['Camera']
obj.location = 5.940126419067383, -1.5779496431350708, 1.481608510017395
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4317570924758911, 0.04782100021839142, 1.2992597818374634
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(217 + frame)
obj = cameras['Camera']
obj.location = 5.927642822265625, -1.5766199827194214, 1.4755629301071167
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.432197093963623, 0.04625631496310234, 1.3006887435913086
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(218 + frame)
obj = cameras['Camera']
obj.location = 5.9149346351623535, -1.5763256549835205, 1.4694706201553345
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.4329097270965576, 0.043926432728767395, 1.302297592163086
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(219 + frame)
obj = cameras['Camera']
obj.location = 5.902390956878662, -1.5752642154693604, 1.4633429050445557
obj.scale = 1.0, 0.9999996423721313, 0.9999995827674866
obj.rotation_euler = 1.434172511100769, 0.03791433572769165, 1.3063983917236328
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(220 + frame)
obj = cameras['Camera']
obj.location = 5.890437126159668, -1.5733476877212524, 1.4571075439453125
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.4348701238632202, 0.03786962106823921, 1.3109605312347412
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(221 + frame)
obj = cameras['Camera']
obj.location = 5.878163814544678, -1.5716758966445923, 1.4505054950714111
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.4351940155029297, 0.037904947996139526, 1.314761996269226
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(222 + frame)
obj = cameras['Camera']
obj.location = 5.867358207702637, -1.5695178508758545, 1.4433010816574097
obj.scale = 1.0000003576278687, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.4340341091156006, 0.0372612401843071, 1.3162994384765625
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(223 + frame)
obj = cameras['Camera']
obj.location = 5.855620384216309, -1.5683696269989014, 1.437730312347412
obj.scale = 1.000000238418579, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.4325424432754517, 0.03731488436460495, 1.3147428035736084
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(224 + frame)
obj = cameras['Camera']
obj.location = 5.843482971191406, -1.5679283142089844, 1.4327833652496338
obj.scale = 0.9999998211860657, 0.9999999403953552, 1.000000238418579
obj.rotation_euler = 1.4309104681015015, 0.03603324666619301, 1.3123492002487183
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(225 + frame)
obj = cameras['Camera']
obj.location = 5.832269191741943, -1.565595269203186, 1.4284007549285889
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.429227590560913, 0.03509746119379997, 1.3120561838150024
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(226 + frame)
obj = cameras['Camera']
obj.location = 5.82014274597168, -1.5638971328735352, 1.4234731197357178
obj.scale = 1.0, 1.0000005960464478, 1.0000005960464478
obj.rotation_euler = 1.4283878803253174, 0.03290016949176788, 1.3136391639709473
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(227 + frame)
obj = cameras['Camera']
obj.location = 5.80697774887085, -1.5625979900360107, 1.4197008609771729
obj.scale = 1.0, 1.000000238418579, 1.0
obj.rotation_euler = 1.4281213283538818, 0.028950603678822517, 1.3172492980957031
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(228 + frame)
obj = cameras['Camera']
obj.location = 5.79319953918457, -1.561171054840088, 1.4161221981048584
obj.scale = 0.9999997019767761, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4277307987213135, 0.0244479738175869, 1.3221122026443481
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(229 + frame)
obj = cameras['Camera']
obj.location = 5.778852462768555, -1.5594496726989746, 1.4126631021499634
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.426716685295105, 0.02310619316995144, 1.326249361038208
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(230 + frame)
obj = cameras['Camera']
obj.location = 5.76416015625, -1.5578861236572266, 1.4094020128250122
obj.scale = 1.0, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.42486572265625, 0.021127872169017792, 1.3286492824554443
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(231 + frame)
obj = cameras['Camera']
obj.location = 5.749238967895508, -1.5556871891021729, 1.4063310623168945
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4225257635116577, 0.016226015985012054, 1.3293473720550537
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(232 + frame)
obj = cameras['Camera']
obj.location = 5.7363457679748535, -1.5531524419784546, 1.403346061706543
obj.scale = 1.0, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.418688178062439, 0.013896947726607323, 1.3285515308380127
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(233 + frame)
obj = cameras['Camera']
obj.location = 5.720233917236328, -1.5535871982574463, 1.4012607336044312
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0
obj.rotation_euler = 1.416179895401001, 0.011278174817562103, 1.3265289068222046
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(234 + frame)
obj = cameras['Camera']
obj.location = 5.7049055099487305, -1.5490163564682007, 1.3987234830856323
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.4131475687026978, 0.00972905382514, 1.3273311853408813
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(235 + frame)
obj = cameras['Camera']
obj.location = 5.688261985778809, -1.548818588256836, 1.3959877490997314
obj.scale = 1.0, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.410478115081787, 0.00670324731618166, 1.3272029161453247
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(236 + frame)
obj = cameras['Camera']
obj.location = 5.672652244567871, -1.5463639497756958, 1.392638921737671
obj.scale = 1.000000238418579, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.406809687614441, 0.0065434579737484455, 1.3280836343765259
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(237 + frame)
obj = cameras['Camera']
obj.location = 5.657051086425781, -1.5438902378082275, 1.3895313739776611
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.403173804283142, 0.006228617858141661, 1.3286739587783813
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(238 + frame)
obj = cameras['Camera']
obj.location = 5.641672134399414, -1.5409703254699707, 1.3864402770996094
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3997201919555664, 0.006409438326954842, 1.3291871547698975
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(239 + frame)
obj = cameras['Camera']
obj.location = 5.6252923011779785, -1.5386512279510498, 1.3837339878082275
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.3973963260650635, 0.007239844650030136, 1.3299922943115234
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(240 + frame)
obj = cameras['Camera']
obj.location = 5.608816623687744, -1.5369551181793213, 1.381560206413269
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.396041989326477, 0.0068260966800153255, 1.3317475318908691
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(241 + frame)
obj = cameras['Camera']
obj.location = 5.592764377593994, -1.5342780351638794, 1.3799153566360474
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3952651023864746, 0.007711844518780708, 1.3342796564102173
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(242 + frame)
obj = cameras['Camera']
obj.location = 5.575639724731445, -1.5326389074325562, 1.378516674041748
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3953120708465576, 0.009064129553735256, 1.336196780204773
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(243 + frame)
obj = cameras['Camera']
obj.location = 5.560014724731445, -1.5296032428741455, 1.3769797086715698
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.3949689865112305, 0.01099987979978323, 1.3384937047958374
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(244 + frame)
obj = cameras['Camera']
obj.location = 5.543896675109863, -1.5282189846038818, 1.3765065670013428
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3951560258865356, 0.013306282460689545, 1.3401356935501099
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(245 + frame)
obj = cameras['Camera']
obj.location = 5.527956485748291, -1.5256649255752563, 1.3768373727798462
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.395666241645813, 0.018300652503967285, 1.3427776098251343
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(246 + frame)
obj = cameras['Camera']
obj.location = 5.512613773345947, -1.5221664905548096, 1.3769056797027588
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.396502137184143, 0.02350703813135624, 1.3465808629989624
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(247 + frame)
obj = cameras['Camera']
obj.location = 5.49614953994751, -1.5187088251113892, 1.3784499168395996
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3983783721923828, 0.025914238765835762, 1.3511135578155518
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(248 + frame)
obj = cameras['Camera']
obj.location = 5.47935152053833, -1.5156941413879395, 1.3809746503829956
obj.scale = 1.0, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.4003651142120361, 0.02800785005092621, 1.3554800748825073
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(249 + frame)
obj = cameras['Camera']
obj.location = 5.462192535400391, -1.5110546350479126, 1.3838238716125488
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.4028042554855347, 0.029536228626966476, 1.3608840703964233
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(250 + frame)
obj = cameras['Camera']
obj.location = 5.441715717315674, -1.5118093490600586, 1.3883519172668457
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4069275856018066, 0.029499612748622894, 1.3630528450012207
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(251 + frame)
obj = cameras['Camera']
obj.location = 5.423540115356445, -1.5063132047653198, 1.3918427228927612
obj.scale = 0.9999999403953552, 1.0000004768371582, 1.0000007152557373
obj.rotation_euler = 1.410037875175476, 0.02976818010210991, 1.366344928741455
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(252 + frame)
obj = cameras['Camera']
obj.location = 5.4049153327941895, -1.500571846961975, 1.397119402885437
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4132241010665894, 0.02953951247036457, 1.3675763607025146
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(253 + frame)
obj = cameras['Camera']
obj.location = 5.386360168457031, -1.4943188428878784, 1.4028830528259277
obj.scale = 1.0, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.417102575302124, 0.030029289424419403, 1.367307424545288
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(254 + frame)
obj = cameras['Camera']
obj.location = 5.3673787117004395, -1.4866728782653809, 1.409461259841919
obj.scale = 1.000000238418579, 0.9999998807907104, 1.0000001192092896
obj.rotation_euler = 1.4202251434326172, 0.03057888150215149, 1.3665612936019897
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(255 + frame)
obj = cameras['Camera']
obj.location = 5.34863805770874, -1.4793643951416016, 1.415881872177124
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.423181176185608, 0.030779534950852394, 1.365847110748291
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(256 + frame)
obj = cameras['Camera']
obj.location = 5.329787254333496, -1.472306728363037, 1.4225897789001465
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4259226322174072, 0.031558770686388016, 1.3647918701171875
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(257 + frame)
obj = cameras['Camera']
obj.location = 5.311064720153809, -1.463887333869934, 1.4290897846221924
obj.scale = 1.0, 0.9999995827674866, 0.9999995827674866
obj.rotation_euler = 1.427812099456787, 0.03383418917655945, 1.3639748096466064
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(258 + frame)
obj = cameras['Camera']
obj.location = 5.292675018310547, -1.4548991918563843, 1.4362244606018066
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999997615814209
obj.rotation_euler = 1.4288325309753418, 0.03603667393326759, 1.3632514476776123
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(259 + frame)
obj = cameras['Camera']
obj.location = 5.274576663970947, -1.4452598094940186, 1.4422821998596191
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.4293346405029297, 0.038646191358566284, 1.3634777069091797
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(260 + frame)
obj = cameras['Camera']
obj.location = 5.2566142082214355, -1.4364936351776123, 1.4487111568450928
obj.scale = 1.000000238418579, 1.000000238418579, 1.0
obj.rotation_euler = 1.4298961162567139, 0.040589261800050735, 1.3649367094039917
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(261 + frame)
obj = cameras['Camera']
obj.location = 5.2385334968566895, -1.427691102027893, 1.4552152156829834
obj.scale = 1.0000003576278687, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.4305381774902344, 0.041886553168296814, 1.3681142330169678
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(262 + frame)
obj = cameras['Camera']
obj.location = 5.219997406005859, -1.4188249111175537, 1.461627721786499
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.431348443031311, 0.0419926643371582, 1.3725969791412354
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(263 + frame)
obj = cameras['Camera']
obj.location = 5.201176643371582, -1.4103091955184937, 1.4680222272872925
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.4320379495620728, 0.04129134491086006, 1.3772038221359253
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(264 + frame)
obj = cameras['Camera']
obj.location = 5.182391166687012, -1.4012579917907715, 1.474163293838501
obj.scale = 1.0000001192092896, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4322015047073364, 0.03860657662153244, 1.3821334838867188
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(265 + frame)
obj = cameras['Camera']
obj.location = 5.1627302169799805, -1.391830325126648, 1.4800910949707031
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.4324419498443604, 0.03614865243434906, 1.3860045671463013
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(266 + frame)
obj = cameras['Camera']
obj.location = 5.142922878265381, -1.3822077512741089, 1.4857423305511475
obj.scale = 0.9999998211860657, 0.9999995827674866, 0.9999998211860657
obj.rotation_euler = 1.432328462600708, 0.03487088531255722, 1.3884211778640747
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(267 + frame)
obj = cameras['Camera']
obj.location = 5.122584342956543, -1.372082233428955, 1.49111008644104
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4322715997695923, 0.03331761062145233, 1.3902264833450317
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(268 + frame)
obj = cameras['Camera']
obj.location = 5.102053165435791, -1.362322211265564, 1.4965403079986572
obj.scale = 1.0, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.432124137878418, 0.03006570227444172, 1.391993522644043
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(269 + frame)
obj = cameras['Camera']
obj.location = 5.080998420715332, -1.3524348735809326, 1.5019240379333496
obj.scale = 0.9999996423721313, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.4322155714035034, 0.026377933099865913, 1.3942452669143677
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(270 + frame)
obj = cameras['Camera']
obj.location = 5.059842586517334, -1.3426973819732666, 1.5073487758636475
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4324034452438354, 0.02423989400267601, 1.3965260982513428
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(271 + frame)
obj = cameras['Camera']
obj.location = 5.0384931564331055, -1.3327620029449463, 1.5126850605010986
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.4326798915863037, 0.02236614190042019, 1.398964524269104
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(272 + frame)
obj = cameras['Camera']
obj.location = 5.017086505889893, -1.3231136798858643, 1.517796277999878
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4331201314926147, 0.021306417882442474, 1.4008338451385498
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(273 + frame)
obj = cameras['Camera']
obj.location = 4.995351314544678, -1.3143858909606934, 1.5231389999389648
obj.scale = 0.9999998807907104, 1.0, 0.9999998211860657
obj.rotation_euler = 1.4336820840835571, 0.018098009750247, 1.403023600578308
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(274 + frame)
obj = cameras['Camera']
obj.location = 4.974172592163086, -1.3035846948623657, 1.527393102645874
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.433913230895996, 0.014505491591989994, 1.4065557718276978
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(275 + frame)
obj = cameras['Camera']
obj.location = 4.952582836151123, -1.2948108911514282, 1.5326266288757324
obj.scale = 1.0, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.434154987335205, 0.010860046371817589, 1.4099645614624023
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(276 + frame)
obj = cameras['Camera']
obj.location = 4.931384086608887, -1.2865498065948486, 1.5374643802642822
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.4341789484024048, 0.005530007649213076, 1.4135380983352661
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(277 + frame)
obj = cameras['Camera']
obj.location = 4.9098801612854, -1.2791006565093994, 1.5414230823516846
obj.scale = 0.9999998807907104, 0.9999997019767761, 0.9999998211860657
obj.rotation_euler = 1.4342864751815796, -0.0006958434241823852, 1.4168505668640137
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(278 + frame)
obj = cameras['Camera']
obj.location = 4.8887104988098145, -1.2716095447540283, 1.5456868410110474
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.4342577457427979, -0.003177128965035081, 1.4196640253067017
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(279 + frame)
obj = cameras['Camera']
obj.location = 4.867728233337402, -1.2647068500518799, 1.549046516418457
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4339888095855713, -0.005273631773889065, 1.4222581386566162
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(280 + frame)
obj = cameras['Camera']
obj.location = 4.846108436584473, -1.2581453323364258, 1.5522825717926025
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.433764934539795, -0.010116291232407093, 1.4255316257476807
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(281 + frame)
obj = cameras['Camera']
obj.location = 4.824437141418457, -1.2523739337921143, 1.55513596534729
obj.scale = 1.0, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4334264993667603, -0.013568895868957043, 1.4288493394851685
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(282 + frame)
obj = cameras['Camera']
obj.location = 4.803397178649902, -1.2473894357681274, 1.5577112436294556
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.4320240020751953, -0.016146285459399223, 1.432479739189148
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(283 + frame)
obj = cameras['Camera']
obj.location = 4.782064914703369, -1.2423136234283447, 1.5594947338104248
obj.scale = 1.0, 0.9999999403953552, 1.0
obj.rotation_euler = 1.4302157163619995, -0.018107466399669647, 1.4369192123413086
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(284 + frame)
obj = cameras['Camera']
obj.location = 4.760693550109863, -1.2366032600402832, 1.5603432655334473
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.428467035293579, -0.019461747258901596, 1.4415719509124756
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(285 + frame)
obj = cameras['Camera']
obj.location = 4.739494800567627, -1.2322490215301514, 1.5617330074310303
obj.scale = 1.000000238418579, 0.9999998211860657, 1.0000001192092896
obj.rotation_euler = 1.4268302917480469, -0.02001134119927883, 1.4454530477523804
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(286 + frame)
obj = cameras['Camera']
obj.location = 4.718588829040527, -1.2270145416259766, 1.5619251728057861
obj.scale = 1.0000001192092896, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.425423264503479, -0.02052042819559574, 1.4493354558944702
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(287 + frame)
obj = cameras['Camera']
obj.location = 4.697873592376709, -1.2224156856536865, 1.5629856586456299
obj.scale = 0.9999998211860657, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4244132041931152, -0.021911734715104103, 1.4529306888580322
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(288 + frame)
obj = cameras['Camera']
obj.location = 4.677556037902832, -1.217246413230896, 1.5636706352233887
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4237947463989258, -0.023505141958594322, 1.4566349983215332
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(289 + frame)
obj = cameras['Camera']
obj.location = 4.6576080322265625, -1.2118821144104004, 1.564561128616333
obj.scale = 0.9999999403953552, 1.000000238418579, 1.0
obj.rotation_euler = 1.4234873056411743, -0.025275366380810738, 1.4591866731643677
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(290 + frame)
obj = cameras['Camera']
obj.location = 4.637747764587402, -1.2066420316696167, 1.565356731414795
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4240567684173584, -0.026830805465579033, 1.460945725440979
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(291 + frame)
obj = cameras['Camera']
obj.location = 4.618314743041992, -1.201112985610962, 1.5662044286727905
obj.scale = 1.0000004768371582, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4249123334884644, -0.02837311662733555, 1.4624547958374023
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(292 + frame)
obj = cameras['Camera']
obj.location = 4.599149227142334, -1.1955169439315796, 1.5667951107025146
obj.scale = 1.000000238418579, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.4262244701385498, -0.029371459037065506, 1.4634088277816772
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(293 + frame)
obj = cameras['Camera']
obj.location = 4.580473899841309, -1.1901483535766602, 1.5674097537994385
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4279255867004395, -0.03076338768005371, 1.464341402053833
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(294 + frame)
obj = cameras['Camera']
obj.location = 4.562042713165283, -1.1851023435592651, 1.5679692029953003
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.4298186302185059, -0.031714726239442825, 1.4648215770721436
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(295 + frame)
obj = cameras['Camera']
obj.location = 4.544210910797119, -1.1798069477081299, 1.5684936046600342
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.432098388671875, -0.0319841243326664, 1.4659862518310547
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(296 + frame)
obj = cameras['Camera']
obj.location = 4.527336597442627, -1.174353837966919, 1.5688313245773315
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.4343477487564087, -0.0316220223903656, 1.4671882390975952
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(297 + frame)
obj = cameras['Camera']
obj.location = 4.510237693786621, -1.1693155765533447, 1.5696632862091064
obj.scale = 1.000000238418579, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4374643564224243, -0.030594635754823685, 1.468058466911316
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(298 + frame)
obj = cameras['Camera']
obj.location = 4.494041442871094, -1.1636877059936523, 1.5698301792144775
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4401977062225342, -0.029735257849097252, 1.4689147472381592
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(299 + frame)
obj = cameras['Camera']
obj.location = 4.477611064910889, -1.1581547260284424, 1.5705952644348145
obj.scale = 1.0000003576278687, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.4435436725616455, -0.027415383607149124, 1.4694005250930786
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(300 + frame)
obj = cameras['Camera']
obj.location = 4.461803436279297, -1.1534091234207153, 1.5704395771026611
obj.scale = 0.9999999403953552, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4464327096939087, -0.025478171184659004, 1.4697835445404053
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(301 + frame)
obj = cameras['Camera']
obj.location = 4.445167541503906, -1.1477574110031128, 1.5704982280731201
obj.scale = 1.000000238418579, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.4495861530303955, -0.022952841594815254, 1.470993161201477
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(302 + frame)
obj = cameras['Camera']
obj.location = 4.42862606048584, -1.1422317028045654, 1.5703928470611572
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.452505350112915, -0.019634876400232315, 1.471806287765503
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(303 + frame)
obj = cameras['Camera']
obj.location = 4.412151336669922, -1.1364037990570068, 1.5698068141937256
obj.scale = 1.000000238418579, 0.9999997019767761, 0.9999998807907104
obj.rotation_euler = 1.4549614191055298, -0.01674261875450611, 1.4722106456756592
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(304 + frame)
obj = cameras['Camera']
obj.location = 4.3952484130859375, -1.1305232048034668, 1.5683780908584595
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.0
obj.rotation_euler = 1.4573192596435547, -0.013427994213998318, 1.471981406211853
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(305 + frame)
obj = cameras['Camera']
obj.location = 4.378422737121582, -1.124394178390503, 1.5673027038574219
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.4592899084091187, -0.009942506439983845, 1.4713712930679321
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(306 + frame)
obj = cameras['Camera']
obj.location = 4.36160135269165, -1.1184908151626587, 1.5665993690490723
obj.scale = 0.9999998807907104, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.4607722759246826, -0.008571390062570572, 1.4702421426773071
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(307 + frame)
obj = cameras['Camera']
obj.location = 4.344363212585449, -1.111564040184021, 1.565500259399414
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4619539976119995, -0.008086009882390499, 1.469638705253601
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(308 + frame)
obj = cameras['Camera']
obj.location = 4.327319145202637, -1.105311393737793, 1.5648577213287354
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4627546072006226, -0.0059701669961214066, 1.4683730602264404
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(309 + frame)
obj = cameras['Camera']
obj.location = 4.309772491455078, -1.099007248878479, 1.5642610788345337
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.4633430242538452, -0.003582790493965149, 1.4678947925567627
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(310 + frame)
obj = cameras['Camera']
obj.location = 4.29237699508667, -1.0920931100845337, 1.563492774963379
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4637304544448853, 0.0006250360165722668, 1.468153476715088
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(311 + frame)
obj = cameras['Camera']
obj.location = 4.274567127227783, -1.0846450328826904, 1.5623236894607544
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4638659954071045, 0.0035627963952720165, 1.4690419435501099
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(312 + frame)
obj = cameras['Camera']
obj.location = 4.256006240844727, -1.076972484588623, 1.560895323753357
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4641305208206177, 0.005837616045027971, 1.4692957401275635
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(313 + frame)
obj = cameras['Camera']
obj.location = 4.238157749176025, -1.0692492723464966, 1.558638334274292
obj.scale = 0.9999998211860657, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.464106798171997, 0.008177883923053741, 1.4687467813491821
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(314 + frame)
obj = cameras['Camera']
obj.location = 4.220098495483398, -1.061571478843689, 1.5569806098937988
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.4641320705413818, 0.008868983946740627, 1.468414545059204
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(315 + frame)
obj = cameras['Camera']
obj.location = 4.202226638793945, -1.0542298555374146, 1.5553029775619507
obj.scale = 1.000000238418579, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.4639828205108643, 0.009209522046148777, 1.4682109355926514
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(316 + frame)
obj = cameras['Camera']
obj.location = 4.18472957611084, -1.0469944477081299, 1.553412675857544
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000004768371582
obj.rotation_euler = 1.4640477895736694, 0.010464705526828766, 1.4680932760238647
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(317 + frame)
obj = cameras['Camera']
obj.location = 4.16743278503418, -1.0400035381317139, 1.5515564680099487
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.46435546875, 0.011646140366792679, 1.4685691595077515
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(318 + frame)
obj = cameras['Camera']
obj.location = 4.150506019592285, -1.0324409008026123, 1.5499420166015625
obj.scale = 1.0, 0.9999997019767761, 1.0000001192092896
obj.rotation_euler = 1.46523916721344, 0.013289043679833412, 1.4698837995529175
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(319 + frame)
obj = cameras['Camera']
obj.location = 4.133623123168945, -1.0252530574798584, 1.547966718673706
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4666515588760376, 0.013954863883554935, 1.4714750051498413
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(320 + frame)
obj = cameras['Camera']
obj.location = 4.117203712463379, -1.0175914764404297, 1.5466142892837524
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4676766395568848, 0.01335067767649889, 1.4728336334228516
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(321 + frame)
obj = cameras['Camera']
obj.location = 4.101226806640625, -1.00931978225708, 1.5455424785614014
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.4686068296432495, 0.011538290418684483, 1.4732048511505127
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(322 + frame)
obj = cameras['Camera']
obj.location = 4.085473537445068, -1.0009026527404785, 1.5445516109466553
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4696799516677856, 0.007788348477333784, 1.4723217487335205
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(323 + frame)
obj = cameras['Camera']
obj.location = 4.070028781890869, -0.9929300546646118, 1.5450656414031982
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000004768371582
obj.rotation_euler = 1.4710524082183838, 0.00570865161716938, 1.4705262184143066
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(324 + frame)
obj = cameras['Camera']
obj.location = 4.05487060546875, -0.9858008623123169, 1.5450787544250488
obj.scale = 0.9999995827674866, 1.0, 0.9999998211860657
obj.rotation_euler = 1.4725979566574097, 0.005026059690862894, 1.4690988063812256
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(325 + frame)
obj = cameras['Camera']
obj.location = 4.03992223739624, -0.9782577753067017, 1.545208215713501
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4740808010101318, 0.0048242127522826195, 1.4694219827651978
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(326 + frame)
obj = cameras['Camera']
obj.location = 4.024551868438721, -0.9708789587020874, 1.5454821586608887
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.4758899211883545, 0.005316152703016996, 1.470628261566162
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(327 + frame)
obj = cameras['Camera']
obj.location = 4.009537696838379, -0.9631748199462891, 1.5456130504608154
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.4775335788726807, 0.00590071314945817, 1.4722529649734497
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(328 + frame)
obj = cameras['Camera']
obj.location = 3.9943737983703613, -0.9559597969055176, 1.5459102392196655
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.4790650606155396, 0.005946055520325899, 1.4735859632492065
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(329 + frame)
obj = cameras['Camera']
obj.location = 3.979647397994995, -0.9487558603286743, 1.5461307764053345
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4800562858581543, 0.005312836728990078, 1.4747982025146484
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(330 + frame)
obj = cameras['Camera']
obj.location = 3.9642629623413086, -0.9413630962371826, 1.546522617340088
obj.scale = 1.0, 1.0000005960464478, 1.0000007152557373
obj.rotation_euler = 1.4812408685684204, 0.004661065060645342, 1.4759535789489746
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(331 + frame)
obj = cameras['Camera']
obj.location = 3.948770761489868, -0.9349300861358643, 1.5472333431243896
obj.scale = 1.0000003576278687, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4822787046432495, 0.0038390913978219032, 1.476517915725708
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(332 + frame)
obj = cameras['Camera']
obj.location = 3.933438777923584, -0.928623378276825, 1.5479990243911743
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.0
obj.rotation_euler = 1.4829083681106567, 0.0029844818636775017, 1.4773377180099487
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(333 + frame)
obj = cameras['Camera']
obj.location = 3.9175076484680176, -0.9223271608352661, 1.5488009452819824
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4836214780807495, 0.002174604218453169, 1.4785399436950684
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(334 + frame)
obj = cameras['Camera']
obj.location = 3.901740074157715, -0.9161900877952576, 1.549562931060791
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4838671684265137, 0.0012614767765626311, 1.479689359664917
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(335 + frame)
obj = cameras['Camera']
obj.location = 3.8854658603668213, -0.9105840921401978, 1.5509166717529297
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999996423721313
obj.rotation_euler = 1.4841678142547607, 0.00023654752294532955, 1.4807735681533813
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(336 + frame)
obj = cameras['Camera']
obj.location = 3.869137763977051, -0.9051438570022583, 1.5517261028289795
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4840744733810425, -0.0008437378564849496, 1.4819358587265015
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(337 + frame)
obj = cameras['Camera']
obj.location = 3.852776288986206, -0.8999689221382141, 1.5528762340545654
obj.scale = 0.9999997615814209, 0.9999995827674866, 0.9999998211860657
obj.rotation_euler = 1.4831714630126953, -0.002640236634761095, 1.4832240343093872
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(338 + frame)
obj = cameras['Camera']
obj.location = 3.8368217945098877, -0.8947065472602844, 1.5538779497146606
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4809861183166504, -0.004065705928951502, 1.4840689897537231
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(339 + frame)
obj = cameras['Camera']
obj.location = 3.821269989013672, -0.8897897601127625, 1.555442452430725
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.477687954902649, -0.006586840841919184, 1.4852107763290405
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(340 + frame)
obj = cameras['Camera']
obj.location = 3.8062546253204346, -0.8850102424621582, 1.5566562414169312
obj.scale = 1.000000238418579, 0.9999998807907104, 1.0
obj.rotation_euler = 1.4739323854446411, -0.0071513052098453045, 1.4866669178009033
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(341 + frame)
obj = cameras['Camera']
obj.location = 3.7908358573913574, -0.8798719644546509, 1.5582630634307861
obj.scale = 1.0, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4699387550354004, -0.007038137409836054, 1.4892513751983643
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(342 + frame)
obj = cameras['Camera']
obj.location = 3.7756340503692627, -0.8746264576911926, 1.5597116947174072
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.465416669845581, -0.0053903935477137566, 1.491809606552124
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(343 + frame)
obj = cameras['Camera']
obj.location = 3.7605655193328857, -0.8694509267807007, 1.5613288879394531
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4609674215316772, -0.003225629683583975, 1.4947911500930786
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(344 + frame)
obj = cameras['Camera']
obj.location = 3.7452728748321533, -0.8636107444763184, 1.56309175491333
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4565824270248413, -0.0013355884002521634, 1.4983034133911133
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(345 + frame)
obj = cameras['Camera']
obj.location = 3.730025053024292, -0.8574333190917969, 1.5649926662445068
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4522087574005127, 0.0009852126240730286, 1.5013023614883423
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(346 + frame)
obj = cameras['Camera']
obj.location = 3.7146124839782715, -0.8515812158584595, 1.56693696975708
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999997019767761
obj.rotation_euler = 1.4475780725479126, 0.0013858666643500328, 1.503668189048767
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(347 + frame)
obj = cameras['Camera']
obj.location = 3.699100971221924, -0.8449581265449524, 1.56868577003479
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4425708055496216, 0.0006737656658515334, 1.5054367780685425
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(348 + frame)
obj = cameras['Camera']
obj.location = 3.6833157539367676, -0.840002715587616, 1.5706684589385986
obj.scale = 0.9999997615814209, 0.9999995827674866, 0.9999996423721313
obj.rotation_euler = 1.4374923706054688, -0.002054054057225585, 1.5050368309020996
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(349 + frame)
obj = cameras['Camera']
obj.location = 3.6676671504974365, -0.8338180184364319, 1.5727323293685913
obj.scale = 1.0, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.4323561191558838, -0.004303690977394581, 1.5047067403793335
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(350 + frame)
obj = cameras['Camera']
obj.location = 3.6519217491149902, -0.829197108745575, 1.5750443935394287
obj.scale = 1.0, 1.0000004768371582, 1.000000238418579
obj.rotation_euler = 1.4274944067001343, -0.0062381853349506855, 1.5036873817443848
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(351 + frame)
obj = cameras['Camera']
obj.location = 3.636136054992676, -0.8251811265945435, 1.5777275562286377
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4230215549468994, -0.008042532950639725, 1.5033155679702759
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(352 + frame)
obj = cameras['Camera']
obj.location = 3.619947910308838, -0.8213076591491699, 1.580507755279541
obj.scale = 0.9999998807907104, 1.0, 1.0
obj.rotation_euler = 1.4190144538879395, -0.009461378678679466, 1.5033280849456787
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(353 + frame)
obj = cameras['Camera']
obj.location = 3.604004144668579, -0.817779541015625, 1.5836353302001953
obj.scale = 1.000000238418579, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4153684377670288, -0.0098178181797266, 1.5038028955459595
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(354 + frame)
obj = cameras['Camera']
obj.location = 3.587372064590454, -0.8143128156661987, 1.586817979812622
obj.scale = 0.9999997615814209, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.4126534461975098, -0.009219986386597157, 1.5044214725494385
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(355 + frame)
obj = cameras['Camera']
obj.location = 3.570188283920288, -0.8114980459213257, 1.590170979499817
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4106465578079224, -0.00804395042359829, 1.5047461986541748
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(356 + frame)
obj = cameras['Camera']
obj.location = 3.552669048309326, -0.8089370131492615, 1.5935752391815186
obj.scale = 1.0000003576278687, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4093517065048218, -0.0055573685094714165, 1.5045557022094727
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(357 + frame)
obj = cameras['Camera']
obj.location = 3.5349481105804443, -0.8069629073143005, 1.597031831741333
obj.scale = 1.0000001192092896, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4084593057632446, -0.004896164406090975, 1.5040439367294312
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(358 + frame)
obj = cameras['Camera']
obj.location = 3.5170159339904785, -0.8056020736694336, 1.6006466150283813
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4079415798187256, -0.004827618133276701, 1.5028756856918335
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(359 + frame)
obj = cameras['Camera']
obj.location = 3.4988608360290527, -0.8033205270767212, 1.6040337085723877
obj.scale = 1.0, 1.000000238418579, 1.0
obj.rotation_euler = 1.4075311422348022, -0.005365423858165741, 1.5005639791488647
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(360 + frame)
obj = cameras['Camera']
obj.location = 3.480329751968384, -0.8020275831222534, 1.6076371669769287
obj.scale = 1.0, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.4074703454971313, -0.00660628080368042, 1.4961845874786377
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(361 + frame)
obj = cameras['Camera']
obj.location = 3.4618051052093506, -0.8014627695083618, 1.6113675832748413
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.40752112865448, -0.007464136462658644, 1.4918431043624878
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(362 + frame)
obj = cameras['Camera']
obj.location = 3.4434642791748047, -0.8006662130355835, 1.615513801574707
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4076130390167236, -0.008011814206838608, 1.4876066446304321
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(363 + frame)
obj = cameras['Camera']
obj.location = 3.424649238586426, -0.8004374504089355, 1.619273066520691
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.408194899559021, -0.0070556700229644775, 1.4833996295928955
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(364 + frame)
obj = cameras['Camera']
obj.location = 3.4057846069335938, -0.8004595637321472, 1.6235653162002563
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.409178376197815, -0.006137761753052473, 1.479453206062317
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(365 + frame)
obj = cameras['Camera']
obj.location = 3.386913776397705, -0.8006027936935425, 1.6272096633911133
obj.scale = 1.0, 0.9999997019767761, 0.9999998211860657
obj.rotation_euler = 1.4101297855377197, -0.005004961974918842, 1.477595567703247
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(366 + frame)
obj = cameras['Camera']
obj.location = 3.3675899505615234, -0.8009974360466003, 1.6309846639633179
obj.scale = 1.0000001192092896, 0.9999997615814209, 1.0
obj.rotation_euler = 1.4112690687179565, -0.003413350088521838, 1.4771003723144531
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(367 + frame)
obj = cameras['Camera']
obj.location = 3.3469676971435547, -0.7946467399597168, 1.6315186023712158
obj.scale = 1.0000004768371582, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4122471809387207, -0.003035631263628602, 1.4776713848114014
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(368 + frame)
obj = cameras['Camera']
obj.location = 3.3263440132141113, -0.788541316986084, 1.6319355964660645
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4129146337509155, -0.002623002277687192, 1.478542685508728
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(369 + frame)
obj = cameras['Camera']
obj.location = 3.3056931495666504, -0.7829517126083374, 1.63223397731781
obj.scale = 1.0, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4131686687469482, -0.0022107555996626616, 1.4791524410247803
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(370 + frame)
obj = cameras['Camera']
obj.location = 3.284903049468994, -0.7790208458900452, 1.6324143409729004
obj.scale = 1.0, 0.9999998807907104, 0.9999997019767761
obj.rotation_euler = 1.4126465320587158, -0.001951501821167767, 1.478959560394287
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(371 + frame)
obj = cameras['Camera']
obj.location = 3.2598063945770264, -0.7720853686332703, 1.638708472251892
obj.scale = 0.9999837875366211, 0.9999824166297913, 0.9999849200248718
obj.rotation_euler = 1.4112683534622192, -0.0019382338505238295, 1.4770195484161377
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(372 + frame)
obj = cameras['Camera']
obj.location = 3.2392163276672363, -0.7757108211517334, 1.6342318058013916
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4102246761322021, -4.2165663671767106e-07, 1.4736981391906738
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(373 + frame)
obj = cameras['Camera']
obj.location = 3.218524694442749, -0.7790440917015076, 1.6297343969345093
obj.scale = 0.9999841451644897, 0.9999827742576599, 0.9999853372573853
obj.rotation_euler = 1.4091074466705322, 0.001947029959410429, 1.4703460931777954
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(374 + frame)
obj = cameras['Camera']
obj.location = 3.1980903148651123, -0.7829646468162537, 1.6258347034454346
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.407228946685791, 0.004648310132324696, 1.4676698446273804
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(375 + frame)
obj = cameras['Camera']
obj.location = 3.1772007942199707, -0.7868831157684326, 1.6219549179077148
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4050004482269287, 0.008292007260024548, 1.466369867324829
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(376 + frame)
obj = cameras['Camera']
obj.location = 3.1549322605133057, -0.7905569672584534, 1.6172144412994385
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4028398990631104, 0.012770155444741249, 1.4666502475738525
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(377 + frame)
obj = cameras['Camera']
obj.location = 3.1326136589050293, -0.793410062789917, 1.6124926805496216
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.4003918170928955, 0.01730971783399582, 1.4676910638809204
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(378 + frame)
obj = cameras['Camera']
obj.location = 3.110513925552368, -0.7945362329483032, 1.60707426071167
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3971017599105835, 0.021254489198327065, 1.468811273574829
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(379 + frame)
obj = cameras['Camera']
obj.location = 3.088257312774658, -0.7964372038841248, 1.6019561290740967
obj.scale = 1.0, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.3937745094299316, 0.024579113349318504, 1.4690254926681519
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(380 + frame)
obj = cameras['Camera']
obj.location = 3.065549373626709, -0.7966015338897705, 1.596742868423462
obj.scale = 1.0, 1.0000003576278687, 0.9999999403953552
obj.rotation_euler = 1.390651822090149, 0.027329254895448685, 1.469436764717102
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(381 + frame)
obj = cameras['Camera']
obj.location = 3.043012857437134, -0.7957369685173035, 1.5917398929595947
obj.scale = 1.0, 0.9999998211860657, 0.9999997019767761
obj.rotation_euler = 1.3876899480819702, 0.029122721403837204, 1.4695258140563965
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(382 + frame)
obj = cameras['Camera']
obj.location = 3.0206284523010254, -0.7943342924118042, 1.5872222185134888
obj.scale = 1.0000001192092896, 1.0, 0.9999998211860657
obj.rotation_euler = 1.3849332332611084, 0.029950134456157684, 1.4688421487808228
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(383 + frame)
obj = cameras['Camera']
obj.location = 2.9979333877563477, -0.7925218343734741, 1.5830936431884766
obj.scale = 1.000000238418579, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.3828169107437134, 0.030012967064976692, 1.4675122499465942
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(384 + frame)
obj = cameras['Camera']
obj.location = 2.9745430946350098, -0.7919436693191528, 1.5798513889312744
obj.scale = 0.9999999403953552, 1.0, 0.9999997019767761
obj.rotation_euler = 1.3811166286468506, 0.029511192813515663, 1.4655293226242065
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(385 + frame)
obj = cameras['Camera']
obj.location = 2.952375888824463, -0.7901365756988525, 1.5772894620895386
obj.scale = 0.9999998807907104, 0.9999998807907104, 1.0
obj.rotation_euler = 1.379587173461914, 0.02937338873744011, 1.4641776084899902
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(386 + frame)
obj = cameras['Camera']
obj.location = 2.9287526607513428, -0.7894153594970703, 1.5756924152374268
obj.scale = 0.9999999403953552, 1.0, 1.0
obj.rotation_euler = 1.3785699605941772, 0.02960759587585926, 1.4632993936538696
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(387 + frame)
obj = cameras['Camera']
obj.location = 2.904262065887451, -0.7886358499526978, 1.574399709701538
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3778716325759888, 0.030145492404699326, 1.4631948471069336
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(388 + frame)
obj = cameras['Camera']
obj.location = 2.8800137042999268, -0.7874533534049988, 1.5731333494186401
obj.scale = 1.0000001192092896, 0.9999995231628418, 0.9999997615814209
obj.rotation_euler = 1.377036213874817, 0.030872704461216927, 1.463557243347168
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(389 + frame)
obj = cameras['Camera']
obj.location = 2.855320692062378, -0.7863506078720093, 1.5723568201065063
obj.scale = 0.9999998807907104, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3761777877807617, 0.031421031802892685, 1.4640944004058838
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(390 + frame)
obj = cameras['Camera']
obj.location = 2.830052375793457, -0.7851533889770508, 1.5719902515411377
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.375413179397583, 0.03150203078985214, 1.4646471738815308
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(391 + frame)
obj = cameras['Camera']
obj.location = 2.8041820526123047, -0.7838342189788818, 1.5721503496170044
obj.scale = 1.0, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3747025728225708, 0.030988382175564766, 1.4650651216506958
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(392 + frame)
obj = cameras['Camera']
obj.location = 2.7783102989196777, -0.7824012041091919, 1.5727611780166626
obj.scale = 0.9999999403953552, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3739386796951294, 0.030349910259246826, 1.4653260707855225
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(393 + frame)
obj = cameras['Camera']
obj.location = 2.752141237258911, -0.7809078097343445, 1.573984146118164
obj.scale = 1.0, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3731746673583984, 0.02969629317522049, 1.4654631614685059
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(394 + frame)
obj = cameras['Camera']
obj.location = 2.7256569862365723, -0.7794142961502075, 1.575904130935669
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.3725744485855103, 0.029628818854689598, 1.4653066396713257
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(395 + frame)
obj = cameras['Camera']
obj.location = 2.6995115280151367, -0.7784429788589478, 1.5786434412002563
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.3717548847198486, 0.030522840097546577, 1.4652491807937622
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(396 + frame)
obj = cameras['Camera']
obj.location = 2.672650098800659, -0.7768038511276245, 1.5815074443817139
obj.scale = 1.000000238418579, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.371402382850647, 0.03247504681348801, 1.4658169746398926
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(397 + frame)
obj = cameras['Camera']
obj.location = 2.6456544399261475, -0.7750455141067505, 1.5847752094268799
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.3711862564086914, 0.034916285425424576, 1.4666249752044678
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(398 + frame)
obj = cameras['Camera']
obj.location = 2.6180198192596436, -0.7725940942764282, 1.5881128311157227
obj.scale = 1.0, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3710851669311523, 0.03784269839525223, 1.4676352739334106
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(399 + frame)
obj = cameras['Camera']
obj.location = 2.5896894931793213, -0.7702549695968628, 1.591387391090393
obj.scale = 0.9999999403953552, 0.9999995231628418, 0.9999995231628418
obj.rotation_euler = 1.371242642402649, 0.040465209633111954, 1.4684120416641235
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(400 + frame)
obj = cameras['Camera']
obj.location = 2.562105655670166, -0.7670269012451172, 1.59437894821167
obj.scale = 1.0000001192092896, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3713895082473755, 0.04170976206660271, 1.4687386751174927
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(401 + frame)
obj = cameras['Camera']
obj.location = 2.532594680786133, -0.7617884874343872, 1.597489833831787
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.373022198677063, 0.041095223277807236, 1.4655641317367554
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(402 + frame)
obj = cameras['Camera']
obj.location = 2.5040125846862793, -0.7586368918418884, 1.6009671688079834
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3732961416244507, 0.03815184533596039, 1.4591790437698364
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(403 + frame)
obj = cameras['Camera']
obj.location = 2.475022792816162, -0.7582541704177856, 1.6053962707519531
obj.scale = 0.9999999403953552, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.3734214305877686, 0.03550708293914795, 1.4521352052688599
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(404 + frame)
obj = cameras['Camera']
obj.location = 2.446604013442993, -0.7586457133293152, 1.610509991645813
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3735967874526978, 0.03486291691660881, 1.4485729932785034
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(405 + frame)
obj = cameras['Camera']
obj.location = 2.4180357456207275, -0.7596576809883118, 1.6154502630233765
obj.scale = 1.0000003576278687, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3739650249481201, 0.03643215447664261, 1.4483397006988525
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(406 + frame)
obj = cameras['Camera']
obj.location = 2.389352798461914, -0.7593199014663696, 1.619920015335083
obj.scale = 0.9999998807907104, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3746037483215332, 0.03911115601658821, 1.4505878686904907
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(407 + frame)
obj = cameras['Camera']
obj.location = 2.3607935905456543, -0.7571114301681519, 1.6237891912460327
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3753679990768433, 0.04155451059341431, 1.4532902240753174
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(408 + frame)
obj = cameras['Camera']
obj.location = 2.3329310417175293, -0.7534785866737366, 1.6271259784698486
obj.scale = 1.0, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3759801387786865, 0.042466722428798676, 1.4543647766113281
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(409 + frame)
obj = cameras['Camera']
obj.location = 2.305755138397217, -0.7490886449813843, 1.6310657262802124
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.376383900642395, 0.041932910680770874, 1.4532769918441772
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(410 + frame)
obj = cameras['Camera']
obj.location = 2.278264284133911, -0.7464685440063477, 1.6354997158050537
obj.scale = 1.0, 0.9999996423721313, 0.9999995827674866
obj.rotation_euler = 1.376888394355774, 0.04100126028060913, 1.4512015581130981
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(411 + frame)
obj = cameras['Camera']
obj.location = 2.251361846923828, -0.742688775062561, 1.6398981809616089
obj.scale = 1.0000001192092896, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3774421215057373, 0.04056262969970703, 1.4499832391738892
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(412 + frame)
obj = cameras['Camera']
obj.location = 2.2255170345306396, -0.7384066581726074, 1.6443147659301758
obj.scale = 1.0, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.377767562866211, 0.03959041088819504, 1.4488515853881836
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(413 + frame)
obj = cameras['Camera']
obj.location = 2.1997227668762207, -0.7340402603149414, 1.649073839187622
obj.scale = 1.000000238418579, 1.0, 1.000000238418579
obj.rotation_euler = 1.3780027627944946, 0.03839748725295067, 1.4475055932998657
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(414 + frame)
obj = cameras['Camera']
obj.location = 2.1748170852661133, -0.7295924425125122, 1.653927206993103
obj.scale = 1.0, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3781194686889648, 0.0374784991145134, 1.446959137916565
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(415 + frame)
obj = cameras['Camera']
obj.location = 2.150421619415283, -0.7255906462669373, 1.6587612628936768
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.378143072128296, 0.037710949778556824, 1.4476431608200073
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(416 + frame)
obj = cameras['Camera']
obj.location = 2.1266722679138184, -0.7209544777870178, 1.6632697582244873
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000004768371582
obj.rotation_euler = 1.378145456314087, 0.03843788802623749, 1.4497485160827637
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(417 + frame)
obj = cameras['Camera']
obj.location = 2.1036295890808105, -0.7163630127906799, 1.6677873134613037
obj.scale = 1.0000001192092896, 0.9999995827674866, 0.9999998211860657
obj.rotation_euler = 1.3780670166015625, 0.03951442241668701, 1.4530436992645264
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(418 + frame)
obj = cameras['Camera']
obj.location = 2.080343008041382, -0.7124684453010559, 1.6721584796905518
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3781410455703735, 0.041364602744579315, 1.4573684930801392
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(419 + frame)
obj = cameras['Camera']
obj.location = 2.058234453201294, -0.7082638740539551, 1.6746456623077393
obj.scale = 1.0, 0.9999997019767761, 0.9999995231628418
obj.rotation_euler = 1.3782508373260498, 0.044032588601112366, 1.4631764888763428
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(420 + frame)
obj = cameras['Camera']
obj.location = 2.035550594329834, -0.7034841775894165, 1.6781463623046875
obj.scale = 1.0000001192092896, 1.0000005960464478, 1.0000004768371582
obj.rotation_euler = 1.3790301084518433, 0.04685145244002342, 1.4698246717453003
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(421 + frame)
obj = cameras['Camera']
obj.location = 2.013277530670166, -0.6983928680419922, 1.6809024810791016
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.000000238418579
obj.rotation_euler = 1.3799309730529785, 0.04863810911774635, 1.4761101007461548
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(422 + frame)
obj = cameras['Camera']
obj.location = 1.9917353391647339, -0.692751407623291, 1.6828486919403076
obj.scale = 1.0000001192092896, 1.0000007152557373, 1.0000005960464478
obj.rotation_euler = 1.3806394338607788, 0.04854399710893631, 1.4809774160385132
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(423 + frame)
obj = cameras['Camera']
obj.location = 1.9702613353729248, -0.6874772310256958, 1.6843154430389404
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.381211519241333, 0.04649152234196663, 1.4839106798171997
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(424 + frame)
obj = cameras['Camera']
obj.location = 1.9496467113494873, -0.682462751865387, 1.685090184211731
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3817213773727417, 0.04320725426077843, 1.4847966432571411
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(425 + frame)
obj = cameras['Camera']
obj.location = 1.9286906719207764, -0.6782518029212952, 1.6852141618728638
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3823637962341309, 0.03911609575152397, 1.4841535091400146
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(426 + frame)
obj = cameras['Camera']
obj.location = 1.9075913429260254, -0.6763889789581299, 1.685208797454834
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3832931518554688, 0.035403184592723846, 1.4838210344314575
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(427 + frame)
obj = cameras['Camera']
obj.location = 1.8907113075256348, -0.6737926602363586, 1.6847574710845947
obj.scale = 0.9999999403953552, 0.9999999403953552, 1.0
obj.rotation_euler = 1.383042335510254, 0.03246458247303963, 1.4854869842529297
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(428 + frame)
obj = cameras['Camera']
obj.location = 1.8724247217178345, -0.6724141836166382, 1.6817259788513184
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.3834556341171265, 0.029935650527477264, 1.4883531332015991
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(429 + frame)
obj = cameras['Camera']
obj.location = 1.8543494939804077, -0.6692584156990051, 1.6791203022003174
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3838287591934204, 0.027459140866994858, 1.4921345710754395
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(430 + frame)
obj = cameras['Camera']
obj.location = 1.8374860286712646, -0.6663939952850342, 1.6764229536056519
obj.scale = 1.0, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.383501648902893, 0.024100402370095253, 1.494652509689331
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(431 + frame)
obj = cameras['Camera']
obj.location = 1.8196823596954346, -0.6639108657836914, 1.6725035905838013
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3828837871551514, 0.01895207352936268, 1.4950261116027832
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(432 + frame)
obj = cameras['Camera']
obj.location = 1.8028311729431152, -0.6604567170143127, 1.66878342628479
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3816981315612793, 0.013399184681475163, 1.493937611579895
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(433 + frame)
obj = cameras['Camera']
obj.location = 1.7843561172485352, -0.6565163135528564, 1.6643832921981812
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.381141185760498, 0.008150952868163586, 1.4927228689193726
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(434 + frame)
obj = cameras['Camera']
obj.location = 1.7663824558258057, -0.651584267616272, 1.6611837148666382
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3805183172225952, 0.004040778148919344, 1.4922502040863037
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(435 + frame)
obj = cameras['Camera']
obj.location = 1.748159646987915, -0.6467961668968201, 1.6577495336532593
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3801779747009277, 0.0009897620184347034, 1.4919936656951904
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(436 + frame)
obj = cameras['Camera']
obj.location = 1.7286388874053955, -0.6411529779434204, 1.6542381048202515
obj.scale = 0.9999999403953552, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.3801764249801636, -0.0018986964132636786, 1.4911545515060425
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(437 + frame)
obj = cameras['Camera']
obj.location = 1.709206461906433, -0.6339396238327026, 1.651124119758606
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3801730871200562, -0.005022687371820211, 1.4884459972381592
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(438 + frame)
obj = cameras['Camera']
obj.location = 1.6885274648666382, -0.6269134283065796, 1.6482245922088623
obj.scale = 1.000000238418579, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.3804188966751099, -0.008908476680517197, 1.483147144317627
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(439 + frame)
obj = cameras['Camera']
obj.location = 1.6683043241500854, -0.6206027269363403, 1.6455470323562622
obj.scale = 1.0000001192092896, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3805705308914185, -0.012541553005576134, 1.4760706424713135
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(440 + frame)
obj = cameras['Camera']
obj.location = 1.6472796201705933, -0.6145372986793518, 1.6428964138031006
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.3807352781295776, -0.014676100574433804, 1.4696317911148071
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(441 + frame)
obj = cameras['Camera']
obj.location = 1.627149224281311, -0.6091783046722412, 1.6399688720703125
obj.scale = 1.0000004768371582, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.38048255443573, -0.014154894277453423, 1.4650448560714722
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(442 + frame)
obj = cameras['Camera']
obj.location = 1.6053966283798218, -0.6026422381401062, 1.6376547813415527
obj.scale = 1.0000003576278687, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.380385160446167, -0.010580673813819885, 1.4639146327972412
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(443 + frame)
obj = cameras['Camera']
obj.location = 1.5854227542877197, -0.5969216823577881, 1.6356656551361084
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.379652976989746, -0.0048796264454722404, 1.4647412300109863
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(444 + frame)
obj = cameras['Camera']
obj.location = 1.564098596572876, -0.5881572961807251, 1.6344878673553467
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3794673681259155, 0.0010006721131503582, 1.4672448635101318
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(445 + frame)
obj = cameras['Camera']
obj.location = 1.5437610149383545, -0.578721284866333, 1.6338083744049072
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.379129409790039, 0.005730777513235807, 1.4688552618026733
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(446 + frame)
obj = cameras['Camera']
obj.location = 1.523047685623169, -0.5688027739524841, 1.6331347227096558
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3788620233535767, 0.008363494649529457, 1.4694545269012451
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(447 + frame)
obj = cameras['Camera']
obj.location = 1.5032860040664673, -0.55858314037323, 1.6326204538345337
obj.scale = 1.0000001192092896, 0.9999998807907104, 1.0000001192092896
obj.rotation_euler = 1.3785004615783691, 0.009854798205196857, 1.4698853492736816
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(448 + frame)
obj = cameras['Camera']
obj.location = 1.4834164381027222, -0.5507546663284302, 1.632191777229309
obj.scale = 1.0, 1.0, 1.000000238418579
obj.rotation_euler = 1.3783643245697021, 0.011315896175801754, 1.4710521697998047
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(449 + frame)
obj = cameras['Camera']
obj.location = 1.4645265340805054, -0.5418651103973389, 1.6311304569244385
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.3780696392059326, 0.012835323810577393, 1.4741228818893433
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(450 + frame)
obj = cameras['Camera']
obj.location = 1.445295810699463, -0.5338176488876343, 1.629802942276001
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3780019283294678, 0.013850420713424683, 1.478181004524231
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(451 + frame)
obj = cameras['Camera']
obj.location = 1.4267312288284302, -0.5239037871360779, 1.6277492046356201
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999997019767761
obj.rotation_euler = 1.3771833181381226, 0.014505135826766491, 1.4826722145080566
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(452 + frame)
obj = cameras['Camera']
obj.location = 1.407231330871582, -0.5148324966430664, 1.6244338750839233
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3761217594146729, 0.013244557194411755, 1.4858430624008179
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(453 + frame)
obj = cameras['Camera']
obj.location = 1.3878586292266846, -0.5044048428535461, 1.6207753419876099
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3745203018188477, 0.011079193092882633, 1.4878946542739868
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(454 + frame)
obj = cameras['Camera']
obj.location = 1.3689295053482056, -0.49499309062957764, 1.6166726350784302
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3722199201583862, 0.008762222714722157, 1.4887042045593262
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(455 + frame)
obj = cameras['Camera']
obj.location = 1.349737286567688, -0.4860313832759857, 1.6117676496505737
obj.scale = 0.9999999403953552, 1.0, 0.9999998211860657
obj.rotation_euler = 1.3698656558990479, 0.007539477664977312, 1.489514946937561
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(456 + frame)
obj = cameras['Camera']
obj.location = 1.3302397727966309, -0.4765437841415405, 1.6064813137054443
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3675627708435059, 0.007274821866303682, 1.4911912679672241
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(457 + frame)
obj = cameras['Camera']
obj.location = 1.310401201248169, -0.46684563159942627, 1.6007083654403687
obj.scale = 0.9999998807907104, 1.0, 1.000000238418579
obj.rotation_euler = 1.365225911140442, 0.008382339030504227, 1.4930745363235474
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(458 + frame)
obj = cameras['Camera']
obj.location = 1.2905468940734863, -0.45611345767974854, 1.595043420791626
obj.scale = 1.0, 0.9999995827674866, 0.9999999403953552
obj.rotation_euler = 1.3624866008758545, 0.00954946968704462, 1.4947723150253296
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(459 + frame)
obj = cameras['Camera']
obj.location = 1.2711306810379028, -0.4453160762786865, 1.5891813039779663
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.359444260597229, 0.01068657636642456, 1.4961364269256592
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(460 + frame)
obj = cameras['Camera']
obj.location = 1.2528049945831299, -0.435174822807312, 1.5832208395004272
obj.scale = 1.000000238418579, 1.0000005960464478, 1.0000007152557373
obj.rotation_euler = 1.3561949729919434, 0.014542009681463242, 1.4979567527770996
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(461 + frame)
obj = cameras['Camera']
obj.location = 1.2346465587615967, -0.42512404918670654, 1.5776828527450562
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.3540927171707153, 0.019001495093107224, 1.5021393299102783
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(462 + frame)
obj = cameras['Camera']
obj.location = 1.2180535793304443, -0.41485562920570374, 1.572753667831421
obj.scale = 1.000000238418579, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.3527519702911377, 0.02501841075718403, 1.5086627006530762
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(463 + frame)
obj = cameras['Camera']
obj.location = 1.201209306716919, -0.403099000453949, 1.567521095275879
obj.scale = 1.0, 1.0000005960464478, 1.0000005960464478
obj.rotation_euler = 1.352152705192566, 0.032008346170186996, 1.5165749788284302
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(464 + frame)
obj = cameras['Camera']
obj.location = 1.1844604015350342, -0.3920813798904419, 1.5640138387680054
obj.scale = 0.9999998807907104, 1.0, 1.0
obj.rotation_euler = 1.3518650531768799, 0.033886659890413284, 1.52371346950531
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(465 + frame)
obj = cameras['Camera']
obj.location = 1.1674137115478516, -0.38105809688568115, 1.5614893436431885
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3508155345916748, 0.03488248586654663, 1.529679298400879
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(466 + frame)
obj = cameras['Camera']
obj.location = 1.1496883630752563, -0.3685426712036133, 1.5592997074127197
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3491250276565552, 0.03283737599849701, 1.533544898033142
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(467 + frame)
obj = cameras['Camera']
obj.location = 1.1312588453292847, -0.35917744040489197, 1.5566613674163818
obj.scale = 1.0, 1.0, 0.9999997615814209
obj.rotation_euler = 1.3478331565856934, 0.030302438884973526, 1.5346850156784058
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(468 + frame)
obj = cameras['Camera']
obj.location = 1.1129740476608276, -0.3512197732925415, 1.5556010007858276
obj.scale = 1.0000001192092896, 1.0, 0.9999997615814209
obj.rotation_euler = 1.3471161127090454, 0.030432898551225662, 1.5380061864852905
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(469 + frame)
obj = cameras['Camera']
obj.location = 1.0935015678405762, -0.34377193450927734, 1.5557118654251099
obj.scale = 1.0, 1.0000003576278687, 1.0000004768371582
obj.rotation_euler = 1.3470786809921265, 0.03052701987326145, 1.543204426765442
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(470 + frame)
obj = cameras['Camera']
obj.location = 1.0729972124099731, -0.3343712389469147, 1.5559673309326172
obj.scale = 1.000000238418579, 1.0000007152557373, 1.0000005960464478
obj.rotation_euler = 1.3469599485397339, 0.029589224606752396, 1.5493032932281494
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(471 + frame)
obj = cameras['Camera']
obj.location = 1.051604986190796, -0.3251517415046692, 1.5570292472839355
obj.scale = 1.0, 0.9999998807907104, 1.0
obj.rotation_euler = 1.3459160327911377, 0.02682090364396572, 1.5537045001983643
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(472 + frame)
obj = cameras['Camera']
obj.location = 1.0306081771850586, -0.3163990378379822, 1.557907223701477
obj.scale = 0.9999999403953552, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.3436678647994995, 0.02370990440249443, 1.5562498569488525
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(473 + frame)
obj = cameras['Camera']
obj.location = 1.0107965469360352, -0.30823981761932373, 1.5586930513381958
obj.scale = 0.9999997615814209, 0.999999463558197, 0.9999997019767761
obj.rotation_euler = 1.3407809734344482, 0.02137283980846405, 1.558646321296692
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(474 + frame)
obj = cameras['Camera']
obj.location = 0.9901796579360962, -0.30073678493499756, 1.5592032670974731
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.3385241031646729, 0.020724168047308922, 1.5623050928115845
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(475 + frame)
obj = cameras['Camera']
obj.location = 0.9694443941116333, -0.2934059798717499, 1.5593820810317993
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3370769023895264, 0.020993534475564957, 1.5678714513778687
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(476 + frame)
obj = cameras['Camera']
obj.location = 0.9487621188163757, -0.28598177433013916, 1.5594520568847656
obj.scale = 1.0, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3364472389221191, 0.024750422686338425, 1.574918508529663
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(477 + frame)
obj = cameras['Camera']
obj.location = 0.9281708598136902, -0.2771206498146057, 1.5596157312393188
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3363789319992065, 0.025771740823984146, 1.5829459428787231
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(478 + frame)
obj = cameras['Camera']
obj.location = 0.9066606760025024, -0.2682773470878601, 1.5589736700057983
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.3369956016540527, 0.0290658138692379, 1.5905247926712036
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(479 + frame)
obj = cameras['Camera']
obj.location = 0.885785698890686, -0.25887951254844666, 1.5582560300827026
obj.scale = 1.0, 1.0, 0.9999998211860657
obj.rotation_euler = 1.337497353553772, 0.02819833904504776, 1.597420573234558
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(480 + frame)
obj = cameras['Camera']
obj.location = 0.864067554473877, -0.2487308531999588, 1.5558950901031494
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3379158973693848, 0.02711368538439274, 1.6027201414108276
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(481 + frame)
obj = cameras['Camera']
obj.location = 0.8421031832695007, -0.23819366097450256, 1.5542023181915283
obj.scale = 1.0, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3375842571258545, 0.022453319281339645, 1.605684518814087
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(482 + frame)
obj = cameras['Camera']
obj.location = 0.8199657797813416, -0.22725693881511688, 1.5515668392181396
obj.scale = 1.0000003576278687, 1.0000009536743164, 1.0000008344650269
obj.rotation_euler = 1.3366782665252686, 0.01795964501798153, 1.6051735877990723
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(483 + frame)
obj = cameras['Camera']
obj.location = 0.7984554171562195, -0.2174345850944519, 1.5480172634124756
obj.scale = 1.0000003576278687, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3355129957199097, 0.013266606256365776, 1.6018335819244385
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(484 + frame)
obj = cameras['Camera']
obj.location = 0.7775818109512329, -0.20760947465896606, 1.5441535711288452
obj.scale = 0.9999997615814209, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.334602952003479, 0.008574174717068672, 1.5983015298843384
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(485 + frame)
obj = cameras['Camera']
obj.location = 0.7577074766159058, -0.19784265756607056, 1.5402857065200806
obj.scale = 1.0000003576278687, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3340262174606323, 0.004974206909537315, 1.5949976444244385
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(486 + frame)
obj = cameras['Camera']
obj.location = 0.7367569804191589, -0.18749681115150452, 1.5363192558288574
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3340126276016235, 0.00024951164959929883, 1.5914326906204224
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(487 + frame)
obj = cameras['Camera']
obj.location = 0.7172966599464417, -0.17825204133987427, 1.5319280624389648
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3338109254837036, -0.003916515037417412, 1.5864195823669434
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(488 + frame)
obj = cameras['Camera']
obj.location = 0.697574257850647, -0.1703639030456543, 1.5272983312606812
obj.scale = 1.0000003576278687, 1.0, 1.0
obj.rotation_euler = 1.3341505527496338, -0.006337649188935757, 1.5811539888381958
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(489 + frame)
obj = cameras['Camera']
obj.location = 0.6782792210578918, -0.16369906067848206, 1.5220410823822021
obj.scale = 0.9999999403953552, 0.9999998211860657, 1.0
obj.rotation_euler = 1.3349305391311646, -0.007320256903767586, 1.5763744115829468
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(490 + frame)
obj = cameras['Camera']
obj.location = 0.6590851545333862, -0.1581834852695465, 1.5162417888641357
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999997019767761
obj.rotation_euler = 1.3362476825714111, -0.0065399352461099625, 1.5727570056915283
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(491 + frame)
obj = cameras['Camera']
obj.location = 0.6395100355148315, -0.15343663096427917, 1.5101159811019897
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3382316827774048, -0.004211907275021076, 1.570602297782898
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(492 + frame)
obj = cameras['Camera']
obj.location = 0.6203136444091797, -0.14834433794021606, 1.5041477680206299
obj.scale = 1.000000238418579, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.3404768705368042, -0.0020812873262912035, 1.570272445678711
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(493 + frame)
obj = cameras['Camera']
obj.location = 0.6007818579673767, -0.14264364540576935, 1.4965174198150635
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.342670202255249, -0.0010115631157532334, 1.5703827142715454
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(494 + frame)
obj = cameras['Camera']
obj.location = 0.5817133188247681, -0.13641175627708435, 1.4907701015472412
obj.scale = 0.9999998807907104, 0.9999996423721313, 0.9999998807907104
obj.rotation_euler = 1.3439987897872925, -0.0012224236270412803, 1.5698356628417969
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(495 + frame)
obj = cameras['Camera']
obj.location = 0.561200737953186, -0.13079842925071716, 1.485102653503418
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.3452509641647339, -0.0018347634468227625, 1.5682967901229858
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(496 + frame)
obj = cameras['Camera']
obj.location = 0.5412113666534424, -0.12614381313323975, 1.479278802871704
obj.scale = 0.9999999403953552, 1.0, 0.9999999403953552
obj.rotation_euler = 1.346261978149414, -0.0022652919869869947, 1.5663648843765259
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(497 + frame)
obj = cameras['Camera']
obj.location = 0.5198773145675659, -0.12215330451726913, 1.4733929634094238
obj.scale = 1.000000238418579, 1.000000238418579, 0.9999998807907104
obj.rotation_euler = 1.3475383520126343, -0.002810852834954858, 1.5649949312210083
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(498 + frame)
obj = cameras['Camera']
obj.location = 0.4991554617881775, -0.1180044561624527, 1.4679315090179443
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.0000007152557373
obj.rotation_euler = 1.3486331701278687, -0.0033720172941684723, 1.5644844770431519
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(499 + frame)
obj = cameras['Camera']
obj.location = 0.4785827100276947, -0.11483287066221237, 1.4624453783035278
obj.scale = 1.0000003576278687, 1.0000007152557373, 1.0000003576278687
obj.rotation_euler = 1.3495891094207764, -0.0031132884323596954, 1.5643401145935059
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(500 + frame)
obj = cameras['Camera']
obj.location = 0.45761242508888245, -0.11203981935977936, 1.4571810960769653
obj.scale = 0.9999998807907104, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3506962060928345, -0.003241694299504161, 1.5653154850006104
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(501 + frame)
obj = cameras['Camera']
obj.location = 0.4360653758049011, -0.10965282469987869, 1.4519615173339844
obj.scale = 0.9999998211860657, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.3519680500030518, -0.003582955803722143, 1.567116618156433
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(502 + frame)
obj = cameras['Camera']
obj.location = 0.41442805528640747, -0.10719390213489532, 1.4470961093902588
obj.scale = 0.9999997615814209, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3527032136917114, -0.0034358662087470293, 1.569365382194519
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(503 + frame)
obj = cameras['Camera']
obj.location = 0.39259523153305054, -0.10521705448627472, 1.4420113563537598
obj.scale = 1.000000238418579, 1.0000007152557373, 1.0000004768371582
obj.rotation_euler = 1.3527144193649292, -0.0030398049857467413, 1.571593999862671
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(504 + frame)
obj = cameras['Camera']
obj.location = 0.36997920274734497, -0.10262793302536011, 1.437377691268921
obj.scale = 1.000000238418579, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3519877195358276, -0.0031385000329464674, 1.5742334127426147
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(505 + frame)
obj = cameras['Camera']
obj.location = 0.3475882411003113, -0.09941768646240234, 1.432824730873108
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.3504992723464966, -0.0024545853957533836, 1.5767871141433716
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(506 + frame)
obj = cameras['Camera']
obj.location = 0.32412850856781006, -0.09617068618535995, 1.4271435737609863
obj.scale = 0.9999998807907104, 1.000000238418579, 1.0
obj.rotation_euler = 1.3488008975982666, -0.001048352336511016, 1.579330563545227
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(507 + frame)
obj = cameras['Camera']
obj.location = 0.30075258016586304, -0.09256814420223236, 1.4221926927566528
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.3469880819320679, 0.0003109198296442628, 1.5823394060134888
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(508 + frame)
obj = cameras['Camera']
obj.location = 0.27736711502075195, -0.08888354897499084, 1.4178789854049683
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3455688953399658, 0.0028659948147833347, 1.5858399868011475
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(509 + frame)
obj = cameras['Camera']
obj.location = 0.25373396277427673, -0.08444894850254059, 1.4132612943649292
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.344704508781433, 0.004614576697349548, 1.5899395942687988
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(510 + frame)
obj = cameras['Camera']
obj.location = 0.2298821657896042, -0.07981450855731964, 1.4097697734832764
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.3444344997406006, 0.005381298251450062, 1.594596028327942
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(511 + frame)
obj = cameras['Camera']
obj.location = 0.2066698670387268, -0.07344480603933334, 1.4071487188339233
obj.scale = 1.0, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.3437248468399048, 0.005678774788975716, 1.5994019508361816
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(512 + frame)
obj = cameras['Camera']
obj.location = 0.1838729977607727, -0.06647468358278275, 1.4045778512954712
obj.scale = 0.9999999403953552, 0.9999994039535522, 0.9999993443489075
obj.rotation_euler = 1.3425872325897217, 0.005760213825851679, 1.6024757623672485
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(513 + frame)
obj = cameras['Camera']
obj.location = 0.1611652672290802, -0.05871794372797012, 1.4027838706970215
obj.scale = 1.0, 1.0000004768371582, 1.000000238418579
obj.rotation_euler = 1.3417563438415527, 0.005392823368310928, 1.6044164896011353
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(514 + frame)
obj = cameras['Camera']
obj.location = 0.139428049325943, -0.05047120898962021, 1.401616096496582
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.341131567955017, 0.005241886246949434, 1.6055558919906616
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(515 + frame)
obj = cameras['Camera']
obj.location = 0.11783672869205475, -0.041279472410678864, 1.4015581607818604
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.3411718606948853, 0.004480954259634018, 1.6063238382339478
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(516 + frame)
obj = cameras['Camera']
obj.location = 0.09619870781898499, -0.031932033598423004, 1.4007573127746582
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3420886993408203, 0.004019186366349459, 1.6056995391845703
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(517 + frame)
obj = cameras['Camera']
obj.location = 0.07423628866672516, -0.021862544119358063, 1.4011337757110596
obj.scale = 0.9999998807907104, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.343015432357788, 0.004490179941058159, 1.6040723323822021
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(518 + frame)
obj = cameras['Camera']
obj.location = 0.05223038047552109, -0.012639015913009644, 1.401362419128418
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.3443725109100342, 0.004602554254233837, 1.6012904644012451
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(519 + frame)
obj = cameras['Camera']
obj.location = 0.030513020232319832, -0.002802737057209015, 1.4022326469421387
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.346468448638916, 0.0030204930808395147, 1.5990407466888428
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(520 + frame)
obj = cameras['Camera']
obj.location = 0.008589538745582104, 0.0056496188044548035, 1.4026578664779663
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.3495304584503174, 0.0032650919165462255, 1.5966277122497559
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(521 + frame)
obj = cameras['Camera']
obj.location = -0.01391917746514082, 0.015029332600533962, 1.402899146080017
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3533093929290771, 0.004875322803854942, 1.5951721668243408
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(522 + frame)
obj = cameras['Camera']
obj.location = -0.036484092473983765, 0.02073395997285843, 1.4037492275238037
obj.scale = 0.9999999403953552, 0.9999995231628418, 0.9999996423721313
obj.rotation_euler = 1.3566646575927734, 0.006412103306502104, 1.5944597721099854
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(523 + frame)
obj = cameras['Camera']
obj.location = -0.05802236497402191, 0.02622189372777939, 1.4043397903442383
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3594186305999756, 0.006722043734043837, 1.5961191654205322
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(524 + frame)
obj = cameras['Camera']
obj.location = -0.08091616630554199, 0.03030969202518463, 1.405509352684021
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.363317608833313, 0.005789225455373526, 1.6004928350448608
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(525 + frame)
obj = cameras['Camera']
obj.location = -0.10262960195541382, 0.036804892122745514, 1.407597303390503
obj.scale = 1.000000238418579, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3659337759017944, 0.0030074024107307196, 1.6064509153366089
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(526 + frame)
obj = cameras['Camera']
obj.location = -0.12471963465213776, 0.044164106249809265, 1.4101495742797852
obj.scale = 1.000000238418579, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.3673765659332275, 0.0007176205399446189, 1.6115409135818481
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(527 + frame)
obj = cameras['Camera']
obj.location = -0.14680960774421692, 0.05177509784698486, 1.4122838973999023
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3680329322814941, -0.0015793860657140613, 1.614156723022461
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(528 + frame)
obj = cameras['Camera']
obj.location = -0.16898472607135773, 0.05921860784292221, 1.4142940044403076
obj.scale = 1.000000238418579, 1.0, 1.000000238418579
obj.rotation_euler = 1.3681405782699585, -0.0019637371879070997, 1.6144499778747559
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(529 + frame)
obj = cameras['Camera']
obj.location = -0.1918477565050125, 0.06607536971569061, 1.416208267211914
obj.scale = 0.9999998211860657, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3683284521102905, -0.000515450316015631, 1.6129891872406006
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(530 + frame)
obj = cameras['Camera']
obj.location = -0.21428292989730835, 0.0737384483218193, 1.4179415702819824
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3684273958206177, 0.003281809389591217, 1.6116315126419067
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(531 + frame)
obj = cameras['Camera']
obj.location = -0.23743318021297455, 0.08013009279966354, 1.4202690124511719
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3698055744171143, 0.0068356990814208984, 1.611384391784668
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(532 + frame)
obj = cameras['Camera']
obj.location = -0.26163995265960693, 0.0875057801604271, 1.4231090545654297
obj.scale = 0.9999998807907104, 0.9999998807907104, 1.0
obj.rotation_euler = 1.372192621231079, 0.008471464738249779, 1.6135400533676147
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(533 + frame)
obj = cameras['Camera']
obj.location = -0.2861069440841675, 0.09322693943977356, 1.4253854751586914
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.375522255897522, 0.008947239257395267, 1.6173378229141235
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(534 + frame)
obj = cameras['Camera']
obj.location = -0.30948904156684875, 0.10167614370584488, 1.4293289184570312
obj.scale = 0.9999999403953552, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.377488613128662, 0.0067206197418272495, 1.624682903289795
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(535 + frame)
obj = cameras['Camera']
obj.location = -0.33408084511756897, 0.11161539703607559, 1.4331988096237183
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3787978887557983, 0.0051956879906356335, 1.6298754215240479
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(536 + frame)
obj = cameras['Camera']
obj.location = -0.35937920212745667, 0.12254387885332108, 1.436814546585083
obj.scale = 0.9999998211860657, 1.0000001192092896, 0.9999998211860657
obj.rotation_euler = 1.3793138265609741, 0.0022384794428944588, 1.6324949264526367
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(537 + frame)
obj = cameras['Camera']
obj.location = -0.38581088185310364, 0.13381850719451904, 1.4399735927581787
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.000000238418579
obj.rotation_euler = 1.3791366815567017, -0.00207223417237401, 1.6328279972076416
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(538 + frame)
obj = cameras['Camera']
obj.location = -0.4125208258628845, 0.14526087045669556, 1.4428433179855347
obj.scale = 1.0000003576278687, 1.0, 1.0
obj.rotation_euler = 1.3777027130126953, -0.006158600095659494, 1.6315782070159912
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(539 + frame)
obj = cameras['Camera']
obj.location = -0.4391745626926422, 0.1567862629890442, 1.4456056356430054
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.375322699546814, -0.007318318355828524, 1.6290839910507202
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(540 + frame)
obj = cameras['Camera']
obj.location = -0.4665378928184509, 0.1679072380065918, 1.4482409954071045
obj.scale = 0.9999998807907104, 1.0, 1.0
obj.rotation_euler = 1.3728103637695312, -0.008056561462581158, 1.6262757778167725
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(541 + frame)
obj = cameras['Camera']
obj.location = -0.4927324056625366, 0.1798364371061325, 1.4514085054397583
obj.scale = 1.0, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.369541049003601, -0.007409737911075354, 1.624009609222412
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(542 + frame)
obj = cameras['Camera']
obj.location = -0.5196607112884521, 0.19086484611034393, 1.4542174339294434
obj.scale = 1.000000238418579, 0.9999998211860657, 1.0
obj.rotation_euler = 1.3669013977050781, -0.00684011448174715, 1.6226277351379395
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(543 + frame)
obj = cameras['Camera']
obj.location = -0.5395452380180359, 0.20194223523139954, 1.4549777507781982
obj.scale = 1.0000001192092896, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.3620332479476929, -0.00705376174300909, 1.6215746402740479
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(544 + frame)
obj = cameras['Camera']
obj.location = -0.5676317811012268, 0.21315419673919678, 1.4580371379852295
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.3598679304122925, -0.00701838219538331, 1.623254418373108
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(545 + frame)
obj = cameras['Camera']
obj.location = -0.5937298536300659, 0.225589781999588, 1.460777759552002
obj.scale = 1.000000238418579, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.356593370437622, -0.006424371153116226, 1.6251696348190308
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(546 + frame)
obj = cameras['Camera']
obj.location = -0.620964765548706, 0.23729677498340607, 1.4628807306289673
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3537856340408325, -0.007016381248831749, 1.6266030073165894
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(547 + frame)
obj = cameras['Camera']
obj.location = -0.6481750011444092, 0.24889588356018066, 1.4643570184707642
obj.scale = 1.000000238418579, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.3506518602371216, -0.005541197024285793, 1.6273787021636963
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(548 + frame)
obj = cameras['Camera']
obj.location = -0.67503821849823, 0.26114436984062195, 1.465914249420166
obj.scale = 1.0000003576278687, 1.0, 1.000000238418579
obj.rotation_euler = 1.3475401401519775, -0.0009243670501746237, 1.628091812133789
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(549 + frame)
obj = cameras['Camera']
obj.location = -0.7003385424613953, 0.2718204855918884, 1.4663259983062744
obj.scale = 1.0000003576278687, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.3451071977615356, 0.002417917363345623, 1.6283143758773804
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(550 + frame)
obj = cameras['Camera']
obj.location = -0.72663414478302, 0.28431472182273865, 1.4683204889297485
obj.scale = 1.0, 0.9999997019767761, 0.9999997615814209
obj.rotation_euler = 1.3444253206253052, 0.005590970162302256, 1.6306841373443604
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(551 + frame)
obj = cameras['Camera']
obj.location = -0.751863956451416, 0.2949969172477722, 1.4698965549468994
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999996423721313
obj.rotation_euler = 1.34602952003479, 0.0065308609046041965, 1.6345477104187012
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(552 + frame)
obj = cameras['Camera']
obj.location = -0.7753576636314392, 0.3061985671520233, 1.4724756479263306
obj.scale = 0.9999998211860657, 0.9999995827674866, 0.9999995827674866
obj.rotation_euler = 1.348414421081543, 0.005357206333428621, 1.6416661739349365
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(553 + frame)
obj = cameras['Camera']
obj.location = -0.7989078760147095, 0.31612640619277954, 1.475450038909912
obj.scale = 1.000000238418579, 0.9999997019767761, 1.0000001192092896
obj.rotation_euler = 1.3525199890136719, 0.003373634535819292, 1.6504788398742676
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(554 + frame)
obj = cameras['Camera']
obj.location = -0.8201743960380554, 0.3268217146396637, 1.4787089824676514
obj.scale = 1.0000001192092896, 0.9999997019767761, 0.9999997615814209
obj.rotation_euler = 1.3566052913665771, 0.00022015853028278798, 1.6582006216049194
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(555 + frame)
obj = cameras['Camera']
obj.location = -0.8425618410110474, 0.33687224984169006, 1.4819122552871704
obj.scale = 0.9999999403953552, 1.0, 0.9999997615814209
obj.rotation_euler = 1.3619831800460815, -0.002590795047581196, 1.6631921529769897
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(556 + frame)
obj = cameras['Camera']
obj.location = -0.8642721176147461, 0.34808969497680664, 1.4852731227874756
obj.scale = 0.9999998211860657, 0.999999463558197, 0.999999463558197
obj.rotation_euler = 1.3668034076690674, -0.006034781225025654, 1.6656358242034912
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(557 + frame)
obj = cameras['Camera']
obj.location = -0.8859650492668152, 0.35899144411087036, 1.4883472919464111
obj.scale = 0.9999997615814209, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.372490644454956, -0.005870274733752012, 1.6653848886489868
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(558 + frame)
obj = cameras['Camera']
obj.location = -0.9072534441947937, 0.3698119521141052, 1.4912904500961304
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3778284788131714, -0.006274206563830376, 1.6634889841079712
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(559 + frame)
obj = cameras['Camera']
obj.location = -0.9295674562454224, 0.3795814514160156, 1.494625210762024
obj.scale = 1.0000004768371582, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3838496208190918, -0.007357729133218527, 1.6617388725280762
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(560 + frame)
obj = cameras['Camera']
obj.location = -0.9501578211784363, 0.38974764943122864, 1.4983112812042236
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3893464803695679, -0.007074220106005669, 1.661185383796692
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(561 + frame)
obj = cameras['Camera']
obj.location = -0.9719732403755188, 0.3997558057308197, 1.502124309539795
obj.scale = 1.0000003576278687, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3949865102767944, -0.006645790301263332, 1.662274718284607
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(562 + frame)
obj = cameras['Camera']
obj.location = -0.994137167930603, 0.40733540058135986, 1.5045738220214844
obj.scale = 1.0, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.400559902191162, -0.007044665049761534, 1.662932276725769
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(563 + frame)
obj = cameras['Camera']
obj.location = -1.0163601636886597, 0.4163309931755066, 1.5078014135360718
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4050229787826538, -0.006120749749243259, 1.6637890338897705
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(564 + frame)
obj = cameras['Camera']
obj.location = -1.0382435321807861, 0.4235151410102844, 1.5109779834747314
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4087821245193481, -0.004873337224125862, 1.6637014150619507
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(565 + frame)
obj = cameras['Camera']
obj.location = -1.0611600875854492, 0.4306967258453369, 1.514114260673523
obj.scale = 1.0000004768371582, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4121054410934448, -0.004107896704226732, 1.6638246774673462
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(566 + frame)
obj = cameras['Camera']
obj.location = -1.0836849212646484, 0.4363709092140198, 1.5172444581985474
obj.scale = 0.9999998211860657, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4146463871002197, -0.002827179618179798, 1.663378119468689
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(567 + frame)
obj = cameras['Camera']
obj.location = -1.106363296508789, 0.44184908270835876, 1.5202136039733887
obj.scale = 0.9999999403953552, 0.9999996423721313, 0.9999996423721313
obj.rotation_euler = 1.4163963794708252, -0.0014523660065606236, 1.663049340248108
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(568 + frame)
obj = cameras['Camera']
obj.location = -1.129019856452942, 0.4476568102836609, 1.5230717658996582
obj.scale = 1.0000003576278687, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.417409062385559, 0.001222653198055923, 1.6626403331756592
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(569 + frame)
obj = cameras['Camera']
obj.location = -1.1514965295791626, 0.4528049826622009, 1.5254700183868408
obj.scale = 1.0, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4179961681365967, 0.00474892370402813, 1.661657691001892
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(570 + frame)
obj = cameras['Camera']
obj.location = -1.1742082834243774, 0.4576002359390259, 1.527238130569458
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.4185223579406738, 0.00874405074864626, 1.6602824926376343
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(571 + frame)
obj = cameras['Camera']
obj.location = -1.1977975368499756, 0.4608619809150696, 1.5285431146621704
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4195747375488281, 0.011608066037297249, 1.658812403678894
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(572 + frame)
obj = cameras['Camera']
obj.location = -1.2205792665481567, 0.4648636281490326, 1.5294283628463745
obj.scale = 1.0000003576278687, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4203464984893799, 0.013188102282583714, 1.6586319208145142
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(573 + frame)
obj = cameras['Camera']
obj.location = -1.243322730064392, 0.46876606345176697, 1.5299170017242432
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4212956428527832, 0.014114770106971264, 1.6597843170166016
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(574 + frame)
obj = cameras['Camera']
obj.location = -1.2666572332382202, 0.4727694094181061, 1.529484510421753
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.4226139783859253, 0.014629618264734745, 1.6615628004074097
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(575 + frame)
obj = cameras['Camera']
obj.location = -1.2893078327178955, 0.47674593329429626, 1.5283887386322021
obj.scale = 1.0000003576278687, 1.000000238418579, 1.0000004768371582
obj.rotation_euler = 1.42354154586792, 0.015108367428183556, 1.662890911102295
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(576 + frame)
obj = cameras['Camera']
obj.location = -1.3116525411605835, 0.479404091835022, 1.5265542268753052
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.424200415611267, 0.01728854514658451, 1.6626014709472656
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(577 + frame)
obj = cameras['Camera']
obj.location = -1.3335479497909546, 0.48206955194473267, 1.5239320993423462
obj.scale = 1.0000003576278687, 1.0000005960464478, 1.000000238418579
obj.rotation_euler = 1.424484133720398, 0.019775109365582466, 1.6612305641174316
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(578 + frame)
obj = cameras['Camera']
obj.location = -1.3546123504638672, 0.48513638973236084, 1.5207593441009521
obj.scale = 0.9999999403953552, 0.9999996423721313, 0.9999997615814209
obj.rotation_euler = 1.4235507249832153, 0.0270738173276186, 1.6574198007583618
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(579 + frame)
obj = cameras['Camera']
obj.location = -1.3753379583358765, 0.48833322525024414, 1.517816424369812
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.422987461090088, 0.03104519285261631, 1.6533876657485962
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(580 + frame)
obj = cameras['Camera']
obj.location = -1.3956542015075684, 0.4913008511066437, 1.5139806270599365
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.4232263565063477, 0.03457771986722946, 1.6510556936264038
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(581 + frame)
obj = cameras['Camera']
obj.location = -1.415073275566101, 0.4935411810874939, 1.510926365852356
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.4240931272506714, 0.037625886499881744, 1.650928258895874
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(582 + frame)
obj = cameras['Camera']
obj.location = -1.4337553977966309, 0.4958454966545105, 1.5073531866073608
obj.scale = 1.0000003576278687, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.4253661632537842, 0.039859164506196976, 1.652604341506958
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(583 + frame)
obj = cameras['Camera']
obj.location = -1.4528028964996338, 0.4968917667865753, 1.5032432079315186
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.4274884462356567, 0.04122313857078552, 1.6550610065460205
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(584 + frame)
obj = cameras['Camera']
obj.location = -1.4711472988128662, 0.500053882598877, 1.4987263679504395
obj.scale = 1.0, 1.0000003576278687, 1.0000004768371582
obj.rotation_euler = 1.429128646850586, 0.04291064664721489, 1.6585921049118042
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(585 + frame)
obj = cameras['Camera']
obj.location = -1.4895193576812744, 0.504103422164917, 1.4937286376953125
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.000000238418579
obj.rotation_euler = 1.4303045272827148, 0.04530813544988632, 1.6617653369903564
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(586 + frame)
obj = cameras['Camera']
obj.location = -1.507819414138794, 0.5070260763168335, 1.4882608652114868
obj.scale = 1.0, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4311968088150024, 0.047588612884283066, 1.663357138633728
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(587 + frame)
obj = cameras['Camera']
obj.location = -1.525893211364746, 0.5105176568031311, 1.4816086292266846
obj.scale = 1.0000004768371582, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4317573308944702, 0.04782087355852127, 1.6644915342330933
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(588 + frame)
obj = cameras['Camera']
obj.location = -1.543832778930664, 0.514696478843689, 1.4755628108978271
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.4321973323822021, 0.0462564192712307, 1.6662311553955078
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(589 + frame)
obj = cameras['Camera']
obj.location = -1.56154465675354, 0.5178297758102417, 1.4694706201553345
obj.scale = 1.0, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.4329094886779785, 0.04392654076218605, 1.6681474447250366
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(590 + frame)
obj = cameras['Camera']
obj.location = -1.5793077945709229, 0.5217409729957581, 1.4633429050445557
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4341726303100586, 0.03791458532214165, 1.6725523471832275
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(591 + frame)
obj = cameras['Camera']
obj.location = -1.5967587232589722, 0.5266638994216919, 1.4571075439453125
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4348700046539307, 0.03786984086036682, 1.6774157285690308
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(592 + frame)
obj = cameras['Camera']
obj.location = -1.614351749420166, 0.5312463641166687, 1.4505054950714111
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4351937770843506, 0.037904925644397736, 1.6815149784088135
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(593 + frame)
obj = cameras['Camera']
obj.location = -1.6306816339492798, 0.5368118286132812, 1.4433010816574097
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.434033751487732, 0.03726142272353172, 1.6833471059799194
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(594 + frame)
obj = cameras['Camera']
obj.location = -1.6474510431289673, 0.5411033034324646, 1.437730312347412
obj.scale = 0.9999998211860657, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4325419664382935, 0.0373152494430542, 1.6820818185806274
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(595 + frame)
obj = cameras['Camera']
obj.location = -1.6642725467681885, 0.5445935130119324, 1.4327834844589233
obj.scale = 0.9999997615814209, 0.9999997019767761, 0.9999996423721313
obj.rotation_euler = 1.4309104681015015, 0.036033086478710175, 1.6799769401550293
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(596 + frame)
obj = cameras['Camera']
obj.location = -1.6808422803878784, 0.550184428691864, 1.4284007549285889
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.4292277097702026, 0.035097572952508926, 1.6799689531326294
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(597 + frame)
obj = cameras['Camera']
obj.location = -1.6979689598083496, 0.55485600233078, 1.4234732389450073
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4283881187438965, 0.032900214195251465, 1.6818335056304932
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(598 + frame)
obj = cameras['Camera']
obj.location = -1.7158524990081787, 0.558784008026123, 1.4197008609771729
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4281208515167236, 0.028950830921530724, 1.6857222318649292
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(599 + frame)
obj = cameras['Camera']
obj.location = -1.734285831451416, 0.5626115798950195, 1.4161221981048584
obj.scale = 0.9999996423721313, 1.0, 1.0
obj.rotation_euler = 1.427730679512024, 0.02444807067513466, 1.6908609867095947
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(600 + frame)
obj = cameras['Camera']
obj.location = -1.7532877922058105, 0.5665099024772644, 1.412663221359253
obj.scale = 1.0, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4267170429229736, 0.023106195032596588, 1.6952705383300781
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(601 + frame)
obj = cameras['Camera']
obj.location = -1.7724865674972534, 0.5701372623443604, 1.4094020128250122
obj.scale = 1.0, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.4248656034469604, 0.021128050982952118, 1.6979395151138306
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(602 + frame)
obj = cameras['Camera']
obj.location = -1.7920598983764648, 0.5742748379707336, 1.4063310623168945
obj.scale = 0.9999998807907104, 0.9999996423721313, 0.9999996423721313
obj.rotation_euler = 1.4225258827209473, 0.016225993633270264, 1.6989035606384277
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(603 + frame)
obj = cameras['Camera']
obj.location = -1.8097928762435913, 0.5794582366943359, 1.403346061706543
obj.scale = 1.0000004768371582, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4186882972717285, 0.013897115364670753, 1.6983704566955566
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(604 + frame)
obj = cameras['Camera']
obj.location = -1.8293894529342651, 0.5807104110717773, 1.4012607336044312
obj.scale = 1.0, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.4161796569824219, 0.011278585530817509, 1.696607232093811
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(605 + frame)
obj = cameras['Camera']
obj.location = -1.8499972820281982, 0.5869134664535522, 1.3987234830856323
obj.scale = 1.0000004768371582, 1.0000008344650269, 1.0000008344650269
obj.rotation_euler = 1.4131474494934082, 0.009729218669235706, 1.6976656913757324
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(606 + frame)
obj = cameras['Camera']
obj.location = -1.8701789379119873, 0.5885628461837769, 1.395987629890442
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.410477638244629, 0.0067034196108579636, 1.6977903842926025
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(607 + frame)
obj = cameras['Camera']
obj.location = -1.890148401260376, 0.592690110206604, 1.392638921737671
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4068095684051514, 0.0065435608848929405, 1.6989210844039917
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(608 + frame)
obj = cameras['Camera']
obj.location = -1.9100451469421387, 0.596838116645813, 1.3895313739776611
obj.scale = 1.000000238418579, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.4031739234924316, 0.006228640675544739, 1.6997580528259277
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(609 + frame)
obj = cameras['Camera']
obj.location = -1.9298303127288818, 0.6014820337295532, 1.3864402770996094
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3997200727462769, 0.006409558933228254, 1.7005146741867065
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(610 + frame)
obj = cameras['Camera']
obj.location = -1.9502612352371216, 0.605202317237854, 1.3837339878082275
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3973960876464844, 0.007240153383463621, 1.7015600204467773
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(611 + frame)
obj = cameras['Camera']
obj.location = -1.9704902172088623, 0.6083070039749146, 1.381560206413269
obj.scale = 1.0, 0.9999997615814209, 0.9999995827674866
obj.rotation_euler = 1.396041750907898, 0.006826330907642841, 1.703552007675171
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(612 + frame)
obj = cameras['Camera']
obj.location = -1.9906108379364014, 0.6124786138534546, 1.3799153566360474
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3952654600143433, 0.007711493875831366, 1.7063184976577759
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(613 + frame)
obj = cameras['Camera']
obj.location = -2.0112853050231934, 0.615292489528656, 1.378516674041748
obj.scale = 1.0, 1.000000238418579, 0.9999999403953552
obj.rotation_euler = 1.3953121900558472, 0.009064343757927418, 1.7084661722183228
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(614 + frame)
obj = cameras['Camera']
obj.location = -2.0310046672821045, 0.6199522614479065, 1.3769797086715698
obj.scale = 0.9999998211860657, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3949687480926514, 0.01100000087171793, 1.71099054813385
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(615 + frame)
obj = cameras['Camera']
obj.location = -2.0505127906799316, 0.6228925585746765, 1.3765065670013428
obj.scale = 1.000000238418579, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.3951563835144043, 0.013306332752108574, 1.712856650352478
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(616 + frame)
obj = cameras['Camera']
obj.location = -2.070213794708252, 0.6269873380661011, 1.3768374919891357
obj.scale = 1.0, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3956661224365234, 0.01830061338841915, 1.7157199382781982
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(617 + frame)
obj = cameras['Camera']
obj.location = -2.089635133743286, 0.6321781873703003, 1.3769056797027588
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.3965020179748535, 0.023507148027420044, 1.719740867614746
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(618 + frame)
obj = cameras['Camera']
obj.location = -2.110018730163574, 0.6369214057922363, 1.3784499168395996
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0
obj.rotation_euler = 1.3983783721923828, 0.025914425030350685, 1.7244880199432373
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(619 + frame)
obj = cameras['Camera']
obj.location = -2.1304850578308105, 0.6411293745040894, 1.3809746503829956
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.400364637374878, 0.02800801396369934, 1.7290656566619873
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(620 + frame)
obj = cameras['Camera']
obj.location = -2.151810646057129, 0.6467165350914001, 1.3838238716125488
obj.scale = 1.0, 1.000000238418579, 1.0
obj.rotation_euler = 1.4028041362762451, 0.02953631989657879, 1.7346785068511963
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(621 + frame)
obj = cameras['Camera']
obj.location = -2.174187183380127, 0.6460678577423096, 1.3883519172668457
obj.scale = 1.0, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4069273471832275, 0.02949959971010685, 1.7370518445968628
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(622 + frame)
obj = cameras['Camera']
obj.location = -2.1966404914855957, 0.6520774364471436, 1.3918427228927612
obj.scale = 1.0, 1.0, 0.9999999403953552
obj.rotation_euler = 1.410037875175476, 0.029768243432044983, 1.7405458688735962
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(623 + frame)
obj = cameras['Camera']
obj.location = -2.2195332050323486, 0.6581472158432007, 1.3971192836761475
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4132239818572998, 0.02953966334462166, 1.7419756650924683
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(624 + frame)
obj = cameras['Camera']
obj.location = -2.2424817085266113, 0.6647170186042786, 1.4028830528259277
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.417102575302124, 0.03002943843603134, 1.741902470588684
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(625 + frame)
obj = cameras['Camera']
obj.location = -2.2662694454193115, 0.6724245548248291, 1.409461259841919
obj.scale = 1.0000001192092896, 1.0000005960464478, 1.000000238418579
obj.rotation_euler = 1.4202250242233276, 0.030579017475247383, 1.7413487434387207
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(626 + frame)
obj = cameras['Camera']
obj.location = -2.289644241333008, 0.6799031496047974, 1.415881872177124
obj.scale = 1.0000003576278687, 1.0, 1.000000238418579
obj.rotation_euler = 1.423181176185608, 0.030779745429754257, 1.74082350730896
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(627 + frame)
obj = cameras['Camera']
obj.location = -2.3129642009735107, 0.6871045827865601, 1.4225897789001465
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000004768371582
obj.rotation_euler = 1.4259226322174072, 0.03155874088406563, 1.7399541139602661
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(628 + frame)
obj = cameras['Camera']
obj.location = -2.336596965789795, 0.6956170797348022, 1.4290896654129028
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999996423721313
obj.rotation_euler = 1.427812099456787, 0.033834077417850494, 1.7393196821212769
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(629 + frame)
obj = cameras['Camera']
obj.location = -2.360062599182129, 0.7047780752182007, 1.4362244606018066
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4288322925567627, 0.036036811769008636, 1.7387754917144775
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(630 + frame)
obj = cameras['Camera']
obj.location = -2.3834307193756104, 0.7146481871604919, 1.4422821998596191
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.4293347597122192, 0.03864631429314613, 1.73917818069458
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(631 + frame)
obj = cameras['Camera']
obj.location = -2.4062888622283936, 0.7237531542778015, 1.4487111568450928
obj.scale = 0.999999463558197, 0.9999995231628418, 0.9999995231628418
obj.rotation_euler = 1.4298962354660034, 0.04058948904275894, 1.7408097982406616
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(632 + frame)
obj = cameras['Camera']
obj.location = -2.429201602935791, 0.7328454852104187, 1.4552152156829834
obj.scale = 0.9999999403953552, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.4305380582809448, 0.04188684746623039, 1.7441569566726685
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(633 + frame)
obj = cameras['Camera']
obj.location = -2.452497720718384, 0.7418270111083984, 1.461627721786499
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4313485622406006, 0.04199272021651268, 1.7488069534301758
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(634 + frame)
obj = cameras['Camera']
obj.location = -2.4758620262145996, 0.750373899936676, 1.4680222272872925
obj.scale = 1.0000001192092896, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4320379495620728, 0.04129123315215111, 1.7535768747329712
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(635 + frame)
obj = cameras['Camera']
obj.location = -2.499325752258301, 0.7594296336174011, 1.474163293838501
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4322017431259155, 0.03860662505030632, 1.7586671113967896
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(636 + frame)
obj = cameras['Camera']
obj.location = -2.523676872253418, 0.7685097455978394, 1.4800910949707031
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.432442307472229, 0.0361485481262207, 1.7626948356628418
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(637 + frame)
obj = cameras['Camera']
obj.location = -2.5481698513031006, 0.7777140140533447, 1.4857423305511475
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.432328462600708, 0.03487074002623558, 1.7652652263641357
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(638 + frame)
obj = cameras['Camera']
obj.location = -2.573275566101074, 0.787185549736023, 1.4911099672317505
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4322714805603027, 0.033317774534225464, 1.7672207355499268
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(639 + frame)
obj = cameras['Camera']
obj.location = -2.598361015319824, 0.7962433695793152, 1.4965404272079468
obj.scale = 1.0000001192092896, 1.000000238418579, 0.9999998211860657
obj.rotation_euler = 1.4321240186691284, 0.03006581962108612, 1.7691349983215332
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(640 + frame)
obj = cameras['Camera']
obj.location = -2.623913526535034, 0.8052220344543457, 1.5019240379333496
obj.scale = 0.9999998807907104, 1.0000005960464478, 1.0000004768371582
obj.rotation_euler = 1.432215690612793, 0.026377784088253975, 1.771531343460083
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(641 + frame)
obj = cameras['Camera']
obj.location = -2.6494386196136475, 0.8140207529067993, 1.5073487758636475
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.432403326034546, 0.024240044876933098, 1.7739529609680176
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(642 + frame)
obj = cameras['Camera']
obj.location = -2.6751508712768555, 0.8229278326034546, 1.5126850605010986
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4326800107955933, 0.022366242483258247, 1.7765295505523682
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(643 + frame)
obj = cameras['Camera']
obj.location = -2.7007458209991455, 0.8315423727035522, 1.517796277999878
obj.scale = 1.0000003576278687, 1.0, 1.0
obj.rotation_euler = 1.4331200122833252, 0.021306486800312996, 1.7785329818725586
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(644 + frame)
obj = cameras['Camera']
obj.location = -2.726238250732422, 0.8391760587692261, 1.5231389999389648
obj.scale = 1.000000238418579, 1.0000005960464478, 1.0000004768371582
obj.rotation_euler = 1.4336822032928467, 0.018098345026373863, 1.7808544635772705
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(645 + frame)
obj = cameras['Camera']
obj.location = -2.7519142627716064, 0.848938524723053, 1.527393102645874
obj.scale = 0.9999997615814209, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.433913230895996, 0.014505510218441486, 1.7845144271850586
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(646 + frame)
obj = cameras['Camera']
obj.location = -2.777158260345459, 0.8566601872444153, 1.5326266288757324
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.4341545104980469, 0.010860252194106579, 1.7880479097366333
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(647 + frame)
obj = cameras['Camera']
obj.location = -2.801779270172119, 0.8640463352203369, 1.5374643802642822
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.4341790676116943, 0.005530188791453838, 1.7917436361312866
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(648 + frame)
obj = cameras['Camera']
obj.location = -2.8263235092163086, 0.8705612421035767, 1.541422963142395
obj.scale = 1.000000238418579, 1.000000238418579, 1.0
obj.rotation_euler = 1.4342869520187378, -0.0006958621670491993, 1.7951748371124268
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(649 + frame)
obj = cameras['Camera']
obj.location = -2.8505024909973145, 0.8772341012954712, 1.5456868410110474
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4342576265335083, -0.0031769168563187122, 1.7981033325195312
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(650 + frame)
obj = cameras['Camera']
obj.location = -2.8742270469665527, 0.8834255933761597, 1.549046516418457
obj.scale = 0.9999997615814209, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4339889287948608, -0.005273571703583002, 1.8008095026016235
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(651 + frame)
obj = cameras['Camera']
obj.location = -2.898345470428467, 0.8890610933303833, 1.552282691001892
obj.scale = 1.0, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4337648153305054, -0.010116278193891048, 1.8041918277740479
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(652 + frame)
obj = cameras['Camera']
obj.location = -2.9221553802490234, 0.8939388990402222, 1.5551360845565796
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.433426856994629, -0.01356871984899044, 1.8076155185699463
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(653 + frame)
obj = cameras['Camera']
obj.location = -2.945021629333496, 0.8983154296875, 1.5577112436294556
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4320240020751953, -0.016146164387464523, 1.8113481998443604
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(654 + frame)
obj = cameras['Camera']
obj.location = -2.968125343322754, 0.9026643633842468, 1.5594948530197144
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.43021559715271, -0.018107298761606216, 1.815887212753296
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(655 + frame)
obj = cameras['Camera']
obj.location = -2.9914357662200928, 0.9075850248336792, 1.5603432655334473
obj.scale = 0.9999999403953552, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4284669160842896, -0.019461626186966896, 1.8206360340118408
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(656 + frame)
obj = cameras['Camera']
obj.location = -3.0140128135681152, 0.9113062024116516, 1.5617330074310303
obj.scale = 1.0, 0.9999999403953552, 0.9999997615814209
obj.rotation_euler = 1.4268300533294678, -0.02001134678721428, 1.8246098756790161
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(657 + frame)
obj = cameras['Camera']
obj.location = -3.036578416824341, 0.9159491062164307, 1.5619251728057861
obj.scale = 0.9999998807907104, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.4254233837127686, -0.020520424470305443, 1.8285819292068481
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(658 + frame)
obj = cameras['Camera']
obj.location = -3.058663845062256, 0.9200676083564758, 1.5629855394363403
obj.scale = 1.0, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4244134426116943, -0.021911989897489548, 1.832263708114624
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(659 + frame)
obj = cameras['Camera']
obj.location = -3.080526828765869, 0.9248603582382202, 1.5636706352233887
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4237949848175049, -0.023505007848143578, 1.8360517024993896
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(660 + frame)
obj = cameras['Camera']
obj.location = -3.1020514965057373, 0.9299666285514832, 1.5645610094070435
obj.scale = 1.0, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4234873056411743, -0.025275321677327156, 1.8386832475662231
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(661 + frame)
obj = cameras['Camera']
obj.location = -3.123380184173584, 0.9349863529205322, 1.565356731414795
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.424056887626648, -0.026830745860934258, 1.8405191898345947
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(662 + frame)
obj = cameras['Camera']
obj.location = -3.144352436065674, 0.9404290318489075, 1.566204309463501
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4249120950698853, -0.02837320975959301, 1.8421013355255127
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(663 + frame)
obj = cameras['Camera']
obj.location = -3.165036916732788, 0.9460296034812927, 1.5667952299118042
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4262243509292603, -0.029371388256549835, 1.8431262969970703
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(664 + frame)
obj = cameras['Camera']
obj.location = -3.185112476348877, 0.9515960216522217, 1.5674097537994385
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.427925705909729, -0.0307631753385067, 1.8441258668899536
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(665 + frame)
obj = cameras['Camera']
obj.location = -3.2047736644744873, 0.956949770450592, 1.5679692029953003
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4298185110092163, -0.031714461743831635, 1.8446704149246216
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(666 + frame)
obj = cameras['Camera']
obj.location = -3.2239065170288086, 0.9627529978752136, 1.5684936046600342
obj.scale = 1.0, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4320982694625854, -0.031983934342861176, 1.845895767211914
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(667 + frame)
obj = cameras['Camera']
obj.location = -3.242142677307129, 0.9690545201301575, 1.5688313245773315
obj.scale = 1.0000005960464478, 1.000000238418579, 1.0
obj.rotation_euler = 1.434348225593567, -0.031622156500816345, 1.847156047821045
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(668 + frame)
obj = cameras['Camera']
obj.location = -3.2603659629821777, 0.9748835563659668, 1.569663166999817
obj.scale = 1.000000238418579, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.4374642372131348, -0.030594460666179657, 1.8480801582336426
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(669 + frame)
obj = cameras['Camera']
obj.location = -3.277902603149414, 0.9815909266471863, 1.5698301792144775
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.4401977062225342, -0.029735010117292404, 1.8489879369735718
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(670 + frame)
obj = cameras['Camera']
obj.location = -3.2955563068389893, 0.9881190061569214, 1.5705952644348145
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4435433149337769, -0.027415446937084198, 1.849521517753601
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(671 + frame)
obj = cameras['Camera']
obj.location = -3.3122715950012207, 0.9941425323486328, 1.5704396963119507
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.4464325904846191, -0.025477947667241096, 1.8499492406845093
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(672 + frame)
obj = cameras['Camera']
obj.location = -3.3300273418426514, 1.0006968975067139, 1.5704982280731201
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.449586272239685, -0.022952791303396225, 1.851200819015503
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(673 + frame)
obj = cameras['Camera']
obj.location = -3.347581148147583, 1.007164716720581, 1.5703929662704468
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.4525057077407837, -0.01963498257100582, 1.8520523309707642
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(674 + frame)
obj = cameras['Camera']
obj.location = -3.365119218826294, 1.0139334201812744, 1.5698068141937256
obj.scale = 0.9999995827674866, 0.9999999403953552, 1.0
obj.rotation_euler = 1.4549611806869507, -0.016742516309022903, 1.8524913787841797
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(675 + frame)
obj = cameras['Camera']
obj.location = -3.3830058574676514, 1.0205879211425781, 1.568378210067749
obj.scale = 0.9999997615814209, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.457318902015686, -0.013427898287773132, 1.8522944450378418
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(676 + frame)
obj = cameras['Camera']
obj.location = -3.4008474349975586, 1.0274966955184937, 1.5673027038574219
obj.scale = 0.9999998211860657, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4592901468276978, -0.009942266158759594, 1.8517132997512817
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(677 + frame)
obj = cameras['Camera']
obj.location = -3.4185357093811035, 1.0341931581497192, 1.5665993690490723
obj.scale = 1.0, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4607720375061035, -0.008571214973926544, 1.8506100177764893
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(678 + frame)
obj = cameras['Camera']
obj.location = -3.436924457550049, 1.0416804552078247, 1.565500259399414
obj.scale = 1.0000003576278687, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4619539976119995, -0.00808575376868248, 1.8500289916992188
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(679 + frame)
obj = cameras['Camera']
obj.location = -3.4548158645629883, 1.0486094951629639, 1.564857840538025
obj.scale = 1.000000238418579, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.462754726409912, -0.0059700473211705685, 1.8487823009490967
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(680 + frame)
obj = cameras['Camera']
obj.location = -3.473127603530884, 1.055394172668457, 1.5642611980438232
obj.scale = 1.000000238418579, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4633432626724243, -0.003582869190722704, 1.8483201265335083
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(681 + frame)
obj = cameras['Camera']
obj.location = -3.491456985473633, 1.0627963542938232, 1.563492774963379
obj.scale = 0.9999997019767761, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.4637303352355957, 0.0006251164595596492, 1.8485918045043945
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(682 + frame)
obj = cameras['Camera']
obj.location = -3.5103018283843994, 1.07053542137146, 1.562323808670044
obj.scale = 1.0, 1.0000004768371582, 1.0000001192092896
obj.rotation_euler = 1.4638659954071045, 0.0035626415628939867, 1.849489688873291
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(683 + frame)
obj = cameras['Camera']
obj.location = -3.529864549636841, 1.0781993865966797, 1.560895323753357
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4641302824020386, 0.005837887059897184, 1.8497495651245117
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(684 + frame)
obj = cameras['Camera']
obj.location = -3.548715114593506, 1.0861691236495972, 1.5586384534835815
obj.scale = 0.9999998807907104, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4641069173812866, 0.008177917450666428, 1.8492040634155273
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(685 + frame)
obj = cameras['Camera']
obj.location = -3.567678451538086, 1.0940138101577759, 1.5569806098937988
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.4641317129135132, 0.00886913575232029, 1.8488718271255493
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(686 + frame)
obj = cameras['Camera']
obj.location = -3.586278200149536, 1.1016101837158203, 1.5553028583526611
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.4639825820922852, 0.009209685027599335, 1.8486649990081787
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(687 + frame)
obj = cameras['Camera']
obj.location = -3.6044230461120605, 1.1092418432235718, 1.5534127950668335
obj.scale = 0.9999999403953552, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4640480279922485, 0.010464750230312347, 1.8485416173934937
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(688 + frame)
obj = cameras['Camera']
obj.location = -3.622222423553467, 1.1167151927947998, 1.5515564680099487
obj.scale = 1.0000003576278687, 1.0, 1.000000238418579
obj.rotation_euler = 1.46435546875, 0.011646146886050701, 1.849007487297058
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(689 + frame)
obj = cameras['Camera']
obj.location = -3.6398239135742188, 1.1248512268066406, 1.5499420166015625
obj.scale = 1.0, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4652396440505981, 0.013289160095155239, 1.8503098487854004
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(690 + frame)
obj = cameras['Camera']
obj.location = -3.6571812629699707, 1.132650375366211, 1.547966718673706
obj.scale = 1.0, 0.999999463558197, 0.9999996423721313
obj.rotation_euler = 1.466651201248169, 0.013954952359199524, 1.8518842458724976
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(691 + frame)
obj = cameras['Camera']
obj.location = -3.6742162704467773, 1.1410548686981201, 1.546614408493042
obj.scale = 1.0, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4676767587661743, 0.013350741937756538, 1.8532240390777588
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(692 + frame)
obj = cameras['Camera']
obj.location = -3.6910006999969482, 1.1501848697662354, 1.5455423593521118
obj.scale = 1.0000003576278687, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4686068296432495, 0.01153847947716713, 1.8535726070404053
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(693 + frame)
obj = cameras['Camera']
obj.location = -3.7075650691986084, 1.1595265865325928, 1.5445516109466553
obj.scale = 0.9999998211860657, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4696797132492065, 0.007788372691720724, 1.8526633977890015
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(694 + frame)
obj = cameras['Camera']
obj.location = -3.7236104011535645, 1.1685643196105957, 1.5450655221939087
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4710524082183838, 0.005708601325750351, 1.8508394956588745
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(695 + frame)
obj = cameras['Camera']
obj.location = -3.7390084266662598, 1.176918864250183, 1.5450787544250488
obj.scale = 0.9999997019767761, 1.0, 1.0
obj.rotation_euler = 1.4725979566574097, 0.00502593070268631, 1.8493802547454834
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(696 + frame)
obj = cameras['Camera']
obj.location = -3.754301071166992, 1.185729742050171, 1.545208215713501
obj.scale = 1.0000003576278687, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4740805625915527, 0.004824397619813681, 1.8496679067611694
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(697 + frame)
obj = cameras['Camera']
obj.location = -3.769855499267578, 1.1942248344421387, 1.5454821586608887
obj.scale = 1.0, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.475890040397644, 0.00531612616032362, 1.8508358001708984
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(698 + frame)
obj = cameras['Camera']
obj.location = -3.78513503074646, 1.2031471729278564, 1.5456129312515259
obj.scale = 1.0000001192092896, 1.0000005960464478, 1.0000005960464478
obj.rotation_euler = 1.4775338172912598, 0.005900741554796696, 1.8524194955825806
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(699 + frame)
obj = cameras['Camera']
obj.location = -3.800302028656006, 1.2115538120269775, 1.5459102392196655
obj.scale = 0.9999998807907104, 0.9999999403953552, 1.000000238418579
obj.rotation_euler = 1.4790650606155396, 0.005946154240518808, 1.853707194328308
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(700 + frame)
obj = cameras['Camera']
obj.location = -3.8149940967559814, 1.2201054096221924, 1.5461307764053345
obj.scale = 0.9999999403953552, 0.9999998807907104, 1.0
obj.rotation_euler = 1.4800562858581543, 0.005312827881425619, 1.854871153831482
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(701 + frame)
obj = cameras['Camera']
obj.location = -3.8303005695343018, 1.2285813093185425, 1.546522617340088
obj.scale = 1.000000238418579, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4812408685684204, 0.004661127924919128, 1.8559753894805908
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(702 + frame)
obj = cameras['Camera']
obj.location = -3.845283031463623, 1.2361193895339966, 1.5472332239151
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.4822783470153809, 0.003839341923594475, 1.8564848899841309
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(703 + frame)
obj = cameras['Camera']
obj.location = -3.86000394821167, 1.243592619895935, 1.5479990243911743
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4829083681106567, 0.002984717721119523, 1.8572475910186768
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(704 + frame)
obj = cameras['Camera']
obj.location = -3.875211238861084, 1.2508265972137451, 1.5488009452819824
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.4836214780807495, 0.0021748337894678116, 1.8583890199661255
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(705 + frame)
obj = cameras['Camera']
obj.location = -3.890137195587158, 1.2579655647277832, 1.549562931060791
obj.scale = 1.0, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.4838671684265137, 0.001261347089894116, 1.8594741821289062
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(706 + frame)
obj = cameras['Camera']
obj.location = -3.905273914337158, 1.2644169330596924, 1.5509166717529297
obj.scale = 0.9999998211860657, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.4841679334640503, 0.00023663000320084393, 1.8604910373687744
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(707 + frame)
obj = cameras['Camera']
obj.location = -3.9203288555145264, 1.270686388015747, 1.5517261028289795
obj.scale = 0.9999998211860657, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.484074354171753, -0.0008436412317678332, 1.861582636833191
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(708 + frame)
obj = cameras['Camera']
obj.location = -3.9352502822875977, 1.2766903638839722, 1.5528761148452759
obj.scale = 0.9999996423721313, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.4831711053848267, -0.0026403276715427637, 1.8627971410751343
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(709 + frame)
obj = cameras['Camera']
obj.location = -3.9497616291046143, 1.282918095588684, 1.5538779497146606
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4809859991073608, -0.004065604414790869, 1.86356520652771
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(710 + frame)
obj = cameras['Camera']
obj.location = -3.9637043476104736, 1.288966178894043, 1.5554425716400146
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.477687954902649, -0.006586694158613682, 1.8646270036697388
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(711 + frame)
obj = cameras['Camera']
obj.location = -3.977027654647827, 1.295077919960022, 1.5566562414169312
obj.scale = 1.0, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.4739325046539307, -0.007151330355554819, 1.865999698638916
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(712 + frame)
obj = cameras['Camera']
obj.location = -3.990795612335205, 1.301364541053772, 1.5582631826400757
obj.scale = 1.0, 0.9999998211860657, 0.9999996423721313
obj.rotation_euler = 1.4699383974075317, -0.007038121111690998, 1.8684978485107422
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(713 + frame)
obj = cameras['Camera']
obj.location = -4.004332065582275, 1.3078224658966064, 1.5597116947174072
obj.scale = 1.0000001192092896, 1.0, 0.9999998211860657
obj.rotation_euler = 1.4654165506362915, -0.005390303209424019, 1.8709660768508911
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(714 + frame)
obj = cameras['Camera']
obj.location = -4.017653942108154, 1.314258098602295, 1.5613288879394531
obj.scale = 1.0, 0.999999463558197, 0.9999995231628418
obj.rotation_euler = 1.4609670639038086, -0.003225334919989109, 1.873854637145996
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(715 + frame)
obj = cameras['Camera']
obj.location = -4.031360626220703, 1.321218490600586, 1.56309175491333
obj.scale = 1.0, 0.9999997019767761, 0.9999997615814209
obj.rotation_euler = 1.4565824270248413, -0.0013356396229937673, 1.8772711753845215
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(716 + frame)
obj = cameras['Camera']
obj.location = -4.045085906982422, 1.328500509262085, 1.5649925470352173
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4522093534469604, 0.0009852921357378364, 1.880171298980713
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(717 + frame)
obj = cameras['Camera']
obj.location = -4.058776378631592, 1.3354108333587646, 1.56693696975708
obj.scale = 1.0000004768371582, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4475780725479126, 0.001385900191962719, 1.8824340105056763
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(718 + frame)
obj = cameras['Camera']
obj.location = -4.072775363922119, 1.342991590499878, 1.5686858892440796
obj.scale = 0.9999998807907104, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.442570686340332, 0.0006736174691468477, 1.8840973377227783
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(719 + frame)
obj = cameras['Camera']
obj.location = -4.0863471031188965, 1.3489139080047607, 1.5706684589385986
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4374927282333374, -0.0020542454440146685, 1.8835886716842651
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(720 + frame)
obj = cameras['Camera']
obj.location = -4.100178241729736, 1.3560190200805664, 1.5727323293685913
obj.scale = 0.9999998807907104, 0.9999995827674866, 0.9999996423721313
obj.rotation_euler = 1.4323558807373047, -0.0043036798015236855, 1.8831459283828735
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(721 + frame)
obj = cameras['Camera']
obj.location = -4.1134538650512695, 1.3616254329681396, 1.5750445127487183
obj.scale = 0.9999998211860657, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4274944067001343, -0.006237987894564867, 1.8820111751556396
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(722 + frame)
obj = cameras['Camera']
obj.location = -4.126476764678955, 1.3666476011276245, 1.5777275562286377
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.423021674156189, -0.008042576722800732, 1.8815211057662964
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(723 + frame)
obj = cameras['Camera']
obj.location = -4.139756202697754, 1.371377944946289, 1.580507755279541
obj.scale = 1.0, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.4190142154693604, -0.009461353532969952, 1.8814116716384888
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(724 + frame)
obj = cameras['Camera']
obj.location = -4.15261173248291, 1.3758680820465088, 1.5836353302001953
obj.scale = 1.0, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4153683185577393, -0.009817791171371937, 1.8817616701126099
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(725 + frame)
obj = cameras['Camera']
obj.location = -4.166019439697266, 1.3800370693206787, 1.5868182182312012
obj.scale = 1.0, 0.9999998807907104, 0.9999996423721313
obj.rotation_euler = 1.4126538038253784, -0.00921999104321003, 1.8822520971298218
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(726 + frame)
obj = cameras['Camera']
obj.location = -4.179633617401123, 1.3833879232406616, 1.5901710987091064
obj.scale = 1.0000001192092896, 0.9999996423721313, 0.9999996423721313
obj.rotation_euler = 1.4106463193893433, -0.008043743669986725, 1.882445216178894
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(727 + frame)
obj = cameras['Camera']
obj.location = -4.193399906158447, 1.3863693475723267, 1.5935752391815186
obj.scale = 1.000000238418579, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4093517065048218, -0.005557136610150337, 1.8821202516555786
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(728 + frame)
obj = cameras['Camera']
obj.location = -4.207070350646973, 1.388720154762268, 1.597031831741333
obj.scale = 1.0, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.4084593057632446, -0.004895892459899187, 1.881471037864685
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(729 + frame)
obj = cameras['Camera']
obj.location = -4.220646858215332, 1.390415072441101, 1.6006466150283813
obj.scale = 1.0000004768371582, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.4079416990280151, -0.004827849566936493, 1.8801618814468384
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(730 + frame)
obj = cameras['Camera']
obj.location = -4.234705448150635, 1.3928722143173218, 1.6040338277816772
obj.scale = 1.000000238418579, 1.0, 1.000000238418579
obj.rotation_euler = 1.4075309038162231, -0.005365272052586079, 1.877705693244934
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(731 + frame)
obj = cameras['Camera']
obj.location = -4.248680114746094, 1.3942617177963257, 1.6076371669769287
obj.scale = 0.9999997615814209, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4074702262878418, -0.0066064391285181046, 1.8731789588928223
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(732 + frame)
obj = cameras['Camera']
obj.location = -4.2623162269592285, 1.3949675559997559, 1.6113674640655518
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.40752112865448, -0.007464038673788309, 1.8686871528625488
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(733 + frame)
obj = cameras['Camera']
obj.location = -4.275803565979004, 1.3959455490112305, 1.615513801574707
obj.scale = 1.0, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4076130390167236, -0.0080118952319026, 1.8642971515655518
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(734 + frame)
obj = cameras['Camera']
obj.location = -4.289456367492676, 1.3962104320526123, 1.619273066520691
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4081950187683105, -0.007055498193949461, 1.8599328994750977
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(735 + frame)
obj = cameras['Camera']
obj.location = -4.302996635437012, 1.3962138891220093, 1.6235653162002563
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.4091784954071045, -0.00613781251013279, 1.8558268547058105
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(736 + frame)
obj = cameras['Camera']
obj.location = -4.31643533706665, 1.3960919380187988, 1.6272096633911133
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4101300239562988, -0.005005143117159605, 1.853805661201477
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(737 + frame)
obj = cameras['Camera']
obj.location = -4.330138206481934, 1.3955588340759277, 1.6309845447540283
obj.scale = 1.0000003576278687, 1.0000001192092896, 1.0
obj.rotation_euler = 1.411268949508667, -0.0034131070133298635, 1.853143334388733
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(738 + frame)
obj = cameras['Camera']
obj.location = -4.347462177276611, 1.400813102722168, 1.6315184831619263
obj.scale = 1.000000238418579, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4122470617294312, -0.003035428235307336, 1.85354483127594
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(739 + frame)
obj = cameras['Camera']
obj.location = -4.364628791809082, 1.4058279991149902, 1.6319355964660645
obj.scale = 1.000000238418579, 1.000000238418579, 1.0
obj.rotation_euler = 1.4129148721694946, -0.0026228060014545918, 1.8542429208755493
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(740 + frame)
obj = cameras['Camera']
obj.location = -4.381562232971191, 1.4103446006774902, 1.6322338581085205
obj.scale = 1.0, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.4131687879562378, -0.002210544189438224, 1.8546764850616455
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(741 + frame)
obj = cameras['Camera']
obj.location = -4.397955894470215, 1.413257122039795, 1.6324143409729004
obj.scale = 0.9999997615814209, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4126465320587158, -0.0019512177677825093, 1.8543040752410889
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(742 + frame)
obj = cameras['Camera']
obj.location = -4.419390678405762, 1.4173760414123535, 1.6387083530426025
obj.scale = 0.9999769330024719, 0.9999812245368958, 0.9999849200248718
obj.rotation_euler = 1.4112683534622192, -0.0019381754100322723, 1.8521822690963745
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(743 + frame)
obj = cameras['Camera']
obj.location = -4.432696342468262, 1.4133113622665405, 1.6342318058013916
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.4102245569229126, -1.9665525030632125e-07, 1.8486744165420532
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(744 + frame)
obj = cameras['Camera']
obj.location = -4.446139335632324, 1.4094685316085815, 1.6297343969345093
obj.scale = 0.9999776482582092, 0.9999814629554749, 0.9999850392341614
obj.rotation_euler = 1.4091078042984009, 0.0019471141276881099, 1.8451342582702637
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(745 + frame)
obj = cameras['Camera']
obj.location = -4.459065914154053, 1.4051635265350342, 1.6258347034454346
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000005960464478
obj.rotation_euler = 1.4072291851043701, 0.004648284055292606, 1.842265248298645
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(746 + frame)
obj = cameras['Camera']
obj.location = -4.472357749938965, 1.4006816148757935, 1.6219549179077148
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.4050003290176392, 0.008291900157928467, 1.840769648551941
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(747 + frame)
obj = cameras['Camera']
obj.location = -4.48695707321167, 1.3959119319915771, 1.6172144412994385
obj.scale = 1.0, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4028398990631104, 0.01277026254683733, 1.8408516645431519
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(748 + frame)
obj = cameras['Camera']
obj.location = -4.501839637756348, 1.3918774127960205, 1.6124926805496216
obj.scale = 1.0000004768371582, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4003922939300537, 0.017309803515672684, 1.8416908979415894
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(749 + frame)
obj = cameras['Camera']
obj.location = -4.517089366912842, 1.3895187377929688, 1.60707426071167
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3971017599105835, 0.021254807710647583, 1.8426053524017334
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(750 + frame)
obj = cameras['Camera']
obj.location = -4.5321364402771, 1.3863691091537476, 1.6019560098648071
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3937747478485107, 0.024579333141446114, 1.84261155128479
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(751 + frame)
obj = cameras['Camera']
obj.location = -4.548173904418945, 1.3846622705459595, 1.596742868423462
obj.scale = 1.0, 1.0000005960464478, 1.0000005960464478
obj.rotation_euler = 1.3906517028808594, 0.02732946164906025, 1.8428113460540771
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(752 + frame)
obj = cameras['Camera']
obj.location = -4.564365386962891, 1.3839648962020874, 1.5917398929595947
obj.scale = 0.9999999403953552, 0.9999995231628418, 0.9999995231628418
obj.rotation_euler = 1.3876898288726807, 0.029122725129127502, 1.8426859378814697
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(753 + frame)
obj = cameras['Camera']
obj.location = -4.5805463790893555, 1.383813738822937, 1.5872223377227783
obj.scale = 1.0, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.3849329948425293, 0.02995002269744873, 1.8417842388153076
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(754 + frame)
obj = cameras['Camera']
obj.location = -4.597103118896484, 1.3839188814163208, 1.5830936431884766
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3828169107437134, 0.030013039708137512, 1.8402336835861206
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(755 + frame)
obj = cameras['Camera']
obj.location = -4.613793849945068, 1.3826119899749756, 1.5798513889312744
obj.scale = 1.0000005960464478, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.3811169862747192, 0.02951132133603096, 1.838026523590088
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(756 + frame)
obj = cameras['Camera']
obj.location = -4.629727363586426, 1.3828831911087036, 1.5772894620895386
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.379587173461914, 0.029373377561569214, 1.8364468812942505
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(757 + frame)
obj = cameras['Camera']
obj.location = -4.646559715270996, 1.3816025257110596, 1.5756924152374268
obj.scale = 1.000000238418579, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.3785700798034668, 0.029607674106955528, 1.8353379964828491
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(758 + frame)
obj = cameras['Camera']
obj.location = -4.66416072845459, 1.3800499439239502, 1.5743998289108276
obj.scale = 1.0000004768371582, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3778712749481201, 0.030145619064569473, 1.834999680519104
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(759 + frame)
obj = cameras['Camera']
obj.location = -4.68161678314209, 1.3789516687393188, 1.5731332302093506
obj.scale = 0.9999997615814209, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3770360946655273, 0.03087272308766842, 1.8351250886917114
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(760 + frame)
obj = cameras['Camera']
obj.location = -4.699394702911377, 1.3776060342788696, 1.572356939315796
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.37617826461792, 0.03142084553837776, 1.8354225158691406
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(761 + frame)
obj = cameras['Camera']
obj.location = -4.717679977416992, 1.376129388809204, 1.5719902515411377
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.375413417816162, 0.03150219842791557, 1.8357312679290771
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(762 + frame)
obj = cameras['Camera']
obj.location = -4.736510753631592, 1.3745372295379639, 1.5721503496170044
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3747025728225708, 0.030988171696662903, 1.835902452468872
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(763 + frame)
obj = cameras['Camera']
obj.location = -4.7553181648254395, 1.373042106628418, 1.5727612972259521
obj.scale = 1.0, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.3739386796951294, 0.030349990352988243, 1.8359135389328003
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(764 + frame)
obj = cameras['Camera']
obj.location = -4.774361610412598, 1.3714853525161743, 1.573984146118164
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.373174786567688, 0.029696334153413773, 1.8357977867126465
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(765 + frame)
obj = cameras['Camera']
obj.location = -4.793638706207275, 1.3698039054870605, 1.575904130935669
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3725745677947998, 0.029628874734044075, 1.8353850841522217
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(766 + frame)
obj = cameras['Camera']
obj.location = -4.812348365783691, 1.3677490949630737, 1.5786434412002563
obj.scale = 1.0, 1.0, 0.9999998211860657
obj.rotation_euler = 1.3717550039291382, 0.030522840097546577, 1.835067629814148
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(767 + frame)
obj = cameras['Camera']
obj.location = -4.831902980804443, 1.3660480976104736, 1.5815075635910034
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.371402382850647, 0.032475393265485764, 1.8353726863861084
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(768 + frame)
obj = cameras['Camera']
obj.location = -4.851563453674316, 1.3644002676010132, 1.5847752094268799
obj.scale = 1.000000238418579, 1.0, 0.9999998211860657
obj.rotation_euler = 1.3711864948272705, 0.034916363656520844, 1.8359153270721436
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(769 + frame)
obj = cameras['Camera']
obj.location = -4.872008323669434, 1.3631582260131836, 1.5881128311157227
obj.scale = 0.9999999403953552, 1.000000238418579, 1.0
obj.rotation_euler = 1.3710848093032837, 0.03784290328621864, 1.836656093597412
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(770 + frame)
obj = cameras['Camera']
obj.location = -4.892998218536377, 1.3615516424179077, 1.591387391090393
obj.scale = 0.9999995231628418, 0.9999997615814209, 1.0
obj.rotation_euler = 1.3712424039840698, 0.04046520218253136, 1.8371609449386597
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(771 + frame)
obj = cameras['Camera']
obj.location = -4.913548469543457, 1.3610347509384155, 1.59437894821167
obj.scale = 1.000000238418579, 1.0, 0.9999998807907104
obj.rotation_euler = 1.371389389038086, 0.04170997440814972, 1.8372122049331665
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(772 + frame)
obj = cameras['Camera']
obj.location = -4.936562538146973, 1.361690878868103, 1.597489833831787
obj.scale = 0.9999998211860657, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.373022198677063, 0.041095342487096786, 1.8337587118148804
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(773 + frame)
obj = cameras['Camera']
obj.location = -4.957889556884766, 1.3607251644134521, 1.6009671688079834
obj.scale = 0.9999998807907104, 0.9999999403953552, 0.9999997019767761
obj.rotation_euler = 1.3732960224151611, 0.038151875138282776, 1.8270915746688843
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(774 + frame)
obj = cameras['Camera']
obj.location = -4.978542327880859, 1.3570207357406616, 1.6053962707519531
obj.scale = 0.9999998807907104, 0.9999996423721313, 0.9999997019767761
obj.rotation_euler = 1.373421311378479, 0.035506945103406906, 1.8197628259658813
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(775 + frame)
obj = cameras['Camera']
obj.location = -4.998324394226074, 1.3527894020080566, 1.6105101108551025
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.3735967874526978, 0.03486321493983269, 1.815911889076233
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(776 + frame)
obj = cameras['Camera']
obj.location = -5.0179595947265625, 1.3479156494140625, 1.6154502630233765
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3739651441574097, 0.03643221780657768, 1.8153876066207886
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(777 + frame)
obj = cameras['Camera']
obj.location = -5.038127899169922, 1.3442516326904297, 1.6199201345443726
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999997615814209
obj.rotation_euler = 1.3746038675308228, 0.03911091759800911, 1.8173412084579468
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(778 + frame)
obj = cameras['Camera']
obj.location = -5.05879020690918, 1.3423686027526855, 1.6237890720367432
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999996423721313
obj.rotation_euler = 1.3753678798675537, 0.04155459627509117, 1.8197453022003174
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(779 + frame)
obj = cameras['Camera']
obj.location = -5.079253196716309, 1.3420565128326416, 1.6271259784698486
obj.scale = 0.9999997615814209, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.3759801387786865, 0.04246677830815315, 1.8205188512802124
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(780 + frame)
obj = cameras['Camera']
obj.location = -5.09928035736084, 1.3426873683929443, 1.6310656070709229
obj.scale = 0.9999998807907104, 1.0, 1.0
obj.rotation_euler = 1.376383662223816, 0.041933007538318634, 1.8191266059875488
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(781 + frame)
obj = cameras['Camera']
obj.location = -5.118906021118164, 1.341543436050415, 1.6354997158050537
obj.scale = 1.0, 0.9999998807907104, 1.0
obj.rotation_euler = 1.3768885135650635, 0.04100148007273674, 1.8167437314987183
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(782 + frame)
obj = cameras['Camera']
obj.location = -5.138331413269043, 1.341684103012085, 1.6398981809616089
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3774418830871582, 0.04056275263428688, 1.8152146339416504
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(783 + frame)
obj = cameras['Camera']
obj.location = -5.156889915466309, 1.3426603078842163, 1.6443147659301758
obj.scale = 1.000000238418579, 1.0, 1.000000238418579
obj.rotation_euler = 1.377767562866211, 0.039590299129486084, 1.8137693405151367
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(784 + frame)
obj = cameras['Camera']
obj.location = -5.175364971160889, 1.3437230587005615, 1.6490739583969116
obj.scale = 0.9999998211860657, 0.999999463558197, 0.9999995827674866
obj.rotation_euler = 1.378002405166626, 0.03839758411049843, 1.8121055364608765
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(785 + frame)
obj = cameras['Camera']
obj.location = -5.192976951599121, 1.3451693058013916, 1.653927206993103
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3781194686889648, 0.03747836500406265, 1.811239242553711
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(786 + frame)
obj = cameras['Camera']
obj.location = -5.209891319274902, 1.346368432044983, 1.6587613821029663
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3781427145004272, 0.03771115094423294, 1.8115993738174438
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(787 + frame)
obj = cameras['Camera']
obj.location = -5.226363658905029, 1.3483786582946777, 1.6632697582244873
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3781453371047974, 0.038437943905591965, 1.8133784532546997
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(788 + frame)
obj = cameras['Camera']
obj.location = -5.242090702056885, 1.3505866527557373, 1.6677873134613037
obj.scale = 1.0000004768371582, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3780673742294312, 0.03951437398791313, 1.8163437843322754
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(789 + frame)
obj = cameras['Camera']
obj.location = -5.25773811340332, 1.3520441055297852, 1.6721585988998413
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.378141164779663, 0.041364751756191254, 1.8203351497650146
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(790 + frame)
obj = cameras['Camera']
obj.location = -5.272336483001709, 1.3541970252990723, 1.6746456623077393
obj.scale = 0.9999999403953552, 0.9999997019767761, 0.9999996423721313
obj.rotation_euler = 1.3782505989074707, 0.04403256997466087, 1.8258068561553955
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(791 + frame)
obj = cameras['Camera']
obj.location = -5.287606239318848, 1.35667085647583, 1.6781463623046875
obj.scale = 1.0, 0.9999998807907104, 0.9999997019767761
obj.rotation_euler = 1.3790301084518433, 0.04685184359550476, 1.8321150541305542
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(792 + frame)
obj = cameras['Camera']
obj.location = -5.302540302276611, 1.3595699071884155, 1.6809024810791016
obj.scale = 1.0000001192092896, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.379931092262268, 0.04863821342587471, 1.8380578756332397
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(793 + frame)
obj = cameras['Camera']
obj.location = -5.316919326782227, 1.3632285594940186, 1.6828486919403076
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3806394338607788, 0.04854411259293556, 1.8425792455673218
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(794 + frame)
obj = cameras['Camera']
obj.location = -5.331038475036621, 1.3665533065795898, 1.6843154430389404
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.381211519241333, 0.04649171605706215, 1.8451634645462036
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(795 + frame)
obj = cameras['Camera']
obj.location = -5.344198226928711, 1.3699262142181396, 1.685090184211731
obj.scale = 0.9999998211860657, 1.0, 1.0
obj.rotation_euler = 1.3817211389541626, 0.043207380920648575, 1.845697045326233
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(796 + frame)
obj = cameras['Camera']
obj.location = -5.357332229614258, 1.3724117279052734, 1.6852142810821533
obj.scale = 0.9999998807907104, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3823636770248413, 0.039116207510232925, 1.8446983098983765
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(797 + frame)
obj = cameras['Camera']
obj.location = -5.369708061218262, 1.372635841369629, 1.685208797454834
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3832931518554688, 0.0354030504822731, 1.8440073728561401
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(798 + frame)
obj = cameras['Camera']
obj.location = -5.378329753875732, 1.3750176429748535, 1.6847575902938843
obj.scale = 1.0, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.383042573928833, 0.032464735209941864, 1.8453110456466675
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(799 + frame)
obj = cameras['Camera']
obj.location = -5.387774467468262, 1.375745177268982, 1.681726098060608
obj.scale = 0.9999997615814209, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.3834556341171265, 0.029935698956251144, 1.8478116989135742
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(800 + frame)
obj = cameras['Camera']
obj.location = -5.397584915161133, 1.3781944513320923, 1.6791203022003174
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3838287591934204, 0.02745950035750866, 1.8512250185012817
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(801 + frame)
obj = cameras['Camera']
obj.location = -5.406097888946533, 1.380780577659607, 1.6764230728149414
obj.scale = 1.0000001192092896, 0.9999997615814209, 1.0
obj.rotation_euler = 1.383501648902893, 0.024100562557578087, 1.853371262550354
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(802 + frame)
obj = cameras['Camera']
obj.location = -5.415287971496582, 1.3826597929000854, 1.6725035905838013
obj.scale = 0.9999998807907104, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3828835487365723, 0.018952269107103348, 1.8533698320388794
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(803 + frame)
obj = cameras['Camera']
obj.location = -5.423865795135498, 1.3857662677764893, 1.6687833070755005
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3816980123519897, 0.013399232178926468, 1.8519039154052734
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(804 + frame)
obj = cameras['Camera']
obj.location = -5.434069633483887, 1.3887410163879395, 1.6643831729888916
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.381140947341919, 0.008151031099259853, 1.8503072261810303
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(805 + frame)
obj = cameras['Camera']
obj.location = -5.444083213806152, 1.3928022384643555, 1.6611835956573486
obj.scale = 1.0000004768371582, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3805183172225952, 0.004040827509015799, 1.8494503498077393
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(806 + frame)
obj = cameras['Camera']
obj.location = -5.454221725463867, 1.3966262340545654, 1.6577495336532593
obj.scale = 0.9999999403953552, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.3801778554916382, 0.000989799969829619, 1.8488065004348755
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(807 + frame)
obj = cameras['Camera']
obj.location = -5.465805530548096, 1.4007810354232788, 1.6542381048202515
obj.scale = 1.0000003576278687, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.380176305770874, -0.001898638205602765, 1.8475767374038696
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(808 + frame)
obj = cameras['Camera']
obj.location = -5.477788925170898, 1.406421422958374, 1.651124119758606
obj.scale = 0.9999997615814209, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.380172848701477, -0.005022670608013868, 1.8444738388061523
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(809 + frame)
obj = cameras['Camera']
obj.location = -5.490811347961426, 1.4114371538162231, 1.6482244729995728
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.3804188966751099, -0.008908303454518318, 1.838778018951416
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(810 + frame)
obj = cameras['Camera']
obj.location = -5.5030837059021, 1.4159246683120728, 1.6455470323562622
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.0000005960464478
obj.rotation_euler = 1.3805707693099976, -0.012541438452899456, 1.831300973892212
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(811 + frame)
obj = cameras['Camera']
obj.location = -5.51596736907959, 1.419889211654663, 1.6428964138031006
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.3807353973388672, -0.014676001854240894, 1.8244584798812866
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(812 + frame)
obj = cameras['Camera']
obj.location = -5.527695655822754, 1.4234853982925415, 1.6399688720703125
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.38048255443573, -0.014154630713164806, 1.8194643259048462
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(813 + frame)
obj = cameras['Camera']
obj.location = -5.541289329528809, 1.427607536315918, 1.6376547813415527
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.380384922027588, -0.010580452159047127, 1.81792414188385
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(814 + frame)
obj = cameras['Camera']
obj.location = -5.552870750427246, 1.4315667152404785, 1.6356656551361084
obj.scale = 0.9999997615814209, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.379652738571167, -0.004879589658230543, 1.8183379173278809
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(815 + frame)
obj = cameras['Camera']
obj.location = -5.566701889038086, 1.4378973245620728, 1.6344878673553467
obj.scale = 1.000000238418579, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3794673681259155, 0.0010007495293393731, 1.8204253911972046
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(816 + frame)
obj = cameras['Camera']
obj.location = -5.579777717590332, 1.4451850652694702, 1.6338084936141968
obj.scale = 1.0, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.379129409790039, 0.005730774719268084, 1.8216158151626587
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(817 + frame)
obj = cameras['Camera']
obj.location = -5.593298435211182, 1.452779769897461, 1.6331346035003662
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3788621425628662, 0.008363804779946804, 1.8217922449111938
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(818 + frame)
obj = cameras['Camera']
obj.location = -5.605964183807373, 1.4609715938568115, 1.6326205730438232
obj.scale = 1.0000003576278687, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3785006999969482, 0.009854881092905998, 1.821797490119934
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(819 + frame)
obj = cameras['Camera']
obj.location = -5.617839336395264, 1.4668662548065186, 1.6321918964385986
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999996423721313
obj.rotation_euler = 1.3783639669418335, 0.011315976269543171, 1.822534203529358
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(820 + frame)
obj = cameras['Camera']
obj.location = -5.629094123840332, 1.4740769863128662, 1.6311304569244385
obj.scale = 1.0000001192092896, 1.0000004768371582, 1.000000238418579
obj.rotation_euler = 1.3780696392059326, 0.012835316359996796, 1.825173020362854
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(821 + frame)
obj = cameras['Camera']
obj.location = -5.640311241149902, 1.4803626537322998, 1.6298030614852905
obj.scale = 1.0000003576278687, 1.000000238418579, 1.0
obj.rotation_euler = 1.3780019283294678, 0.013850466348230839, 1.8287951946258545
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(822 + frame)
obj = cameras['Camera']
obj.location = -5.651472568511963, 1.4886138439178467, 1.6277490854263306
obj.scale = 1.0000004768371582, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3771835565567017, 0.014505310915410519, 1.8328475952148438
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(823 + frame)
obj = cameras['Camera']
obj.location = -5.663161754608154, 1.4957354068756104, 1.6244338750839233
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3761221170425415, 0.0132446875795722, 1.8355765342712402
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(824 + frame)
obj = cameras['Camera']
obj.location = -5.675119400024414, 1.5041590929031372, 1.6207754611968994
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3745206594467163, 0.011079381220042706, 1.8371829986572266
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(825 + frame)
obj = cameras['Camera']
obj.location = -5.686244964599609, 1.5117626190185547, 1.6166727542877197
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3722196817398071, 0.008762490935623646, 1.8375436067581177
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(826 + frame)
obj = cameras['Camera']
obj.location = -5.6973981857299805, 1.5188363790512085, 1.6117676496505737
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999997615814209
obj.rotation_euler = 1.3698660135269165, 0.0075394585728645325, 1.8379029035568237
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(827 + frame)
obj = cameras['Camera']
obj.location = -5.7089524269104, 1.526283621788025, 1.6064811944961548
obj.scale = 0.9999997019767761, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3675626516342163, 0.007274884730577469, 1.8391244411468506
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(828 + frame)
obj = cameras['Camera']
obj.location = -5.720826148986816, 1.5337953567504883, 1.600708246231079
obj.scale = 1.000000238418579, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.365225911140442, 0.008382448926568031, 1.8405495882034302
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(829 + frame)
obj = cameras['Camera']
obj.location = -5.73299503326416, 1.5422580242156982, 1.5950433015823364
obj.scale = 0.9999997615814209, 1.0, 0.9999999403953552
obj.rotation_euler = 1.362486481666565, 0.009549564681947231, 1.8417856693267822
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(830 + frame)
obj = cameras['Camera']
obj.location = -5.744708061218262, 1.5509144067764282, 1.5891811847686768
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3594446182250977, 0.010686748661100864, 1.8426859378814697
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(831 + frame)
obj = cameras['Camera']
obj.location = -5.755101203918457, 1.5593070983886719, 1.5832207202911377
obj.scale = 1.0, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3561946153640747, 0.014542333781719208, 1.844037413597107
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(832 + frame)
obj = cameras['Camera']
obj.location = -5.765243053436279, 1.567652940750122, 1.5776827335357666
obj.scale = 1.0000001192092896, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3540929555892944, 0.019001442939043045, 1.847749948501587
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(833 + frame)
obj = cameras['Camera']
obj.location = -5.773907661437988, 1.5767146348953247, 1.572753667831421
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.3527514934539795, 0.02501855045557022, 1.853798747062683
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(834 + frame)
obj = cameras['Camera']
obj.location = -5.783246040344238, 1.587073802947998, 1.567521095275879
obj.scale = 0.9999995827674866, 1.0, 1.0000003576278687
obj.rotation_euler = 1.3521524667739868, 0.03200845047831535, 1.8612335920333862
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(835 + frame)
obj = cameras['Camera']
obj.location = -5.792168617248535, 1.5967499017715454, 1.5640137195587158
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.351865291595459, 0.03388660401105881, 1.8678922653198242
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(836 + frame)
obj = cameras['Camera']
obj.location = -5.801305294036865, 1.6063110828399658, 1.5614893436431885
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3508155345916748, 0.03488226979970932, 1.8733739852905273
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(837 + frame)
obj = cameras['Camera']
obj.location = -5.811514377593994, 1.6170297861099243, 1.5592997074127197
obj.scale = 0.9999998807907104, 1.000000238418579, 0.9999999403953552
obj.rotation_euler = 1.3491252660751343, 0.0328373983502388, 1.8767529726028442
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(838 + frame)
obj = cameras['Camera']
obj.location = -5.82125186920166, 1.6245265007019043, 1.5566613674163818
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3478330373764038, 0.030302442610263824, 1.8774025440216064
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(839 + frame)
obj = cameras['Camera']
obj.location = -5.830315589904785, 1.630728006362915, 1.5556011199951172
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3471163511276245, 0.03043307177722454, 1.8802306652069092
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(840 + frame)
obj = cameras['Camera']
obj.location = -5.840253829956055, 1.636031150817871, 1.5557119846343994
obj.scale = 1.0000001192092896, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3470789194107056, 0.030527036637067795, 1.8849321603775024
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(841 + frame)
obj = cameras['Camera']
obj.location = -5.851755142211914, 1.6428097486495972, 1.5559673309326172
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3469598293304443, 0.029589008539915085, 1.8905314207077026
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(842 + frame)
obj = cameras['Camera']
obj.location = -5.863961696624756, 1.649104118347168, 1.5570292472839355
obj.scale = 0.9999999403953552, 1.0000004768371582, 1.0000004768371582
obj.rotation_euler = 1.3459160327911377, 0.02682083286345005, 1.8944298028945923
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(843 + frame)
obj = cameras['Camera']
obj.location = -5.875571250915527, 1.6550748348236084, 1.5579073429107666
obj.scale = 1.0000001192092896, 0.9999998211860657, 1.0
obj.rotation_euler = 1.3436681032180786, 0.023709876462817192, 1.8964688777923584
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(844 + frame)
obj = cameras['Camera']
obj.location = -5.885804176330566, 1.6608632802963257, 1.5586930513381958
obj.scale = 1.0, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.340781331062317, 0.021372945979237556, 1.8983560800552368
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(845 + frame)
obj = cameras['Camera']
obj.location = -5.8965020179748535, 1.6657466888427734, 1.5592032670974731
obj.scale = 0.9999998807907104, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3385241031646729, 0.020724352449178696, 1.901502251625061
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(846 + frame)
obj = cameras['Camera']
obj.location = -5.907193183898926, 1.6704109907150269, 1.5593820810317993
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3370766639709473, 0.020993508398532867, 1.9065525531768799
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(847 + frame)
obj = cameras['Camera']
obj.location = -5.917795181274414, 1.6751630306243896, 1.5594520568847656
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.3364473581314087, 0.02475031465291977, 1.9130810499191284
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(848 + frame)
obj = cameras['Camera']
obj.location = -5.928723335266113, 1.681281566619873, 1.5596157312393188
obj.scale = 1.0, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3363789319992065, 0.02577166259288788, 1.920586109161377
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(849 + frame)
obj = cameras['Camera']
obj.location = -5.94044303894043, 1.6870627403259277, 1.5589736700057983
obj.scale = 0.9999998211860657, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.3369956016540527, 0.029065880924463272, 1.9276397228240967
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(850 + frame)
obj = cameras['Camera']
obj.location = -5.951679229736328, 1.6935606002807617, 1.5582560300827026
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3374968767166138, 0.028198128566145897, 1.934006690979004
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(851 + frame)
obj = cameras['Camera']
obj.location = -5.963889122009277, 1.7004709243774414, 1.5558950901031494
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.3379156589508057, 0.027113592252135277, 1.9387742280960083
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(852 + frame)
obj = cameras['Camera']
obj.location = -5.9763898849487305, 1.707651138305664, 1.5542023181915283
obj.scale = 1.0000003576278687, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.337584376335144, 0.022453254088759422, 1.9412041902542114
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(853 + frame)
obj = cameras['Camera']
obj.location = -5.989117622375488, 1.7151364088058472, 1.5515668392181396
obj.scale = 0.9999999403953552, 1.000000238418579, 0.9999999403953552
obj.rotation_euler = 1.3366780281066895, 0.017959721386432648, 1.940154790878296
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(854 + frame)
obj = cameras['Camera']
obj.location = -6.000819206237793, 1.7217581272125244, 1.5480172634124756
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3355127573013306, 0.013266405090689659, 1.9362739324569702
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(855 + frame)
obj = cameras['Camera']
obj.location = -6.011848449707031, 1.7285752296447754, 1.5441535711288452
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3346030712127686, 0.008574185892939568, 1.9321969747543335
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(856 + frame)
obj = cameras['Camera']
obj.location = -6.021842956542969, 1.73564612865448, 1.5402857065200806
obj.scale = 0.9999996423721313, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3340259790420532, 0.0049741859547793865, 1.9283454418182373
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(857 + frame)
obj = cameras['Camera']
obj.location = -6.032973289489746, 1.7428934574127197, 1.5363192558288574
obj.scale = 0.9999999403953552, 0.9999998807907104, 1.0
obj.rotation_euler = 1.3340123891830444, 0.00024948391364887357, 1.9242290258407593
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(858 + frame)
obj = cameras['Camera']
obj.location = -6.042269706726074, 1.7495702505111694, 1.5319280624389648
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.333810806274414, -0.003916620742529631, 1.918662428855896
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(859 + frame)
obj = cameras['Camera']
obj.location = -6.051302909851074, 1.754858374595642, 1.5272982120513916
obj.scale = 1.0, 0.9999997019767761, 0.9999997615814209
obj.rotation_euler = 1.3341501951217651, -0.006337660830467939, 1.9128389358520508
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(860 + frame)
obj = cameras['Camera']
obj.location = -6.0594658851623535, 1.7591078281402588, 1.5220410823822021
obj.scale = 1.000000238418579, 1.000000238418579, 0.9999998807907104
obj.rotation_euler = 1.3349308967590332, -0.0073201642371714115, 1.907499074935913
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(861 + frame)
obj = cameras['Camera']
obj.location = -6.067093849182129, 1.7622839212417603, 1.5162417888641357
obj.scale = 1.0, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3362479209899902, -0.006540155503898859, 1.9033178091049194
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(862 + frame)
obj = cameras['Camera']
obj.location = -6.074766159057617, 1.764587640762329, 1.5101159811019897
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3382314443588257, -0.004212105181068182, 1.9005955457687378
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(863 + frame)
obj = cameras['Camera']
obj.location = -6.082129001617432, 1.7673192024230957, 1.5041477680206299
obj.scale = 0.9999998807907104, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3404768705368042, -0.0020812724251300097, 1.899695873260498
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(864 + frame)
obj = cameras['Camera']
obj.location = -6.089939117431641, 1.7704966068267822, 1.4965174198150635
obj.scale = 0.9999999403953552, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3426703214645386, -0.0010116251651197672, 1.8992328643798828
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(865 + frame)
obj = cameras['Camera']
obj.location = -6.097417831420898, 1.774306297302246, 1.4907699823379517
obj.scale = 0.9999997615814209, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3439987897872925, -0.0012223621597513556, 1.8981093168258667
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(866 + frame)
obj = cameras['Camera']
obj.location = -6.105997562408447, 1.7770415544509888, 1.4851024150848389
obj.scale = 1.0000003576278687, 1.0000004768371582, 1.000000238418579
obj.rotation_euler = 1.345251202583313, -0.0018346873112022877, 1.8959904909133911
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(867 + frame)
obj = cameras['Camera']
obj.location = -6.113709449768066, 1.7790169715881348, 1.479278802871704
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3462618589401245, -0.002265283837914467, 1.8934756517410278
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(868 + frame)
obj = cameras['Camera']
obj.location = -6.122419834136963, 1.7799129486083984, 1.4733929634094238
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3475381135940552, -0.002810757141560316, 1.89151930809021
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(869 + frame)
obj = cameras['Camera']
obj.location = -6.130538463592529, 1.7811332941055298, 1.4679315090179443
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3486335277557373, -0.003371930681169033, 1.890419840812683
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(870 + frame)
obj = cameras['Camera']
obj.location = -6.138134479522705, 1.781455397605896, 1.4624454975128174
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3495887517929077, -0.0031133582815527916, 1.8896821737289429
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(871 + frame)
obj = cameras['Camera']
obj.location = -6.14592981338501, 1.7812693119049072, 1.4571812152862549
obj.scale = 1.0, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.3506962060928345, -0.003241604659706354, 1.890061616897583
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(872 + frame)
obj = cameras['Camera']
obj.location = -6.154077529907227, 1.780494213104248, 1.451961636543274
obj.scale = 0.9999997615814209, 0.9999995827674866, 0.9999996423721313
obj.rotation_euler = 1.3519682884216309, -0.003583015874028206, 1.8912642002105713
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(873 + frame)
obj = cameras['Camera']
obj.location = -6.1622724533081055, 1.7797362804412842, 1.4470961093902588
obj.scale = 1.0000001192092896, 0.9999995231628418, 0.9999997615814209
obj.rotation_euler = 1.3527030944824219, -0.003435819875448942, 1.8929104804992676
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(874 + frame)
obj = cameras['Camera']
obj.location = -6.170443058013916, 1.778440237045288, 1.4420113563537598
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3527140617370605, -0.0030397633090615273, 1.894533634185791
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(875 + frame)
obj = cameras['Camera']
obj.location = -6.179488182067871, 1.7774549722671509, 1.4373774528503418
obj.scale = 1.0000004768371582, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.3519879579544067, -0.003138586413115263, 1.896564245223999
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(876 + frame)
obj = cameras['Camera']
obj.location = -6.188453197479248, 1.7771109342575073, 1.432824730873108
obj.scale = 0.9999999403953552, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.3504992723464966, -0.0024546897038817406, 1.8985060453414917
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(877 + frame)
obj = cameras['Camera']
obj.location = -6.19838809967041, 1.7764451503753662, 1.4271435737609863
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3488013744354248, -0.0010483573423698545, 1.9004348516464233
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(878 + frame)
obj = cameras['Camera']
obj.location = -6.208288669586182, 1.7761237621307373, 1.4221928119659424
obj.scale = 1.0, 0.9999997615814209, 0.9999996423721313
obj.rotation_euler = 1.3469879627227783, 0.0003108486416749656, 1.9028254747390747
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(879 + frame)
obj = cameras['Camera']
obj.location = -6.218165397644043, 1.7758595943450928, 1.4178791046142578
obj.scale = 1.0000003576278687, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3455690145492554, 0.0028660085517913103, 1.9057042598724365
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(880 + frame)
obj = cameras['Camera']
obj.location = -6.228450775146484, 1.7762104272842407, 1.4132612943649292
obj.scale = 1.0000003576278687, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3447043895721436, 0.004614551551640034, 1.9091792106628418
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(881 + frame)
obj = cameras['Camera']
obj.location = -6.238946437835693, 1.7766648530960083, 1.409769892692566
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.344434380531311, 0.005381301511079073, 1.9132080078125
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(882 + frame)
obj = cameras['Camera']
obj.location = -6.249311923980713, 1.7789497375488281, 1.4071487188339233
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.3437250852584839, 0.005678585264831781, 1.9173827171325684
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(883 + frame)
obj = cameras['Camera']
obj.location = -6.259406089782715, 1.7819170951843262, 1.4045779705047607
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3425874710083008, 0.005760224536061287, 1.919822335243225
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(884 + frame)
obj = cameras['Camera']
obj.location = -6.269599437713623, 1.7856416702270508, 1.4027838706970215
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.3417563438415527, 0.005392610095441341, 1.9211260080337524
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(885 + frame)
obj = cameras['Camera']
obj.location = -6.278949737548828, 1.7901146411895752, 1.401616096496582
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.341131567955017, 0.005241943523287773, 1.9216244220733643
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(886 + frame)
obj = cameras['Camera']
obj.location = -6.28839111328125, 1.7955124378204346, 1.4015581607818604
obj.scale = 0.9999997615814209, 0.9999998807907104, 0.9999997019767761
obj.rotation_euler = 1.3411718606948853, 0.004481001291424036, 1.921748399734497
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(887 + frame)
obj = cameras['Camera']
obj.location = -6.297853469848633, 1.8010261058807373, 1.4007573127746582
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0
obj.rotation_euler = 1.3420888185501099, 0.004019240848720074, 1.9204769134521484
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(888 + frame)
obj = cameras['Camera']
obj.location = -6.307782173156738, 1.8071072101593018, 1.4011338949203491
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3430155515670776, 0.004490201827138662, 1.918199896812439
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(889 + frame)
obj = cameras['Camera']
obj.location = -6.317418098449707, 1.8123513460159302, 1.401362419128418
obj.scale = 1.0000004768371582, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3443727493286133, 0.004602494183927774, 1.9147640466690063
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(890 + frame)
obj = cameras['Camera']
obj.location = -6.326901912689209, 1.818249225616455, 1.4022326469421387
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3464683294296265, 0.0030204621143639088, 1.9118577241897583
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(891 + frame)
obj = cameras['Camera']
obj.location = -6.33608865737915, 1.8227477073669434, 1.4026577472686768
obj.scale = 1.000000238418579, 1.0000001192092896, 0.9999998211860657
obj.rotation_euler = 1.349530577659607, 0.0032652050722390413, 1.9087847471237183
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(892 + frame)
obj = cameras['Camera']
obj.location = -6.346045970916748, 1.8279310464859009, 1.402899146080017
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.353309154510498, 0.004875414073467255, 1.9066654443740845
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(893 + frame)
obj = cameras['Camera']
obj.location = -6.354866027832031, 1.8295795917510986, 1.4037492275238037
obj.scale = 0.9999997615814209, 0.9999997019767761, 0.9999995827674866
obj.rotation_euler = 1.3566645383834839, 0.00641207629814744, 1.905287265777588
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(894 + frame)
obj = cameras['Camera']
obj.location = -6.362578392028809, 1.8313162326812744, 1.4043397903442383
obj.scale = 0.9999998211860657, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.359418511390686, 0.006722132675349712, 1.9062772989273071
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(895 + frame)
obj = cameras['Camera']
obj.location = -6.37108850479126, 1.831286907196045, 1.4055092334747314
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.363317608833313, 0.005789271555840969, 1.9099781513214111
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(896 + frame)
obj = cameras['Camera']
obj.location = -6.379148006439209, 1.8338879346847534, 1.407597303390503
obj.scale = 1.000000238418579, 1.0000001192092896, 0.9999998807907104
obj.rotation_euler = 1.3659337759017944, 0.0030072906520217657, 1.9152600765228271
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(897 + frame)
obj = cameras['Camera']
obj.location = -6.387757778167725, 1.837178111076355, 1.4101495742797852
obj.scale = 0.9999998807907104, 0.9999997019767761, 0.9999996423721313
obj.rotation_euler = 1.3673763275146484, 0.000717655464541167, 1.919670820236206
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(898 + frame)
obj = cameras['Camera']
obj.location = -6.396380424499512, 1.8406893014907837, 1.4122838973999023
obj.scale = 0.9999997615814209, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3680325746536255, -0.0015791901387274265, 1.9216043949127197
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(899 + frame)
obj = cameras['Camera']
obj.location = -6.404967308044434, 1.843996524810791, 1.414293885231018
obj.scale = 1.0000001192092896, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3681403398513794, -0.00196369388140738, 1.9212121963500977
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(900 + frame)
obj = cameras['Camera']
obj.location = -6.413967132568359, 1.846517562866211, 1.416208267211914
obj.scale = 0.9999998211860657, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.3683282136917114, -0.0005156758124940097, 1.919062614440918
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(901 + frame)
obj = cameras['Camera']
obj.location = -6.4227399826049805, 1.849915623664856, 1.4179415702819824
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3684271574020386, 0.0032817681785672903, 1.917013168334961
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(902 + frame)
obj = cameras['Camera']
obj.location = -6.431742191314697, 1.8518691062927246, 1.4202690124511719
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.3698058128356934, 0.00683578522875905, 1.9160709381103516
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(903 + frame)
obj = cameras['Camera']
obj.location = -6.441984176635742, 1.8544256687164307, 1.4231090545654297
obj.scale = 0.9999999403953552, 1.0000007152557373, 1.0000005960464478
obj.rotation_euler = 1.3721927404403687, 0.008471548557281494, 1.9175280332565308
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(904 + frame)
obj = cameras['Camera']
obj.location = -6.451909065246582, 1.8553086519241333, 1.4253854751586914
obj.scale = 1.000000238418579, 0.9999999403953552, 1.0
obj.rotation_euler = 1.3755221366882324, 0.008947250433266163, 1.9206244945526123
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(905 + frame)
obj = cameras['Camera']
obj.location = -6.461553573608398, 1.8591020107269287, 1.4293289184570312
obj.scale = 1.0, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.3774887323379517, 0.006720658857375383, 1.9272650480270386
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(906 + frame)
obj = cameras['Camera']
obj.location = -6.472729682922363, 1.8639400005340576, 1.4331989288330078
obj.scale = 0.9999998211860657, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3787976503372192, 0.005195797421038151, 1.9317489862442017
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(907 + frame)
obj = cameras['Camera']
obj.location = -6.484806060791016, 1.8694998025894165, 1.4368146657943726
obj.scale = 1.0000001192092896, 0.9999995231628418, 0.9999995827674866
obj.rotation_euler = 1.3793140649795532, 0.002238559303805232, 1.9336576461791992
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(908 + frame)
obj = cameras['Camera']
obj.location = -6.497994422912598, 1.8750402927398682, 1.4399735927581787
obj.scale = 0.9999998807907104, 0.9999995827674866, 0.9999995827674866
obj.rotation_euler = 1.3791364431381226, -0.0020724115893244743, 1.9332764148712158
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(909 + frame)
obj = cameras['Camera']
obj.location = -6.511428356170654, 1.8806449174880981, 1.4428433179855347
obj.scale = 0.9999998807907104, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.3777023553848267, -0.006158630363643169, 1.9313088655471802
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(910 + frame)
obj = cameras['Camera']
obj.location = -6.52476692199707, 1.8863344192504883, 1.4456055164337158
obj.scale = 0.9999997615814209, 0.9999997615814209, 0.9999997615814209
obj.rotation_euler = 1.3753223419189453, -0.0073183448985219, 1.9280940294265747
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(911 + frame)
obj = cameras['Camera']
obj.location = -6.538588523864746, 1.8914179801940918, 1.4482409954071045
obj.scale = 0.9999998211860657, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.3728100061416626, -0.008056770078837872, 1.924561619758606
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(912 + frame)
obj = cameras['Camera']
obj.location = -6.551463603973389, 1.8976051807403564, 1.4514086246490479
obj.scale = 1.0, 0.9999995827674866, 0.9999997615814209
obj.rotation_euler = 1.3695406913757324, -0.007409992162138224, 1.9215686321258545
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(913 + frame)
obj = cameras['Camera']
obj.location = -6.564711093902588, 1.9027040004730225, 1.4542174339294434
obj.scale = 1.0000001192092896, 0.9999997019767761, 0.9999996423721313
obj.rotation_euler = 1.3669015169143677, -0.0068403067998588085, 1.9194562435150146
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(914 + frame)
obj = cameras['Camera']
obj.location = -6.5711565017700195, 1.9098941087722778, 1.4549777507781982
obj.scale = 1.000000238418579, 1.000000238418579, 0.9999999403953552
obj.rotation_euler = 1.3620333671569824, -0.007053500507026911, 1.9176698923110962
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(915 + frame)
obj = cameras['Camera']
obj.location = -6.585419654846191, 1.9148035049438477, 1.4580371379852295
obj.scale = 0.9999998807907104, 0.9999998807907104, 1.0000001192092896
obj.rotation_euler = 1.359867811203003, -0.007018337957561016, 1.9186124801635742
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(916 + frame)
obj = cameras['Camera']
obj.location = -6.598071098327637, 1.9214518070220947, 1.460777759552002
obj.scale = 0.9999998211860657, 1.0, 0.9999998807907104
obj.rotation_euler = 1.356593370437622, -0.006424300372600555, 1.9197877645492554
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(917 + frame)
obj = cameras['Camera']
obj.location = -6.6115217208862305, 1.9270610809326172, 1.4628808498382568
obj.scale = 1.000000238418579, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3537859916687012, -0.0070161777548491955, 1.920478105545044
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(918 + frame)
obj = cameras['Camera']
obj.location = -6.624843597412109, 1.932563066482544, 1.4643571376800537
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.3506518602371216, -0.005541081074625254, 1.9205068349838257
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(919 + frame)
obj = cameras['Camera']
obj.location = -6.637958526611328, 1.9387764930725098, 1.465914249420166
obj.scale = 1.000000238418579, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3475401401519775, -0.0009242685628123581, 1.92047119140625
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(920 + frame)
obj = cameras['Camera']
obj.location = -6.6490478515625, 1.9439215660095215, 1.466326117515564
obj.scale = 1.0000003576278687, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.3451075553894043, 0.0024178405292332172, 1.91994047164917
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(921 + frame)
obj = cameras['Camera']
obj.location = -6.661545276641846, 1.950509786605835, 1.468320608139038
obj.scale = 1.000000238418579, 1.0, 0.9999998807907104
obj.rotation_euler = 1.3444254398345947, 0.005590735003352165, 1.9215539693832397
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(922 + frame)
obj = cameras['Camera']
obj.location = -6.672425270080566, 1.9556552171707153, 1.4698965549468994
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.34602952003479, 0.00653090188279748, 1.924658179283142
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(923 + frame)
obj = cameras['Camera']
obj.location = -6.681726455688477, 1.961779236793518, 1.4724757671356201
obj.scale = 1.000000238418579, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3484145402908325, 0.005357253830879927, 1.9310147762298584
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(924 + frame)
obj = cameras['Camera']
obj.location = -6.69064474105835, 1.9666500091552734, 1.475450038909912
obj.scale = 0.9999998807907104, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3525199890136719, 0.003373832209035754, 1.9390617609024048
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(925 + frame)
obj = cameras['Camera']
obj.location = -6.69752311706543, 1.972887396812439, 1.4787089824676514
obj.scale = 0.9999997615814209, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3566051721572876, 0.00022023665951564908, 1.946014642715454
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(926 + frame)
obj = cameras['Camera']
obj.location = -6.7052202224731445, 1.978170394897461, 1.4819122552871704
obj.scale = 1.000000238418579, 1.0, 0.9999998807907104
obj.rotation_euler = 1.361983060836792, -0.0025906001683324575, 1.950234055519104
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(927 + frame)
obj = cameras['Camera']
obj.location = -6.712523460388184, 1.9847443103790283, 1.4852731227874756
obj.scale = 0.9999995231628418, 0.9999995231628418, 0.999999463558197
obj.rotation_euler = 1.366803526878357, -0.006034814286977053, 1.9519023895263672
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(928 + frame)
obj = cameras['Camera']
obj.location = -6.719653606414795, 1.9910016059875488, 1.4883474111557007
obj.scale = 0.9999997019767761, 0.999999463558197, 0.9999996423721313
obj.rotation_euler = 1.3724907636642456, -0.005870405118912458, 1.9508732557296753
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(929 + frame)
obj = cameras['Camera']
obj.location = -6.726300239562988, 1.99727463722229, 1.4912904500961304
obj.scale = 1.0000001192092896, 0.9999996423721313, 0.9999995231628418
obj.rotation_euler = 1.3778283596038818, -0.0062742154113948345, 1.9481955766677856
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(930 + frame)
obj = cameras['Camera']
obj.location = -6.733561038970947, 2.002232551574707, 1.494625210762024
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.3838495016098022, -0.0073575410060584545, 1.9456603527069092
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(931 + frame)
obj = cameras['Camera']
obj.location = -6.739212989807129, 2.008033275604248, 1.4983112812042236
obj.scale = 1.0, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.3893465995788574, -0.007074153516441584, 1.9443191289901733
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(932 + frame)
obj = cameras['Camera']
obj.location = -6.745923042297363, 2.013319969177246, 1.5021240711212158
obj.scale = 1.0, 0.9999998807907104, 1.0000001192092896
obj.rotation_euler = 1.3949863910675049, -0.006645738612860441, 1.9446172714233398
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(933 + frame)
obj = cameras['Camera']
obj.location = -6.7522196769714355, 2.016157627105713, 1.5045738220214844
obj.scale = 0.9999999403953552, 0.9999998807907104, 0.9999997019767761
obj.rotation_euler = 1.4005602598190308, -0.007044758182018995, 1.9444804191589355
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(934 + frame)
obj = cameras['Camera']
obj.location = -6.758901596069336, 2.0203192234039307, 1.5078014135360718
obj.scale = 0.9999998211860657, 0.9999996423721313, 0.9999995231628418
obj.rotation_euler = 1.4050227403640747, -0.006120659876614809, 1.944539189338684
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(935 + frame)
obj = cameras['Camera']
obj.location = -6.764685153961182, 2.0228147506713867, 1.5109779834747314
obj.scale = 0.9999997019767761, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4087821245193481, -0.004873276688158512, 1.9436506032943726
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(936 + frame)
obj = cameras['Camera']
obj.location = -6.771398067474365, 2.0250015258789062, 1.5141141414642334
obj.scale = 0.9999997019767761, 0.9999997615814209, 0.9999996423721313
obj.rotation_euler = 1.4121052026748657, -0.004107877612113953, 1.9429701566696167
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(937 + frame)
obj = cameras['Camera']
obj.location = -6.777252197265625, 2.0258281230926514, 1.5172444581985474
obj.scale = 0.9999999403953552, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4146467447280884, -0.002827274613082409, 1.941716194152832
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(938 + frame)
obj = cameras['Camera']
obj.location = -6.78313684463501, 2.0264034271240234, 1.5202136039733887
obj.scale = 0.9999998807907104, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4163964986801147, -0.0014524605358019471, 1.9405773878097534
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(939 + frame)
obj = cameras['Camera']
obj.location = -6.789024353027344, 2.0272817611694336, 1.5230717658996582
obj.scale = 0.9999998807907104, 1.000000238418579, 1.0000003576278687
obj.rotation_euler = 1.41740882396698, 0.0012226216495037079, 1.9393545389175415
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(940 + frame)
obj = cameras['Camera']
obj.location = -6.794497489929199, 2.0275540351867676, 1.5254700183868408
obj.scale = 1.0000003576278687, 1.0000003576278687, 1.0000004768371582
obj.rotation_euler = 1.4179965257644653, 0.004749008920043707, 1.937555193901062
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(941 + frame)
obj = cameras['Camera']
obj.location = -6.800039768218994, 2.0274009704589844, 1.527238130569458
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999997019767761
obj.rotation_euler = 1.4185224771499634, 0.008744125254452229, 1.9353594779968262
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(942 + frame)
obj = cameras['Camera']
obj.location = -6.805944919586182, 2.025515556335449, 1.5285431146621704
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998211860657
obj.rotation_euler = 1.4195749759674072, 0.011608203873038292, 1.9330662488937378
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(943 + frame)
obj = cameras['Camera']
obj.location = -6.811217308044434, 2.0245397090911865, 1.529428482055664
obj.scale = 1.0, 1.0000004768371582, 1.0000003576278687
obj.rotation_euler = 1.4203464984893799, 0.013188080862164497, 1.9320590496063232
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(944 + frame)
obj = cameras['Camera']
obj.location = -6.8163628578186035, 2.0234577655792236, 1.5299171209335327
obj.scale = 0.9999997019767761, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4212958812713623, 0.014114913530647755, 1.9323818683624268
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(945 + frame)
obj = cameras['Camera']
obj.location = -6.8220415115356445, 2.0222933292388916, 1.529484510421753
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4226138591766357, 0.014629479497671127, 1.9333277940750122
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(946 + frame)
obj = cameras['Camera']
obj.location = -6.826995372772217, 2.021266460418701, 1.5283886194229126
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4235414266586304, 0.015108342282474041, 1.9338195323944092
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(947 + frame)
obj = cameras['Camera']
obj.location = -6.831244468688965, 2.019029140472412, 1.5265542268753052
obj.scale = 0.9999997615814209, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.4241999387741089, 0.01728854700922966, 1.9326905012130737
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(948 + frame)
obj = cameras['Camera']
obj.location = -6.835000991821289, 2.016897201538086, 1.5239322185516357
obj.scale = 1.0000004768371582, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.4244840145111084, 0.019775215536355972, 1.9304777383804321
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(949 + frame)
obj = cameras['Camera']
obj.location = -6.8380022048950195, 2.015348434448242, 1.520759105682373
obj.scale = 0.9999999403953552, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4235507249832153, 0.027073942124843597, 1.92582106590271
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(950 + frame)
obj = cameras['Camera']
obj.location = -6.8406548500061035, 2.013991355895996, 1.517816424369812
obj.scale = 1.0000003576278687, 1.000000238418579, 0.9999999403953552
obj.rotation_euler = 1.422987461090088, 0.031045066192746162, 1.9209400415420532
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(951 + frame)
obj = cameras['Camera']
obj.location = -6.842785835266113, 2.0124964714050293, 1.513980507850647
obj.scale = 0.9999998211860657, 0.9999999403953552, 1.0
obj.rotation_euler = 1.423225998878479, 0.03457772359251976, 1.9177558422088623
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(952 + frame)
obj = cameras['Camera']
obj.location = -6.843804359436035, 2.010509967803955, 1.5109264850616455
obj.scale = 1.0000001192092896, 0.9999997615814209, 0.9999996423721313
obj.rotation_euler = 1.424093246459961, 0.03762586787343025, 1.9167733192443848
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(953 + frame)
obj = cameras['Camera']
obj.location = -6.8440656661987305, 2.008751630783081, 1.5073530673980713
obj.scale = 1.0000004768371582, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.425365924835205, 0.03985925391316414, 1.917590856552124
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(954 + frame)
obj = cameras['Camera']
obj.location = -6.844296455383301, 2.005654811859131, 1.503243088722229
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4274882078170776, 0.04122309759259224, 1.9191856384277344
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(955 + frame)
obj = cameras['Camera']
obj.location = -6.844337463378906, 2.0047554969787598, 1.4987263679504395
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000004768371582
obj.rotation_euler = 1.4291285276412964, 0.042910609394311905, 1.9218518733978271
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(956 + frame)
obj = cameras['Camera']
obj.location = -6.844576835632324, 2.0046768188476562, 1.4937286376953125
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4303045272827148, 0.04530807584524155, 1.9241571426391602
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(957 + frame)
obj = cameras['Camera']
obj.location = -6.844395160675049, 2.0035006999969482, 1.4882609844207764
obj.scale = 1.000000238418579, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.4311965703964233, 0.047588370740413666, 1.924877643585205
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(958 + frame)
obj = cameras['Camera']
obj.location = -6.844073295593262, 2.002902030944824, 1.481608510017395
obj.scale = 1.000000238418579, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4317572116851807, 0.047820817679166794, 1.9251371622085571
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(959 + frame)
obj = cameras['Camera']
obj.location = -6.843740463256836, 2.00297474861145, 1.4755630493164062
obj.scale = 0.9999999403953552, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.4321972131729126, 0.0462564192712307, 1.9259990453720093
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(960 + frame)
obj = cameras['Camera']
obj.location = -6.8428544998168945, 2.002065420150757, 1.469470739364624
obj.scale = 1.0000001192092896, 0.9999998807907104, 1.0
obj.rotation_euler = 1.432909607887268, 0.04392668604850769, 1.9270343780517578
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(961 + frame)
obj = cameras['Camera']
obj.location = -6.842155456542969, 2.001864433288574, 1.4633430242538452
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4341726303100586, 0.03791460767388344, 1.9305551052093506
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(962 + frame)
obj = cameras['Camera']
obj.location = -6.841355800628662, 2.0026936531066895, 1.4571075439453125
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.4348700046539307, 0.037869859486818314, 1.9345312118530273
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(963 + frame)
obj = cameras['Camera']
obj.location = -6.8405351638793945, 2.0031256675720215, 1.4505054950714111
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4351940155029297, 0.037905141711235046, 1.9377400875091553
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(964 + frame)
obj = cameras['Camera']
obj.location = -6.838680744171143, 2.0047998428344727, 1.4433010816574097
obj.scale = 1.0000001192092896, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.434033751487732, 0.037261415272951126, 1.9386781454086304
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(965 + frame)
obj = cameras['Camera']
obj.location = -6.836865425109863, 2.0050978660583496, 1.437730312347412
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.4325425624847412, 0.037315063178539276, 1.936516523361206
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(966 + frame)
obj = cameras['Camera']
obj.location = -6.8348283767700195, 2.004577159881592, 1.4327833652496338
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.430910587310791, 0.03603318706154823, 1.9335110187530518
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(967 + frame)
obj = cameras['Camera']
obj.location = -6.833022117614746, 2.0061211585998535, 1.4284007549285889
obj.scale = 1.0000003576278687, 0.9999998211860657, 0.9999997615814209
obj.rotation_euler = 1.4292274713516235, 0.03509748354554176, 1.9325997829437256
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(968 + frame)
obj = cameras['Camera']
obj.location = -6.8314528465271, 2.006603956222534, 1.4234731197357178
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.428387999534607, 0.03290010616183281, 1.9335579872131348
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(969 + frame)
obj = cameras['Camera']
obj.location = -6.830368518829346, 2.0061497688293457, 1.4197008609771729
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.4281210899353027, 0.028950653970241547, 1.9365366697311401
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(970 + frame)
obj = cameras['Camera']
obj.location = -6.829729080200195, 2.005431652069092, 1.4161221981048584
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000004768371582
obj.rotation_euler = 1.4277307987213135, 0.024448074400424957, 1.9407626390457153
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(971 + frame)
obj = cameras['Camera']
obj.location = -6.829601287841797, 2.004613161087036, 1.412663221359253
obj.scale = 0.9999998807907104, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.426716923713684, 0.023106150329113007, 1.9442557096481323
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(972 + frame)
obj = cameras['Camera']
obj.location = -6.82952880859375, 2.0034565925598145, 1.4094020128250122
obj.scale = 0.9999999403953552, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4248658418655396, 0.021127862855792046, 1.9460052251815796
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(973 + frame)
obj = cameras['Camera']
obj.location = -6.829889297485352, 2.0026750564575195, 1.4063310623168945
obj.scale = 0.9999999403953552, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.4225260019302368, 0.016225948929786682, 1.9460467100143433
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(974 + frame)
obj = cameras['Camera']
obj.location = -6.8286542892456055, 2.0033302307128906, 1.403346061706543
obj.scale = 1.0, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.4186879396438599, 0.013897087424993515, 1.9445877075195312
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(975 + frame)
obj = cameras['Camera']
obj.location = -6.828212738037109, 1.999690055847168, 1.4012606143951416
obj.scale = 0.9999997019767761, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.4161795377731323, 0.011278367601335049, 1.9418954849243164
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(976 + frame)
obj = cameras['Camera']
obj.location = -6.829889297485352, 2.0005807876586914, 1.3987233638763428
obj.scale = 1.000000238418579, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4131479263305664, 0.009728945791721344, 1.9420222043991089
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(977 + frame)
obj = cameras['Camera']
obj.location = -6.8299880027771, 1.997131109237671, 1.395987629890442
obj.scale = 1.0000003576278687, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.410478115081787, 0.00670341681689024, 1.9412113428115845
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(978 + frame)
obj = cameras['Camera']
obj.location = -6.830417633056641, 1.9961121082305908, 1.3926390409469604
obj.scale = 1.000000238418579, 1.0, 0.9999998807907104
obj.rotation_euler = 1.4068094491958618, 0.006543431431055069, 1.9414033889770508
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(979 + frame)
obj = cameras['Camera']
obj.location = -6.830727577209473, 1.995102882385254, 1.3895313739776611
obj.scale = 1.0000001192092896, 1.000000238418579, 1.000000238418579
obj.rotation_euler = 1.4031736850738525, 0.0062284949235618114, 1.9412986040115356
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(980 + frame)
obj = cameras['Camera']
obj.location = -6.8309807777404785, 1.9945778846740723, 1.3864402770996094
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3997201919555664, 0.006409517023712397, 1.9411101341247559
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(981 + frame)
obj = cameras['Camera']
obj.location = -6.831581115722656, 1.9929749965667725, 1.383734107017517
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.3973965644836426, 0.00724013103172183, 1.9412071704864502
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(982 + frame)
obj = cameras['Camera']
obj.location = -6.8317766189575195, 1.9907974004745483, 1.3815600872039795
obj.scale = 0.9999999403953552, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.3960415124893188, 0.006826228927820921, 1.942247986793518
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(983 + frame)
obj = cameras['Camera']
obj.location = -6.832058906555176, 1.9896552562713623, 1.3799153566360474
obj.scale = 1.0000001192092896, 0.9999998807907104, 0.9999998807907104
obj.rotation_euler = 1.3952653408050537, 0.007711632642894983, 1.9440596103668213
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(984 + frame)
obj = cameras['Camera']
obj.location = -6.832501411437988, 1.9870387315750122, 1.378516674041748
obj.scale = 1.0000004768371582, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3953123092651367, 0.009064395911991596, 1.9452499151229858
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(985 + frame)
obj = cameras['Camera']
obj.location = -6.832387924194336, 1.9864153861999512, 1.3769795894622803
obj.scale = 1.0000001192092896, 0.9999999403953552, 0.9999998211860657
obj.rotation_euler = 1.3949692249298096, 0.011000074446201324, 1.9468129873275757
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(986 + frame)
obj = cameras['Camera']
obj.location = -6.831605911254883, 1.9841420650482178, 1.3765064477920532
obj.scale = 1.0, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.3951561450958252, 0.01330636627972126, 1.9477146863937378
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(987 + frame)
obj = cameras['Camera']
obj.location = -6.831221580505371, 1.9829199314117432, 1.3768374919891357
obj.scale = 0.9999998211860657, 1.0000001192092896, 1.0000003576278687
obj.rotation_euler = 1.3956658840179443, 0.01830049231648445, 1.9496101140975952
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(988 + frame)
obj = cameras['Camera']
obj.location = -6.83075475692749, 1.982802391052246, 1.3769056797027588
obj.scale = 0.9999999403953552, 1.000000238418579, 1.0
obj.rotation_euler = 1.396502137184143, 0.02350720576941967, 1.9526610374450684
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(989 + frame)
obj = cameras['Camera']
obj.location = -6.831052780151367, 1.9820016622543335, 1.3784499168395996
obj.scale = 0.9999999403953552, 1.0000003576278687, 1.0000003576278687
obj.rotation_euler = 1.398377776145935, 0.02591436356306076, 1.9564346075057983
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(990 + frame)
obj = cameras['Camera']
obj.location = -6.831253528594971, 1.9806373119354248, 1.380974531173706
obj.scale = 1.0000001192092896, 1.0000003576278687, 1.0000001192092896
obj.rotation_euler = 1.4003651142120361, 0.028007909655570984, 1.9600352048873901
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(991 + frame)
obj = cameras['Camera']
obj.location = -6.832541465759277, 1.9803937673568726, 1.3838238716125488
obj.scale = 0.9999999403953552, 0.9999999403953552, 0.9999998807907104
obj.rotation_euler = 1.4028043746948242, 0.029536325484514236, 1.9646670818328857
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(992 + frame)
obj = cameras['Camera']
obj.location = -6.833378791809082, 1.9738174676895142, 1.3883519172668457
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4069273471832275, 0.029499638825654984, 1.966057538986206
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(993 + frame)
obj = cameras['Camera']
obj.location = -6.835736274719238, 1.9736864566802979, 1.3918427228927612
obj.scale = 1.0, 1.0000003576278687, 1.000000238418579
obj.rotation_euler = 1.410037875175476, 0.02976813167333603, 1.968564748764038
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(994 + frame)
obj = cameras['Camera']
obj.location = -6.838479042053223, 1.9734948873519897, 1.3971192836761475
obj.scale = 0.9999997615814209, 0.9999997019767761, 0.9999997019767761
obj.rotation_euler = 1.4132236242294312, 0.02953949198126793, 1.969004511833191
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(995 + frame)
obj = cameras['Camera']
obj.location = -6.841320037841797, 1.9737577438354492, 1.4028830528259277
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4171026945114136, 0.030029352754354477, 1.9679385423660278
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(996 + frame)
obj = cameras['Camera']
obj.location = -6.845168113708496, 1.9749243259429932, 1.409461259841919
obj.scale = 1.0000001192092896, 1.0, 0.9999999403953552
obj.rotation_euler = 1.4202253818511963, 0.030579010024666786, 1.9663883447647095
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(997 + frame)
obj = cameras['Camera']
obj.location = -6.848499298095703, 1.9759422540664673, 1.415881872177124
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999997019767761
obj.rotation_euler = 1.4231808185577393, 0.030779732391238213, 1.9648634195327759
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(998 + frame)
obj = cameras['Camera']
obj.location = -6.85164737701416, 1.9766868352890015, 1.4225897789001465
obj.scale = 0.9999997019767761, 0.9999995827674866, 0.9999997019767761
obj.rotation_euler = 1.4259225130081177, 0.03155871108174324, 1.9629912376403809
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(999 + frame)
obj = cameras['Camera']
obj.location = -6.855368137359619, 1.9786354303359985, 1.4290896654129028
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4278122186660767, 0.03383404761552811, 1.9613534212112427
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1000 + frame)
obj = cameras['Camera']
obj.location = -6.859088897705078, 1.9812612533569336, 1.4362244606018066
obj.scale = 1.0000001192092896, 0.9999998807907104, 1.0000001192092896
obj.rotation_euler = 1.428832769393921, 0.03603683039546013, 1.9598067998886108
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1001 + frame)
obj = cameras['Camera']
obj.location = -6.862886905670166, 1.9846093654632568, 1.4422821998596191
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999998211860657
obj.rotation_euler = 1.4293346405029297, 0.0386461578309536, 1.9592076539993286
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1002 + frame)
obj = cameras['Camera']
obj.location = -6.866036415100098, 1.9873310327529907, 1.4487111568450928
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.429896354675293, 0.04058922082185745, 1.9598392248153687
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1003 + frame)
obj = cameras['Camera']
obj.location = -6.86925745010376, 1.9900352954864502, 1.4552152156829834
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4305381774902344, 0.04188661649823189, 1.9621870517730713
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1004 + frame)
obj = cameras['Camera']
obj.location = -6.872845649719238, 1.9925565719604492, 1.461627721786499
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4313486814498901, 0.041992586106061935, 1.965839147567749
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1005 + frame)
obj = cameras['Camera']
obj.location = -6.876430511474609, 1.994647741317749, 1.4680222272872925
obj.scale = 0.9999998807907104, 0.9999998211860657, 1.0
obj.rotation_euler = 1.4320379495620728, 0.041291289031505585, 1.9696117639541626
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1006 + frame)
obj = cameras['Camera']
obj.location = -6.8802385330200195, 1.9972227811813354, 1.474163293838501
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.4322017431259155, 0.03860657662153244, 1.9737063646316528
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1007 + frame)
obj = cameras['Camera']
obj.location = -6.8849382400512695, 1.9996426105499268, 1.4800910949707031
obj.scale = 1.0000001192092896, 0.9999998807907104, 1.0
obj.rotation_euler = 1.4324421882629395, 0.03614851087331772, 1.976739764213562
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1008 + frame)
obj = cameras['Camera']
obj.location = -6.889824390411377, 2.002163887023926, 1.4857423305511475
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.4323285818099976, 0.034870557487010956, 1.9783165454864502
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1009 + frame)
obj = cameras['Camera']
obj.location = -6.895386219024658, 2.0048294067382812, 1.49111008644104
obj.scale = 0.9999998211860657, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.4322714805603027, 0.03331765905022621, 1.9792799949645996
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1010 + frame)
obj = cameras['Camera']
obj.location = -6.900860786437988, 2.0071067810058594, 1.4965403079986572
obj.scale = 1.0, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.4321240186691284, 0.03006584942340851, 1.9802032709121704
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1011 + frame)
obj = cameras['Camera']
obj.location = -6.906798362731934, 2.0092220306396484, 1.5019237995147705
obj.scale = 1.0, 0.9999999403953552, 1.0
obj.rotation_euler = 1.4322158098220825, 0.026377739384770393, 1.9816099405288696
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1012 + frame)
obj = cameras['Camera']
obj.location = -6.912693023681641, 2.0111799240112305, 1.5073487758636475
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.4324034452438354, 0.02423984929919243, 1.98304283618927
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1013 + frame)
obj = cameras['Camera']
obj.location = -6.918813705444336, 2.013218879699707, 1.5126850605010986
obj.scale = 1.0, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4326798915863037, 0.02236608974635601, 1.9846317768096924
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1014 + frame)
obj = cameras['Camera']
obj.location = -6.924782752990723, 2.0150089263916016, 1.517796277999878
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4331201314926147, 0.021306637674570084, 1.9856491088867188
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1015 + frame)
obj = cameras['Camera']
obj.location = -6.930475234985352, 2.015873670578003, 1.5231389999389648
obj.scale = 0.9999997019767761, 0.9999995827674866, 0.9999998211860657
obj.rotation_euler = 1.4336819648742676, 0.01809810660779476, 1.9869855642318726
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1016 + frame)
obj = cameras['Camera']
obj.location = -6.936802864074707, 2.0187981128692627, 1.527393102645874
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.4339135885238647, 0.014505380764603615, 1.989662766456604
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1017 + frame)
obj = cameras['Camera']
obj.location = -6.94231653213501, 2.0198259353637695, 1.5326266288757324
obj.scale = 0.9999998807907104, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.4341546297073364, 0.010860239155590534, 1.992213487625122
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1018 + frame)
obj = cameras['Camera']
obj.location = -6.947178840637207, 2.020663022994995, 1.5374643802642822
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4341789484024048, 0.005530193448066711, 1.9949281215667725
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1019 + frame)
obj = cameras['Camera']
obj.location = -6.951811790466309, 2.0206737518310547, 1.541422963142395
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4342869520187378, -0.0006959305610507727, 1.9973795413970947
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1020 + frame)
obj = cameras['Camera']
obj.location = -6.956148624420166, 2.020923614501953, 1.5456868410110474
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4342578649520874, -0.003177115460857749, 1.9993294477462769
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1021 + frame)
obj = cameras['Camera']
obj.location = -6.959970474243164, 2.0208020210266113, 1.549046516418457
obj.scale = 0.9999995827674866, 0.9999995231628418, 0.9999997019767761
obj.rotation_euler = 1.4339888095855713, -0.005273547489196062, 2.0010581016540527
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1022 + frame)
obj = cameras['Camera']
obj.location = -6.9640984535217285, 2.020066738128662, 1.5522825717926025
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.433765172958374, -0.010116204619407654, 2.003464937210083
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1023 + frame)
obj = cameras['Camera']
obj.location = -6.967803001403809, 2.0186591148376465, 1.5551360845565796
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.0000001192092896
obj.rotation_euler = 1.4334266185760498, -0.013568740338087082, 2.005913734436035
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1024 + frame)
obj = cameras['Camera']
obj.location = -6.970514297485352, 2.0169544219970703, 1.5577112436294556
obj.scale = 1.0, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4320240020751953, -0.01614627055823803, 2.0086731910705566
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1025 + frame)
obj = cameras['Camera']
obj.location = -6.973484992980957, 2.015183925628662, 1.5594947338104248
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.430215835571289, -0.018107447773218155, 2.012240171432495
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1026 + frame)
obj = cameras['Camera']
obj.location = -6.976799488067627, 2.013942003250122, 1.5603432655334473
obj.scale = 0.9999999403953552, 0.9999998807907104, 0.9999999403953552
obj.rotation_euler = 1.4284669160842896, -0.019461723044514656, 2.0160183906555176
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1027 + frame)
obj = cameras['Camera']
obj.location = -6.979196548461914, 2.0116724967956543, 1.5617328882217407
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4268302917480469, -0.02001139149069786, 2.0190231800079346
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1028 + frame)
obj = cameras['Camera']
obj.location = -6.981791019439697, 2.010317325592041, 1.5619251728057861
obj.scale = 0.9999999403953552, 0.9999998211860657, 1.0
obj.rotation_euler = 1.425423502922058, -0.02052062191069126, 2.0220274925231934
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1029 + frame)
obj = cameras['Camera']
obj.location = -6.983847618103027, 2.008547067642212, 1.5629856586456299
obj.scale = 1.0000001192092896, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4244134426116943, -0.02191193960607052, 2.024742603302002
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1030 + frame)
obj = cameras['Camera']
obj.location = -6.985842704772949, 2.007486581802368, 1.5636706352233887
obj.scale = 0.9999998807907104, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.4237948656082153, -0.02350504882633686, 2.0275650024414062
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1031 + frame)
obj = cameras['Camera']
obj.location = -6.9875993728637695, 2.0068039894104004, 1.5645610094070435
obj.scale = 0.9999997615814209, 0.9999997019767761, 0.9999998211860657
obj.rotation_euler = 1.4234873056411743, -0.025275448337197304, 2.0292327404022217
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1032 + frame)
obj = cameras['Camera']
obj.location = -6.989177703857422, 2.0060794353485107, 1.565356731414795
obj.scale = 1.0, 0.9999997615814209, 0.9999998807907104
obj.rotation_euler = 1.424056887626648, -0.026830721646547318, 2.03010630607605
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1033 + frame)
obj = cameras['Camera']
obj.location = -6.990516662597656, 2.0058419704437256, 1.566204309463501
obj.scale = 1.0000003576278687, 1.0, 1.0
obj.rotation_euler = 1.4249123334884644, -0.0283732358366251, 2.0307281017303467
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1034 + frame)
obj = cameras['Camera']
obj.location = -6.991629600524902, 2.0058188438415527, 1.5667951107025146
obj.scale = 1.0, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4262244701385498, -0.02937140129506588, 2.0307929515838623
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1035 + frame)
obj = cameras['Camera']
obj.location = -6.9921722412109375, 2.0058789253234863, 1.5674097537994385
obj.scale = 1.0, 0.9999999403953552, 0.9999999403953552
obj.rotation_euler = 1.42792546749115, -0.030763214454054832, 2.030834197998047
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1036 + frame)
obj = cameras['Camera']
obj.location = -6.992297172546387, 2.0058109760284424, 1.5679690837860107
obj.scale = 0.9999998807907104, 0.9999998211860657, 1.0
obj.rotation_euler = 1.4298185110092163, -0.03171461448073387, 2.0304222106933594
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1037 + frame)
obj = cameras['Camera']
obj.location = -6.992016315460205, 2.00628399848938, 1.5684934854507446
obj.scale = 1.0, 0.9999998807907104, 1.0
obj.rotation_euler = 1.4320982694625854, -0.03198393061757088, 2.0306923389434814
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1038 + frame)
obj = cameras['Camera']
obj.location = -6.990972995758057, 2.007413387298584, 1.5688313245773315
obj.scale = 1.0, 0.9999998807907104, 1.0
obj.rotation_euler = 1.4343479871749878, -0.031622156500816345, 2.030998468399048
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1039 + frame)
obj = cameras['Camera']
obj.location = -6.989860534667969, 2.0080809593200684, 1.569663166999817
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999999403953552
obj.rotation_euler = 1.4374642372131348, -0.030594531446695328, 2.030970335006714
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1040 + frame)
obj = cameras['Camera']
obj.location = -6.988260746002197, 2.0097367763519287, 1.5698299407958984
obj.scale = 0.9999999403953552, 0.9999998211860657, 1.0
obj.rotation_euler = 1.4401978254318237, -0.029735160991549492, 2.0309269428253174
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1041 + frame)
obj = cameras['Camera']
obj.location = -6.986772537231445, 2.011195182800293, 1.5705952644348145
obj.scale = 0.9999998211860657, 0.9999996423721313, 0.9999998807907104
obj.rotation_euler = 1.4435433149337769, -0.027415389195084572, 2.030510902404785
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1042 + frame)
obj = cameras['Camera']
obj.location = -6.984299659729004, 2.012324810028076, 1.5704395771026611
obj.scale = 0.9999998807907104, 0.9999997019767761, 0.9999998211860657
obj.rotation_euler = 1.4464327096939087, -0.025477981194853783, 2.0299909114837646
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1043 + frame)
obj = cameras['Camera']
obj.location = -6.982973098754883, 2.0137898921966553, 1.5704981088638306
obj.scale = 1.0, 0.9999998807907104, 1.0
obj.rotation_euler = 1.449586272239685, -0.022952882573008537, 2.0302960872650146
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1044 + frame)
obj = cameras['Camera']
obj.location = -6.981461524963379, 2.0152056217193604, 1.5703928470611572
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.0
obj.rotation_euler = 1.4525057077407837, -0.019635094329714775, 2.0302023887634277
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1045 + frame)
obj = cameras['Camera']
obj.location = -6.98001766204834, 2.016920804977417, 1.569806694984436
obj.scale = 0.9999997615814209, 0.9999997019767761, 0.9999998211860657
obj.rotation_euler = 1.4549612998962402, -0.016742480918765068, 2.029698133468628
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1046 + frame)
obj = cameras['Camera']
obj.location = -6.978926181793213, 2.0184617042541504, 1.5683780908584595
obj.scale = 0.9999998807907104, 0.9999998211860657, 0.9999998211860657
obj.rotation_euler = 1.4573191404342651, -0.013427821919322014, 2.0285592079162598
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1047 + frame)
obj = cameras['Camera']
obj.location = -6.9778642654418945, 2.0202627182006836, 1.5673027038574219
obj.scale = 0.9999998211860657, 0.9999997615814209, 0.9999999403953552
obj.rotation_euler = 1.4592900276184082, -0.009942406788468361, 2.0270371437072754
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1048 + frame)
obj = cameras['Camera']
obj.location = -6.976642608642578, 2.0218820571899414, 1.5665993690490723
obj.scale = 0.9999999403953552, 0.9999998211860657, 0.9999998807907104
obj.rotation_euler = 1.4607722759246826, -0.008571350947022438, 2.0249948501586914
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1049 + frame)
obj = cameras['Camera']
obj.location = -6.976275444030762, 2.024160385131836, 1.565500259399414
obj.scale = 1.0, 0.9999998211860657, 1.0
obj.rotation_euler = 1.46195387840271, -0.008085799403488636, 2.0234763622283936
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# new frame
scene.frame_set(1050 + frame)
obj = cameras['Camera']
obj.location = -6.975352764129639, 2.0259761810302734, 1.5648577213287354
obj.scale = 0.9999997019767761, 0.9999996423721313, 0.9999998211860657
obj.rotation_euler = 1.462754487991333, -0.005970153026282787, 2.0212936401367188
obj.keyframe_insert("location")
obj.keyframe_insert("scale")
obj.keyframe_insert("rotation_euler")
data = obj.data
data.lens = 50.0
data.keyframe_insert("lens")

# markers
