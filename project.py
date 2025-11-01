valid = True
while valid:
     # MAIN MENU
     print("\n\n\t\t===================================\t\t\n")
     print("\t\t       MULTI-PURPOSE CALCULATOR\t\t\n")
     print("\t\t===================================\t\t\n")
     print("\t\tA) Arithmetic Operation\t\t")
     print("\t\tC) Conversions\t\t")
     print(f"\t\tG) Geometrical Calculations\t\t")
     print(f"\t\tQ) Quit\t\t")
     print("\n\t\t===================================\t\t")

     choice_initial = input("\nEnter your choice: ").strip().upper()
     while choice_initial not in ["A","C","G","Q"]:
          print(f"Invalid Input. Please enter A, C, G or Q")
          choice_initial = input("Enter your choice: ")




     if choice_initial == "A":
          #ARITHMETIC OPERATION
          print("\n","-"*7,"ARITHMETIC OPERATION","-"*7)
          print("\n1) Addition\n")
          print("2) Subtraction\n")
          print("3) Multiplication\n")
          print("4) Division\n")
          print("5) Square\n")
          print("6) Square Root\n")
          print("7) Cube\n")
          print("8) Cube Root\n")
          print("9 a^b\n")
          print("-"*36,"\n")
          
          
          choice = input("Enter your choice: ").strip()
          while choice not in ["1","2","3","4","5","6","7","8","9"]:
               print("Invalid Choice.")
               choice = input("\nEnter valid choice: ").strip()
          if choice in ["1","2","3","4"]:
               while True:
                    x = input("\n\nEnter the first number: ").strip()
                    
                    if x == "" or x == "-":
                         print("Invalid input.")
                         continue

                    if x.count("-") > 1 or x.count(".") > 1:
                         print("Invalid input.")
                         continue

                    if "-" in x and x[0] != "-":
                         print("Invalid input.")
                         continue

                    valid_check = True
                    for ch in x:
                         if ch not in ["0","1","2","3","4","5","6","7","8","9",".","-"]:
                              valid_check = False
                              break
                    if not valid_check:
                         print("Invalid input.")
                         continue

                    if x.startswith(".") or x.endswith(".") or x.startswith("-.") :
                         print("Invalid input.")
                         continue
                    x = float(x)
                    break
     
               while True:
                    y = input("Enter the second number: ").strip()
                    
                    if y == "" or y == "-":
                         print("Invalid input.")
                         continue

                    if y.count("-") > 1 or y.count(".") > 1:
                         print("Invalid input.")
                         continue

                    if "-" in y and y[0] != "-":
                         print("Invalid input.")
                         continue

                    valid_check = True
                    for ch in y:
                         if ch not in "0123456789.-":
                              valid_check = False
                              break
                    if not valid_check:
                         print("Invalid input.")
                         continue

                    if y.startswith(".") or y.endswith(".") or y.startswith("-.") :
                         print("Invalid input.")
                         continue
                    y = float(y)
                    break


               if(choice == "1"):
                    print(f"\n{x} + {y} = {x+y}.\n")
                         
               elif(choice == "2"):
                    print(f"\n{x} - {y} = {x-y}.\n")
                              
               elif(choice == "3"):
                    print(f"\n{x} * {y} = {x*y}.\n")
                                   
               elif(choice == "4"):
                    if y==0:
                         print(f"\nIt is not possible to divide the number by 0.\n")                           
                    else:
                         print(f"""\n{x} / {y} = {x/y}""")
                   
          elif choice in ["5","6","7","8"]:
               while True:
                    x = input("\n\nEnter the number: ").strip()
                    
                    if x == "" or x == "-":
                         print("Invalid input.")
                         continue

                    if x.count("-") > 1 or x.count(".") > 1:
                         print("Invalid input.")
                         continue

                    if "-" in x and x[0] != "-":
                         print("Invalid input.")
                         continue

                    valid_check = True
                    for ch in x:
                         if ch not in ["0","1","2","3","4","5","6","7","8","9",".","-"]:
                              valid_check = False
                              break
                    if not valid_check:
                         print("Invalid input.")
                         continue

                    if x.startswith(".") or x.endswith(".") or x.startswith("-.") :
                         print("Invalid input.")
                         continue
                    x = float(x)
                    break  
               if choice == "5":
                    print(x,"^2 = ", x**2)   
               elif choice == "6":
                    print(x,"^1/2 = ", x**(1/2))
               elif choice == "7":
                    print(x,"^3 = ", x**3)
               elif choice == "8":
                    print(x,"^1/3 = ", x**(1/3))
          
          elif choice == "9":
               while True:
                    x = input("\n\nEnter the base: ").strip()
                    
                    if x == "" or x == "-":
                         print("Invalid input.")
                         continue

                    if x.count("-") > 1 or x.count(".") > 1:
                         print("Invalid input.")
                         continue

                    if "-" in x and x[0] != "-":
                         print("Invalid input.")
                         continue

                    valid_check = True
                    for ch in x:
                         if ch not in ["0","1","2","3","4","5","6","7","8","9",".","-"]:
                              valid_check = False
                              break
                    if not valid_check:
                         print("Invalid input.")
                         continue

                    if x.startswith(".") or x.endswith(".") or x.startswith("-.") :
                         print("Invalid input.")
                         continue
                    x = float(x)
                    break

               while True:
                    y = input("Enter the power: ").strip()
                    
                    if y == "" or y == "-":
                         print("Invalid input.")
                         continue

                    if y.count("-") > 1 or y.count(".") > 1:
                         print("Invalid input.")
                         continue

                    if "-" in y and y[0] != "-":
                         print("Invalid input.")
                         continue

                    valid_check = True
                    for ch in y:
                         if ch not in "0123456789.-":
                              valid_check = False
                              break
                    if not valid_check:
                         print("Invalid input.")
                         continue

                    if y.startswith(".") or y.endswith(".") or y.startswith("-.") :
                         print("Invalid input.")
                         continue
                    y = float(y)
                    break
               print(x,"^",y," = ",x**y)
               


     # CONVERSION
     elif choice_initial == "C":
          print("\n","-"*7,"CONVERSION","-"*7)
          print(f"\n1) Base Conversion\n")
          print(f"2) Temperature Conversion\n")
          print("-"*26,"\n")
          conv_choice = input("Enter your choice: ").strip()
          while conv_choice not in ["1","2"]:
               print("Invalid Choice.")
               conv_choice = input("\nEnter valid choice: ").strip()

          if conv_choice == "1":
               print("\n","-"*7,"BASE CONVERSION","-"*7)
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
               print("-"*31,"\n")

               bas_con_choice = input("Enter your choice: ").strip()
               while bas_con_choice not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                    print(f"Invalid Input. Enter number from 1 to 12.")
                    bas_con_choice = input("Enter your choice: ")

               if bas_con_choice in ["1","2","3"]:
                    valid_check = True
                    while valid_check:
                         dec_num = input("Enter the decimal number to be converted: ").strip()
                         for each_num in dec_num:
                              if each_num not in ["0","1","2","3","4","5","6","7","8","9"]:
                                   print(f"\nInvalid Input.\n")
                                   break
                         else:
                              valid_check = False
                    dec_num = int(dec_num)
               
                    if bas_con_choice == "1": 
                         prev = ""
                         fin_num = dec_num
                         while dec_num!=0:
                              remainder = dec_num%2
                              prev = prev + str(remainder)
                              dec_num = dec_num//2
                         print(f"The binary value of {fin_num} is {prev[::-1]}.\n")
                                                          
                    elif bas_con_choice == "2":
                         prev = ""
                         fin_num = dec_num
                         while dec_num!=0:
                              remainder = dec_num%8
                              prev = prev + str(remainder)
                              dec_num = dec_num//8
                         print(f"The octal value of {fin_num} is {prev[::-1]}.\n")
                        
                    elif bas_con_choice == "3":
                         prev = ""
                         fin_num = dec_num
                         hex_num = "0123456789ABCDEF"
                         while dec_num!=0:
                              remainder = dec_num%16
                              prev = prev + hex_num[remainder]
                              dec_num = dec_num//16
                         print(f"The hexadecimal value of {fin_num} is {prev[::-1]}.\n")
                         
                                       
               elif bas_con_choice == "4" or bas_con_choice == "5" or bas_con_choice == "6":
                    valid_check = True
                    while valid_check:
                         bin_num = input("Enter the binary number to be converted: ").strip()
                         for each_num in bin_num:
                              if each_num != "0" and each_num != "1":
                                   print(f"\nInvalid Input.\n")
                                   break
                         else:
                              valid_check = False
                             
                    if bas_con_choice == "4":
                         print(f"\nThe decimal value of {bin_num} is {int(bin_num,2)}.\n")
                                                  
                    elif bas_con_choice == "5":
                         dec = int(bin_num,2)
                         print(f"The octal value of {bin_num} is {oct(dec)[2:]}.\n")
                         
                    elif bas_con_choice == "6":
                         dec = int(bin_num,2)
                         print(f"The hexadecimal value of {bin_num} is {hex(dec)[2:].upper()}.\n")
                              

               elif bas_con_choice == "7" or bas_con_choice == "8" or bas_con_choice == "9":
                    oc_no_test = "01234567"
                    valid_check = True
                    while valid_check:
                         oct_num = input("\nEnter the octal number to be converted: ").strip()
                         for each in oct_num:
                              if each not in oc_no_test:
                                   print(f"Invalid Input.\n")
                                   break
                         else:
                              valid_check = False
                                        
                    if bas_con_choice == "7":
                         print(f"The decimal value of {oct_num} is {int(oct_num,8)}.\n")
                              
                    elif bas_con_choice == "8":
                         dec = int(oct_num,8)
                         print(f"The binary value of {oct_num} is {bin(dec)[2:]}.\n")
                         
                    elif bas_con_choice == "9":
                         dec = int(oct_num,8)
                         print(f"The hexadecimal value of {oct_num} is {hex(dec)[2:].upper()}.\n")
                              
               
               elif bas_con_choice == "10" or bas_con_choice == "11" or bas_con_choice == "12":
                    hex_no_test = "0123456789ABCDEF"
                    valid_check = True
                    while valid_check:
                         hex_num = input("\nEnter the hexadecimal number to be converted: ").upper().strip()
                         for each in hex_num:
                              if each not in hex_no_test:
                                   print(f"Invalid Input.\n")
                                   break
                         else:
                              valid_check = False
                             
                    if bas_con_choice == "10":
                         print(f"The decimal value of {hex_num} is {int(hex_num,16)}.\n")
                              
                    elif bas_con_choice == "11":
                         dec = int(hex_num,16)
                         print(f"The binary value of {hex_num} is {bin(dec)[2:]}.\n")
                         
                    elif bas_con_choice == "12":
                         dec = int(hex_num,16)
                         print(f"The octal value of {hex_num} is {oct(dec)[2:]}.\n")
                              
               
                   
          if conv_choice == "2":
               print("\n","-"*7,"TEMPERATURE CONVERSION","-"*7)
               print(f"\n1) Celsius to Fahrenheit\n")
               print(f"2) Celsius to Kelvin\n")
               print(f"3) Fahrenheit to Celsius\n")
               print(f"4) Fahrenheit to Kelvin\n")
               print(f"5) Kelvin to Celsius\n")
               print(f"6) Kelvin to Fahrenheit\n")
               print("-"*38,"\n")
               temp_choice = input("\nEnter your choice: ").strip()
               while temp_choice not in ["1","2","3","4","5","6"]:
                    print(f"Invalid Input. Enter number from 1 to 6.")
                    temp_choice = input("Enter your choice: ")

               if temp_choice == "1" or temp_choice == "2":
                        
                    while True:
                         cel = input("\nEnter the temperature in Celsius: ")
                         
                         if cel == "" or cel == "-":
                              print("Invalid input.")
                              continue

                         if cel.count("-") > 1 or cel.count(".") > 1:
                              print("Invalid input.")
                              continue

                         if "-" in cel and cel[0] != "-":
                              print("Invalid input.")
                              continue

                         valid_check = True
                         for ch in cel:
                              if ch not in "0123456789.-":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid input.")
                              continue

                         if cel.startswith(".") or cel.endswith(".") or cel.startswith("-.") :
                              print("Invalid input.")
                              continue
                         cel = float(cel)
                         break
               

               if temp_choice == "1":
                    fin_temp = 9*cel/5 + 32
                    print(f"\n{cel}{chr(176)}C = {fin_temp}{chr(176)}F\n")
                    
               elif temp_choice == "2":
                    fin_temp = cel + 273
                    print(f"\n{cel}{chr(176)}C = {fin_temp}{chr(176)}K\n")
                    
                    
               if temp_choice == "3" or temp_choice == "4":
                    while True:
                         fah = input("\nEnter the temperature in Fahrenheit: ")
                         
                         if fah == "" or fah == "-":
                              print("Invalid input.")
                              continue

                         if fah.count("-") > 1 or fah.count(".") > 1:
                              print("Invalid input.")
                              continue

                         if "-" in fah and fah[0] != "-":
                              print("Invalid input.")
                              continue

                         valid_check = True
                         for ch in fah:
                              if ch not in "0123456789.-":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid input.")
                              continue

                         if fah.startswith(".") or fah.endswith(".") or fah.startswith("-.") :
                              print("Invalid input.")
                              continue
                         fah = float(fah)
                         break
                    
               if temp_choice == "3":
                    fin_temp = 5*(fah - 32)/9
                    print(f"\n{fah}{chr(176)}F= {fin_temp}{chr(176)}C\n")
                    
               elif temp_choice == "4":
                    fin_temp = 5*(fah - 32)/9 + 273
                    print(f"\n{fah}{chr(176)}F= {fin_temp}{chr(176)}K\n")
                   

               if temp_choice == "5" or temp_choice.strip() == "6":
                    while True:
                         kel = input("\nEnter the temperature in Kelvin: ")
                         
                         if kel == "" or kel == "-":
                              print("Invalid input.")
                              continue

                         if kel.count("-") > 1 or kel.count(".") > 1:
                              print("Invalid input.")
                              continue

                         if "-" in kel and kel[0] != "-":
                              print("Invalid input.")
                              continue

                         valid_check = True
                         for ch in kel:
                              if ch not in "0123456789.-":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid input.")
                              continue

                         if kel.startswith(".") or kel.endswith(".") or kel.startswith("-.") :
                              print("Invalid input.")
                              continue
                         kel = float(kel)
                         break
                    
               if temp_choice == "5":
                    fin_temp = kel - 273
                    print(f"\n{kel}{chr(176)}K= {fin_temp}{chr(176)}C\n")    

               elif temp_choice == "6":
                    fin_temp = 9*(kel-273)/5 + 32
                    print(f"\n{kel}{chr(176)}K= {fin_temp}{chr(176)}F\n")
                    



     
     # GEOMETRICAL CALCULATION
     elif choice_initial == "G":
          PI = 22/7
          print("\n","-"*7,"GEOMETRICAL CALCULATION","-"*7)
          print(f"\n1)Area\n")
          print(f"2) Volume\n")
          print("-"*39,"\n")
          geo_choice = input("\nEnter your choice: ").strip()
          while geo_choice not in ["1","2"]:
               print(f"Invalid Choice.")
               geo_choice = input("\nPlease enter the valid choice: ").strip()

          if geo_choice == "1":
               print("\n","-"*7,"AREA","-"*7)
               print(f"\n1) Area of rectangle\n")
               print(f"2) Area of square\n")
               print(f"3) Area of circle\n")
               print("-"*20,"\n")
               area_choice = input("Enter your choice: ").strip()
               while area_choice not in ["1","2","3"]:
                    print(f"Invalid Choice.")
                    area_choice = input("\nPlease enter the valid choice: ").strip()
                    
               if area_choice == "1":
                    while True:
                         length = input("\nEnter the length of rectangle: ").strip()

                         if length == "" or length == "-":
                              print("Invalid Input.")
                              continue
                         if length.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in length:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         length = float(length)
                         break
                    
                    while True:
                         breadth = input("\nEnter the breadth of the rectangle: ").strip()
                         if breadth == "" or breadth == "-":
                              print("Invalid Input.")
                              continue
                         if breadth.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in breadth:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         breadth = float(breadth)
                         break
                    area = (length) * (breadth)
                    print(f"\nlength of rectangle = {length}")
                    print(f"breadth of rectangle = {breadth}")
                    print(f"Area of rectangle = {area}\n")

               elif area_choice == "2":
                    while True:
                         length = input("\nEnter the length of square: ").strip()

                         if length == "" or length == "-":
                              print("Invalid Input.")
                              continue
                         if length.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in length:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         length = float(length)
                         break
                    area = (length)**2
                    print(f"\nlength of square = {length}")
                    print(f"Area of square = {area}\n")

               elif area_choice == "3":    
                    while True:
                         radius = input(f"\nEnter the radius of the circle: ").strip()
                         if radius == "" or radius == "-":
                              print("Invalid Input.")
                              continue
                         if radius.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in radius:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         radius = float(radius)
                         break
                    area = PI * (radius)**2
                    print(f"\nRadius of the circle = {radius}")
                    print(f"Area of the circle = {area}\n")



          if geo_choice == "2":
               print("\n","-"*7,"VOLUME","-"*7)
               print(f"\n1) Volume of Cuboid\n")
               print(f"2) Volume of Cube\n")
               print(f"3) Volume of cone\n")
               print(f"4) Volume of Cylinder\n")
               print(f"5) Sphere\n")
               print("-"*22,"\n")

               vol_choice = input("\nEnter your choice: ")
               while vol_choice not in ["1","2","3","4","5"]:
                    print(f"\nInvalid choice.")
                    vol_choice = input("Please enter 1, 2, 3, 4 or 5: ")

               if vol_choice == "1":
                    while True:
                         length = input("\nEnter the length of a cuboid: ").strip()

                         if length == "" or length == "-":
                              print("Invalid Input.")
                              continue
                         if length.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in length:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         length = float(length)
                         break
                    
                    while True:
                         breadth = input("\nEnter the breadth of the cuboid: ").strip()

                         if breadth == "" or breadth == "-":
                              print("Invalid Input.")
                              continue
                         if breadth.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in breadth:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         breadth = float(breadth)
                         break
                    
                    while True:
                         height = input("\nEnter the height of the cuboid: ").strip()

                         if height == "" or height == "-":
                              print("Invalid Input.")
                              continue
                         if height.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in height:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         height = float(height)
                         break
                    volume = (length) * (breadth) * (height)
                    print(f"\nLength = {length}\tbreadth = {breadth}\theight = {height}")
                    print(f"Volume of cuboid = {volume}")

               elif vol_choice == "2":
                    while True:
                         length = input("\nEnter the length of the cube: ").strip()

                         if length == "" or length == "-":
                              print("Invalid Input.")
                              continue
                         if length.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in length:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         length = float(length)
                         break                  
                    volume = (length)**3
                    print(f"\nLength of the cube = {length}")
                    print(f"Volume of the cube = {volume}")
               
               elif vol_choice == "3":
                    
                    while True:
                         radius = input("\nEnter the radius of the base of a cone: ").strip()

                         if radius == "" or radius == "-":
                              print("Invalid Input.")
                              continue
                         if radius.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in radius:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         radius = float(radius)
                         break
                    
                    while True:
                         height = input("\nEnter the height of the cone: ").strip()

                         if height == "" or height == "-":
                              print("Invalid Input.")
                              continue
                         if height.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in height:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         height = float(height)
                         break                  
                    volume = (1/3)*(PI) * (radius)**2 * (height)
                    print(f"Radius = {radius}\theight = {height}")
                    print(f"Volume of the cone = {volume}")

               elif vol_choice == "4":
                    while True:
                         radius = input("\nEnter the radius of the base of a cylinder: ").strip()

                         if radius == "" or radius == "-":
                              print("Invalid Input.")
                              continue
                         if radius.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in radius:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         radius = float(radius)
                         break


                    while True:
                         height = input("\nEnter the height of the cylinder: ").strip()

                         if height == "" or height == "-":
                              print("Invalid Input.")
                              continue
                         if height.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in height:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         height = float(height)
                         break
                    volume = (PI) * (radius)**2 * (height)
                    print(f"Radius = {radius}\theight = {height}")
                    print(f"Volume of the cylinder = {volume}")

               elif vol_choice == "5":
                    while True:
                         radius = input("\nEnter the radius of the sphere: ").strip()

                         if radius == "" or radius == "-":
                              print("Invalid Input.")
                              continue
                         if radius.count(".")>1:
                              print("Invalid Input.")
                              continue
                         valid_check = True
                         for ch in radius:
                              if ch not in "0123456789.":
                                   valid_check = False
                                   break
                         if not valid_check:
                              print("Invalid Input.")
                              continue
                         radius = float(radius)
                         break
                    volume = (4/3)*(PI)*(radius)**3
                    print(f"Radius = {radius}")
                    print(f"Volume of the sphere = {volume}")




     # QUIT
     elif choice_initial.strip().upper() == "Q":
          valid = False
          print("\n")
          print("="*50)
          print(f"\nThanks for using the calculator. Have a nice day!\n")
          print("="*50)
          print("\n")







