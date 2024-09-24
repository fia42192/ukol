text = input(str("Zadej text: "))


with open ("txt.txt", "a") as f:
    f.write(text + " ")





with open ("txt.txt", "r") as f:
    pocet_znaku = f.read()
    pocet_slov_2 = pocet_znaku.split(" ")
    pocet_slov = 0
    for i in pocet_slov_2:
        pocet_slov += 1

# pocet_slov = pocet_znaku.count(" ")
# pocet_slov = pocet_znaku.split()
# pocet_slov_2 = pocet_znaku.split(" ")
pocet_radku = pocet_znaku.count("\n")

# for i in pocet_slov_2:
#     pocet_slov = 0
#     pocet_slov += 1

print(pocet_znaku)
print("Počet znaků: ", len(pocet_znaku))
print("Počet slov: ", pocet_slov)

print("Počet řádků: ", pocet_radku + 1)


