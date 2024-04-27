# Project: Travel-Converter, Pia Truebenbach A01763478


'''
Description of the program:

The Travel-Cconverter aims to be a useful tool for the conversion of different values and units that are of relevance when traveling through Europe(Germany), Mexiko and the United States of America.
The possibility of expanding the project to include other countries exists too.

A list of the project's functions is shown below. Additional information such as units, input, output and other required information is also displayed.


• Currency Converter (Units: MXN, USD, Euro), (Conversion: Calculation); (Needed Information: Exchange rates); (Input: Initial Currency, final currency, value in initial currency); (Output: Value in final currency)

• Length Converter (Units: Metric, Imperial), (Conversion: Calculation); (Needed Information: Conversion rates); (Input: Initial Unit, final unit, value in initial unit); (Output: Value in final unit)

• Temperature Converter (Units: Celsius, Fahrenheit), (Conversion: Calculation); (Needed Information: Conversion rates); (Input: Initial Unit, final unit, value in initial unit); (Output: Value in final unit)

• Shoesize Converter (Units: EURO, USA, cm),(Conversion: Assignment); (Needed Information: Assignments of values); (Input: Gender, Initial Unit, final unit, value in initial unit); (Output: Value in final unit for certain gender)

• Sizes of Clothes Converter (Units: EURO(Germany), US, Mex, Letters), (Conversion: Assignment); (Needed Information: Assignments of values); (Input: Gender, Initial Unit, final unit, value in initial unit); (Output: Value in final unit for certain gender)
'''

#Functions where the conversion is determined by calculations

#Currency

'''
Input: Initial value (in Mex$)
Output: Final value (in US$)
Process: 1. calculate the final value by using the initial value and the exchange rate
         2. return the final value
'''
def currency_mxn_to_usd(initial_value):
    final_value=initial_value/17.07 #exchange rate
    return final_value


'''
Input: Initial value (in US$)
Output: Final value (in Mex$)
Process: 1. calculate the final value by using the initial value and the exchange rate
         2. return the final value
'''
def currency_usd_to_mxn(initial_value):
    final_value=initial_value*17.07 #exchange rate
    return final_value    


'''
Input: Initial value (in €)
Output: Final value (in US$)
Process: 1. calculate the final value by using the initial value and the exchange rate
         2. return the final value
'''
def currency_euro_to_usd(initial_value):
    final_value=initial_value/0.92 #exchange rate
    return final_value    


'''
Input: Initial value (in US$)
Output: Final value (in €)
Process: 1. calculate the final value by using the initial value and the exchange rate
         2. return the final value
'''
def currency_usd_to_euro(initial_value):
    final_value=initial_value*0.92 #exchange rate
    return final_value    

'''
Input: Initial value (in €)
Output: Final value (in Mex$)
Process: 1. calculate the final value by using the initial value and the exchange rate
         2. return the final value
'''
def currency_euro_to_mxn(initial_value):
    final_value=initial_value/0.054 #exchange rate
    return final_value    

'''
Input: Initial value (in Mex$)
Output: Final value (in €)
Process: 1. calculate the final value by using the initial value and the exchange rate
         2. return the final value
'''
def currency_mxn_to_euro(initial_value):
    final_value=initial_value*0.054 #exchange rate
    return final_value   



#Length

#imperial to metric

'''
Input: Initial value (in in)
Output: Final value (in cm)
Process: 1. calculate the final value by using the initial value and the conversion
         2. return the final value
'''
def in_to_cm(initial_value):
    final_value=initial_value*2.54 #conversion rate
    return final_value 

    
'''
Input: Initial value (in ft)
Output: Final value (in dm)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def ft_to_dm(initial_value):
    final_value=initial_value*30.48 #conversion rate
    return final_value 
    

'''
Input: Initial value (in yd)
Output: Final value (in m)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def yd_to_m(initial_value):
    final_value=initial_value*0.9144 #conversion rate
    return final_value 
    

'''
Input: Initial value (in mi)
Output: Final value (in km)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def mi_to_km(initial_value):
    final_value=initial_value*1.609344 #conversion rate
    return final_value 
    

#metric to imperial

'''
Input: Initial value (in cm)
Output: Final value (in in)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def cm_to_in(initial_value):
    final_value=initial_value/2.54 #conversion rate
    return final_value 


