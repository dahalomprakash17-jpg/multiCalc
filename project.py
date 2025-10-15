valid = True
while valid:
     print("\n\n\t\t===================================\t\t\n")
     print("\t\t       MULTI-PURPOSE CALCULATOR\t\t\n")
     print("\t\t===================================\t\t\n")
     print("\t\tA) Arithmetic Operation\t\t")
     print("\t\tC) Conversions\t\t")
     print("\t\tAR) Area\t\t")
     print("\t\tV) Volume\t\t")
     print("\t\tQ) Quit\t\t")
     print("\n\t\t===================================\t\t")

     choice_initial = input("\nEnter your choice: ")

     if choice_initial.strip().upper()=="A":
          print("\n1) Addition\n")
          print("2) Subtraction\n")
          print("3) Multiplication\n")
          print("4) Division:\n")
          choice = input("Enter your choice: ")

          x = input("\nEnter the first number: ")
          check_num = ("0","1","2","3","4","5","6","7","8","9",".")
     
          for i in x:
               while i not in check_num and i[0] != "-":
                    print("Invalid Input")
                    x = input("\nEnter the correct number: ")
                    
                    for j in range(len(x)):
                         i = x[j]
               
                    
          x = float(x)
          y = input("\nEnter the second number: ")
          for i in y:
               while i not in check_num and i[0] != "-":
                    print("Invalid Input")
                    y = input("\nEnter the correct number: ")

          y = float(y)


          if(choice.strip() == "1"):
               print(f"\n{x} + {y} = {x+y}.\n")
               user_choice = input("\nEnter y to continue and n to quit: ")
               if user_choice.strip().lower() == "n":
                    valid = False
                    print(f"\nGoodBye\n")
                    
     

          elif(choice.strip() == "2"):
               print(f"\n{x} - {y} = {x-y}.\n")
               user_choice = input("\nEnter y to continue and n to quit: ")
               if user_choice.strip().lower() == "n":
                    valid = False
                    print(f"\nGoodBye\n")
                    
               

          elif(choice.strip() == "3"):
               print(f"\n{x} * {y} = {x*y}.\n")
               user_choice = input("\nEnter y to continue and n to quit: ")
               if user_choice.strip().lower() == "n":
                    valid = False
                    print(f"\nGoodBye\n")
                    
               

          elif(choice.strip() == "4"):
               if y==0:
                    print(f"\nIt is not possible to divide the number by 0.\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
               
                    
               else:
                    print(f"""\n{x} / {y} = {x/y}""")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
                         

          else:
               print(f"\nInvalid Input.\n")
               user_choice = input("\nEnter y to continue and n to quit: ")
               if user_choice.strip().lower() == "n":
                    valid = False
                    print(f"\nGoodBye\n")  
               
               
     elif choice_initial.strip().upper()=="C":
          print(f"\n1) Base Conversion\n")
          print(f"2) Temperature Conversion\n")
          conv_choice = input("Enter your choice: ")

          if conv_choice.strip() == "1":
               print(f"\n1) Decimal to Binary:\n")
               print(f"2) Decimal to Octal:\n")
               print(f"3) Decimal to Hexadecimal:\n")
               print(f"4) Binary to Decimal:\n")
               print(f"5) Binary to Octal:\n")
               print(f"6) Binary to Hexadecimal:\n")
               print(f"7) Octal to Decimal:\n")
               print(f"8) Octal to Binary:\n")
               print(f"9) Octal to Hexadecimal:\n")
               print(f"10) Hexadecimal to Decimal:\n")
               print(f"11) Hexadecimal to Binary:\n")
               print(f"12) Hexadecimal to Octal:\n")


               bas_con_choice = input("Enter your choice: ")

               if bas_con_choice.strip() in ["1","2","3"]:
                    dec_num = int(input("\nEnter the decimal number to be converted: "))
               
                    if bas_con_choice.strip() == "1": 
                         prev = ""
                         fin_num = dec_num
                         while dec_num!=0:
                              remainder = dec_num%2
                              prev = prev + str(remainder)
                              dec_num = dec_num//2
                         print(f"The binary value of {fin_num} is {prev[::-1]}.\n")
                         user_choice = input("\nEnter y to continue and n to quit: ")
                         if user_choice.strip().lower() == "n":
                              valid = False
                              print(f"\nGoodBye\n")
                                   
                              
                              

                    elif bas_con_choice.strip() == "2":
                         prev = ""
                         fin_num = dec_num
                         while dec_num!=0:
                              remainder = dec_num%8
                              prev = prev + str(remainder)
                              dec_num = dec_num//8
                         print(f"The octal value of {fin_num} is {prev[::-1]}.\n")
                         user_choice = input("\nEnter y to continue and n to quit: ")
                         if user_choice.strip().lower() == "n":
                              valid = False
                              print(f"\nGoodBye\n")
                                   

                    elif bas_con_choice.strip() == "3":
                         prev = ""
                         fin_num = dec_num
                         hex_num = "0123456789ABCDEF"
                         while dec_num!=0:
                              remainder = dec_num%16
                              prev = prev + hex_num[remainder]
                              dec_num = dec_num//16
                         print(f"The hexadecimal value of {fin_num} is {prev[::-1]}.\n")
                         user_choice = input("\nEnter y to continue and n to quit: ")
                         if user_choice.strip().lower() == "n":
                              valid = False
                              print(f"\nGoodBye\n")
                                   
                    

               elif bas_con_choice.strip() == "4" or bas_con_choice.strip() == "5" or bas_con_choice.strip() == "6":
                    bin_num = (input("Enter the binary number to be converted: "))
                    for each_num in bin_num:
                         if each_num != "0" and each_num != "1":
                              print(f"\nInvalid Input.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")

                    else:
                         if bas_con_choice.strip() == "4":
                              print(f"\nThe decimal value of {bin_num} is {int(bin_num,2)}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
                                             
                         elif bas_con_choice.strip() == "5":
                              dec = int(bin_num,2)
                              print(f"The octal value of {bin_num} is {oct(dec)[2:]}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")

                         elif bas_con_choice.strip() == "6":
                              dec = int(bin_num,2)
                              print(f"The hexadecimal value of {bin_num} is {hex(dec)[2:].upper()}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")

               elif bas_con_choice.strip() == "7" or bas_con_choice.strip() == "8" or bas_con_choice.strip() == "9":
                    oct_num = input("\nEnter the octal number to be converted: ")
                    oc_no_test = "01234567"
                    for each in oct_num:
                         if each not in oc_no_test:
                              print(f"Invalid Input.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
                              
                    else:
                         if bas_con_choice.strip() == "7":
                              print(f"The decimal value of {oct_num} is {int(oct_num,8)}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
                         
                         elif bas_con_choice.strip() == "8":
                              dec = int(oct_num,8)
                              print(f"The binary value of {oct_num} is {bin(dec)[2:]}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
                         
                         elif bas_con_choice.strip() == "9":
                              dec = int(oct_num,8)
                              print(f"The hexadecimal value of {oct_num} is {hex(dec)[2:].upper()}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
               
               elif bas_con_choice.strip() == "10" or bas_con_choice.strip() == "11" or bas_con_choice.strip() == "12":
                    hex_num = input("\nEnter the hexadecimal number to be converted: ").upper()
                    hex_no_test = "0123456789ABCDEF"
                    for each in hex_num:
                         if each not in hex_no_test:
                              print(f"Invalid Input.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
                    
                    else:
                         if bas_con_choice.strip() == "10":
                              print(f"The decimal value of {hex_num} is {int(hex_num,16)}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
                         
                         elif bas_con_choice.strip() == "11":
                              dec = int(hex_num,16)
                              print(f"The binary value of {hex_num} is {bin(dec)[2:]}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
                         
                         elif bas_con_choice.strip() == "12":
                              dec = int(hex_num,16)
                              print(f"The octal value of {hex_num} is {oct(dec)[2:]}.\n")
                              user_choice = input("\nEnter y to continue and n to quit: ")
                              if user_choice.strip().lower() == "n":
                                   valid = False
                                   print(f"\nGoodBye\n")
               
               else:
                    print(f"Invalid Input.\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")



          if conv_choice.strip() == "2":
               print(f"\n1) Celsius to Fahrenheit\n")
               print(f"2) Celsius to Kelvin\n")
               print(f"3) Fahrenheit to Celsius\n")
               print(f"4) Fahrenheit to Kelvin\n")
               print(f"5) Kelvin to Celsius\n")
               print(f"6) Kelvin to Fahrenheit\n")
               temp_choice = input("\nEnter your choice: ")

               if temp_choice.lstrip().rstrip() == "1" or temp_choice.lstrip().rstrip() == "2":
                    cel = int(input("\nEnter the temperature in Celsius: "))
               
               if temp_choice.lstrip().rstrip() == "1":
                    fin_temp = 9*cel/5 + 32
                    print(f"\n{cel}{chr(176)}C = {fin_temp}{chr(176)}F\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
                    

               
               if temp_choice.strip() == "2":
                    fin_temp = cel + 273
                    print(f"\n{cel}{chr(176)}C = {fin_temp}{chr(176)}K\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
                    
               
               if temp_choice.strip() == "3" or temp_choice.strip() == "4":
                    fah = int(input("\nEnter the temperature in Fahrenheit: "))
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
               
               if temp_choice.strip() == "3":
                    fin_temp = 5*(fah - 32)/9
                    print(f"\n{fah}{chr(176)}F= {fin_temp}{chr(176)}C\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
                    

               if temp_choice.strip() == "4":
                    fin_temp = 5*(fah - 32)/9 + 273
                    print(f"\n{fah}{chr(176)}F= {fin_temp}{chr(176)}K\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
                    

               if temp_choice.strip() == "5" or temp_choice.strip() == "6":
                    kel = int(input("\nEnter the temperature in Kelvin: "))
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
               
               if temp_choice.strip() == "5":
                    fin_temp = kel - 273
                    print(f"\n{kel}{chr(176)}K= {fin_temp}{chr(176)}C\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
                    

               if temp_choice.strip() == "6":
                    fin_temp = 9*(kel-273)/5 + 32
                    print(f"\n{kel}{chr(176)}K= {fin_temp}{chr(176)}F\n")
                    user_choice = input("\nEnter y to continue and n to quit: ")
                    if user_choice.strip().lower() == "n":
                         valid = False
                         print(f"\nGoodBye\n")
                    







