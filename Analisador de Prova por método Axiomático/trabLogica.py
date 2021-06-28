# -*- coding: utf-8 -*-


# Siglas
sigla1 = "A1"
sigla2 = "A2"
sigla3 = "A3"
sigla4 = "A4"
sigla5 = "A5"
sigla6 = "A6"
sigla7 = "A7"
sigla8 = "A8"
sigla9 = "A9"
sigla10 = "A10"

# Axiomas
A1 = "(p>(q>p))"
A2 = "(p>(q>r))>((p>q)>(p>r))"
A3 = "p>(q>(p∧q))"
A4 = "(p∧q)>p"
A5 = "(p∧q)>q"
A6 = "p>(p∨q)"
A7 = "q>(p∨q)"
A8 = "(p>r)>((q>r)>((p∨q)>r))"
A9 = "(p>q)>((p>~q)>~p)"
A10 = "~~p>p"

def compara_str(a,b):
    i = 0
    while i < len(a):
        if(a[i] != b[i]):
            return False
        i+=1
    return True


def comparar_string(string1, string2):
    for i in range(0, len(string2)):
        print(string1)
        print(string2)
        print(i)
        print(len(string2[i:(i + len(string1))]), len(string1))
        print("")

        aux_string2 = string2[i:len(string1)]
        if(compara_str(string1, aux_string2)):
            return True
        if((i+len(string1) == len(string2))):
            return False
    return False


testando = "gostaria que acertace A1 porfavor"

if(comparar_string(sigla1, testando)):
    print("deu bom")
else:
    print("deu ruim")
