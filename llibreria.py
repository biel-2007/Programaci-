# 1. Entrada de dades (mínim 8)
articles = []
print("Introdueix articles (nom i preu). Posa '$' per acabar.")
while len(articles) < 8 or (nom := input("> ")) != "$":
    if nom == "$": continue 
    preu = float(input(f"Preu {nom}: "))
    if preu <= 0: break
    articles.append([nom, preu])

# 2. Mostrar catàleg
print("\nLLIBRERIA ESCOLAR\n" + "-"*25)
for i, (n, p) in enumerate(articles, 1):
    print(f"{i} - {n} ........... {p}€")
print("-" * 25 + "\n0 - PAGAR")

# 3. Compra i total
total = 0
while (opcio := int(input("Article? "))) != 0:
    if 1 <= opcio <= len(articles):
        total += articles[opcio-1][1]

print(f"\nIMPORT TOTAL: {total}€")