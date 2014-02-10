
""" Textbook of Computable General Equilibrium Modeling Page 72(93) 
    output 81 (102)
"""
from parameter import Parameter
from calibration import Calibration
from simulation import Simulation


table = [
            ['BRD', 'MLK'],
            ['.....'],
            ['.....'],
            ['.....'],
            ['.....'],
            ['.....'],
            ['.....']
        ]



parameter = Parameter(
	index=['BRD', 'MLK', 'CAP', 'LAB', 'HH', 'GOV'],
	industries=['BRD', 'MLK'],
	factors=['CAP', 'LAB'],
	consumers=['HH'],  #'GOV'
)
parameter.sam['HH']['BRD'] = 15
parameter.sam['HH']['MLK'] = 35
parameter.sam['BRD']['CAP'] = 5
parameter.sam['MLK']['CAP'] = 20
parameter.sam['BRD']['LAB'] = 10
parameter.sam['MLK']['LAB'] = 15
parameter.sam['CAP']['HH'] = 25
parameter.sam['LAB']['HH'] = 25


print parameter

doc = {
    'X0': "X0 household consumption of the i-th good ",
    'G0': "G0 government consumption of i-th good or k-th factor ",
    'F0': "F0 the h-th factor input by the j-th firm ",
    'Z0': "Z0 output of the j-th good",
    'alpha': "alpha share parameter in utility function"
    # ...
}
print doc

calibration = Calibration(parameter)
print(calibration)
simulation = Simulation(calibration, parameter, debug=True)
print(simulation)