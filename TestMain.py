def sayHello():
    hello = "my name is yangjianzhou"
    print(hello)

def writeFile():
    fileContent = "this is content"
    f = open("python.txt","w")
    f.write(fileContent)
    f.close()

def doLoop():
    programLanguage = ["java","js","go","sql","c","c++","python"]
    index = 0
    for language in programLanguage :
        print(index , " : " , language)
        index = index +1

if __name__ == "__main__":
    sayHello()
    writeFile()
    doLoop()

