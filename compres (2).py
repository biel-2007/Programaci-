# --- PRÀCTICA DE GESTIÓ DE COMPRES ---

codi_client = input("Introdueix la referència del comprador: ") 
import_inicial = float(input("Quin és el cost base de l'article?: ")) 
percentatge_desc = float(input("Quin descompte s'ha d'aplicar (%): ")) 
taxa_iva = float(input("Quin és l'IVA corresponent (%): ")) 

# Càlculs matemàtics
preu_rebaixat = import_inicial - (import_inicial * percentatge_desc / 100) 
total_factura = preu_rebaixat + (preu_rebaixat * taxa_iva / 100) 

print("Resum de l'operació per al client: " + codi_client)
print("L'import final a liquidar és de: " + str(total_factura) + "€")