from sys import argv as CommandLineArguments

if (len(CommandLineArguments) < 4) or (len(CommandLineArguments) > 4):
    print("Error. The Correct Syntax Is <Operrator> <FirstInteger> <SecondInteger>\n")
    print("You Can Assign The Following Arguments To The <Operator>")
    print("Addition, Subtraction, Multiplication, Division")

    exit()

Operator = str(CommandLineArguments[1])

try:
    FirstInteger = float(CommandLineArguments[2])
except:
    print("Error. FirstInteger Not Valid. Please Enter An Integer Without Alphabetic Characters")

    exit()

try:
    SecondInteger = float(CommandLineArguments[3])
except:
    print("Error. SecondInteger Not Valid. Please Enter An Integer Without Alphabetic Characters")

    exit()


match Operator.lower():
    case "addition":
        print(f"Addition Answer Is : {FirstInteger + SecondInteger}")

    case "subtraction":
        print(f"Subtraction Answer Is : {FirstInteger - SecondInteger}")

    case "multiplication":
        print(f"Multiplication Answer Is : {FirstInteger * SecondInteger}")

    case "division":
        if SecondInteger != 0:
            print(f"Division Answer Is : {FirstInteger / SecondInteger}")
        else:
            print("Error : Sorry. I Can Not Divide An Integer To Zero")

    case _:
        print("Error : Sorry. Your Operator Not Valid")