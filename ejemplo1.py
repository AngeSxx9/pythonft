import random
# Represa Hidroituango

# ENTRADAS
nivelAgua = random.randint(0, 500)

print(f"Digite el nivel de agua: {nivelAgua}")

# PROCESO
if nivelAgua >= 0 and nivelAgua <= 250:
    print(f"El sensor marca {nivelAgua}, muy bajo..")
elif nivelAgua > 250 and nivelAgua <= 400:
    print(f"El sensor marca {nivelAgua}. Operando normal")
else:
    print(f"El sensor marca {nivelAgua}, PELIGRO!")
