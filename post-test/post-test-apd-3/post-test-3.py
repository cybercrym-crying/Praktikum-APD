# Label Tampilan
sama_sisi = """========================   
||         **         ||          
||        ****        ||   
||       ******       ||          
||      ********      ||
||     **********     ||
========================"""

sama_kaki = """========================
||          *         ||          
||         ***        ||     
||        *****       ||
||       *******      ||
||      *********     ||
========================"""

sembarang = """========================
||            *       ||
||          ****      ||
||        *******     ||
||      **********    ||
||    *************   ||
========================"""
gabungan_segitiga = """|| Sama Sisi            Sama Kaki             Sembarang ||
||     **                   *                     *     ||
||    ****                 ***                  ****    ||
||   ******               *****               *******   ||       
||  ********             *******            **********  ||          
|| **********           *********         ************* ||"""

print(58 * "=")
print("||" + "\t" + " " * 6 + "Program Penentu Jenis Segitiga" + "\t" + " " * 8 + "||")
print(58 * "=")
print(f"{gabungan_segitiga}")
print(58 * "=")

# Masukan sisi
sisi_A = int(input("Masukan Sisi A : "))
sisi_B = int(input("Masukan Sisi B : "))
sisi_C = int(input("Masukan Sisi C : "))

# Rumus Luas Segitiga
L_sama_sisi = ((3**0.5) / 4) * sisi_A**2
L_sama_kaki = 0.5 * sisi_C * ((sisi_A**2 - (sisi_C / 2) ** 2) ** 0.5)
L_sembarang = (sisi_A + sisi_B + sisi_C) / 2

# Proses Penentuan Segitiga
if sisi_A + sisi_B > sisi_C:

    if sisi_A == sisi_B and sisi_B == sisi_C:
        print(f"Luas Segitiga  : {L_sama_sisi:.3}")
        print(24 * "=" + f"\n|| Segitiga Sama Sisi || \n{sama_sisi}")

    elif sisi_A == sisi_B or sisi_B == sisi_C or sisi_A == sisi_C:
        print(f"Luas Segitiga  : {L_sama_kaki:.3}")
        print(24 * "=" + f"\n|| Segitiga Sama Kaki || \n{sama_kaki}")

    else:
        print(f"Luas Segitiga  : {L_sembarang:.3}")
        print(24 * "=" + f"\n||  Segita Sembarang  || \n{sembarang}")

else:
    print("Bukan Segitiga")
