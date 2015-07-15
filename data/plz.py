import math

def convert(day, maxi):
	return (math.cos(2*math.pi*(day-1)/maxi), math.sin(2*math.pi*(day-1)/maxi))

def toPolarRepresentation(data, value, maxi):
	sini = []
	cosi = []

	for i in range(len(data[value])):
		(c, s) = convert(data[value][i], maxi)
		sini.append(s)
		cosi.append(c)

	data[value+"_sin"] = sini
	data[value+"_cos"] = cosi

	return data

kIn = {"date": range(1, 30)}

print kIn
data = kIn
data = toPolarRepresentation(data, "date", 31)
pyOut = data
print pyOut