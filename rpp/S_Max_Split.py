def maxSplit(s):
    balancedCount = 0
    subStr = ""
    balancedStr = []
    
    for char in s:
        subStr += char
        if char == 'L':
            balancedCount += 1
        else:
            balancedCount -= 1
        
        if balancedCount == 0:
            balancedStr.append(subStr)
            subStr = ""

    print(len(balancedStr))
    for Str in balancedStr:
        print(Str)

s = input()
maxSplit(s)

