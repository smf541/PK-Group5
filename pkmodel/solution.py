#
# Solution class
# Want users to be able to add multiple pairs of models and protocols
# want these to then have ODE solutions that are accessible via plots
# or as array

import numpy
import matplotlib.pyplot
from protocol import Protocol

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self):
        self.models = []
        self.protocols = []

    def add(self, model, protocol):  # perhaps allow this to pass a list?
        self.models.append(model)
        self.protocols.append(protocol)

    @property
    def list(self):
        """
        Lists the (model, protocol) combinations in the solution object
        """
        out = []
        # we can assume protocols same length as methods, as user only adds
        # them as a pair 
        for i in range(0, len(self.models)):  
            out.append((self.models[i], self.protocols[i]))
        return out 

    def remove(self, model, protocol):
        """Removes a model and protocol pair from the solution"""
        self.models.remove(model)
        self.protocols.remove(protocol)

    # Below two functions don't strictly need to be a class method, 
    # could have them as external functions and call them in, but that's
    # not as clean 

    def get_model_variables(self, model):
        """
        Takes a Model object and returns the variables in it as a
        1-D array 

        Parameters:
        ----------

        model: Model object

        returns: 1-D numpy array
        """
        

    def ode_system(self, model, protocol, t=0):
        """
        Takes as input a Model object and a Protocol object, 
        then returns the system of ODEs for this pair 

        Parameters:
        ----------

        model: Model object
        protocol: Protocol object

        returns: 1-D list of ordinary differential equations 
        """
        dose_fn = protocol.dose()
        # From what I remember of how odeint works, it's enough to pass it
        # a list of expressions, which calculate a value
        # So, try and express the system as such:

        # First unpack the variables, which should be a list of 

    def solution(self, model, protocol, time):
        """
        Calcuates the ODE solution for a specific model and protocol

        Parameters:
        ----------

        model: Model object
        protocol: Protocol object
        time: numpy 1-D array, gives the time array for passing to odeint

        returns: numpy ndarray, containing the numerical solutions to the system
        """
        with numpy as np:
            y0 = np.zeros((len(model)+1), dtype=float)
            # set the first element of the initial conditions array y0
            # to be the initial value of the 0th compartment, which is the 
            # compartment in which we get drug delivery (central for intravenous)
            y0[0] = protocol.starting_dose
        # Now we need to define the model in terms of ODEs
        system = self.ode_system(model, protocol)
        numerical_solution = scipy.integrate.odeint(func=system, y0=y0, t=time)

        if model.delivery_mode == 'intravenous':
            return numerical_solution[0]
        elif model.delivery_mode == 'subcutaneous':
            return numerical_solution[1]
        else:
            raise ValueError("Model delivery mode incorrectly defined. Options are: 'intravenous', or 'subcutaneous'.")


    # IMPORTANT - 
    # If intravenous, we are interested in plotting the variable in the 0th 
    # position of the array defined above. If subcutaneous, we are interested
    # in the variable at the 1th position.

    def visualise(self, inputs=self.list, layout='overlay', time_res=100):
        """
        Plots the ODE solutions of the model.
        
        Parameters:
        ----------
        
        inputs: list of tuples, the (model, protocol) pairs in the solution
        that you wish to visualise. Defaults to all such pairs in the solution

        layout: string, either 'overlay' or 'side_by_side'. Specifies if the 
        solutions are show overlain on one plot, or as independent plots
        side by side. Defaults to 'overlay'. 

        time_res: int, the number of elements in the time and ODE solution
        array used for plotting.
        
        """
        for input in inputs:
            model = input[0]  # specify where the model object is 
            protocol = input[1] # specify where the protocol object is 
            time = numpy.linspace(0, protocol.time_span, time_res) 
            ODE_solution = self.solution(model, protocol, time_res) # make this a function of time array
            matplotlib.pyplot.plot(time, ODE_solution)
        matplotlib.pyplot.show()

model1 = 1
model2 = 2
prot1 = Protocol()
prot2 = Protocol()

sol = Solution()
sol.add(model1, prot1)
sol.add(model2, prot2)