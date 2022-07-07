def num2words(num): 
	Units = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'] 

	Multi_10 = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']

	# dictionary to help determine where to place number suffix

	Expo_100 = {100: 'Hundred',1000:'Thousand', 1000000:'Million', 1000000000:'Billion', 1000000000000:'Tillion'} 
	# checking whether user input is in units, Multi_10 lists or above 100 dictionary
	if num < 20: 
		return Units[num] 
	
	if num < 100: 
		return Multi_10[(int)(num/10)-2] + ('' if num%10==0 else ' ' + Units[num%10])

	# looping through dictionary keys to find the highest instance if the key is < or = to the num variable
	break_point = max([key for key in Expo_100.keys() if key <= num]) 

	return num2words((int)(num/break_point)) + ' ' + Expo_100[break_point] + ('' if num%break_point==0 else ' ' + num2words(num%break_point))

    # print the result
print(num2words(int(input("Enter a number: "))))

