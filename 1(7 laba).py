while True:
    while True:
        text = input('Введіть текст:')
        golosni = 0
        prugolosni = 0

        vowel = set('aeiouy')
        consonant = set('bcdfghjklmnpqrstvwxz')
        letter = set('aeiouybcdfghjklmnpqrstvwxz1234567890')

        for i in text:
            if i in letter:
                pass
            else:
                print('Текст може містити лише малі латинські літери та цифри')
                print()
                break

        if (text[-1] != '.'):
            print('В кінці тексту має бути крапка')
            print()
            continue

        for i in text:
            if (i in vowel):
                golosni += 1
            elif (i in consonant):
                prugolosni += 1
            else:
                pass

        print('golosni:', golosni)
        print('prugolosni:', prugolosni)

        if golosni > prugolosni:
            print('Голосних більше ніж приголосних')
        elif prugolosni > golosni:
            print('Приголосних більше ніж голосних')
