# para (inteiro i = 0; i < 10; i + 1) {
#   bloco...
# }

# for variavel in  ("A", "B")
for i in range(1 , 20, 3): # (0, 1, 2, 3, ..., 9)
# for i in range(20, 1, -2): # (0, 1, 2, 3, ..., 9)
    print(i)

print("Fim do programa.")

print("Break\n")
# pare
# break - interrompe o laço
for i in range(10): # 7
    if i == 8: break
    print(i)

print("Continue\n")
# continue
# continue - interrompe o iteração
for i in range(10): # 9
    if i == 8: continue
    print(i)

