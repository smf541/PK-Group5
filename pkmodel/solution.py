#
# Solution class
# Want users to be able to add multiple pairs of models and protocols
# want these to then have ODE solutions that are accessible via plots
# or as array

import numpy
import matplotlib.pyplot
import scipy
from protocol import Protocol
from model import Model


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

    def ode_system(self, q, t, model, protocol):
        """
        Takes as input an array-like list of variables q, a float time t, 
        a Model object and a Protocol object, 
        then returns the system of ODEs for this pair 

        Parameters:
        ----------
        q: array-like object of variables q
        t: float, representing time 
        model: Model object
        protocol: Protocol object

        returns: 1-D list of functions of ordinary differential equations 
        """
        dose_fn = protocol.dose()

        if model.delivery_mode == 'iv':
            num_variables = len(model.list_compartments())
        elif model.delivery_mode == 'sc':
            num_variables = len(model.list_compartments()) + 1
        
        # in the iv case, q0=qc
        # in the sc case, q0=input compartment, and q1=qc

        # get the global model parameters
        v_c = model.v_c
        cl = model.cl 
        ka = model.ka
        # get the parameters for each compartment 
        # this is a list which 
        compartment_parameters = model.list_compartments()
        # now extract the ones we need
        q_p = [qp for (v, qp) in compartment_parameters]
        v_p = [vp for (vp, q) in compartment_parameters]

        # create a list of transitions
        transitions = [q_p[i] * ((q[0] / v_c) - (q[i] / v_p[i])) for i in range(1, num_variables)]

        if model.delivery_mode == 'iv':
            central = dose_fn(t) - (q[0] / v_c) * cl  # need to pass this dose_fn t as we need it in float type
            # now update central to include transitions
            for transition in transitions:
                central += transition
            return [central].append(transitions)

        elif model.delivery_mode == 'sc':
            input = dose_fn(t) - ka * q[0]
            central = ka * q[0] - (q[1] / v_c) * cl
            for transition in transitions:
                central += transitions
            return [input, central].append(transitions)

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
        if model.delivery_mode == 'iv':
            num_variables = len(model.list_compartments()) + 1
        elif model.delivery_mode == 'sc':
            num_variables = len(model.list_compartments()) + 2

        y0 = numpy.zeros((num_variables), dtype=float)
        # set the first element of the initial conditions array y0
        # to be the initial value of the 0th compartment, which is the 
        # compartment in which we get drug delivery (central for intravenous)
        if model.delivery_mode == 'iv':
            y0[0] = protocol.initial_dose
        elif model.delivery_mode == 'sc':
            y0[1] = protocol.initial_dose
        # Now we need to define the model in terms of ODEs
        # system = self.ode_system(model=model, protocol=protocol)
        numerical_solution = scipy.integrate.odeint(func=self.ode_system(model=model, protocol=protocol), y0=y0, t=time)


        # TODO: update this to the new model modes
        if model.delivery_mode == 'iv':
            return numerical_solution[0]
        elif model.delivery_mode == 'sc':
            return numerical_solution[1]
        else:
            raise ValueError("Model delivery mode incorrectly defined. Options are: 'intravenous', or 'subcutaneous'.")

    # IMPORTANT - 
    # If intravenous, we are interested in plotting the variable in the 0th 
    # position of the array defined above. If subcutaneous, we are interested
    # in the variable at the 1th position.

    def visualise(self, inputs, layout='overlay', time_res=100):
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
            protocol = input[1]  # specify where the protocol object is 
            time = numpy.linspace(0, protocol.time_span, time_res) 
            ODE_solution = self.solution(model, protocol, time_res) # make this a function of time array
            matplotlib.pyplot.plot(time, ODE_solution)
        matplotlib.pyplot.show()


model1 = Model('iv')
model2 = Model('sc')
prot1 = Protocol()
prot2 = Protocol()

sol = Solution()
sol.add(model1, prot1)
sol.add(model2, prot2)

time = numpy.linspace(0, 10, 100)
output1 = sol.solution(model1, prot1, time)
output2 = sol.solution(model2, prot2, time)
output3 = sol.solution(model1, prot2, time)
