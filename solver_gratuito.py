from pyscipopt import Model, quicksum
import time

#CONSTANTES:
D_C1 = [40,200,110,190,0,68,170,0,140,0,0]
D_C2 = [0,0,70,180,136,160,55,70,120,30,180]

B, V, C = 4, 80, 50

# # #CONSTANTES:
# D_C1 = [50,220,140,210,0,80,180,0,70,0,0]
# D_C2 = [0,0,40,120,240,260,30,60,50,10,180]

# B, V, C = 4, 60, 70

#VARIAVEIS:
N_C1 = [0,0,0,0,0,0,0,0,0,0,0]
N_C2 = [0,0,0,0,0,0,0,0,0,0,0]

X_C1 = [0,0,0,0,0,0,0,0,0,0,0]
X_C2 = [0,0,0,0,0,0,0,0,0,0,0]

model = Model()
model.hideOutput() 

for i in range(0,11):
    X_C1[i] = model.addVar(name=f"x_c1_{i}", vtype="I", lb = 0)
    X_C2[i] = model.addVar(name=f"x_c2_{i}", vtype="I", lb = 0)
    N_C1[i] = model.addVar(name=f"n_c1_{i}", vtype="I", lb = 0)
    N_C2[i] = model.addVar(name=f"n_c2_{i}", vtype="I", lb = 0)

model.setObjective(quicksum(X_C1[i] + X_C2[i] for i in range(0,11)), "minimize")

model.addCons(N_C1[0] == B)
model.addCons(N_C2[0] == 0)
model.addCons(N_C2[10] + X_C1[10] - X_C2[10] == 0)

for t in range(0,10):
    model.addCons(N_C1[t+1] == N_C1[t] - X_C1[t] + X_C2[t])
    model.addCons(N_C2[t+1] == N_C2[t] - X_C2[t] + X_C1[t])

for t in range(0,11):
    model.addCons(X_C1[t] <= N_C1[t])
    model.addCons(X_C2[t] <= N_C2[t] + X_C1[t])

for t in range(0,11):
    model.addCons(D_C1[t] <= C * X_C1[t])
    model.addCons(D_C2[t] <= C * X_C2[t])

for t in range(0,11):
    model.addCons(N_C1[t] + N_C2[t] == B)

model.addCons(quicksum(X_C1[i] + X_C2[i] for i in range(0,11)) <= V)

inicio = time.perf_counter()

model.optimize()

fim = time.perf_counter()

status = model.getStatus()

if status == "optimal" or status == "feasible":

    sol = model.getBestSol()

    print("N_C1: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{sol[N_C1[t]]}, ", end="");
        else:
            print(f"{sol[N_C1[t]]}]\n", end="");
    
    print("N_C2: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{sol[N_C2[t]]}, ", end="");
        else:
            print(f"{sol[N_C2[t]]}]\n", end="");
    
    print("X_C1: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{sol[X_C1[t]]}, ", end="");
        else:
            print(f"{sol[X_C1[t]]}]\n", end="");
    
    print("X_C2: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{sol[X_C2[t]]}, ", end="");
        else:
            print(f"{sol[X_C2[t]]}]\n", end="");

    print("\n\n ========= Infos da Solução ================ \n\n")

    print(f"Status: {status}")
    print("Valor objetivo:", model.getObjVal())
    print("Gap de otimalidade:", model.getGap() * 100, "%")
else:
    print(f"Status: {status}")
    print("Nenhuma solução encontrada.")

print(f"Tempo de processamento: {(fim - inicio) * 1e3:.3f} milisegundos \n\n")
