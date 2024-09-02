def inverter_string(s):
    
    invertida = ""
    
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida

string_original = input("Informe a string que deseja inverter: ")

string_invertida = inverter_string(string_original)

print("String invertida:", string_invertida)
