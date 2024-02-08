# Program For find the  PGCD and PPCM for two numbers
def pgcd(a,b):
	if b == 0:
		return a
	else :
		r = a%b
		return pgcd(b,r)
def ppcm(a,b):
    if a == 0 or b == 0:
        return 0
    else :
        return (a*b)//pgcd(a,b)

