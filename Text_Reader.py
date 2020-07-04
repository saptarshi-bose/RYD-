import PyPDF2
import re
import json
q=[]
opt1,opt2,opt3,opt4=[],[],[],[]
ans=[]
class test:
    def con(self):
          
        fileName = open('Test.pdf','rb')
        pdfr = PyPDF2.PdfFileReader(fileName)
        c = "Aakash Educational Services Pvt. Ltd. - Regd. Office : Aakash Tower, 8, Pusa Road, New Delhi-110005 Ph.011-47623456"
        len1 = len(c)
        d = "The Living World"
        len2 = len(d)
        for i in range(0,pdfr.numPages):
            p = 0
            page = pdfr.getPage(i)
            pagecontent =  page.extractText()
            while(p<len(pagecontent)):
                if(pagecontent[p] == " "):
                    print(" ",end = '')
                    p+=1
                elif(pagecontent[p:p+2].isnumeric()):
                    p=p+2
  
                elif(pagecontent[p:p+6] != "Aakash"):
                    if(pagecontent[p:p+10] == "The Living"):
                        p=p+9
                    if(pagecontent[p] == '('):
                        print("\n(",end='')
                    elif(pagecontent[p].isnumeric() and pagecontent[p-1]!='('):
                        print("\n",end='')
                        print(pagecontent[p],end='')
                    else:
                        print(pagecontent[p],end='')
                    p+=1
                elif(pagecontent[p:p+2].isnumeric()):
                    p+=1
                else:
                    p=p+len1
                if "[" in j:
                        start=j.index("[")
                        end=j.index("]")+1
                        temp=j[start:end]
                        j=j.replace(temp,"")
                if "(1)" or "(2)" or "(3)" or "(4)" in j:
                        if "(1)" in j and "Sol.Answer" not in j:
                            start=j.index("1")
                            end=0
                        if "(2)" in j:
                            end=j.index("2")-1
                        else:
                            end=len(j)
                        opt1=j[start:end]
                        if len(opt1)>2 and j[start+1]==")":
                            option1.append(opt1)
                        if "(2)" in j and "Sol.Answer" not in j:
                            start=j.index("2")
                            end=0
                            if "(3)" in j:
                                end=j.index("3")-1
                            else:
                                end=len(j)
                            opt2=j[start:end]
                            if len(opt2)>2 and j[start+1]==")":
                                option2.append(opt2)
                        if "(3)" in j and "Sol.Answer" not in j:
                            start=j.index("3")
                            end=0
                            if "(4)" in j:
                                end=j.index("4")-1
                            else:
                                end=len(j)
                            opt3=j[start:end]
                            if len(opt3)>2 and j[start+1]==")":
                                option3.append(opt3)
                        if "(4)" in j:
                            start=j.index("4")
                            end=0
                            if "Sol.Answer" in j:
                                end=j.index(".")-3
                            else:
                                end=len(j)
                            opt4=j[start:end]
                            if len(opt3)>2 and j[start+1]==")":
                                option3.append(opt4)
                if len(j)>1:
                    temp=re.findall("[123456789]",j)
                    for y in temp:
                        try:
                            if j[j.index(y)+1]=="." or j[j.index(y)+2]==".":
                                q.append(j[j.index(y):])
                                break
                        except:
                            pass   
        
            
    
if __name__=="__main__":
    st1=test()
    st1.con()
    file1=open("questions.txt","a")
    file1.write("\n".join(q))
    file1.close()
    file1=open("answers.txt","a")
    file1.write("\n".join(ans))
    file1.close()
    file1=open("c1.txt","a")
    file1.write("\n".join(opt1))
    file1.close()
    file1=open("c2.txt","a")
    file1.write("\n".join(opt2))
    file1.close()
    file1=open("c3.txt","a")
    file1.write("\n".join(opt3))
    file1.close()
    file1=open("c4.txt","a")
    file1.write("\n".join(opt4))
    file1.close()
    file7=open("final.json","a")
    for i in questions:
        for j in i:
            for k in range(len(j)):
                while(j[k]!="\n"):
                    file7.write(j[k])
                    break
        break
        for i in opt1:
            for j in i:
                for k in range(len(j)):
                    while(j[k]!="\n"):
                        file7.write(j[k])
                        break
            file7.write("\n")
            #break
            for i in opt2:
                for j in i:
                    for k in range(len(j)):
                        while(j[k]!="\n"):
                            file7.write(j[k])
                            break
                file7.write("\n")
                #break
                for i in opt3:
                    for j in i:
                        for k in range(len(j)):
                            while(j[k]!="\n"):
                                file7.write(j[k])
                                break
                    file7.write("\n")
                    #break
                    for i in opt4:
                        for j in i:
                            for k in range(len(j)):
                                while(j[k]!="\n"):
                                    file7.write(j[k])
                                    break
                        file7.write("\n")
                        #break
                        for i in ans:
                            file7.write("\n"+"Answers : ")
                            for j in i:
                                for k in range(len(j)):
                                    while(j[k]!="\n"):
                                        file7.write(j[k])
                                        break
                            file7.write("\n")
                            break
