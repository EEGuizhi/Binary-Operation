<!-- BSChen (Guizhi) -->
# Binary Operation Tool User Guide
This is a simple tool for doing binary operations in Python,
binary number variables are implemented with 1-dim integer numpy array. </br>
\- *developed by B.S.Chen (Guizhi)*


## Introduction
The main purpose of this tool is to help users simulate, generate,
and better understand the data flow and relationships between variables
when writing **Verilog** code.


## Outline
- [Declaration](#declaration)
- [Operating values in decimal](#operating-values-in-decimal)
- [Operating values in binary](#operating-values-in-binary)
- [Printing](#printing)
- [Arithmetic operations](#arithmetic-operations)
- [Logic operations](#logic-operations)
- [Truncating & Getting single bit value](#truncating--getting-single-bit-value)
- [Concatenation](#concatenation)


## Declaration
- **Code** :
    - Simple :
        ```py
        var = binary(<value>, <width>)
        ```
    - Detailed :
        ```py
        var = binary(<value>, <width>, <fixed_point>, <signed>, <prefix>)
        ```
    
- **Parameters** :
    - `value` : The value of the variable, type can be `binary`, `float`, `int`, `numpy.ndarray`, or `str`(hexadecimal).
    - `width` : The bits width of the variable.
    - `fixed_point` : The index of $2^0$ digit in binary format.
    - `signed` : `True` for signed variable, `False` for unsigned variable (value cannot be negative).
    - `prefix` : Showing width & radix info prefix in front of the variable while getting the string format of it.
- **Return** :</br>
    An object of `binary`


## Operating values in decimal
- **Code** :
    - Setting value :
        ```py
        var.dec = <deciaml value>  # can be `int` or `float`
        ```
    - Reading value :
        ```py
        value = var.dec
        ```
- **Notes** : </br>
    If the variable doesn't have enough **bit width** to represent the decimal value,
    it can still be converted to a binary number, but it will not be the same as the original value. (Please see `def dec2bin()`)


## Operating values in binary
- **Code** :
    - Setting value :
        ```py
        var.bin = <value>  # must be `numpy.ndarray`
        ```
    - Reading value :
        ```py
        value = var.bin  # value will be 1-dim `numpy.ndarray`
        ```
    - Example :
        ```py
        var2.bin = var1.bin
        var3.bin = var1.bin[0:3]  # slicing (truncating), same as var1[2:0] in Verilog
        ```
- **Notes** : </br>
    If the variable doesn't have enough **bit width** to represent the decimal value,
    it can still be converted to a binary number, but it will not be the same as the original value. (Please see `def dec2bin()`)



## Printing
- **Code** :
    - Print in binary :
        ```py
        print(var)
        ```
    - Print in decimal :
        ```py
        print(var.dec)
        ```
    - Print in hexadecimal :
        ```py
        print(var.hex)
        ```


## Arithmetic operations
- **Code** :
    - Basic functions :
        - add :
            ```py
            array = add(<value1>, <value2>, <width>)
            # Note : Setting <width> to `None` will take larger width of values as default
            ```
        - subtraction :
            ```py
            array = sub(<value1>, <value2>, <width>)
            # Note : Equivalent to add <value1> with negative <value2>
            ```
        - negative :
            ```py
            array = neg(<value>)
            ```
        - round :
            ```py
            array = rnd(<value>, <width>)
            ```
        - multiplication :
            ```py
            array = mult(<value1>, <value2>, <width>)
            ```
        - division :
            ```py
            array_q, array_r = div(<value1>, <value2>, <width>)  # Getting quotient, remainder
            ```
        - Parametes :
            The `<value>` parameters of the function must be (binary) `numpy.ndarray`, not `binary`,
            return is the same.
    - Operators :
        - Addition`(+)` :
            ```py
            result = num1 + num2 
            # Note : The settings (width, signed) will depends on `num1`
            ```
        - Subtraction`(-)` :
            ```py
            result = num1 - num2
            # Note : The settings (width, signed) will depends on `num1`
            ```
- **Notes** : </br>
    This tool has overloaded the addition`(+)` and subtraction`(-)` operators,
    please note that the settings (width, signed, prefix) when doing operation depends on the **first** binary variable. (Please see `def __add__()` and `def __sub__()`)


## Logic operations



## Truncating & Getting single bit value



## Concatenation


