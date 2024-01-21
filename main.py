#This program is by Yoyo Liu
#Completed 11/6/2021 
#Uploaded to Github 1/21/2024

#import and sort the files: birth_rate, gdp, population and unemployment, make them into lists
with open("birth_rate.txt", "r") as birth_rate:
  birth_content = birth_rate.readlines()
with open("gdp.txt", "r") as gdp:
  gdp_content = gdp.readlines()
with open("population.txt", "r") as population:
  population_content = population.readlines()
with open("unemployment.txt", "r") as unemployment:
  unemployment_content = unemployment.readlines()

#create a loop for user if they want to play again
play_again = 'y'
while play_again == 'y':
  confirm = 'n'
  #make a loop for user to confirm their selection on what they want to so
  while confirm != 'y':
    country_list = ["United States", "China", "Russia", "India", "France", "Germany", "Japan", "United Kingdom", "Korea, South", "Israel", "Saudi Arabia", "Italy", "Spain", "United Arab Emirates", "Canada", "Switzerland", "Australia", "Turkey", "Sweden", "Qatar", "Netherlands", "Singapore", "Iran", "Norway", "Brazil"]#a list of all the 25 most powerful countries

    fact_list = ["Birth rate", "GDP", "Population", "Unemployment"]#list of facts they can see

    print("These are the twenty-five most powerful countries in the wolrd: \n1. United States \n2. China \n3. Russia\n4. India\n5. France\n6. Germany\n7. Japan\n8. United Kingdom\n9. South Korea\n10. Israel\n11. Saudi Arabia\n12. Italy	\n13. Spain\n14. United Arab Emirates\n15. Canada\n16. Switzerland	\n17. Australia\n18. Turkey\n19. Sweden\n20. Qatar\n21. Netherlands\n22. Singapore\n23. Iran\n24. Norway\n25. Brazil")#print the list of countries so the user can select easily
    the_chosen_country = str(input("Pick a nation above to see some facts about it."))#ask the user which country to see

    #create a loop in case the user input something other than a number within 1 and 25
    indicator = False
    while indicator == False: 
      try: 
        if int(the_chosen_country) not in range(1, 26):
          the_chosen_country = str(input("Please select a number between 1 and 25. "))
          indicator = False #loop until the user select a number btween 1 and 25
        else:
          indicator = True#if the selection is valid, quit the loop
      except: 
        the_chosen_country = str(input("Please select a number between 1 and 25. "))#if there's an issue, i.e. inputting a char/decimal, loop again

    the_country = country_list[int(the_chosen_country)-1]#get that country using the chosen number

    print("Which Fact do you want to see? \n1. Birth Rate\n2. GDP\n3. Population\n4. Unemployment")#tell the user what facts they can see

    the_chosen_fact = str(input("Choose a number."))#ask them to choose a fact to see

    #make a loop in case user select anything outside of 1 and 4 as a fact
    indicator = False
    while indicator == False: 
      try: 
        if int(the_chosen_fact) not in range(1, 5):
          the_chosen_fact = str(input("Please select a number between 1 and 4. "))
          indicator = False#loop until the user select a number between 1 and 4
        else:
          indicator = True
          the_chosen_fact = int(the_chosen_fact)#change this to int for easier future use
      except: 
        the_chosen_fact = str(input("Please select a number between 1 and 4. "))#if there's a problem, keep looping

    the_fact = fact_list[the_chosen_fact-1]#get the correct index for the fact

    confirm = input("Please confirm, you want to see " + the_country +"'s " + the_fact.lower() + " , correct? [y/n]")#ask the user to confirm, or keep looping

  if the_chosen_fact == 1:#if the user wanted the birth rate
    special_indication = "The information is displayed as: Country, Birth Rate, Region."#add a special indication for user to understand
    with open("tem_file.txt", 'w') as information:
      for a_line in birth_content: 
        if the_country in a_line: #find line containing the country
          information.write(a_line)#write it to the newly created tem_file
         
  elif the_chosen_fact == 2:# if user want GDP
    special_indication = "The information is displayed as: Country, GDP, Region." #special indication
    with open("tem_file.txt", 'w') as information:
      for a_line in gdp_content: 
        if the_country in a_line: #write line to the new tem_file
          information.write(a_line)

  elif the_chosen_fact == 3:#similar to the two blocks above
    special_indication = "The information is displayed as: Country, Population, Region."
    with open("tem_file.txt", 'w') as information:
      for a_line in population_content: 
        if the_country in a_line: 
          information.write(a_line)

  elif the_chosen_fact == 4:#similar to the blocks above
    special_indication = "The information is displayed as: Country, Unemployment Rate, Region."
    with open("tem_file.txt", 'w') as information:
      for a_line in unemployment_content: 
        if the_country in a_line: 
          information.write(a_line)
  #print the special indication to guide the user
  print(special_indication)
  #print information on the file for the user
  with open("tem_file.txt", "r") as info:
    content = info.read()
    print("Here is the information:\n" + content)
  #ask if user want to see another fact
  play_again = input("Do you want to see another fact? [y/n]")
#thank the user after everything is done. 
print("Thank you for using this program, have a great day. ")