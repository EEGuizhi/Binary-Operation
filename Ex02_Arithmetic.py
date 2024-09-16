# BSChen (Guizhi)
"""
This is a simple example code of using `binary_operation.py` tool.
"""
from binary_operation import *

if __name__ == "__main__":
    # Settings
    var1 = binary(10, width=5, signed=True, prefix=True)
    var2 = binary(8, width=8, signed=False, prefix=True)
    print(f"var1 = {var1} (decimal: {var1.dec})")  # var1 = 5'b0_1010 (decimal: 10)
    print(f"var2 = {var2} (decimal: {var2.dec})")  # var2 = 8'b0000_1000 (decimal: 8)

    print("==================================================")

    # Addition
    print(f"var1 + var2 = {var1 + var2}")  # 5'b1_0010
    print(f"var2 + var1 = {var2 + var1}")  # 8'b0001_0010

    # Substraction
    print(f"var1 - var2 = {var1 - var2}")  # 5'b1_0010
    print(f"var2 - var1 = {var2 - var1}")  # 8'b0001_0010

    print("==================================================")

    # Multiplication
    var3 = binary(mult(var1.bin, var2.bin, 7), prefix=True)
    print(f"var1 * var2 = {var3} (decimal: {var3.dec})")  # 7'b101_0000 (decimal: 80)

    # Division
    var3 = binary(div(var1.bin, var2.bin, 7)[0], prefix=True)
    print(f"var1 / var2 = {var3} (decimal: {var3.dec})")  # 7'b000_0001 (decimal: 1)
