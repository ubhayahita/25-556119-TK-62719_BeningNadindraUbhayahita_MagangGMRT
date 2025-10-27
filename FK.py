import numpy as np 
import math

def R(theta_deg): # define matrix rotasi
    return np.array([
        [math.cos(math.radians(theta_deg)), -math.sin(math.radians(theta_deg)), 0],
        [math.sin(math.radians(theta_deg)), math.cos(math.radians(theta_deg)), 0],
        [0, 0, 1]
    ])

def Tx(a): # define matrix transformasi, dalam problem ini translasi pada sumbu x 
    return np.array([
        [1, 0, a],
        [0, 1, 0],
        [0, 0, 1]
    ])

L1 = float(input("Masukkan panjang femur (L1): ")) # input panjang femur, NIU: 556119
L2 = float(input("Masukkan panjnag tibia (L2): ")) # input panjng tibia, NIF: 62719
q1 = float(input("Masukkan besar sudut rotasi servo 1 (q1 dalam derajat): ")) # input sudut servo 1 
q2 = float(input("Masukkan besar sudut rotasi servo 2 (q2) dalam derajat: ")) # input sudut servo 2

H01 = R(q1) # rotasi pertama
H12 = Tx(L1) # translasi sepanjang femur 
H23 = R(q2) # rotasi kedua 
H34 = Tx(L2) # translasi sepanjang tibia

H04 = H01 @ H12 @ H23 @ H34 # perkalian seluruh matrix transformasi

x = H04[0, 2] # posisi x final
y = H04[1, 2] # posisi y final

print("H04 (matrix hasil) = ")
print(H04)
print(f"\nKoordinat final ujung kaki robot: ({x: .2f} , {y: .2f})")
