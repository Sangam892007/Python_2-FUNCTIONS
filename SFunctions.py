f = open("Intro")
a = (f.readlines())
#print(a[1])
#for i in a:
    #print(i)
Intro = "ReadME file,HELLO WORLD"
Words = Intro.split("e")
print(Words)

#print(f)

def FirstFunc(Author):
    print("This is the first UserDefine Function ",Author)

FirstFunc("Sangam")