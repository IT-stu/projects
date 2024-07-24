class Calculator:
    def add(self,a,b):
        return a+b
    def sud(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "Can't divide by zero."
cal=Calculator()
print("1 to add \n2 to sudrasion \n3 to multipulate \n4 to divided\n5 to exit")
operator = int(input("Enter the Operator == "))

while(operator<=4):
    a=int(input("Enter a First numder "))
    b=int(input("Enter a Second numder "))
    if operator ==1:
        print(f"{a}+{b} = ",cal.add(a,b))
    elif operator ==2:
        print(f"{a}-{b} = ",cal.sud(a,b))
    elif operator ==3:
        print(f"{a}*{b} = ",cal.mul(a,b))
    elif operator ==4:
        print(cal.div(a,b))
    operator = int(input("Enter the Operator "))
    


