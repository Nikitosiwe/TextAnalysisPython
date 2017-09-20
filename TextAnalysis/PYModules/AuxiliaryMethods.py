import re

#Метод принимает текст (который подлжежит анализу). И проверяет его корректность
#для дальнейшей работы с ним. Например текст не должен состоять из одних пробелов,
#табуляций и абзацев
def checkAnalysisText(text):
    if isinstance(text, str):
        if re.search('\S',text)!=None:
            return True
        else:
            return False
    else:
        print("checkAnalysisText - Это не текст")


#Метод разбивает строку на слова и возвращает список найденых слов
def getWordsFromString(text):
    #result = re.split('[\.|,|-|\s|\(|\)|\{|\}|\]|\]|:|;|\<|\>|\'|\"]+', text)
    result = [x for x in re.split('[\W]+', text) if not re.match('\d+',x)]
    return result


#Метод ищет вхождения слова в строке. return ('Cлово',[позиция в строке 1, позиция в строке 2, ....])
def searchWord(word, s):
    i=0
    lst = []
    while(i!=-1):
        i = s.find(word, i+1)
        if i != -1:
            lst.append(i)
        else:
            continue

    return (word, lst)