# STUDI KASUS 1
tinggi_badan = int(input("Masukan Tinggi Badan : "))
batas = "Boleh" if tinggi_badan >= 145 else "Tidak Boleh"
print(batas)

# STUDI KASUS 2
total_belanja = int(input("Masukan Total Belanja : "))
if total_belanja >= 100000:
    print(f"Diskon 20% \nTotal : {100000-(100000*0.2)}")

elif total_belanja >= 50000:
    print(f"Diskon 10% \nTotal : {50000-(50000*0.1)}")

else:
    print("Tidak Dapat Diskon")

print()
nilai = int(input("Masukan Nilai : "))
kelas = input("Masukan Kelas : ")

if nilai >= 80 and kelas == "A":
    print("IPK 4")
elif nilai >= 80 and kelas == "B":
    print("IPK 3")
else:
    print("IPK 2")
