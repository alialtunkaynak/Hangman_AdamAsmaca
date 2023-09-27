import random
from words import word_list

##################################
#mehmetalialtunkaynak
#https://github.com/alialtunkaynak
##################################



def get_word():
    word = random.choice(word_list)
    word_length = len(word)
    
    # Kelimenin harf sayısının 3'te 1'i kadar rastgele harf seçimi
    num_letters_to_replace = word_length // 3
    
    # Eğer harf sayısı 3'e bölünmüyorsa, 3'te 1'in bir eksiği kadar harf seçimi
    if word_length % 3 != 0:
        num_letters_to_replace -= 1
    
    if num_letters_to_replace <= 0:
        num_letters_to_replace = 1  # En az 1 harf ipucu olsun
    
    chosen_indices = random.sample(range(word_length), num_letters_to_replace)
    
    # Kelimenin alt tirelerle başlatılması ve rastgele harf eklenmesi
    word_completion = ["_"] * word_length
    
    # Seçilen rastgele harf indekslerine harfleri yerleştir
    for index in chosen_indices:
        word_completion[index] = word[index]
    
    word_hint = "".join(word_completion)  # Kelimenin alt tireleri ve rastgele harfleri içeren ipucu
    return word.upper(), word_hint





def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



def play(word, hint):
    word_length = len(word)
    word_completion = list(hint)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Haydi Seninle Birlikte Hangman Oynayalım!\n")
    print(display_hangman(tries))
    print("".join(word_completion))  # Kelimenin alt tireleri ve rastgele harfleri içeren ipucu

    while not guessed and tries > 0:
        guess = input("Lütfen bir cümle veya harf giriniz: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Bunu Zaten Denedin Dostum", guess)
            elif guess not in word:
                print(guess, "Maalesef Yanlış Tahmin.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "Eveet doğru bir tahmin !")
                guessed_letters.append(guess)
                for i in range(word_length):
                    if word[i] == guess:
                        word_completion[i] = guess
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == word_length and guess.isalpha():
            if guess in guessed_words:
                print("Bu kelimeyi zaten tahmin ettiniz", guess)
            elif guess != word:
                print(guess, "Nınını Bu Kelime Değil.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = list(word)
        else:
            print("Üzgünüm ama geçerli bir tahmin değil.")
        
        print(display_hangman(tries))
        print("".join(word_completion))
        print("\n")

    if guessed:
        print("Tebrikler, kelimeyi tahmin ettiniz! Sen kazandın!")
    else:
        print("Üzgünüm, deneme süreniz bitti. Kelime ise şuydu :" + word + ". Belki bi dahaki sefere!")

def main():
    word, hint = get_word()
    play(word, hint)
    while input("Tekrar Oynasak mı? (Y/N) ").upper() == "Y":
        word, hint = get_word()
        play(word, hint)

if __name__ == "__main__":
    main()



