def computepay(hrs, rph):
    return hrs * rph
hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hour:"))
if hrs < 40:
    p = computepay(hrs, rph)
    print("Pay", p)
elif hrs > 40:
    hrs = hrs - 40
    hrs = hrs * 1.5 + 40
    p = computepay(hrs, rph)
    print("Pay", p)
