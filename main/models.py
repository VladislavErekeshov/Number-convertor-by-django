from django.db import models
from django.forms.fields import CharField, IntegerField

# Create your models here.
class Convertor(models.Model):
    number = models.CharField(max_length=200)
    b = models.CharField(max_length=10)
    c = models.CharField(max_length=10)
    d = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
        'G':16,
        'H':17,
        'I':18,
        'J':19,
        'K':20,
        'L':21,
        'M':22,
        'N':23,
        'O':24,
        'P':25,
        'Q':26,
        'R':27,
        'S':28,
        'T':29,
        'U':30,
        'V':31,
        'W':32,
        'X':33,
        'Y':34,
        'Z':35
    }

    @staticmethod
    def from_n_to_10(number, b, d):
        number = number.upper()
        number = [number[x:x+1] for x in range(0, len(number), 1)]
        l = []
        ind = []
        ans = 0
        for i in number:
            n = d.get(i)
            l.append(n)
    
        for el in range(0, len(l)):
            ind.append(el)
        ind.reverse()
    
        for i in l:
            s = ind[0]
            ans = ans + i * b ** s 
            ind.remove(s)
        return ans

    @staticmethod
    def from_10_to_n(number, c, d):
        o = list(d.keys())
        l = []
        while number > 0:
            i = number % c
            number = number // c
            h = o[i]
            l.append(h)
        l.reverse()
        l = [str(i) for i in l]
        l = ''.join(l)
        return l

    @staticmethod
    def if_a_bigger_b(number, b, d):
        number = number.upper()
        number = [number[x:x+1] for x in range(0, len(number), 1)]
        l = []
        for i in number:
            n = d.get(i)
            l.append(n)
        for i in l:
            if i > b - 1:
                number = 1
                break
            else:
                number = 0
        return number

    @staticmethod
    def abcerror(number, arr1):
        lg = 0
        for i in arr1:
            for l in number:
                if i == l:
                    lg = lg + 1
        if lg < len(number):
            return 1
        else:
            return 0

    @staticmethod
    def bc(b):
        if b < 2:
            return 1
        else:
            return 0

    
    def main(self):
        arr1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        arr2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
        if self.abcerror(self.number, arr1) == 1:
            res = "Используй только арабские цифры и латиницу"
        
        elif self.abcerror(self.b, arr2) == 1:
            res = "Система может быть только числом от 2 до 36"
            
        elif self.abcerror(self.c, arr2) == 1:
            res = "Система может быть только числом от 2 до 36"
                
        elif self.bc(int(self.b)) == 1:
            res = 'Ошибка системы исчисления (система не может быть меньше 2)'
            
        elif self.bc(int(self.c)) == 1:
            res = 'Ошибка системы исчисления (система не может быть меньше 2)'
                        
        elif self.if_a_bigger_b(self.number, int(self.b), self.d) == 1:
            res = 'Ошибка системы исчисления'
                            
        elif self.number == '0':
            res = self.number
        else:
            ans = self.from_n_to_10(self.number, int(self.b), self.d)
            ans1 = self.from_10_to_n(ans, int(self.c), self.d)
            res = str(ans1)
        return res

    def __str__(self):
        return self.main()