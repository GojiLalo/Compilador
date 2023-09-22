import re

operadores = ['+', '-', '*', '/', '%', '>', '<', '!', '&', '|', '^', '~', '(', ')', '{', '}', '[', ']', ';', ',', '.', ':', '#']
reservadas = ["int","float", "char", "var", "include", "main"]


expRegS = [
    (r'(\d+)', 'DIGITO'),
    (r'([a-zA-Z_]\w*)', 'ID'),
    (r'(\#)', 'ASTERISCO'),
    (r'(\+)', 'MAS'),
    (r'(-)', 'MENOS'),
    (r'(\*)', 'MULTIPLICACION'),
    (r'(/)', 'DIVISION'),
    (r'(%)', 'MODULO'),
    (r'(\()', 'IZQPAREN'),
    (r'(\))', 'DERPAREN'),
    (r'(;)', 'PUNTOCOMA'),
    (r'({)', 'IZQLLAVE'),
    (r'(})', 'DERLLAVE')
]

def obtenerCodigo():
    archivo = open('codigo.txt', 'r')
    codigo = archivo.read()
    return codigo

def obtenerTokens(codigo):
    tmpTokens = []
    tokens = []
    #Separar el codigo en palabras y simbolos
    for o in operadores:
        codigo = codigo.replace(o, ' ' + o + ' ')
    palabras = codigo.split()

    #Clasificar tokens
    for token in palabras:
        for expresion, tipoToken in expRegS:
            if re.match(expresion, token):
                tmpTokens.append((token, tipoToken))

    #Encontrar reservadas
    for token, tipoToken in tmpTokens:
        if token in reservadas:
            tokens.append((token, "PR"))
        if token not in reservadas:
            tokens.append((token, tipoToken))

    for token in tokens:
        print(token)







codigo = obtenerCodigo()
obtenerTokens(codigo)