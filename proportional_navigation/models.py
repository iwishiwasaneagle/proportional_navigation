import numpy as np

class Vehicle(object):
    pass


class HeadingVelocity(Vehicle):
    def __init__(self,psi,x,y,V):
        self._psi = psi # Heading angle relative to global ref frame (x = north, y = east) in DEGREES
        self.x = x
        self.y = y
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

class GlobalVelocity(Vehicle):
    def __init__(self,x,y,xd,yd):
        self.x = x
        self.y = y
        self._xd = xd
        self._yd = yd     
        self._psi = np.arccos(xd/np.sqrt(xd*xd + yd*yd))
    @property
    def psi(self):
        return self._psi
    @psi.setter
    def psi(self, value):
        self._psi = value    
    @property
    def xd(self):
        return self._xd
    @xd.setter
    def xd(self, value):
        self._xd = value
        self._psi = np.arccos(value/np.sqrt(value*value + self._yd*self._yd))
    @property
    def yd(self):
        return self._yd
    @yd.setter
    def psi(self, value):
        self._yd = value
        self._psi = np.arccos(value/np.sqrt(value*value + self._xd*self._xd))
