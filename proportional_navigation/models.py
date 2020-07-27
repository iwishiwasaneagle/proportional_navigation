import numpy as np

class Vehicle(object):
    # We define xd and vd in extensions of this object based on reference frame. x and y will always be defined like this though.
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.xd = None
        self.yd = None


class HeadingVelocity(Vehicle):
    def __init__(self,psi,x,y,V):
        self._psi = psi # Heading angle relative to global ref frame (x = north, y = east) in DEGREES
        super().__init__(x,y)
        self.V = V
        self.xd = V * np.cos(np.deg2rad(psi))
        self.yd = V * np.sin(np.deg2rad(psi))      
    @property
    def psi(self):
        return self._psi
    @psi.setter
    def psi(self, value):
        self._psi = value
        self.xd = self.V * np.cos(np.deg2rad(self._psi))
        self.yd = self.V * np.sin(np.deg2rad(self._psi))
    @psi.deleter
    def psi(self):
        del self._psi

class GlobalVelocity(Vehicle):
    def __init__(self,x,y,xd,yd):
        super().__init__(x,y)
        self.xd = xd
        self.yd = yd     