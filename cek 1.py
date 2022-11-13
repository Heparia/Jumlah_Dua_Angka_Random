import random
s = 0
l = 5
while l > 0 and l <= 5:
    angka_rahasia_1 = random.randint(-20, 20)
    angka_rahasia_2 = random.randint(-20, 20)
    print("What is the result of", angka_rahasia_1, "+", angka_rahasia_2, "?",)
    jawaban = int(input("Jawaban:"))
    if jawaban == angka_rahasia_1 + angka_rahasia_2:
        s += 10
        l = l
        print("Yes, that's right !!! Your score is", s, "(Lives:", l, ")")
    else:
        s -= 2
        l-= 1
        print("No, that's wrong !!! Your score is", s, "Lives:", l, ")")
else:
    print("(GAME OVER)")
