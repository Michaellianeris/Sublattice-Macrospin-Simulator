import numpy as np 


class conFile() :

	def __init__(self):
		
		self.g0 = 2.21e5	   							# gamma zero
		self.gamma = 1.76e11							# gamma
		self.h  = 1.0e-13	   							# Euler step  
		self.t  = 3.5e-9 								# Total time   
		self.a  = 1.1		   							# Damping Contant
		self.Ms = 566e3 								# Saturation Magnetization
		self.A0 = 5.0e-12								# Homogeneous interlattice exchange
		self.Ku = 0.5e6	   								# Uniaxial Anisotropy
		self.mu0 = 4*np.pi*1e-7							# mu zero 
		self.l = 5.0e-9									# lattice constant
		self.H = 0.0e-3									# Field
		self.Fr =1.0e9								    # Frequency 
		self.T = 1/self.Fr								# Period
		self.phase = 0.0*np.pi							# Phase 
		self.flag1 = False								# Current (True) / not Current (False) 
		self.flag2 = False								# flag1 is for J(t) # flag2 is for Ku(t) # flag3 is for H(t) 
		self.flag3 = False
		self.Hex_DC = np.array([0.0,0.0,0.0]) 			# Ex Field Components (DC)
		self.Hex_AC = np.array([0.0,0.0,0.0]) 			# Ex Field Components (AC)	
		self.m1 = np.array([0.256,0.0,-0.965])			# Initial Condition m_1
		self.m2 = np.array([0.25,0.0,0.96])				# Initial Condition m_2
		self.p  = np.array([0.0,0.0,0.0])				# Polarizer
		self.Demag = 0*np.array([0.0259,0.0259,0.9482]) # Demag Tensor 
		self.ani =  np.array([0.0,0.0,1.0])				# Anisotropy 
		self.A0_Amp = 12.0e-12							# J  Amp
		self.Ku_Amp = 0.4e6								# Ku Amp
		self.H_Amp = 0.0e-3								# Field Amp
		
		
		
		
	


