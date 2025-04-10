import numpy as np
from current import Current

class solver:
    def __init__(self, param): 
        self.param = param
        self.Current = Current()

    def mxx(self, m1, m2, t0): 
        param = self.param

        
        k = np.float64((2 * param.Ku) / (param.mu0 * param.Ms**2))
        J = np.float64((4 * param.A0) / (param.mu0 * param.Ms**2 * param.l**2))
        H = np.float64(param.H / (param.mu0 * param.Ms))

        JJ = np.float64(Current.j(self, J, t0))
        kk = np.float64(Current.ku(self, k, t0))
        HH = np.float64(Current.H(self, H, t0))
       

        # Ensure m1, m2 are double precision
        m1 = np.array(m1, dtype=np.float64)
        m2 = np.array(m2, dtype=np.float64)

        n = JJ * m2 + kk * (param.ani * m1) + HH - param.Demag * m1
        pp = np.cross(m1, n)
        bb = np.cross(m1, pp)

        # LLG equation 
        s = np.float64(-1.0*(param.g0 * param.mu0 * param.Ms) / (1 + param.a**2) * (pp + param.a * bb)) 
        return s

    def Heun(self, m1, m2, t0):  # Heun Method
        param = self.param
        h = np.float64(param.h * (param.mu0 * param.g0 * param.Ms))

        m1 = np.array(m1, dtype=np.float64)
        m2 = np.array(m2, dtype=np.float64)

        xx = self.mxx(m1, m2, t0)
        yy = self.mxx(m2, m1, t0)

        mp1 = m1 + h * xx  # Predictor
        mp2 = m2 + h * yy
        mp1 /= np.linalg.norm(mp1)  # Normalize
        mp2 /= np.linalg.norm(mp2)

        m1 = m1 + 0.5 * h * (xx + self.mxx(mp1, mp2, t0))  
        m2 = m2 + 0.5 * h * (yy + self.mxx(mp2, mp1, t0))  # Corrector
        m1 /= np.linalg.norm(m1)
        m2 /= np.linalg.norm(m2)

        return m1, m2

    def RK4(self, m1, m2, t0):  # Runge-Kutta 4th Order Method
        param = self.param
        h = np.float64(param.h * (param.mu0 * param.g0 * param.Ms))

        m1 = np.array(m1, dtype=np.float64)
        m2 = np.array(m2, dtype=np.float64)

        k1 = self.mxx(m1, m2, t0) 
        k2 = self.mxx(m1 + 0.5 * h * k1, m2 + 0.5 * h * k1, t0 + 0.5 * h) 
        k3 = self.mxx(m1 + 0.5 * h * k2, m2 + 0.5 * h * k2, t0 + 0.5 * h) 
        k4 = self.mxx(m1 + h * k3, m2 + h * k3, t0 + h) 

        p1 = self.mxx(m2, m1, t0) 
        p2 = self.mxx(m2 + 0.5 * h * p1, m1 + 0.5 * h * p1, t0 + 0.5 * h) 
        p3 = self.mxx(m2 + 0.5 * h * p2, m1 + 0.5 * h * p2, t0 + 0.5 * h) 
        p4 = self.mxx(m2 + h * p3, m1 + h * p3, t0 + h) 

        m1 = m1 + 0.166 * h * (k1 + 2 * k2 + 2 * k3 + k4)
        m2 = m2 + 0.166 * h * (p1 + 2 * p2 + 2 * p3 + p4)
        m1 /= np.linalg.norm(m1)
        m2 /= np.linalg.norm(m2)

        return m1, m2
