# Protocol class
# With this we want the user to be able to:
# - Specify the type of delivery of the drug (intravenous/subcutaneous)
# - Specify the dynamics of the delivery
# - Call the type as a property
# - alter the dose function

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    initial_dose: float, the initial dose of the drug
    into the system

    delivery_mode: string, either 'intravenous' or 'subcutaneous'

    time_span: int, maximum time of the simulation

    """
    def __init__(self, initial_dose=1, delivery_mode=1, time_span=1):
        self.initial_dose = initial_dose
        self.delivery_mode = delivery_mode
        self.time_span = time_span

    @property
    def type(self):
        return self.delivery_mode

    # Want to be able to access the dose
    @property
    def starting_dose(self):
        # naming this 'initial_dose' creates an error on line 25
        return self.initial_dose

    @property
    def time(self):
        return self.time_span

    # now want a method where the user can access the dose(t)
    # function, which describes the rate of input of the drug over time

    def dose(self, time=None, func=None):
        # we assume the default case is the instantaneous injection,
        # and so time doesn't need to be specified by the user, thus
        # by default we set it to None
        """
        Function describing the rate of drug input over time

        Parameters
        ----------
        time: float, time variable for the simulation, set to None by default
        func: function, function describing the rate of drug input over time,
        set to None by default

        Returns
        -------
        dose(y, t): function
        """

        if func is not None:
            # we need a way to test that func is dependent on time and y
            return func
        else:
            return lambda y, t: 0
            # default case is the instantaneous addition, in which
            # case, there is no further addition, and rate is 0
