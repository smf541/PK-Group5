""" Draft interface for the pkmodel solver (alpha! subject to change)
"""

import pkmodel as pk


model1 = pk.model('delivery_mode', V_c=1.0, CL=1.0, Ka=1.0)
model1.name
model1.add_compartment(Q_p_new=1.0, V_p_new=1.0)
model1.list_compartments()
model1.v_c
model1.cl
model1.ka
model1.delivery_mode
...

model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

proto1 = pk.protocol(proto_type, dose, t_eval, y0)
proto1.proto_type
proto1.dose()
...

solution = pk.solution()
solution.add(model1, proto1)
solution.list()
solution.remove(idx)
solution.visualise(plt_params)  # maybe

