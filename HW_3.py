# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:48:15 2022

@author: shir_al
"""
#   A
n=input('Write the desirable line of the text :')
filename=input('Wrire your file name:')
file='C:/temp/'+filename

def readline(n,file):
    try:
        n=int(n)
        try:
            fhand=open(file)
            lines=fhand.readlines()
            try:
                return('" '+str(lines[n-1].rstrip())+'".')
            except:
                return('"'+"line "+ str(n) +" doesn't exist"+'"')
        except:
            return('"'+"file not found"+'"')
    except:
        return('"'+"invalid input detected"+'"')

print(readline(n,file))

#  B
# ex3_text.txt
filename=input('Wrire your file name:')
file='C:/temp/'+filename
def longest_words(file):
    sortedwords=[]
    try:
        fhand=open(file)  
        data=fhand.read()
        data=data.replace('  ', ' ')
        data=data.replace('-', '')
        data=data.replace('.', ' ')
        data=data.replace(',', ' ')
        data=data.replace('(', ' ')
        data=data.replace(')', ' ')       
        words1=data.split()
        sortedwords=sorted(words1,key=len,reverse=True)
                                                                      
        return(sortedwords[:5])
       
    except:
         print('"'+"file not found"+'"')
         return(sortedwords)
      
    
print(longest_words(file))
    
    
    