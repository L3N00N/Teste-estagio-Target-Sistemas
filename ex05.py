string = "Exemplo de string para inverter"

# Convertendo a string em uma lista de caracteres
lista_caracteres = list(string)

# Obtendo o tamanho da string
tamanho_string = len(string)

# Invertendo a ordem dos caracteres na lista
for i in range(tamanho_string//2):
    lista_caracteres[i], lista_caracteres[tamanho_string-i-1] = lista_caracteres[tamanho_string-i-1], lista_caracteres[i]

# Convertendo a lista de caracteres de volta para uma string
string_invertida = ''.join(lista_caracteres)

# Imprimindo a string invertida
print(string_invertida)
