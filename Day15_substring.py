def issub(s1,s2):
    size1 = len(s1)
    size2 = len(s2)
    i = 0
    j = 0
    #print("size1 = ", size1, " size2 = ", size2)
    
    while(j<size2):
        #print("i = ", i)
        #print("j = ", j)
        if s1[i] == s2[j]:
            #print("inside if", s1[i], s2[j])
            i = i+1
            j = j+1

        else:
            i = 0
            j = j+1

        if i == size1:
            return True

    return False

if __name__ == "__main__":
    print(issub("lloworldhe","helloworldhelloworld"))