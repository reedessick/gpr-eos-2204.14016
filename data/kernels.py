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

    def __init__(self):
        pass # child classes should overwrite this

    def cov(self, x, y):
        return np.zeros((len(x), len(y)), dtype=float)

    def __add__(self, other):
        return SummedKernel([self, other])

#-------------------------------------------------

class SummedKernel(Kernel):
    """an object representing the sum of kernels. Supported to simplify user interface
    """

    def __init__(self, kernels):
        self._kernels = [_ for _ in kernels]

    def cov(self, x, y):
        ans = 0
        for kernel in self._kernels:
            ans += kernel.cov(x, y)
        return ans

#-------------------------------------------------

class WhiteNoise(Kernel):
    """white noise kernel
    cov(x, y) = sigma**2 * delta(x-y)
    """

    def __init__(self, sigma=1.0):
        self._sigma = 1.0

    def cov(self, x, y):
        ans = np.zeros((len(x), len(y)), dtype=float)
        raise NotImplementedError('figure out when x==y and set cov to sigma**2')

#------------------------

class SquaredExponential(Kernel):
    """squared exponential kernel
    cov(x, y) = sigma**2 * np.exp(-0.5*(x-y)**2/length**2)
    """

    def __init__(self, sigma=1.0, length=1.0):
        self._sigma = sigma
        self._length = length

    def cov(self, x, y):
        raise NotImplementedError

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
