

def permutation(str,start,end):

    if(start==end):
        for s in str:
            print(s,end='')
        print('')
        return
    for i in range(start,end+1):
        str[start],str[i]=str[i],str[start]
        permutation(str,start+1,end)
        str[start], str[i] = str[i], str[start]


if __name__ == '__main__':


    a=[1,2,3]
    permutation(a,0,len(a)-1)
    #
    # s = "abc"
    # permutation(list(s),0,len(a)-1)


