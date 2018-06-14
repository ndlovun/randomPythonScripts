#“Write a function that takes three measurements in centimeters as input
# and returns a the volume over a litre”

def volPerLitre(m1,m2,m3):
    cubic_cm = m1 * m2 * m3
    vol_litre = cubic_cm / 1000
    return vol_litre

my_box = volPerLitre(1, 10, 10)
print(my_box)
