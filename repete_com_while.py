#!/usr/bin/env python3

# While - Enquanto

n = 0
# while True: # loop infinito, main loop
#     print(n)
#     n += 1

while n < 101: # Condicao de parada
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1 