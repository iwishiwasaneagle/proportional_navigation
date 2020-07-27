import numpy as np
try:
    import matplotlib.pyplot as plt
    plt_found = True
except ModuleNotFoundError:
    plt_found = False
import proportional_navigation as PN

if __name__ == "__main__":
    pursuer = PN.HeadingVelocity(0,0,0,5)
    target = PN.HeadingVelocity(100,100,50,2)
    options = PN.PNOptions(return_R=True, return_Vc=True)
    dt = 0.01
    N = 3
    
    terminate = False
    t = 0

    log = {'pursuer':{'x':[],'y':[]},'target':{'x':[],'y':[]}}
    while not terminate:
        ret = PN.PN(pursuer,target,N=N,options=options).calculate()
        nL = ret['nL']
        R = ret['R']
        Vc = ret['Vc']

        t = t+dt
        if R < 5 or t > 20:
            if Vc < 0:
                terminate = True

        psipd = nL/pursuer.V

        pursuer.x += pursuer.xd*dt
        pursuer.y += pursuer.yd*dt
        target.x += target.xd*dt
        target.y += target.yd*dt

        pursuer.psi = pursuer.psi + np.rad2deg(dt*psipd)

        log['pursuer']['x'].append(pursuer.x)
        log['pursuer']['y'].append(pursuer.y)
        log['target']['x'].append(target.x)
        log['target']['y'].append(target.y)
    
    if plt_found:
        plt.plot(log['pursuer']['y'],log['pursuer']['x'])
        plt.plot(log['target']['y'],log['target']['x'])
        plt.show()
    else:
        print("matplotlib.pyplot was not found in the env. Plot of xy graph will not be shown")
