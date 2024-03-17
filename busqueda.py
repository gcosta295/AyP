def linear_search(vector,key,keyName=''):
    temp=None
    for element in vector:
        if element.get(keyName) is not None:
            if element[keyName] ==key:
                temp=element
                break
    return temp

class Entero(object):
    def __init__(self,valor):
        self.valor=valor

def get_keyName():
    