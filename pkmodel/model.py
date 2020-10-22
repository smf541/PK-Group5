#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example parameter

    """
    def __init__(self, name, V_c: float=1.0, CL=1.0, Ka=1.0):
        if type(name) == None:
            raise TypeError
        self.__Name = name
        if type(V_c) not in [int, float]:
            raise TypeError
        if type(CL) not in [int, float]:
            raise TypeError
        if type(Ka) not in [int, float]:
            raise TypeError
        self.__V_c = V_c

    def add_compartment(self, Q_p:float, V_p:float):
        if type(Q_p) not in [int, float]:
            raise TypeError
        if type(V_p) not in [int, float]:
            raise TypeError
        return True