'''
Input: Initial value (in dm)
Output: Final value (in ft)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def dm_to_ft(initial_value):
    final_value=initial_value/30.48 #conversion rate
    return final_value 
    

'''
Input: Initial value (in m)
Output: Final value (in yd)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def m_to_yd(initial_value):
    final_value=initial_value/0.9144 #conversion rate
    return final_value 


'''
Input: Initial value (in km)
Output: Final value (in mi)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def km_to_mi(initial_value):
    final_value=initial_value/1.609344 #conversion rate
    return final_value 
    



#Temperature

'''
Input: Initial value (in °F)
Output: Final value (in °C)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def fahrenheit_to_celsius(initial_value):
    final_value=(initial_value-32)/1.79999999
    return final_value
    

'''
Input: Initial value (in °C)
Output: Final value (in °F)
Process: 1. calculate the final value by using the initial value and the conversion rate
         2. return the final value
'''
def celsius_to_fahrenheit(initial_value):
    final_value=initial_value*1.79999999+32
    return final_value
    


#Functions where the conversion is determined by assignments (Lists need to be used

#ShoeSize
# Source: https://www.zappos.com/c/shoe-size-conversion

'''
Input: Initial unit, Final unit, Initial value
Process: 1. Enter Matrix with the corresponding values ((shoesizeWoman[0] as list for US sizes, shoesizeWoman[1] for European sizes, shoesizeWoman[2] for sizes in cm)
        2. Find (with while loop) the initiate value in the list of the initiate unit
        3. Assign the final value to the value of the element in the list list of the final value, which is in the same column as the initiate value
        4. Return value
Output: Final value
'''


#shoesizeWoman with a file

'''
def shoesizeWoman(initial_unit,final_unit,initial_value):
    
    dataWomanShoesize=open('shoesizesWomen.txt','r')
    dataWoman=datWomanShoesize.readlines()
    active=True
    counter=0
    while active:
        for col in range (len(dataWoman[0])):
            if str(dataWoman[initial_unit-1][col])==initial_value:
                final_value=str(dataWoman[final_unit-1][col])
                active=False
            else:
                counter=counter+1
        if counter==len(dataWoman[0]):
            print('Invalid choice of initial value. Enter again.')
            initial_value=str(input('Initial value: '))
            counter=0
    return final_value
'''


#shoesizeWoman with a matrix

def shoesizeWoman(initial_unit,final_unit,initial_value):
    dataWoman=[(4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12),(35,35,35.5,36,36.5,37,37.5,38,38.5,39,39.5,40,40.5,41,41.5,42,42.5),(20.8,21.3,21.6,22.2,22.5,23,23.5,23.8,24.1,24.6,25.1,25.4,25.9,26.2,26.7,27.1,27.6)]
    active=True
    counter=0
    while active:
        for col in range (len(dataWoman[0])):
            if str(dataWoman[initial_unit-1][col])==initial_value:
                final_value=str(dataWoman[final_unit-1][col])
                active=False
            else:
                counter=counter+1
        if counter==len(dataWoman[0]):
            print('Invalid choice of initial value. Enter again.')
            initial_value=str(input('Initial value: '))
            counter=0
    return final_value


'''
Input: Initial unit, Final unit, Initial value
Process: 1. Enter Matrix with the corresponding values ((shoesizeMan[0] as list for US sizes, shoesizeMan[1] for European sizes, shoesizeMan[2] for sizes in cm)
        2. Find (with while loop) the initiate value in the list of the initiate unit
        3. Assign the final value to the value of the element in the list list of the final value, which is in the same column as the initiate value
        4. Return value
Output: Final value
'''

#shoesizeMan with a file
'''
def shoesizeMan(initial_unit,final_unit,initial_value):
    dataManShoesize=open('shoesizesMen.txt','r')
    dataMan=dataManShoesize.readlines()
    active=True
    counter=0
    while active:
        for col in range (1,len(dataMan[0])):
            if str(dataMan[initial_unit-1][col])==initial_value:
                final_value=str(dataMan[final_unit-1][col])
                active=False
            else:
                counter=counter+1
        if counter==len(dataMan[0])-1:
            print('Invalid choice of initial value. Enter again.')
            initial_value=str(input('Initial value: '))
            counter=0
    return final_value
'''

