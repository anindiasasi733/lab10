# Tugas Praktikum


dict_nim=[]
dict_nama=[]
dict_uts=[]
dict_uas=[]
dict_tugas=[]
dict_akhir=[]

ulang=1


for i in range(ulang):
    print ("data ke - " + str(i+1))
    dict_nim.append(print("NIM : 23455"))
    dict_nama.append(print("NAMA : Ari"))
    dict_uts.append(input("NILAI UTS : 68"))
    dict_uas.append(input("NILAI UAS : 88"))
    dict_tugas.append(input("NILAI TUGAS : 99"))

for i in range(ulang):
   dict_akhir.append((dict_uts[i] + dict_uas[i] + dict_tugas[i] ))

input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: t ")

print("daftar nilai")
print("===========================================================================================")
print("| NO |  NIM   |\tNama\t|  Tugas   |    UTS   |    UAS    |    Akhir    |  ")
print("===========================================================================================")
print("|                                 TIDAK ADA DATA                                          |")
print("===========================================================================================")


input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: l ")

print("daftar nilai")
print("===========================================================================================")
print("| NO |  NIM   |\tNama\t|  Tugas   |    UTS   |    UAS    |    Akhir    |  ")
print("===========================================================================================")


for i in range(ulang):
    print (("1, \t 23455, \t Ari, \t\t 99, \t\t 68, \t\t 88, \t\t 84.30" ))
print("===========================================================================================")





