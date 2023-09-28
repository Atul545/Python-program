#First Program
a="Good Afternoon,"
b=input ("Enter name\n")
print(a+b)

#2nd program

letter=''' Dear <|Name|> 
you are geneious!
Date: <|Date|>
'''
name=input("Enter name\n")
date=input("Enter Date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>","date")
print(letter)