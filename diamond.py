rows = 5
# upper half
for i in range(1, rows + 1):
    print(" "*(rows-i)+"*" +
          ("*"*(2*i-3)+"*"if i > 1
           else ""))
    # lower half
for i in range(rows-1, 0, -1):
    print(" "*(rows-i)+"*" +
          ("*"*(2*i-3)+"*"if i > 1
           else ""))
