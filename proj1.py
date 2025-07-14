print(" Welcome to M&K Innovations Pvt. Ltd, ")
print("   ")
print(" Please provide us with the following information so that we may help you in best ways possible:) ")

print("  ")

n=str(input(" Please enter your name: "))       #n represents name of the customer
      
city=str(input(" Please Enter your city : "))  #city in which the house is 
print("  ")
print(" Please select the type of your house according to the codes assigned")  
print("[Duplex=1,  Appartment=2,  Villa=3,  Flats=4,  Bungalow=5,  Farmhouse=6,  Penthouse=7]")
print("  ")

h=int(input(" Please enter type of your house : "))     # h variable stores the type of house for renovation

print("  ")
Duplex=1
Flats=2
Appartment=3
Villa=4
Bungalows=5
Farmhouse=6
Penthouse=7

if h<=7 :
  print(" Please enter the area of your property")
else :
   print(" Please enter a valid number")
   h=int(input(" Please enter type of your house : "))
   print(" Please enter the area of your property")
#print("  ")    #
x=10000
y=eval('h*x')
#print("The base price for renovation with us is",y)         #

a=int(input(" Enter the area in sq.ft. : "))  # a variable represents the area of the house
print("  ")

yes=str("yes")
no=str("no")

m=str(input(" Please enter YES if the material will be provided by you otherwise enter NO : "))  #m represents the material variable
if m==yes :
  mc=0   #mc is material cost
else  : 
  mc=eval('200000')
#print(" The material charges are Rs.",mc)#
print("  ")

hardwood=str('hardwood')
tile=str('tile')
marble=str('marble')
vinyl=str('vinyl')
carpet=str('carpet')

print(" Please choose the type of flooring from the below options. ")
print("  ")

print(" Hardwood(Rs.200/sq.ft.)   Tile(Rs.50/sq.ft.)  Marble(Rs.150/sq.ft.)  Vinyl(Rs.100/sq.ft.)  Carpet(Rs.70/sq.ft.)")

f=str(input(" Enter your choice : "))
fa=int(input(" Enter the area to be floored in sq.ft. : "))    #fa is flooring area

print("  ")

if f==hardwood :
  fc=eval('200*fa')   #fc is flooring cost
elif f==tile :
  fc=eval('50*fa')
elif f==marble :
  fc=eval('150*fa')
elif f==vinyl :
  fc=eval('100*fa')
elif f== carpet :
  fc=eval('70*fa')
else:
  print("Please choose from the given options!")
  f=str(input(" Enter your choice : "))
print("  ")

if f==hardwood :
  fc=eval('200*fa')   
elif f==tile :
  fc=eval('50*fa')
elif f==marble :
  fc=eval('150*fa')
elif f==vinyl :
  fc=eval('100*fa')
elif f== carpet :
  fc=eval('70*fa')
  
#print(fc)                   



print(" Please choose the type of  down ceiling from the below options. ")
print(" ")

metal=str('metal')
pop=str('pop')
gypsum=str('gypsum')
aluminium=str('aluminium')
wooden=str('wooden')


print(" Metal(Rs.275/sq.ft.)  P.O.P(Rs.55/sq.ft.)  Gypsum(Rs.70/sq.ft.)  Aluminium(Rs.200/sq.ft.)  Wooden(Rs.150/sq.ft.)") #c is for ceiling
c=str(input(" Enter your choice : "))
ca=int(input(" Enter the area of ceiling to be covered : "))  #ca is ceiling area


if c==metal :
    cc=eval('275*ca')  #cc is ceiling cost
elif c==pop :
  cc=eval('55*ca')
elif c==gypsum :
  cc=eval('70*ca')
elif c==aluminium :
  cc=eval('200*ca')
elif c==wooden :
  cc=eval('ca*150')
else :
  print("Please choose from the given options!")
  c=str(input(" Enter your choice : "))
  ca=int(input(" Enter the area of ceiling to be covered : "))  #ca is ceiling area
if c==metal :
    cc=eval('275*ca')  
elif c==pop :
  cc=eval('55*ca')
elif c==gypsum :
  cc=eval('70*ca')
elif c==aluminium :
  cc=eval('200*ca')
elif c==wooden :
  cc=eval('150*ca')
#print("The cost for the ceiling is ",cc)    

print(" ")
print(" Please choose the type of wall finish from the given options")


distemper=str("distemper")
enamel=str("enamel")
matte=str("matte")
highgloss=str("high gloss")
semigloss=str("semi gloss")

print("  ")
print(" Distemper(Rs.30/sq.ft.)  Enamel(Rs.25/sq.ft.)  Matte(Rs.50/sq.ft.)  High gloss(Rs.60/sq.ft.)  Semi gloss(Rs.40/sq.ft.)")
w=str(input(" Enter your choice : "))                              #w is the variable for wall
wa=int(input(" Please enter the wall area to be painted : "))      #wa is the wall area to be painted
if w==distemper :
  wc=eval('30*wa')                                                 # wc is the wall cost variable
elif w==enamel :
  wc=eval('25*wa')
elif w==matte :
  wc=eval('50*wa')
elif w==highgloss :
  wc=eval('60*wa')
elif w==semigloss :
  wc=eval('40*wa')
else :
  print(" Please choose from the given options! ")
  w=str(input(" Enter your choice : "))
  wa=int(input(" Please enter the wall area to be painted"))

  if w==distemper :
    wc=eval('30*wa')
  elif w==enamel :
    wc=eval('25*wa')
  elif w==matte :
    wc=eval('50*wa')
  elif w==highgloss :
    wc=eval('60*wa')
  elif w==semigloss :
    wc=eval('40*wa')


l=50        #l is labour
lc=eval('a*l')      #lc is labour cost

debitcard=str("debit card")
creditcard=str("credit card")
cheque=str("cheque")
cash=str("cash")

print(" ")
print(" Please choose a type of payment options from:   Debit card, Credit card, Cheque, Cash ")
mp=str(input(" Please enter the mode of payment thjat would be preferred by you : "))

ta=mc+lc+fc+cc+wc          #ta is total amount
tx=18%ta                  #tx represents tax
gt=ta+tx                     #gt is grand total

print(" ")
print(" Thank you for giving us your valuable time:)  ")
print(" Your bill is generated below.")
print("  ")
print("  ")
print("                      M&K INNOVATIONS PVT. LTD.")
print("                   Innovation becomes reality here")
print(" ")
print("Dated:02/11/2020                                Bill no. BKMD14-284")
print(" ")
print(" Customer name :   ",n)                         #print("City : ",city)
print("  ")
print(" Area of the property :                                      ",a)
print(" Material charges :                                          ",mc)
print(" Labour charges :                                            ",lc)
print(" Flooring charges :                                          ",fc)
print(" Ceiling charges :                                           ",cc)
print(" Wall finish charges :                                       ",wc)
print(" ")
print("                           Total amount                      ",ta)
print("                 Grand total (including all taxes)           ",gt)
print(" Mode of payment : ",mp)
print("  ")
print("                THANK YOU FOR SHOPPING WITH US!")
print(" ")
print("                                        ",n)
print("                                   ____________________________   ")
        
print("                                      Customer's signature")
  




