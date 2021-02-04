a = int(input("Første tal: "))
b = int(input("Andet tal: "))

print("Gennemsnittet er: {}".format((a+b)/2))

# Variation

n = int(input("Hvor mange tal vil du bruge? "))

tal = []
for i in range(n):
    t = int(input("Skriv tal nummer {}: ".format(i+1)))
    tal.append(t)
s = sum(tal)
print("Gennemsnittet er: {}".format(s/n))
