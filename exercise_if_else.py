#Considering x='Hello Python' and the following if/elif/else code block, analyze the code and the write the result that should return, in between the quotes of the result.
#1
x = "Hello Python"

if x.startswith("H") and len(x) > 12:

	print("'/'.join(x[:7])")

elif x[:-1] == "n" and len(x.split('o')) >= 3:

	for i in x.strip('n'):

	    print(i * 2)

else:

	print((x + ' ') * 3 + "!")

#2
	x = "Hello Python"

if x.startswith("H") and len(x) > 12:

	print("'/'.join(x[:7])")

elif x[-1] == "n" and len(x.split('o')) >= 3:

    print(x.lower()[4:])

else:

	print((x + ' ') * 3 + "!")

#3
x = "Hello Python"

if x.startswith("H") or len(x) &gt; 12:

	print('/'.join(x[:7]))

elif x[-1] == "n" and len(x.split('o')) &gt;= 3:

    print(x.lower()[4:])

else:

	print((x + ' ') * 3 + "!")