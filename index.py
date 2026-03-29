nameFirst = "Lachlan"
nameLast = "Nash"
nameFull = nameFirst + " " + nameLast
print(nameFirst + " " + nameLast)
print(nameFull)
f =open ("test.txt", "w")
f.write(nameFull)
f.close()