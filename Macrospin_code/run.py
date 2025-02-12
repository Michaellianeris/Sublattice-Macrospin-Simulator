from solver import solver 
from conf import conFile
import numpy as np 

class run:
    def __init__(self): 
        self.param = conFile()
        self.solver = solver(self.param)
        self.w = 1

    def RUN(self):
        param = self.param
        solver = self.solver

        # Ensure double precision for initial values
        m1 = np.array(param.m1, dtype=np.float64)
        m2 = np.array(param.m2, dtype=np.float64)
        t0 = np.float64(0.0)
        i = np.float64(0.0)
        n = 1
        w = self.w

        # Dimensionless time calculation
        tnew = np.float64(param.t * (param.g0 * param.mu0 * param.Ms))  
        hh = np.float64(param.h * (param.g0 * param.mu0 * param.Ms))  
        k = int(tnew / hh)
        pp = int(k / w)

        # Preallocate results with double precision
        Results1 = np.zeros((pp, 4), dtype=np.float64)
        Results2 = np.zeros((pp, 4), dtype=np.float64)

        for j in range(k): 
            t00 = np.float64(t0 / (param.g0 * param.mu0 * param.Ms))  # Ensure t00 is also double precision

            if j == 0:
                Results1[j, :] = [t00, m1[0], m1[1], m1[2]]
                Results2[j, :] = [t00, m2[0], m2[1], m2[2]]

            # Call the solver method with double precision
            m1, m2 = solver.Heun(m1, m2, t0)

            if i == w:
                Results1[n, :] = [t00, m1[0], m1[1], m1[2]]
                Results2[n, :] = [t00, m2[0], m2[1], m2[2]]
                
                print(f'Spin 1 : t= {t00:.16E}, mx= {m1[0]:.16f}, my={m1[1]:.16f}, mz={m1[2]:.16f}')
                print(f'Spin 2 : t= {t00:.16E}, mx= {m2[0]:.16f}, my={m2[1]:.16f}, mz={m2[2]:.16f}')
                
                n += 1
                i = 0  # Reset counter

            t0 += hh  # Ensure `t0` remains float64
            i += 1

        return [Results1, Results2]
