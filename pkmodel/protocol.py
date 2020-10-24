class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    initial_dose: float, the initial dose of the drug
    into the system

    delivery_mode: string, either 'intravenous' or 'subcutaneous'

    time_span: int, maximum time of the simulation

    """
    def __init__(self, initial_dose: float = 1.0, time_span: float = 1.0):
        if type(initial_dose) not in [int, float]:
            raise TypeError('initial_dose must be int or float')
        if type(time_span) not in [int, float]:
            raise TypeError('time_span must be int or float')
        self.__Initial_dose = initial_dose
        self.__Time_span = time_span
        # define the default dose function to be f(t,y)=0
        self.__Dose_func = lambda t, y: 0

    @property
    def name(self) -> str:
        """str: name is a property constructed from the protocol parameters.
        This protects data integrity by tying results to an immutable label.
        """
        self.__Name = "Protocol-initial_dose=" + str(self.__Initial_dose) + "-time_span=" + str(self.__Time_span)  # noqa: E501
        # inline comment to flake8 to ignore line length needed for name string
        return self.__Name

    def __str__(self):
        """Returns the name of the model as a string.
        """
        return self.name

    # Want to be able to access the dose
    @property
    def initial_dose(self) -> float:
        """float: The initial dose
        """
        return self.__Initial_dose

    @property
    def time_span(self) -> float:
        """float: The time span
        """
        return self.__Time_span

    # now want a method where the user can access the dose(t)
    # function, which describes the rate of input of the drug over time

    @property
    def dose(self):
        """
        Returns the function describing rate of drug input over time
        """
        return self.__Dose_func
        # default case is the instantaneous addition, in which
        # case, there is no further addition, and rate is 0

    def add_dose_function(self, func=None):
        """
        Allows the user to specify the function describing 
        rate of drug input over time

        Parameters
        ----------
        func: function, function describing the rate of drug input over time,
        set to None by default

        Returns
        -------
        dose(t, y): function
        """

        if func is not None:
            # we need a way to test that func is dependent on time and y
            func(1, 2)  # Test that it accepts two arguments
            self.__Dose_func = func
