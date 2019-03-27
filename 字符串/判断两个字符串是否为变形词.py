

def isDeformation1(str1, str2):
    if str1 ==  None or str2 == None or len(str1) != len(str2):
        return False
    array = [0 for i in range(256)]
    for i in range(len(str1)):
        array[ord(str1[i])] += 1
    for i in range(len(str2)):
        array[ord(str2[i])] -= 1
        if array[ord(str2[i])] < 0:
            return False
    return True
