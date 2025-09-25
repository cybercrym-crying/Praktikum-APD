#
# angka = 5
## kosong == false
# string = ""
# if angka >= 5:
#    print("Angka lebih besar sama dengan 5")
#
# if string:
#    print("Berhasil")
#
# print()
# cuaca = "Hujan"
# if cuaca == "Hujan":
#    print("Di Rumah")
# else:
#    print("Nongkrong")
#
# print()
nilai = 70
if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")

print()
status = "Lulus" if nilai >= 70 else "Tidak Lulus"
print(status)
#
# print()
# cuaca = "Mendung"
# if cuaca == "Hujan":
#    print("Dirumah Aja")
#
# elif cuaca == "Mendung":
#    print("Makan Mie")
#
# else:
#    print("Nongkrong")
#
# print()
# usia = int(input("Masukan Usia Anda : "))
# if usia <= 13 and usia >= 1:
#    print("Anak Anak")
# elif usia < 1:
#    print("Tidak valid")
# elif usia <= 18:
#    print("Remaja")
# elif usia <= 40:
#    print("Dewasa")
# else:
#    print("Tua")
#
# print()
## contoh 5
# nilai = int(input("Masukan Nilai : "))
# if nilai >= 90:
#    print("A")
# elif nilai >= 70:
#    print("B")
# elif nilai >= 60:
#    print("C")
# else:
#    print("D")

# Nested if
a = 4
b = 5
c = 6
if a < b:
    if a < c:
        print("a paling kecil")
    else:
        print("c paling kecil")
elif a < c:
    print("c paling besar")
else:
    print("a paling besar")
