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

    def solution(self, model, protocol, time_res=100):
        # y0 = model.initial_value.append(protocol.starting_dose)
        if model == 1:
            return [i**3 for i in range(0, time_res)]
        else:
            return [i**2 for i in range(0, time_res)]

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