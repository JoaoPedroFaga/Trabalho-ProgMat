from gurobipy import Model, GRB, quicksum
import time

# #CONSTANTES:
D_C1 = [50,220,140,210,0,80,180,0,70,0,0]
D_C2 = [0,0,40,120,240,260,30,60,50,10,180]

B, V, C = 4, 60, 70

#VARIAVEIS:
N_C1 = [0,0,0,0,0,0,0,0,0,0,0]
N_C2 = [0,0,0,0,0,0,0,0,0,0,0]

X_C1 = [0,0,0,0,0,0,0,0,0,0,0]
X_C2 = [0,0,0,0,0,0,0,0,0,0,0]

model = Model()
model.setParam("OutputFlag", 0)

for i in range(0,11):
    X_C1[i] = model.addVar(name=f"x_c1_{i}", vtype=GRB.INTEGER, lb = 0)
    X_C2[i] = model.addVar(name=f"x_c2_{i}", vtype=GRB.INTEGER, lb = 0)
    N_C1[i] = model.addVar(name=f"n_c1_{i}", vtype=GRB.INTEGER, lb = 0)
    N_C2[i] = model.addVar(name=f"n_c2_{i}", vtype=GRB.INTEGER, lb = 0)

model.setObjective(quicksum(X_C1[i] + X_C2[i] for i in range(0,11)), GRB.MINIMIZE)

model.addConstr(N_C1[0] == B)
model.addConstr(N_C2[0] == 0)
model.addConstr(N_C2[10] + X_C1[10] - X_C2[10] == 0)

for t in range(0,10):
    model.addConstr(N_C1[t+1] == N_C1[t] - X_C1[t] + X_C2[t])
    model.addConstr(N_C2[t+1] == N_C2[t] - X_C2[t] + X_C1[t])

for t in range(0,11):
    model.addConstr(X_C1[t] <= N_C1[t])
    model.addConstr(X_C2[t] <= N_C2[t] + X_C1[t])

for t in range(0,11):
    model.addConstr(D_C1[t] <= C * X_C1[t])
    model.addConstr(D_C2[t] <= C * X_C2[t])

for t in range(0,11):
    model.addConstr(N_C1[t] + N_C2[t] == B)

model.addConstr(quicksum(X_C1[i] + X_C2[i] for i in range(0,11)) <= V)

inicio = time.perf_counter()

model.optimize()

fim = time.perf_counter()

status = model.Status

if status == GRB.OPTIMAL or status == GRB.FEASIBLE:

    print("N_C1: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{N_C1[t].X}, ", end="");
        else:
            print(f"{N_C1[t].X}]\n", end="");
    
    print("N_C2: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{N_C2[t].X}, ", end="");
        else:
            print(f"{N_C2[t].X}]\n", end="");
    
    print("X_C1: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{X_C1[t].X}, ", end="");
        else:
            print(f"{X_C1[t].X}]\n", end="");
    
    print("X_C2: [", end="")
    for t in range(11):
        if(t != 10):
            print(f"{X_C2[t].X}, ", end="");
        else:
            print(f"{X_C2[t].X}]\n", end="");

    print("\n\n ========= Infos da Solução ================ \n\n")

    print(f"Status: {status}")
    print("Valor objetivo:", model.ObjVal)
    print("Gap de otimalidade:", model.MIPGap * 100, "%")
else:
    print(f"Status: {status}")
    print("Nenhuma solução encontrada.")

print(f"Tempo de processamento: {(fim - inicio) * 1e3:.3f} milisegundos \n\n")