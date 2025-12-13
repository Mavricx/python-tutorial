# Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#        Dear <|Name|>, 
#        You are selected! 
#        <|Date|> 
#         '''
name=input("Enter your name:")
date=input("Enter date:")
letter=f'''Dear {name},
          you are selected! {date}'''
print(letter)

# or using replace function 
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)