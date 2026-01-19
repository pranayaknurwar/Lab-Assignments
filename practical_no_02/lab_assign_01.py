V = float(input("Enter voltage: "))
R = float(input("Enter resistance: "))

I = V / R

print("Current (I):", I, "A")

if I < 0.5:
    print("Low current")
elif 0.5 <= I and I<= 2:
    print("Normal current")
else:
    print("High current")
