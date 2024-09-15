# BSChen (Guizhi)
"""
This is a simple example code of using `binary_operation.py` tool.
"""
from binary_operation import *

if __name__ == "__main__":
    # Basic declaration & printing
    var = binary(10, width=4)
    print(var)  # 1010

    # Operate variable in decimal
    var.dec = 4
    print(var, var.dec)  # 0100 4

    print("==================================================")

    # Detailed declaration (signed & prefix)
    var = binary(10, width=5, signed=True, prefix=True)
    print(var)  # 5'b0_1010

    # Detailed declaration (float number)
    var = binary(0.25, width=4, fixed_point=3)
    print(var, var.dec)  # 0010 0.25

    print("==================================================")

    # Operate variable in binary
    var1 = binary(10, width=5, signed=True, prefix=True)
    var2 = binary(0, width=4, signed=False, prefix=True)
    var2.bin = var1.bin[0:4]  # Same as `var1[3:0]` in Verilog
    print(var2)  # 4'b1010

    # Bitwise concatenation
    tmp = cat([0, 0, var2.bin, 0, 0])  # 00+1010+00
    var2 = binary(tmp, width=tmp.shape[0], prefix=True)
    print(var2)  # 8'b0010_1000

    print("==================================================")

    # Resizing bits width
    var2 = binary_resize(var2, 4)
    print(var2)  # 4'b1000
    var2 = binary_resize(var2, 8)
    print(var2)  # 8'b0000_1000
