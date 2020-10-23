class Protocol:
    """The Protocol class holds the pharmacokinetic parameters related to
    the dose and time span of the dose. It contains a method to return a 
    dose function for the chosen parameters.
    """
    def __init__(self, initial_dose: float = 1.0, time_span: float = 1.0):
        """Initialises a protocol object with chosen initial dose and time span.
        Delivery method is held in the model object (see: Model class documentation).

        Args:
            initial_dose (float): the chosen initial dose, default is 1.0 [ng]
            time_span (float): the time span, the maximum time of the simulation [hours]
        """
        if type(initial_dose) not in [int, float]:
            raise TypeError('initial_dose must be int or float')
        if type(time_span) not in [int, float]:
            raise TypeError('time_span must be int or float')
        self.__Initial_dose = initial_dose
        self.__Time_span = time_span

    @property
    def name(self) -> str:
        """The name is a property constructed from the protocol parameters.
        This protects data integrity by tying results to an immutable label.

        Args:
            None
        Returns:
            name (string)
        """
        self.__Name = "Protocol-initial_dose=" + str(self.__Initial_dose) + "-time_span=" + str(self.__Time_span)  # noqa: E501
        # inline comment to flake8 to ignore line length needed for name string
        return self.__Name

    def __str__(self):
        """Returns:
            the name of the model (string)
        """
        return self.name

    @property
    def initial_dose(self) -> float:
        """Access the initial dose.
            Args:
                None
            Returns:
                the initial dose (float)
        """
        return self.__Initial_dose

    @property
    def time_span(self) -> float:
        """Access the time span.
            Args:
                None
            Returns:
                time span (float) [hours]
        """
        return self.__Time_span

    # now want a method where the user can access the dose(t)
    # function, which describes the rate of input of the drug over time

    def dose(self, time=None, func=None):
        # we assume the default case is the instantaneous injection,
        # and so time doesn't need to be specified by the user, thus
        # by default we set it to None
        """
        Method to access the dose(t) function, which describes the rate
        of input of the drug over time. We assume the default case is the
        instantaneous intravenous injection and so time doesn't need to be
        specified by the user; thus by default we set it to None.

        Args:
            time (float): time variable for the simulation, defaults to None [hours]
            func (function): function describing the rate of drug input over time,
                defaults to None
        Returns:
            dose(y, t) (function)
        """

        if func is not None:  # Tests that func is dependent on time and y
            func(1, 2)  # Test that func accepts two arguments
            return func
        else:
            return lambda y, t: 0
            # Default case is the instantaneous addition, in which
            # case, there is no further addition, and rate is 0.
