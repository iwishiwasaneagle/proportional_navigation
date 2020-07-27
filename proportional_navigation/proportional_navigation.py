import numpy as np
from .models import Vehicle
from .exceptions import (InvalidProportionalGainError,OutOfBoundsRangeError)


class PNOptions:
    def __init__(self, return_R=False,return_Rdot=False,return_Vc=False,return_lambda=False,return_lambdad=False):
        self.return_R=return_R
        self.return_Rdot=return_Rdot
        self.return_Vc=return_Vc
        self.return_lambda=return_lambda
        self.return_lambdad=return_lambdad

class PN:
    def __init__(self, pursuer, target, N=3, options=None):
        if not isinstance(target, Vehicle):
            raise TypeError(f"Pursuer is instance of {type(pursuer)} and not proportional_navigation.Vehicle")
        if not isinstance(pursuer, Vehicle):
            raise TypeError(f"Target is instance of {type(pursuer)} and not proportional_navigation.Vehicle")

        if not isinstance(N, float):
            if not isinstance(N, int):
                raise TypeError(f"N is type {type(N)} and not float or int")
        if N<=0:
            raise InvalidProportionalGainError(N)
        
        if not isinstance(options, PNOptions) and options is not None:
            raise TypeError(f"options is type {type(options)} and not proportional_navigation.PNOptions")
        
        self.target = target
        self.pursuer = pursuer
        self.N = N
        self.options = options
        

    def calculate(self):          
        R = np.sqrt(np.square(self.target.x-self.pursuer.x) + np.square(self.target.y-self.pursuer.y))
        if R<=0:
            raise OutOfBoundsRangeError(R)
        Rdot = ((self.target.x-self.pursuer.x)*(self.target.xd-self.pursuer.xd)+(self.target.y-self.pursuer.y)*(self.target.yd-self.pursuer.yd))/R
        Vc = -Rdot

        cp = np.cos(np.deg2rad(self.pursuer.psi))
        sp = np.sin(np.deg2rad(self.pursuer.psi))
        Cwp = np.array([[cp,sp],[-sp,cp]])

        xr = np.array([[self.target.x-self.pursuer.x],[self.target.y-self.pursuer.yd]])
        xrd = np.array([[self.target.xd-self.pursuer.xd],[self.target.yd-self.pursuer.yd]])

        xrp = [
            [Cwp[0][0]*xr[0][0]+Cwp[0][1]*xr[1][0]],
            [Cwp[1][0]*xr[0][0]+Cwp[1][1]*xr[1][0]]
            ]
        xrdp = [
            Cwp[0][0]*xrd[0][0]+Cwp[0][1]*xrd[1][0],
            Cwp[1][0]*xrd[0][0]+Cwp[1][1]*xrd[1][0]
            ]

        lam = np.arctan2(xrp[1][0],xrp[0][0])
        lamd = (xrdp[1]*xrp[0][0]-xrdp[0]*xrp[1][0])/(np.square(xrp[0][0])/np.square(np.cos(lam)))

        nL = self.N*lamd*Vc

        if self.options is None:
            return nL

        ret = {}
        if self.options.return_R:
            ret["R"] = R
        if self.options.return_Rdot:
            ret["Rdot"] = Rdot
        if self.options.return_Vc:
            ret["Vc"] = Vc
        if self.options.return_lambdad:
            ret["lambdad"] = lamd
        if self.options.return_lambda:
            ret["lambda"] = lam
        ret["nL"] = nL
        return ret
        