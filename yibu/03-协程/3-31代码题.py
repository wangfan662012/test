# coding = utf-8

text = "this is a test of the emergency text system"
f = open("demo.txt", "w")
f.write(text)
f.close()
f1 = open("demo.txt", "r")
new_text = f1.read()
list1 = new_text.split()
for i in  range(len(list1)):
    if i%2 != 0:
        list1[i] = list1[i].upper()
for i in range(len(list1)):
    if i < len(list1):
        list1[i] = list1[i] + " "
mytext = ""
for i in  range(len(list1)):
    mytext += list1[i]
print(mytext)
a = mytext.replace(' ' , '')
print(a)
mydict = {}
for i in set(a):
    if a.count(i) >= 1:
        # print('%s 出现了%d 次!'%(i, a.count(i)))
        mydict[i] = a.count(i)
print(mydict)
b = []
for key in mydict:
    b.append(key*mydict[key])
print(b)
mydict_text = ""
for i in  range(len(b)):
    mydict_text += b[i]
print(mydict_text)
