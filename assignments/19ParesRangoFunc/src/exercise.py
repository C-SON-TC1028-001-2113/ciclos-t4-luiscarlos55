
def main():
    num1 = int(input('Valor 1: ')) 
    num2 = int(input('Valor 2: '))
    if num1>0 and num2>0 :
        if num1!=num2:
            if num1>num2:
                for i in range(num2, num1+1):
                    if i%2==0 :
                        print(i)
            elif num2>num1 :
                for i in range(num1, num2+1):
                    if i%2==0 :
                        print(i)
        else:
            print('No hay pares')

if __name__=='__main__':
    main()
