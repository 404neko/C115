import random

Table=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 48, 49 ]
'''
def Gen(Num):
    array=['' for GenArray in range(Num)]
    print array
    #random.uniform(
    i=int(random.uniform(0,10))%10
    j=0
    k=0
    while k<Num%5:
        i4=j+1
        array[j]=List[i&int('3f',16)]
        i=i>>6
        k+=1
        j=i4
    m=0
    while m<(Num/5):
        n=int(random.uniform(0,10))%10
        i1=0
        while i1<5:
            i2=j+1
            array[j]=List[n&int('3F',16)]
            i3=n>>6
            i1+=1
            n=i3
            j=i2
        m+=1
    sdf=''
    print array
    for aChar in array:
        print type(aChar)
        sdf+=chr(aChar)
    print sdf
'''
def GenExt(Length):
    ReturnArray=''
    for i in range(0,Length):
        aChar=Table[int(random.uniform(0,len(Table)))]
        ReturnArray+=chr(aChar)
    return ReturnArray
