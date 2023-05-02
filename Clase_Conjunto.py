class Conjunto:
    __lista: list
    
    def __init__(self,lista) -> None:
        self.__lista = lista
        pass

    def __add__(self,otro):
        result = []
        for i in self.__lista:
            result.append(i)
        i = 0
        while i < len(otro.__lista):
            if otro.__lista[i] not in result:
                result.append(otro.__lista[i])
                i+=1
        return Conjunto(result)
    
    def __sub__(self,otro):
        result = []
        i = 0
        while i < len(self.__lista):
            if self.__lista[i] not in otro.__lista:
                result.append(self.__lista[i])
                i+=1
        return Conjunto(result)
    
    def __eq__(self,otro):
        if len(self.__lista) == len(otro.__lista):
            i = 0
            while i < self.__lista:
                if self.__lista[i] not in otro.__lista:
                    a = False
                    i = len(self.__lista)
                elif self.__lista[i] in otro.__lista:
                    i+=1
                    a = True
            if a == True:
                return True
        return False

    def __str__(self) -> str:
            return str(self.__lista)