#shoesizeMan with a matrix
def shoesizeMan(initial_unit,final_unit,initial_value):
    dataMan=[(6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,13,14,15,16),(39,39,40,40.5,41,41.5,42,42.5,43,43.5,44,44.5,45,46,47,48,49),(23.5,24.1,24.4,24.8,25.4,25.7,26,26.7,27,27.3,27.9,28.3,28.6,29.4,30.2,31,31.8)]
    active=True
    counter=0
    while active:
        for col in range (len(dataMan[0])):
            if str(dataMan[initial_unit-1][col])==initial_value:
                final_value=str(dataMan[final_unit-1][col])
                active=False
            else:
                counter=counter+1
        if counter==len(dataMan[0]):
            print('Invalid choice of initial value. Enter again.')
            initial_value=str(input('Initial value: '))
            counter=0
    return final_value

#Sizes of Clothes
#Sources: https://images.app.goo.gl/pw7MShcX7TPwbQgD9; https://images.app.goo.gl/rFsDwKMEkCvppyV27

'''
Input: Initial unit, Final unit, Initial value
Process: 1. Enter Matrix with the corresponding values ((size[0] as list for US sizes, size[1] for European sizes, size[2] for mexican sizes, size[3] for sizes as letters)
        2. Find (with while loop) the initiate value in the list of the initiate unit
        3. Assign the final value to the value of the element in the list list of the final value, which is in the same column as the initiate value
        4. Return value
Output: Final value
'''

#size with a matrix

def size(initial_unit,final_unit,initial_value):
    data=[(2,4,6,8,10,12,14,16,18),(32,34,36,38,40,42,44,46,48),(26,28,30,32,34,36,38,40,42),('XS','S','S','M','M','L','L','XL','XL')]
    active=True
    counter=0
    while active:
        for col in range (len(data[0])):
            if str(data[initial_unit-1][col])==initial_value:
                final_value=str(data[final_unit-1][col])
                active=False
            else:
                counter=counter+1
        if counter==len(data[0]):
            print('Invalid choice of initial value. Enter again.')
            initial_value=str(input('Initial value: '))
            counter=0
    return final_value

#size with a file
'''
def size(initial_unit,final_unit,initial_value):
    #data=[(2,4,6,8,10,12,14,16,18),(32,34,36,38,40,42,44,46,48),(26,28,30,32,34,36,38,40,42),('XS','S','S','M','M','L','L','XL','XL')]
    dataSize=open('size.txt','r')
    data=dataSize.readlines()
    active=True
    counter=0
    while active:
        for col in range (1,len(data[0])):
            if str(data[initial_unit-1][col])==initial_value:
                final_value=str(data[final_unit-1][col])
                active=False
            else:
                counter=counter+1
        if counter==len(data[0]):
            print('Invalid choice of initial value. Enter again.')
            initial_value=str(input('Initial value: '))
            counter=0
    return final_value
'''
#Functions concerning decision making

#menu for currency

def menu():
    print('''
Choose your Converter

For the "Currency Converter" enter 1
For the "Length Converter" enter 2
For the "Temperature Converter" enter 3
For the "Shoesize Converter" enter 4
For the "Converter of Clothes" enter 5
''')

def menu_currency_converter():
    print('''
Choose the currencies you want to convert:

For Euro(€) enter 1
For US-Dollar (US$) enter 2
For Mexican Peso (Mex$) enter 3
''')

#menu for length
    
def menu_length_converter():
    print('''
Choose how you want to convert the systems:

For conversion from the metric to the imperial system enter 1
For conversion from the imperial to the metric system enter 2
''')

def menu_metric_to_imperial():
    print('''
Choose the length units you want to convert:

For the conversion from centimeters to inches enter 1
For the conversion from decimeters to feet enter 2
For the conversion from meters to yards enter 3
For the conversion from kilometers to miles enter 4
''')

def menu_imperial_to_metric():
    print('''
Choose the length units you want to convert:

For the conversion from inches to centimeters enter 1
For the conversion from feet to decimeters enter 2
For the conversion from yards to meters enter 3
For the conversion from miles to kilometers enter 4
''')

#temperature menu

def menu_temperature():
    print('''
Choose the conversion of temperature:

For the conversion form Celsius to Fahrenheit enter 1
For the conversion from Fahrenheit to Celsius enter 2
''')

#shoesize menu
    
def menu_shoesize_gender():
        print('''
Choose the gender for the conversion of shoesize:

For the conversion of women´s shoe size enter 1
For the conversion of men´s shoe size enter 2
''')

def menu_shoesize_converter():
        print('''
Choose the units of the shoesize you want to convert:

For unit "US" enter 1
For unit "Europe" enter 2
For unit "Centimeters" enter 3
''')

