import re

operadores = ['+', '-', '*', '/', '%', '>', '<', '!', '&', '|', '^', '~', '(', ')', '{', '}', '[', ']', ';', ',', '.', ':', '#', '"']
reservadas = ["alignas", "alignof", "and", "and_eq", "asm", "auto", "bitand",
    "bitor", "bool", "break", "case", "catch", "char", "char8_t",
    "char16_t", "char32_t", "class", "compl", "concept", "const",
    "consteval", "constexpr", "const_cast", "continue", "co_await",
    "co_return", "co_yield", "decltype", "default", "delete", "do",
    "double", "dynamic_cast", "else", "enum", "explicit", "export",
    "extern", "false", "float", "for", "friend", "goto", "if",
    "inline", "int", "long", "mutable", "namespace", "new", "noexcept",
    "not", "not_eq", "nullptr", "operator", "or", "or_eq", "private",
    "protected", "public", "register", "reinterpret_cast", "requires",
    "return", "short", "signed", "sizeof", "static", "static_assert",
    "static_cast", "struct", "switch", "template", "this", "thread_local",
    "throw", "true", "try", "typedef", "typeid", "typename", "union",
    "unsigned", "using", "virtual", "void", "volatile", "wchar_t", "while",
    "xor", "xor_eq", "cin", "cout", "include", "iostream"]


expRegS = [
    (r'(\d+)', 'DIGITO'),
    (r'([a-zA-Z_]\w*)', 'ID'),
    (r'(\#)', 'ASTERISCO'),
    (r'(\+)', 'MAS'),
    (r'(-)', 'MENOS'),
    (r'(\*)', 'MULTIPLICACION'),
    (r'(/)', 'DIVISION'),
    (r'(%)', 'MODULO'),
    (r'(>)', 'MAYORQUE'),
    (r'(<)', 'MENORQUE'),
    (r'(\()', 'IZQPAREN'),
    (r'(\))', 'DERPAREN'),
    (r'(;)', 'PUNTOCOMA'),
    (r'({)', 'IZQLLAVE'),
    (r'(})', 'DERLLAVE'),
    (r'(")', 'COMILLAS')
]


def obtenerTokens(linea):
    listaTokenstmp = []
    listaTokens = []
    tmpTokens = linea.split()
    #Clasificar tokens
    for t in tmpTokens:
        for expresion, tipoToken in expRegS:
            if re.match(expresion, t):
                listaTokenstmp.append((t, tipoToken))

    #Encontrar reservadas
    for token, tipoToken in listaTokenstmp:
        if token in reservadas:
            listaTokens.append((token, "PR"))
        if token not in reservadas:
            listaTokens.append((token, tipoToken))
    return listaTokens


def obtenerCodigo():
    lineas = []
    listaTokens = []
    with open('codigo.txt') as archivo:
        for linea in archivo:
            for o in operadores:
                linea = linea.replace(o, ' ' + o + ' ')
            listaTokens.append(obtenerTokens(linea))
    return listaTokens


def imprimirTokens(listaTokens):
    print("["+' '.join(listaTokens[0][0]) + "]")









imprimirTokens(obtenerCodigo())
