import numpy as np 
from conf import conFile

class Current:
    def __init__(self):  
        self.param = conFile()

    def j(self, J, t0):
        J = np.float64(J)
        t0 = np.float64(t0)

        if not self.param.flag1:
            return J
        else:
            TT = np.float64(self.param.T * (self.param.mu0 * self.param.g0 * self.param.Ms))
            omega = np.float64(2 * np.pi / TT)
            Jamp = np.float64((4 * self.param.A0_Amp) / (self.param.mu0 * self.param.Ms**2 * self.param.l**2))
            j = np.float64(J + Jamp * np.sin(omega * t0 + self.param.phase))
            return j

    def ku(self, k, t0):
        k = np.float64(k)
        t0 = np.float64(t0)

        if not self.param.flag2:
            return k
        else:
            TT = np.float64(self.param.T * (self.param.mu0 * self.param.g0 * self.param.Ms))
            omega = np.float64(2 * np.pi / TT)
            kamp = np.float64((2 * self.param.Ku_Amp) / (self.param.mu0 * self.param.Ms**2))
            kk = np.float64(k + kamp * np.sin(omega * t0 + self.param.phase))
            return kk

    def H(self, H, t0):
        H = np.float64(H)
        t0 = np.float64(t0)

        if not self.param.flag3:
            return np.float64(H * self.param.Hex_DC)
        else:
            TT = np.float64(self.param.T * (self.param.mu0 * self.param.g0 * self.param.Ms))
            omega = np.float64(2 * np.pi / TT)
            H_Amp = np.float64(self.param.H_Amp / (self.param.mu0 * self.param.Ms))
            HH = np.float64(H * self.param.Hex_DC + self.param.Hex_AC * (H_Amp * np.sin(omega * t0 + self.param.phase)))
            return HH
