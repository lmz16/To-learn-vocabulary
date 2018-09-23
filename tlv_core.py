import random

def wordWrap(string,rowWidth):
    width=0
    flag=[]
    wrapedstr=''
    for count in list(range(0,len(string))):
        width+=judgeCharType(string[count])
        if(width>=rowWidth):
            width=0
            flag.append(count)
    if(len(flag)==0):
        flag.append(len(string))
    if(flag[-1]!=len(string)):
        flag.append(len(string))
    p1=0
    for p2 in flag:
        wrapedstr=wrapedstr+str(string[p1:p2])+'\n'
        p1=p2
    return wrapedstr

def judgeCharType(char):
    if ((char=='，')|((char>'\u4e00') & (char<'\u9fff'))):
        return 2
    elif (char==' '):
        return 0.6667
    else:
        return 1

def wordGrouping(dic,questionNum):
    en=list(dic)
    en=random.sample(en,4*questionNum)
    random.shuffle(en)
    group=[]
    for count in list(range(0,questionNum)):
        temp=[en[count*4],en[count*4+1],en[count*4+2],en[count*4+3]]
        group.append(temp)
    return group

def AnswerButtonSlot(Ab,mark,Pb):
    if(Ab.answer==mark):
        Pb.label.setText(wordWrap('答对了，'+str(Ab.wordGroup[Ab.count-1][Ab.answer])+ \
        '的汉语意思是'+chList2str(Ab.tempdic[Ab.wordGroup[Ab.count-1][Ab.answer]]),43))
    else:
        Pb.label.setText(wordWrap('答错了，'+chList2str(Ab.tempdic[Ab.wordGroup[Ab.count-1][mark]]) \
        +'对应的英文单词是'+str(Ab.wordGroup[Ab.count-1][mark]),43))
    Pb.show()
    if(Ab.count<Ab.questionNum):
        Ab.changeContent1()
    else:
        Ab.close()
        Ab.count=0

def chList2str(chlist):
    chstr=' '
    for ch in chlist:
        chstr=chstr+str(ch)
    return chstr+' '