#size menu

def menu_size_converter():
        print('''
Choose the units of the size you want to convert:

For unit "US" enter 1
For unit "Europe" enter 2
For unit "Mexiko" enter 3
For unit "Letter" enter 4
''')
#general menu

def choice():
    print('''
How do you want to continue?

To use the choosen converter again enter 1
To go back to the converter menu enter 2
To exit the Travel-Converter enter 3
''')

#main
def main():
    print('''Welcome to the Travel Converter - Your helper for a pleasant journey!''')
    active=True
    while active:
        menu()
        converter=int(input('Your choice of converter: '))
        if converter==1: #currency converter
            currency_active=True
            while currency_active:
                menu_currency_converter()
                initial_currency=int(input('Initial currency: '))
                final_currency=int(input('Final currency: '))
                initial_value=float(input('Initial value: '))
                if initial_currency==1 and final_currency==2:
                    print('The final value is ', f'{currency_euro_to_usd(initial_value):.2f}', 'US$.')
                elif initial_currency==1 and final_currency==3:
                    print('The final value is ', f'{currency_euro_to_mxn(initial_value):.2f}', 'Mex$.')
                elif initial_currency==2 and final_currency==1:
                    print('The final value is ', f'{currency_usd_to_euro(initial_value):.2f}', '€.')
                elif initial_currency==2 and final_currency==3:
                    print('The final value is ', f'{currency_usd_to_mxn(initial_value):.2f}', 'Mex$.')
                elif initial_currency==3 and final_currency==1:
                    print('The final value is ', f'{currency_mxn_to_euro(initial_value):.2f}', '€.')
                elif initial_currency==3 and final_currency==2:
                    print('The final value is ', f'{currency_mxn_to_usd(initial_value):.2f}', 'US$.')
                else:
                    print('''
Invalid choice: Try again!''')
                choice()
                decision=int(input('Your decision: '))
                decision_currency_active=True
                while decision_currency_active:
                    if decision==1:
                        decision_currency_active=False
                    elif decision==2:
                        decision_currency_active=False
                        currency_active=False
                    elif decision==3:
                        decision_currency_active=False
                        currency_active=False
                        active=False
                        print('You have exited the Travel-Converter')
                    else:
                        print('Invalid choice: Enter decision again.')
                        choice()
                        decision=int(input('Your decision: '))
        elif converter==2: #length converter
            length_active=True
            while length_active:
                menu_length_converter()
                choice_system=int(input('Choice of conversion: '))
                if choice_system==1:
                    menu_metric_to_imperial()
                    choice_length_units=int(input('Choice of length units: '))
                    initial_value=int(input('Initial value: '))
                    if choice_length_units==1:
                        print('The final value is ', f'{cm_to_in(initial_value):.2f}', 'in.')
                    elif choice_length_units==2:
                        print('The final value is ', f'{dm_to_ft(initial_value):.2f}', 'ft.')
                    elif choice_length_units==3:
                        print('The final value is ', f'{m_to_yd(initial_value):.2f}', 'yd.')
                    elif choice_length_units==4:
                        print('The final value is ', f'{km_to_mi(initial_value):.2f}', 'mi.')
                    else:
                        print('''
Invalid choice: Try again!''')
                elif choice_system==2:
                    menu_imperial_to_metric()
                    choice_length_units=int(input('Choice of length units: '))
                    initial_value=int(input('Initial value: '))
                    if choice_length_units==1:
                        print('The final value is ', f'{in_to_cm(initial_value):.2f}', 'cm.')
                    elif choice_length_units==2:
                        print('The final value is ', f'{ft_to_dm(initial_value):.2f}', 'dm.')
                    elif choice_length_units==3:
                        print('The final value is ', f'{yd_to_m(initial_value):.2f}', 'm.')
                    elif choice_length_units==4:
                        print('The final value is ', f'{mi_to_km(initial_value):.2f}', 'km.')
                    else:
                        print('''
Invalid choice: Try again!''')
                else:
                    print('''
Invalid choice: Try again!''')
                choice()
                decision=int(input('Your decision: '))
                decision_length_active=True
                while decision_length_active==True:
                    if decision==1:
                        decision_length_active=False
                    elif decision==2:
                        decision_length_active=False
                        length_active=False
                    elif decision==3:
                        decision_length_active=False
                        length_active=False
                        active=False
                        print('You have exited the Travel-Converter')
                    else:
                        print('Invalid choice: Enter decision again.')
                        choice()
                        decision=int(input('Your decision: '))
        elif converter==3: #temperature converter
            temperature_active=True
            while temperature_active:
                menu_temperature()
                choice_temperature=int(input('Your choice: '))
                initial_value=int(input('Initial temperature: '))
                if choice_temperature==1:
                    print('The final value is ', f'{celsius_to_fahrenheit(initial_value):.2f}', '°F.')
                if choice_temperature==2:
                    print('The final value is ', f'{fahrenheit_to_celsius(initial_value):.2f}', '°C.')
                else:
                    print('''
Invalid choice: Try again!''')
                choice()
                decision=int(input('Your decision: '))
                decision_temperature_active=True
                while decision_temperature_active==True:
                    if decision==1:
                        decision_temperature_active=False
                    elif decision==2:
                        decision_temperature_active=False
                        temperature_active=False
                    elif decision==3:
                        decision_temperature_active=False
                        temperature_active=False
                        active=False
                        print('You have exited the Travel-Converter')
                    else:
                        print('Invalid choice: Enter decision again.')
                        choice()
                        decision=int(input('Your decision: '))
        elif converter==4: #shoesize converter
            shoesize_active=True
            while shoesize_active:
                menu_shoesize_gender()
                choice_gender=int(input('Your choice: '))
                shoesize_gender_active=True
                while shoesize_gender_active:
                    if choice_gender==1:
                        gender_active=True
                        while gender_active:
                            menu_shoesize_converter()
                            initial_unit=int(input('Initial unit: '))
                            final_unit=int(input('Final unit: '))
                            initial_value=str(input('Initial value: '))
                            if initial_unit==1 or initial_unit==2 or initial_unit==3 and final_unit==1 or final_unit==2 or final_unit==3:
                                print('The final value is', shoesizeWoman(initial_unit,final_unit,initial_value))
                                gender_active=False
                            else:
                                print('Invalid choice. Enter units and value again.')
                        shoesize_gender_active=False
                    if choice_gender==2:
                        gender_active=True
                        while gender_active:
                            menu_shoesize_converter()
                            initial_unit=int(input('Initial unit: '))
                            final_unit=int(input('Final unit: '))
                            initial_value=str(input('Initial value: '))
                            if initial_unit==1 or initial_unit==2 or initial_unit==3 and final_unit==1 or final_unit==2 or final_unit==3:
                                print('The final value is', shoesizeMan(initial_unit,final_unit,initial_value))
                                gender_active=False
                            else:
                                print('Invalid choice. Enter units and value again.')
                        shoesize_gender_active=False
                    else:
                        print('Invalid choice. Enter gender again.')
                        menu_shoesize_gender()
                        choice_gender=int(input('Your choice: '))
                choice()
                decision=int(input('Your decision: '))
                decision_shoesize_active=True
                while decision_shoesize_active==True:
                    if decision==1:
                        decision_shoesize_active=False
                    elif decision==2:
                        decision_shoesize_active=False
                        shoesize_active=False
                    elif decision==3:
                        decision_shoesize_active=False
                        shoesize_active=False
                        active=False
                        print('You have exited the Travel-Converter')
                    else:
                        print('Invalid choice: Enter decision again.')
                        choice()
                        decision=int(input('Your decision: '))
        elif converter==5: #size
            size_active=True
            while size_active:
                menu_size_converter()
                initial_unit=int(input('Initial unit: '))
                final_unit=int(input('Final unit: '))
                initial_value=str(input('Initial value: '))
                if initial_unit==1 or initial_unit==2 or initial_unit==3 or initial_unit==4 and final_unit==1 or final_unit==2 or final_unit==3 or final_unit==4:
                    print('The final value is', size(initial_unit,final_unit,initial_value))
                    gender_active=False
                else:
                    print('Invalid choice. Enter units and value again.')
                choice()
                decision=int(input('Your decision: '))
                decision_size_active=True
                while decision_size_active==True:
                    if decision==1:
                        decision_size_active=False
                    elif decision==2:
                        decision_size_active=False
                        size_active=False
                    elif decision==3:
                        decision_size_active=False
                        size_active=False
                        active=False
                        print('You have exited the Travel-Converter')
                    else:
                        print('Invalid choice: Enter decision again.')
                        choice()
                        decision=int(input('Your decision: '))
                    
                          
main()
