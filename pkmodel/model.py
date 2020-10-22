#
# Model class
# model object inputs: V_c=1.0, CL=1.0, Ka=1.0

# [x]implement name method
# []implement add_compartment( Q_p, V_p) function
# []implement list() function: list compartments and associated parameters
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
        self.V_c = V_c
        self.CL = CL
        self.Ka = Ka
        """V_p (list of floats): Initialises epty string to hold V_p
           for all additional compartments, the volume of the each additional
           compartment [mL]."""
        self.V_p = []
        """Q_p (list of floats): Initialises empty string to hold Q_p
            for all additional compartments, the transition rate between
            the central compartment and each peripheral compartment [mL/h]."""
        self.Q_p = []

    @property
    def name(self) -> str:
        """str: name is a property constructed from the model parameters.
        This protects data integrity by tying results to an immutable label.
        """
        self.__Name = "Model-V_c=" + self.V_c + "-CL=" + self.CL + "-Ka=" + self.Ka
        return self.__Name

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
        self.V_p.append(V_p_new)
        self.Q_p.append(Q_p_new)
