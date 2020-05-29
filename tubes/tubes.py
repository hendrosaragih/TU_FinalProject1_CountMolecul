fopen_mol = open("molekul.cssdf","r")
print(fopen_mol.read())
# cut = fopen_mol.read().splitlines()
# print("Nama %6s Nilai" % " ")
# print ("=======================")
# for n in cut:
# 	line = n.spli("")
# 	print (line[0],line[1].rjust(15-len(line[0]),))
fopen_mol.close()