def contar_pontos_virgulas(frase):
    """
    Função para contar o número de pontos e vírgulas em uma frase.

    Args:
    - frase (str): A frase a ser analisada.

    Returns:
    - int: O número de pontos e vírgulas na frase.
    """
    # Inicializa o contador
    contador = 0
    
    # Itera sobre cada caractere na frase
    for caractere in frase:
        # Se o caractere for um ponto ou vírgula, incrementa o contador
        if caractere == ';':
            contador += 1
    
    # Retorna o contador
    return contador

# Exemplo de uso
frase = "2023;Norte;1;Rond?nia;RO;11;Porto Velho;1100205;Porto Velho;1101;Porto Velho;110001;Madeira-Guapor?;1101;Porto Velho;11001;110020505;EMEF ENG? WADIH DARWICH ZACARIAS;11001003;3;;1;0;RUA CIDADE;2118;INEP 11001003;TRES MARIAS;76812644;69;993807337;1;00009;08FEB23:00:00:00;20DEC23:00:00:00;1;0;0;0;0;;;;;;;;;;;;;;;;;;;;;;;;;;;;;1;3;;;1;1;0;0;0;0;;0;0;0;1;0;1;0;0;0;1;0;0;0;0;0;1;1;0;1;0;0;0;0;0;0;0;1;1;1;1;1;0;1;1;0;1;1;1;1;0;0;0;0;0;0;1;1;0;1;0;1;1;0;0;0;0;0;0;1;1;1;0;1;1;0;0;0;1;0;0;0;1;0;0;0;0;16;0;16;11;0;0;1;1;1;1;0;0;0;0;1;1;1;1;0;0;1;1;0;0;1;2;0;0;1;0;1;1;0;0;0;3;1;1;3;1;4;0;0;0;0;0;0;0;0;0;0;0;0;1;4;1;3;1;1;1;4;0;0;1;2;0;0;0;0;1;0;0;0;0;0;1;0;0;0;0;0;0;0;0;0;;;;;0;;;;;;;1;0;0;0;0;1;0;0;0;0;1;0;1;0;0;1;1;0;0;1;0;0;0;1;1;0;0;0;0;0;0;0;1;1;0;363;0;0;0;363;363;93;73;65;51;81;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;11;11;0;158;205;0;48;4;309;1;1;0;1;335;26;1;0;363;0;0;0;0;0;5;5;0;0;361;2;0;0;0;0;18;0;0;0;18;18;0;0;0;0;0;0;0;10;10;0;18;0;0;0;18;18;0;0;0;0;0;0;0;8;8;0;18;0;0;0;0;0;0;0;0;0"
numero_pontos_virgulas = contar_pontos_virgulas(frase)
print("Número de pontos e vírgulas na frase:", numero_pontos_virgulas)
