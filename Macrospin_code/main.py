from output import output
from run import run 

class MAIN():

	def __init__(self) : 
		
		self.output = output()
		self.run = run()

	
	def main(self):
		
		xx=self.run.RUN()
		self.output.save_data(xx)
		self.output.Two_Dynamics()
		
		

	
	
if __name__ == "__main__":
	a=MAIN()
	a.main()