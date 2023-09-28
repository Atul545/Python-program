#First Program

st="This is a  car"
doublespaces=st.find("  ")#find double space
print(doublespaces)
repl=st.replace("  "," ")#replace double spce to single space
print(repl)

#Second Program(Escape sequence)
letter="Dear Ram, I hove you are good!"
print(letter)
formatletter="Dear Ram,\n \tI hove you are good!"
print(formatletter)