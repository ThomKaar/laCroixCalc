from array import array

#Constants:
LIME_INDEX = 1
LEMON_INDEX = 2
PAMPLEMOUSSE_INDEX = 6
TANGERINE_INDEX = 3
BERRY_INDEX = 4
CRAN_RASPBERRY_INDEX = 5
   
LIME_PRCNT = 0.5
LEMON_PRCNT = 0.25
PAMPLEMOUSSE_PRCNT = 0.25
TANGERINE_PRCNT = 0.5
BERRY_PRCNT = 0.25
CRAN_RASPBERRY_PRCNT = 0.25 
SINGLE_FLAVOR_PRCNT = 1.0
   


def main():
   #Smart and Final variables
   smartPrice = 10.0
   #The number of packages of LaCroix for the Price
   smartQuantity = 4
   #The number of LaCroix within each package
   smartPackSize = 8
   #Von's variables
   vonsPrice = 7.0
   #The number of packages of LaCroix for the Price
   vonsQuantity = 2
   #The number of LaCroix within each package
   vonsPackSize = 12
   #Costco's variables
   costcoPrice = 7.49
   #The number of packages of LaCroix for the Price
   costcoQuantity = 1
   #The number of LaCroix within each package
   costcoPackSize = 24
  
   """
   smartRatio = calcPriceRatio(smartPrice, smartQuantity, smartPackSize)
   vonsRatio = calcPriceRatio(vonsPrice, vonsQuantity, vonsPackSize)
   costcoRatio = calcPriceRatio(costcoPrice, costcoQuantity, costcoPackSize)
    
   print "Smart Ratio is: " + str(smartRatio)
   print "Vons Ratio is: " + str(vonsRatio)
   print "Costco Ratio is: " + str(costcoRatio)
   """
 
   introInfo()
   continue_flag = 'y'
   while(continue_flag == 'y'):
   
      flavorProfile = collectFlavorProfile()
 
      """
      The following is the calculations needed for a finding the ValueRatio for packs of La Croix containing only one flavor
      The ValueRatio = price of package / (tasteCoefficient of flavor X * # of flavor X in the package)
      """
      tasteCoefficient = max(flavorProfile)
      flavorPackageRatio = SINGLE_FLAVOR_PRCNT
      packagePleasantness = calcPleasantness(tasteCoefficient,flavorPackageRatio)
      smartValueRatio = calcValueRatio(smartPrice, packagePleasantness, smartQuantity * smartPackSize)
      vonsValueRatio = calcValueRatio(vonsPrice, packagePleasantness, vonsQuantity * vonsPackSize)

   
      """
      The following are the calculations needed for finding the ValueRatio for packs of LaCroix containing multiple flavors.
      The ValueRatio = price of package / summation(tasteCoefficient of flavor X * # of flavor X in the package)
      """
   
      availableIndexes = buildAvailableIndexesMixed(flavorProfile)
      #for index in availableIndexes:
      #   print '(' + str(index[0]) + ',' +  str(index[1]) + ')'
      packagePleasantnessMixed = calcMixedpackagePleasantness(flavorProfile,availableIndexes, costcoPackSize)
      #print "packagePleasantnessMixed: " + str(packagePleasantnessMixed)
      costcoValueRatio = calcValueRatioMixed(costcoPrice, packagePleasantnessMixed)   
  
      print "\n\nThe following ratios are price per can of La Croix scaled to your taste preferences:" 
      print "   smartValueRatio:  " + str(smartValueRatio)
      print "   vonsValueRatio:   " + str(vonsValueRatio)
      print "   costcoValueRatio: " + str(costcoValueRatio)  
      print " "
      if smartValueRatio >  vonsValueRatio and vonsValueRatio < costcoValueRatio:
         print "Smart and Final La Croix and Costco La Croix are inferior.\nThe best bang for your buck is Vons La Croix."
      elif vonsValueRatio > smartValueRatio and smartValueRatio < costcoValueRatio:
         print "Vons La Croix and Costco La Croix are the weaker choices.\nThe bubblier choice is Smart and Final La Croix"
      elif costcoValueRatio < smartValueRatio and costcoValueRatio < vonsValueRatio:
         print "Costco La Croix is the cat's meow.\nAll other La Croix choices can't compare to it's purrfection." 

      continue_flag = raw_input("Would you like to run the script again (y/n)")
   
