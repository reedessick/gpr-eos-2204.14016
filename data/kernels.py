"""a module to house basic logic for GP kernels
"""
__author__ = "Reed Essick (reed.essick@gmail.com)"

#-------------------------------------------------

import numpy as np

from scipy.special import (gamma, kn)

from configparser import ConfigParser

#-------------------------------------------------

class Kernel(object):
    """an object that represents a covariance kernel
    """

    def __init__(self):
        pass # child classes should overwrite this

    @staticmethod
    def _absissa2diff(x, y):
        return np.outer(x, np.ones_like(y)) - np.outer(np.ones_like(x), y)

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
    cov(x, y; sigma) = sigma**2 * delta(x-y)
    """

    def __init__(self, sigma=1.0):
        self._sigma = 1.0

    def cov(self, x, y):
        diff = self._absissa2diff(x, y)
        return np.where(diff==0, sigma**2, 0.0)

#------------------------

class SquaredExponential(Kernel):
    """squared exponential kernel
    cov(x, y; sigma, length) = sigma**2 * np.exp(-0.5*(x-y)**2/length**2)
    """

    def __init__(self, sigma=1.0, length=1.0):
        self._sigma = sigma
        self._length = length

    def cov(self, x, y):
        diff = self._absissa2diff(x, y)
        return self._sigma**2 * np.exp(-0.5*diff**2/self._length**2)

#------------------------

class Matern(Kernel):
    """matern kernel
    cov(x, y; sigma, length, order) = sigma**2 * (2**(1-order)/Gamma(order)) * (sqrt(2*order)*diff/length)**order * K(sqrt(2*order)*diff/length; order)
where
    K(.;order) is the modified Bessel function of the second kind
    Gamma(.) is the Gamma function
    """

    def __init__(self, sigma=1.0, length=1.0, order=0.0):
        self._sigma = sigma
        self._length = length
        self._order = order

    def cov(self, x, y):
        diff = (2*self._order)**0.5 * self._absissa2diff(x, y) / self._length
        return self._sigma**2 * (2**(1-self._order)/gamma(self._order)) * (diff)**self._order * kn(self._order, diff)

#------------------------

class Polynomial(Kernel):
    """polynomial kernel
    cov(x, y; sigma, order) = sigma** outer(x, y)**order
    """

    def __init__(self, sigma=1.0, order=1.0):
        self._sigma = sigma
        self._order = order

    def cov(self, x, y):
        return self._sigma**2 * np.outer(x, y)**self._order

#-------------------------------------------------

def parse(path, verbose=False):
    if verbose:
        print('loading covariance kernel from : '+path)
    config = ConfigParser()
    config.read(path)

    kernels = []
    for section in config.get_sections():
        raise NotImplementedError

    return SummedKernel(kernels=kernels)
