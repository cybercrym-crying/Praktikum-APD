data = ["True", 100, 200, 100.255, True]
jumlah_int = 0
jumlah_float = 0
print(16 * "=" + "[ DATA SEBELUM ]" + "=" * 16)

print(data, "\n")
for i in data:
    print(f"Data {i} bertipe\t : {type(i)}")
    if type(i) == int:
        jumlah_int += 1
    elif type(i) == float:
        jumlah_float += 1
print(f"\nTipe int berjumlah\t : {jumlah_int}")
print(f"Tipe float berjumlah\t : {jumlah_float}\n")

jumlah_int = 0
jumlah_float = 0
j = 0
print(16 * "=" + "[ DATA SESUDAH ]" + "=" * 16)
for i in data:
    match i:
        case bool():
            data[j] = str(data[j])
        case float():
            data[j] = int(data[j])
            jumlah_int += 1
        case int():
            data[j] = float(data[j])
            jumlah_float += 1
        case str():
            data[j] = bool(data[j])
    j += 1
print(data, "\n")
for i in data:
    print(f"Data {i} bertipe\t : {type(i)}")

print(f"\nTipe int berjumlah\t : {jumlah_int}")
print(f"Tipe float berjumlah\t : {jumlah_float}")
