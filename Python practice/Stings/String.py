#1.create 3 variables to store street, city and country. now create address variable to store entire address using two methods one by using "+"and other by f-string.
street = "Thotavari Street" 
city = "Vijayawada"
country = "INDIA"
#creating address using + operator
address = street + '\n' + city+ '\n' + country
print("Address using '+' operator is ",address)
#2. create a variable to store "Earth revolves around the sun"
s="Earth revolves around the sun"
#2.a. print "revolves" using slice operator
print('print "revolves" using slice operator:',s[6:14])
#2.b. Print 'sun' using slice operator
print ("Print 'sun' using slice operator:", s[-3:])
#3. create 2 variables to store how many fruits and vegitables you eat a day. Now print "I eat x veggies and y fruits daily" where x and y are vegitables and fruits you eat daily
x=4
y=1
print(f'I eat {x} veggies and {y} fruits daily')
#4. Create a string and replace its words later
#4.1. print using 2 lines
s= 'maine 200 banana khaye'
s= s.replace('banana','samosa')
s=s.replace('200','4')
print('Using two lines: ',s)
#4.2. print using one line
s= "maine 200 banana khaye"
s=s.replace('banana','samosa').replace('200','4')
print('using one line: ',s)