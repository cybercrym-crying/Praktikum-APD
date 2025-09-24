jumlah_float = 2
jumlah_int = 1
data = [True, "True", 1, 2, 1.1]
print(data)
print(40 * "=")
print("||" + 11 * " " + " DATA SEBELUM " + 11 * " " + "||")
print(40 * "=")
print("||" + 8 * " " + "DATA" + 5 * " " + "||" + 5 * " " + "TIPE" + 8 * " " + "||")
print(40 * "=")
print(
    f"||"
    + 8 * " "
    + f"{data[0]} \t"
    + "   ||"
    + 2 * " "
    + f"{type(data[0])}"
    + " "
    + "||"
)
print(
    f"||"
    + 8 * " "
    + f"{data[1]} \t"
    + "   ||"
    + 2 * " "
    + f"{type(data[1])}"
    + 2 * " "
    + "||"
)
print(
    f"||"
    + 8 * " "
    + f"{data[2]} \t"
    + "   ||"
    + 2 * " "
    + f"{type(data[2])}"
    + 2 * " "
    + "||"
)
print(
    f"||"
    + 8 * " "
    + f"{data[3]} \t"
    + "   ||"
    + 2 * " "
    + f"{type(data[3])}"
    + 2 * " "
    + "||"
)
print(f"||" + 8 * " " + f"{data[4]} \t" + "   ||" + 2 * " " + f"{type(data[4])}" + "||")
print(40 * "=")
print(f"|| Tipe Data int\t: {jumlah_float}" + 11 * " " + "||")
print(f"|| Tipe Data float\t: {jumlah_int}" + 11 * " " + "||")
print(40 * "=")
jumlah_int = 2
jumlah_float = 1
data[0] = str(data[0])
data[1] = bool(data[1])
data[2] = float(data[2])
data[3] = float(data[3])
data[4] = int(data[4])
print("\n")
print(data)
print(40 * "=")
print("||" + 11 * " " + " DATA SESUDAH " + 11 * " " + "||")
print(40 * "=")
print("||" + 8 * " " + "DATA" + 5 * " " + "||" + 5 * " " + "TIPE" + 8 * " " + "||")
print(40 * "=")
print(
    f"||"
    + 8 * " "
    + f"{data[0]} \t"
    + "   ||"
    + 2 * " "
    + f"{type(data[0])}"
    + 2 * " "
    + "||"
)
print(
    f"||"
    + 8 * " "
    + f"{data[1]} \t"
    + "   ||"
    + 2 * " "
    + f"{type(data[1])}"
    + " "
    + "||"
)
print(f"||" + 8 * " " + f"{data[2]} \t" + "   ||" + 2 * " " + f"{type(data[2])}" + "||")
print(f"||" + 8 * " " + f"{data[3]} \t" + "   ||" + 2 * " " + f"{type(data[3])}" + "||")
print(
    f"||"
    + 8 * " "
    + f"{data[4]} \t"
    + "   ||"
    + 2 * " "
    + f"{type(data[4])}"
    + 2 * " "
    + "||"
)
print(40 * "=")
print(f"|| Tipe Data int\t: {jumlah_float}" + 11 * " " + "||")
print(f"|| Tipe Data float\t: {jumlah_int}" + 11 * " " + "||")
print(40 * "=")
# END OF PROGRAM
