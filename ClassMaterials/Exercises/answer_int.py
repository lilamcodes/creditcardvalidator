class Bucket:

	def __init__(self,name,current_vol, max_vol):
		self.name = name
		self.current_vol = current_vol
		self.max_vol = max_vol

	def __add__(self, bucket2):
		if type(bucket2) == dict:
			self.current_vol += bucket2
			return
		else:
			new_max = self.max_vol + bucket2.max_vol
			new_current = self.current_vol + bucket2.current_vol
			new_name = "{} and {} soup".format(self.name, bucket2.name)
			new_bucket = Bucket(new_name,new_current,new_max)

			return new_bucket

	def __eq__(self, bucket2):

		if bucket2.current_vol/bucket2.max_vol == self.current_vol/self.max_vol:
			return True
		else:
			return False


	def __str__(self):
		percentage = (self.current_vol/self.max_vol) * 100
		return "Bucket is called {} and it is {}% full.".format(self.name, percentage)



bucket1 = Bucket("Milk", 20, 100)
bucket2 = Bucket("Beer", 4, 20)
print(dir(bucket1))
print(dir(3))
print(bucket2)

bucket3 = bucket1 + bucket2
print("after addition", bucket3)

print(bucket1 == bucket2)
print(bucket1 != bucket2)

