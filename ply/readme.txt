def add(a, b):
	return a + b

def sub(a, b):
	return a - b

x = 5
y = 6
wynik = None
wynik = add(x, y)
wynik2 = None
wynik2 = sub(x, y)
print("--------- Test 1 ---------")
if wynik > 10:
	print("Wiecej niz 10")
	print("Koniec")
else:
	print("Mniej niz 10")
	print("Koniec")
print("--------- Test 2 ---------")
if wynik2 > 0:
	print("Wiecej niz 0")
	print("Koniec")
else:
	print("Mniej niz 0")
	print("Koniec")


