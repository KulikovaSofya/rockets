import numpy as np


def snell(theta_inc, n1, n2):
    """
    Compute the reflaction angle using Snell's law
    See https://.....
    
    Parameters
    -----------
    theta_inc : float
        incident angle in radiants
        
    n1, n2 : float
        the reflactory index 
        
    Returns
    -----------
    theta : float 
        refration angle
        
    Example
    -----------
    A ray enters an air-water coundart at pi/4 angle, compute  exit angle
    >>> snell (np.pi/4, 1.00, 1.33)
            0.5605584137424605
    """
    return np.arcsin(n1/n2*np.sin(theta_inc))