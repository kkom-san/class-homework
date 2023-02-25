class number:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def plus(self):     
        return f"덧셈의 계산값은{self.number1 + self.number2}입니다."
    def miuns(self):
        return f"뺄셈의 계산값은{self.number1 - self.number2}입니다."
    def multiplication(self):
        return f"곱셈의 계산값은{self.number1 * self.number2}입니다."
    def square(self):
        return f"제곱의 계산값은{self.number1 ** self.number2}입니다."
    def division(self):
        return f"나눗셈의 계산값은{self.number1 / self.number2}입니다."
    def share(self):
        return f"몫은{self.number1 // self.number2}입니다."
    def rest(self):
        return f"나머지는{self.number1 % self.number2}입니다."

def main():
    while True:
        try:
            number1 = int(input("첫번째 숫자를 입력하세요:"))
            number2 = int(input("두번째 숫자를 입력하세요:"))
            calculator = number(number1, number2)
        
            ans = input("+(덧셈), -(뺄셈), *(곱셈), **(제곱), /(나눗셈), //(몫), %(나머지) 계산하고 싶은 연산자를 쓰시오(기호만):")
            
            if ans == "+":
                print(calculator.plus())
                break
                
            if ans == "-":
                print(calculator.miuns())
                break
            
            if ans == "*":
                print(calculator.multiplication())
                break
            
            if ans == "**":
                print(calculator.square())
                break
                
            if ans == "/":
                print(calculator.division())
                break
            
            if ans == "//":
                print(calculator.share())
                break
            
            if ans == "%":
                print(calculator.rest())
                
            else:
                print("다시 입력해주세요.")
        except:
            print("다시 입력해주세요.")
            
            
main()