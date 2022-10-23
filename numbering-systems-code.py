# ==============================
# Ian Morrison
# cpsc-20000
# Project: Numbering Systems
# ==============================
# ==============================
# Imports
import sys # imports new module
# ==============================
# ============================================
print("\nNumbering Systems Project")
arguments = len(sys.argv)
print("Arguments passed: " + str(arguments))
print("First Argument: " + sys.argv[0])


if arguments == 1:
    print("Argument 2: " + sys.argv[0])
  
    stringNumber = sys.argv[0]
    print(stringNumber)
    intNumber = int(stringNumber)
    hexNumber = hex(intNumber)

    print("Input: " + stringNumber)
    print("Number: " + str(intNumber))
    print("Hex: " + hexNumber)
# ============================================