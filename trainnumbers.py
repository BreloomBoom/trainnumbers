from itertools import product

def finder(operations, no, formats):
    for h, i, j, k in product(formats,operations,operations,operations):
        try:
            equation = h[0] + no[0] + h[1] + i + h[2] + no[1] + h[3] + j + h[4] + no[2] + h[5] + k + h[6] + no[3] + h[7]
            if eval(equation) == 10:
                print(equation)
        except:
            pass

def main():
    operations = ["+","-","*","/"]
    formats = [
        ["", "", "", "", "", "", "", ""],
        ["", "", "(", "", "", ")", "", ""],
        ["(", "", "", ")", "(", "", "", ")"],
        ["", "", "", "", "(", "", "", ")"],
        ["(", "", "", ")", "", "", "", ""],
        ["(", "", "", "", "", ")", "", ""],
        ["", "", "(", "", "", "", "", ")"]
    ]
    no = input("What is your train number? ")
    finder(operations, no, formats)

if __name__ == "__main__":
    main()