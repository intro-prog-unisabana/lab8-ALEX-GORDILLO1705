import sys

def main():
    if len(sys.argv) != 4:
        print("Invalid usage, should be:")
        print("python3 calculator.py <number 1> <operator> <number two>")
        return
    num1_str = sys.argv[1]
    operator = sys.argv[2]
    num2_str = sys.argv[3]

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Error: numero invalido!")
        return
    
    if operator not in ["+", "-", "*", "/"]:
        print("Error: Operador invalido. Use +, -, *, /.")
        return 
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: no se puede dividir por cero.")
            return
        result = num1 / num2   

    if result.is_integer():
        result = int(result)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    