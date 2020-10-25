class Model:
    """The Model class holds the pharmacokinetic parameters chosen for the model.
    The delivery method can be specified, including options for
    intravenous or subcutaneous dosing.
    The Ka property is an absorption rate relevant for non-intravenous dosing.
    """
    def __init__(self, delivery_mode: str, V_c=1.0, CL=1.0, Ka=1.0):
        """Initialises a model with chosen pharmacokinetic parameters and name.
        Defaults to central compartment with V_c = 1.0 mL, CL = 1.0 mL/h, and
        Ka = 1.0 /h with no additional peripheral compartments.
        Args:
            delivery_mode (str): the chosen delivery mode for dosing. Supported
                options include 'intravenous' ('intravenous', 'iv', or 'IV')
                or 'subcutaneous' ('subcutaneous', 'subq', 'sc', or 'SC')
            V_c (float): the volume of the central compartment [mL]
            CL (float): the clearance/elimination rate from the central
                compartment [mL/h]
            Ka (float): the absorption rate,
                for example for subcutaneous dosing [/h]
        """
        # Verify argument types
        if delivery_mode not in ['intravenous', 'iv', 'IV',
                                 'subcutaneous', 'subq', 'sc', 'SC']:
            raise ValueError('Given delivery_mode invalid;'
                             'try "intravenous" or "subcutaneous"')
        if type(V_c) not in [int, float]:
            raise TypeError('V_c must be int or float')
        if type(CL) not in [int, float]:
            raise TypeError('CL must be int or float')
        if type(Ka) not in [int, float]:
            raise TypeError('Ka must be int or float')
        if delivery_mode in ['intravenous', 'iv', 'IV']:
            self.__delivery_mode = 'iv'
        if delivery_mode in ['subcutaneous', 'subq', 'sc', 'SC']:
            self.__delivery_mode = 'sc'
        self.__V_c = V_c
        self.__CL = CL
        self.__Ka = Ka
        """V_p (list of floats): Initialises empty string to hold V_p
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
        return self.name

    def __len__(self) -> int:
        """Returns the number of compartments, including added peripheral compartments.
        Minimum value = 1 for central compartment.
        """
        if len(self.__V_p) != len(self.__Q_p):
            raise Exception('Unequal # of compartment parameters (V_p, Q_p')
        return len(self.__V_p) + 1

    @property
    def name(self) -> str:
        """str: name is a property constructed from the model parameters.
        This protects data integrity by tying results to an immutable label.
        """
        self.__Name = ("Model-" + self.__delivery_mode + "-V_c="
                       + str(self.__V_c) + "-CL=" + str(self.__CL)
                       + "-Ka=" + str(self.__Ka) + "-"
                       + str(len(self.__V_p)) + "compartments")
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

    @property
    def delivery_mode(self) -> str:
        """str: returns either 'iv' or 'sc' for the delivery_mode
        """
        return self.__delivery_mode

    def add_compartment(self, V_p_new: float, Q_p_new: float):
        """Receives V_p and Q_p for the desired additional compartment and
        adds these to the V_p and Q_p class attributes.

        Args:
            V_p_new (float): the volume of the compartment to be added [mL]
            Q_p_new (float): the transition rate between the central
                compartment and the peripheral compartment being added [mL/h]
        """
        # Verify that V_p_new and Q_p_new inputs are numbers
        if type(Q_p_new) not in [int, float]:
            raise TypeError('Q_p_new must be int or float')
        if type(V_p_new) not in [int, float]:
            raise TypeError('V_p_new must be int or float')
        self.__V_p.append(V_p_new)
        self.__Q_p.append(Q_p_new)

    def list_compartments(self):
        """Returns list of lists with a list of [V_p, Q_p] for each compartment.
        """
        list_compartments = []
        for i in range(len(self.__V_p)):
            list_compartments.append([self.__V_p[i], self.__Q_p[i]])
        return list_compartments

    def remove_compartment(self, index: int):
        """Removes peripheral compartment at given index. Index refers to the
        compartment's position given in model.list_compartments().

        Args:
        index (int): the index of the compartment to be removed,
            referring to V_p[index] and Q_p[index]; non-negative
        """
        # Verify valid index choice
        if index < 0:
            raise ValueError('Index must be a non-negative integer')
        if index not in range(len(V_p)):
            raise ValueError('Invalid index for V_p')
        if index not in range(len(Q_p)):
            raise ValueError('Invalid index for Q_p')
        del V_p[index]
        del Q_p[index]
