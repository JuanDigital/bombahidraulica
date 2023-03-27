class multiplica:
	"""docstring for ClassName"""
	def __init__(self,val1,val2):
		self.resX=val2*val1
	def resultado(self):
		return self.resX
		
if __name__ =="__main__":
	multi=multiplica(2,2)
	print(multi.resultado())
		
