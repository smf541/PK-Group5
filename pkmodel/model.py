#
# Model class
# model object inputs: V_c=1.0, CL=1.0, Ka=1.0

# [x]implement name method
# [x]implement add_compartment( Q_p, V_p) function
# [x]implement list_compartments() function: list compartments and their params
# [x]implement __str__ method
# [x] implement __len__ method
# []implement remove( idx ) function
# []implement getters and setters v_c() function
#
#  Args:
#           param1 (str): Description of `param1`.
#           param2 (:obj:`int`, optional): Description of `param2`. Multiple
#              lines are supported.
#           param3 (:obj:`list` of :obj:`str`): Description of `param3`.

class Model:
    """The Model class holds the pharmacokinetic parameters chosen for the model.
    These are properties of the compartments unrelated to the dose protocol.
    The Ka property is an absorption rate relevant for non-intravenous dosing.
    """
    def __init__(self, V_c=1.0, CL=1.0, Ka=1.0):
        """Initialises a model with chosen pharmacokinetic parameters and name.
        Defaults to central compartment with V_c = 1.0 mL, CL = 1.0 mL/h, and
        Ka = 1.0 /h with no additional peripheral compartments.
        Args:
            V_c (float): the volume of the central compartment [mL]
            CL (float): the clearance/elimination rate from the central
                compartment [mL/h]
            Ka (float): the absorption rate,
                for example for subcutaneous dosing [/h]
        """
        # Verify that arguments are numbers
        if V_c != V_c:  # will return True if NaN
            raise TypeError('V_c is NaN, requires int or float')
        if CL != CL:  # will return True if NaN
            raise TypeError('CL is NaN, requires int or float')
        if Ka != Ka:  # will return True if NaN
            raise TypeError('Ka is NaN, requires int or float')
        if type(V_c) not in [int, float]:
            raise TypeError('V_c must be int or float')
        if type(CL) not in [int, float]:
            raise TypeError('CL must be int or float')
        if type(Ka) not in [int, float]:
            raise TypeError('Ka must be int or float')
        self.__V_c = V_c
        self.__CL = CL
        self.__Ka = Ka
        """V_p (list of floats): Initialises epty string to hold V_p
           for all additional compartments, the volume of the each additional
           compartment [mL]."""
        self.__V_p = []
        """Q_p (list of floats): Initialises empty string to hold Q_p
            for all additional compartments, the transition rate between
            the central compartment and each peripheral compartment [mL/h]."""
        self.__Q_p = []

    def __str__(self):
        """Returns the name of the model as a string.
        """
        return self.__Name

    def __len__(self) -> int:
        """Returns the number of compartments, including added peripheral compartments.
        Minimum value = 1 for central compartment.
        """
        if len(V_p) != len(Q_p):
            raise Exception('Unequal # of compartment parameters (V_p, Q_p')
        return len(V_p) + 1

    @property
    def name(self) -> str:
        """str: name is a property constructed from the model parameters.
        This protects data integrity by tying results to an immutable label.
        """
        self.__Name = "Model-V_c=" + str(self.__V_c) + "-CL=" + str(self.__CL) + "-Ka=" + str(self.__Ka) + "-" + str(len(self.__V_p)) + "compartments"
        return self.__Name

    @property
    def v_c(self) -> float:
        """float: the value of V_c for this model
        """
        return self.__V_c

    @property
    def cl(self) -> float:
        """float: the value of CL for this model
        """
        return self.__CL

    @property
    def ka(self) -> float:
        """float: the value of Ka for this model
        """
        return self.__Ka

    def add_compartment(self, V_p_new: float, Q_p_new: float):
        """Receives V_p and Q_p for the desired additional compartment and
        adds these to the V_p and Q_p class attributes.

        Args:
            V_p_new (float): the volume of the compartment to be added [mL]
            Q_p_new (float): the transition rate between the central
                compartment and the peripheral compartment being added [mL/h]
        """
        # Verify that V_p_new and Q_p_new inputs are numbers
        if V_p_new != V_p_new:  # will return True if NaN
            raise TypeError('V_p_new is NaN, requires int or float')
        if Q_p_new != Q_p_new:  # will return True if NaN
            raise TypeError('Q_p_new is NaN, requires int or float')
        if type(Q_p_new) not in [int, float]:
            raise TypeError('Q_p_new must be int or float')
        if type(V_p_new) not in [int, float]:
            raise TypeError('Q_p_new must be int or float')
        self.__V_p.append(V_p_new)
        self.__Q_p.append(Q_p_new)

    def list_compartments(self):
        """Returns list of lists with a list of [V_p, Q_p] for each compartment.
        """
        list_compartments = []
        for i in range(len(self.__V_p)):
            list_compartments.append([self.__V_p[i], self.__Q_p[i]])
        return list_compartments

