# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

from math import sqrt

def fact(n):
	"""Computes the factorial of a natural number.

	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if(n<0):
		raise ValueError
	returnValue=1
	if(n==0):
		return returnValue
	for i in range (1, n+1):
		returnValue*=i
	return returnValue

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + c = 0 polynomial.

	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		  to the roots of the ax^2 + bx + c polynomial.
	"""
	if(a==0):
		if(b==0):
			if(c==0):
				return tuple()#devrait renvoyer une infinite de x
			else:
				return tuple()#valeur correcte
		else:
			result = -c/b
			return result
	else:	
		rho = b**2-4*a*c
		if(rho<0):
			return tuple()
		elif(rho==0):
			result = -b/(2*a)
			return (result)
		else:
			resulta = (-b+sqrt(rho))/(2*a)
			resultb = (-b-sqrt(rho))/(2*a)
			return (resulta, resultb)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds

	Pre: 'function' is a valid Python expression with x as a variable,
		 'lower' <= 'upper',
		 'function' continuous and integrable between 'lower' and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		  of the specified 'function'.
	"""
	nSteps = 100
	step = (upper-lower)/nSteps
	sum=0
	for i in range(nSteps+1):
		x=lower+i*step
		sum+=eval(function)
	integral=sum/nSteps*(upper-lower)
	return integral

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))