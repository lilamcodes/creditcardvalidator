def algerbra(n):
	#  function is n^3 + 3n^2 + 20
	cubed = n**3
	squared = 3*n**2
	constant = 20
	answer = n**3 + 3*n**2 + 20

	print("Cubed", cubed, "Proportion:", cubed/answer*100,"%")
	print("Squared", squared,"Proportion:", squared/answer*100,"%")
	print("Constant", constant,"Proportion:", constant/answer*100,"%")
	print("Answer to function", answer)
	return answer


algerbra(1)