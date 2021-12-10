#THIS PROGRAM IS TO COUNT LETTERS IN A WORD
text = input()
dict = {}
value = 1
for i in range(len(text)):
    x = text[i]
    if x in dict:
        dict[x] = dict.get(x)+1
    else:
        dict[x]=value
print(dict)