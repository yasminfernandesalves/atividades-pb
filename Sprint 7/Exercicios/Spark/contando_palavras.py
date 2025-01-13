# código executado no terminal

text_rdd = sc.textFile("/home/jovyan/README.md")
words_rdd = text_rdd.flatMap(lambda line: line.split(" "))
word_count = words_rdd.countByValue()
for word, count in word_count.items():
    print(f"{word}: {count}")