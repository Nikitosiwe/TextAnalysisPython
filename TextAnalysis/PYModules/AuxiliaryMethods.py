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