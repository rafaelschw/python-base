"""
Repete vogai

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma
das palavras com suas vogais duplicadas.

ex.:
python repete_vogal.py
'Digite uma palavra (ou enter para sair): ' Python
'Digite uma palavra (ou enter para sair): ' Rafael
'Digite uma palavra (ou enter para sair): ' <enter:
Pythoon
Raafaaeel
"""
words = []

while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word: # Condição de parada
        break

    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiouâêãó":
            final_word += letter * 2
        else:
            final_word += letter
        
        # If Ternário:
        # final_word += letter * 2 if letter.lower() in "aeiouâêãó" else letter)

    words.append(final_word) 

print(*words, sep="\n")
# for word in words:
#     print(word)