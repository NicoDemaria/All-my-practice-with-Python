def generaPares(limite):

	num=1


	milista=[]


	while num<limite:

		yield num*2

	
		num=num+1



devuelvePares=generaPares(10)
	
	



print(next(devuelvePares))		









