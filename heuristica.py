import math
import time

# D_C1 = [50,220,140,210,0,80,180,0,70,0,0]
# D_C2 = [0,0,40,120,240,260,30,60,50,10,180]

# B, V, C = 4, 60, 70

D_C1 = [50,220,140,210,0,80,180,0,70,0,0]
D_C2 = [0,0,40,120,240,260,30,60,50,10,180]

B, V, C = 4, 60, 70

N_C1 = [B,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
N_C2 = [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

X_C1 = [0,0,0,0,0,0,0,0,0,0,0]
X_C2 = [0,0,0,0,0,0,0,0,0,0,0]

inicio = time.perf_counter()

total_viagens = 0
for i in range(0,10):
    
    num_c1 = math.ceil(float(D_C1[i])/C)
    num_c2 = math.ceil(float(D_C2[i])/C) - N_C2[i]

    if num_c1 > num_c2: X_C1[i] = num_c1
    else: X_C1[i] = num_c2

    num_c2 = math.ceil(float(D_C2[i])/C)
    num_c1_prox = math.ceil(float(D_C1[i+1])/C) - N_C1[i] + X_C1[i]
    
    if num_c1_prox > num_c2: X_C2[i] = num_c1_prox
    else: X_C2[i] = num_c2

    N_C1[i+1] = N_C1[i] - X_C1[i] + X_C2[i]
    N_C2[i+1] = N_C2[i] - X_C2[i] + X_C1[i]

    total_viagens += X_C1[i] + X_C2[i]

num_c1 = math.ceil(float(D_C1[10])/C)
num_c2 = math.ceil(float(D_C2[10])/C) - N_C2[10]

if num_c1 > num_c2: X_C1[10] = num_c1
else: X_C1[10] = num_c2

X_C2[10] = N_C2[10] + X_C1[10]

total_viagens += X_C1[10] + X_C2[10]

fim = time.perf_counter()

print("N_C1: ", end="")
print(N_C1)
print("N_C2: ", end="")
print(N_C2)
print("X_C1: ", end="")
print(X_C1)
print("X_C2: ", end="")
print(X_C2)

print(f"\nTotal viagens: {total_viagens}")
print(f"Tempo: {(fim-inicio)*1000000:.2f}ns")