import itertools

enterWord = ""
while(len(enterWord) != 7):
    enterWord = input('wprowadz 7 znakow : ')

# lista slow z permutacji
permWords = []
p = itertools.permutations(enterWord)
pl = list(p)
for i in pl:
    permWords.append(''.join(i))

# lista slow istniejacych - pobrac z pliku
fileWords = []
with open('7literowkiSort.txt') as file:
    fileWords = file.readlines()

# porownanie 1 z 2 i wylowienie sensownych
meaningWords = []
for word in permWords:
    if word + '\n' in fileWords: meaningWords.append(word)

# przy pomocy f. czy lista zawiera element - wczesniejsze sortowanie niepotrzebne
uniqueWords = set(meaningWords)

print(uniqueWords)





