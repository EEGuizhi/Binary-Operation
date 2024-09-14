# BSChen (Guizhi)
"""
This is a simple example code of using `binary_operation.py` tool.
"""
from binary_operation import *

if __name__ == "__main__":
    # Basic declaration & printing
    var = binary(10, width=4)
    print(var)

    # Operate variable in decimal
    var.dec = 4
    print(var, var.dec)

    print("==================================================")

    # Detailed declaration (signed & prefix)
    var = binary(10, width=5, signed=True, prefix=True)
    print(var)

    # Detailed declaration (float number)
    var = binary(0.25, width=4, fixed_point=3)
    print(var, var.dec)

    print("==================================================")

    # Operate variable in binary
    var1 = binary(10, width=5, signed=True, prefix=True)
    var2 = binary(0, width=4, signed=False, prefix=True)
    var2.bin = var1.bin[0:4]  # Same as `var1[3:0]` in Verilog
    print(var2)

    # Addition
    var1 = binary(10, width=5, signed=True, prefix=True)
    var2 = binary( 1, width=5, signed=True, prefix=True)
    var2 = var1 + var2
    print(var2)
