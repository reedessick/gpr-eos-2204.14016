"""a module to house basic logic for GP kernels
"""
__author__ = "Reed Essick (reed.essick@gmail.com)"

#-------------------------------------------------

def parse(path, verbose=False):
    raise NotImplementedError('return Kernel object')

#-------------------------------------------------

class Kernel(object):
    """an object that represents a covariance kernel
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def cov(self, x, y):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

#-------------------------------------------------

class SummedKernel(Kernel):
    """an object representing the sum of kernels. Supported to simplify user interface
    """

    def __init__(self, kernels):
        raise NotImplementedError

#-------------------------------------------------

class WhiteNoise(Kernel):
    """white noise kernel
    cov(x, y) = sigma**2 * delta(x-y)
    """

#------------------------

class SquaredExponential(Kernel):
    """squared exponential kernel
    cov(x, y) = sigma**2 * np.exp(-0.5*(x-y)**2/length**2)
    """

#------------------------

class Matern(Kernel):
    """matern kernel
    cov(x,y ) = ... LOOK THIS UP
    """

#------------------------

class Polynomial(Kernel):
    """polynomial kernel
    cov(x, y) = ... LOOK THIS UP
    """

'''
egroup.add_argument('--prior-standard-deviation', default=1.0, type=float,
    help='1D marginal standard deviation for auxiliary variable as part of extension to higher pressures')
egroup.add_argument('--prior-correlation-length', default=0.5, type=float,
    help='correlation length for auxiliary variable as part of extension to higher pressures')

### FIXME! add parameters for Matern kernel, also kernel type (squared exponential, matern, etc)
'''
