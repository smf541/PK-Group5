""" Draft interface for the pkmodel solver (alpha! subject to change)
"""

import pkmodel as pk


model1 = pk.model( 'name', 'V_c'=1.0, 'CL'=1.0, 'X'=1.0, 'Ka_q0'=1.0 )
model1.name
model1.add_compartment( Q_p, V_p )
model1.list()
model1.remove( idx )
model1.v_c()
...

model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

proto1 = pk.protocol( 'type', dose, t_eval, y0 )
proto1.type
proto1.dose()
...

solution = pk.solution()
solution.add( model1, proto1 )
solution.list()
solution.remove( idx )
solution.visualise( plt_params ) # maybe
