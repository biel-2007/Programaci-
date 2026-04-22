# --- PRÀCTICA DE CALCULADORA ---

print("--- Benvingut al sistema de càlcul ---")
v1 = float(input("Escriu el primer valor numèric: ")) 
v2 = float(input("Escriu el segon valor numèric: ")) 
tipus_operacio = input("Tria una opció (+, -, *, /, %): ") 

if tipus_operacio == '+': 
    solucio = v1 + v2 
elif tipus_operacio == '-': 
    solucio = v1 - v2 
elif tipus_operacio == '*': 
    solucio = v1 * v2 
elif tipus_operacio == '/': 
    solucio = v1 / v2 if v2 != 0 else "Error: No es pot dividir per zero"
elif tipus_operacio == '%': 
    solucio = v1 % v2 
else: 
    solucio = "Operació desconeguda"

print("El resultat obtingut és: " + str(solucio))