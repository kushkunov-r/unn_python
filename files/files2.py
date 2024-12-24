def longest_words(file):
    with open(file, "r") as text:
        max = 0
        for i in text.read().split():
            if len(i) > max:
                max = len(i)
        print("Слова имеющие максимальную длину (", max, "):")
        text.seek(0)
        for i in text.read().split():
            if len(i) == max:
                print(i)
    
filename = "article.txt"
longest_words(filename)