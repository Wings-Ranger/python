x = 5
y = "Lachlan"
nameFirst = "Lachlan"
nameLast = "Nash"
nameFull = nameFirst + " " + nameLast
print(x)
print(y)
print(nameFirst + " " + nameLast)
print(nameFull)
f =open ("test.txt", "w")
f.write(nameFull)
f.close()