#determines the value of a LaCroix factoring in taste preferences
def calcValueRatio(price, packagePleasantness, quantity):
   return price/(packagePleasantness*quantity)

#determines the value of LaCroix in mixed packages factoring in taste preferences
def calcValueRatioMixed(price, packagePleasantness):
   return price/packagePleasantness

#determines the value of a LaCroix package without only by LaCroix volume
def calcPriceRatio(price, quantity, packSize):
   return price/(packSize*quantity)

#determines how much the user will enjoy a single flavor package of LaCroix
def calcPleasantness(tasteCoefficient, flavorPackageRatio):
   return tasteCoefficient*flavorPackageRatio

#determines how much the user will enjoy a mixed flavor package of LaCroix
def calcMixedpackagePleasantness(flavorProfile, availableIndexes, quantity):
   packagePleasantness = 0
   for tuple in availableIndexes:
     packagePleasantness += flavorProfile[tuple[0]]*tuple[1]*quantity
   return packagePleasantness

#creates scalars for a single noteworthy LaCroix flavor based upon user input 
def collectFlavorPreference(flavor):
   input_string = "notadigit"
   while not input_string.isdigit():
      input_string = raw_input('\nPlease rate your eagerness to drink ' + flavor + ' La Croix on a scale of 1 to 10: ')
      if(input_string.isdigit() == False or int(input_string) > 10 or int(input_string) < 1):
         print "Input not recognized as a number please put in an integer."   
   return int(input_string)/10.0

#creates an array of scalars for each noteworthy LaCroix flavor to represent taste preferences
def collectFlavorProfile():
   flavor_array = ["Pure", "Lime", "Lemon", "Orange", "Berry", "Cran-Rasperry", "Pamplemousse", "Peach-Pear", "Coconut", "Mango", "Apricot", "Passionfruit", "Mango", "Tangerine", "Key Lime"]
   flavor_profile = array('f')
   for flavor in flavor_array:
      flavor_profile.append(collectFlavorPreference(flavor))
   return flavor_profile


#availableIndexes' elements are tuples that contain the index of the 
#tasteCoefficient and the number of cans in the package that correspond to the 
#LaCroix flavor with said index
#Example:
#[(1,5), (3, 7), (9, 10)]
#constructs the available Indexes list for a mixed package
def buildAvailableIndexesMixed(flavorProfile):   
   mixed0 = [(LIME_INDEX,LIME_PRCNT),(LEMON_INDEX,LEMON_PRCNT),(PAMPLEMOUSSE_INDEX,PAMPLEMOUSSE_PRCNT)]
   mixed1 = [(TANGERINE_INDEX,TANGERINE_PRCNT),(BERRY_INDEX,BERRY_PRCNT),(CRAN_RASPBERRY_INDEX,CRAN_RASPBERRY_PRCNT)]
   return findMaxofMixed(mixed0,mixed1,flavorProfile)   


#determines which mixed package the user will like more
def findMaxofMixed(mixed0, mixed1, flavorProfile):
   mixed0val = 0
   mixed1val = 0
   for flavor in mixed0:
      mixed0val += flavorProfile[flavor[0]] * flavor[1]
   for flavor in mixed1:
      mixed1val += flavorProfile[flavor[0]] * flavor[1]
   if mixed0val > mixed1val:
      return mixed0
   else:
       return mixed1

#prints introduction info
def introInfo():
   print "\n\nThis script's purpose is to help users determine where they should make their next "
   print "LaCroix purchase between the locations of Smart and Final, Vons, and Costco in San "
   print "Luis Obispo CA. The script will first ask you 15 questions to access your taste "
   print "preferences for LaCroix and then it will indicate to you which grocer you should "
   print "make your next purchase at. Enjoy and happy sipping."

   print "\n------------------------------------------------------------------------------------\n"   

if __name__ == "__main__":
   main()
