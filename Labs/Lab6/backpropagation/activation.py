import math


def unipolar_sigmoidal_activation_fxn(net):
    return 1 / (1 + (math.e ** (-net)))
