"""
NBIISH-JUSTIN KENWABIKISE
Flight Calculator that takes flight info,
error checks, and outputs a price summary.

-->TAKES IN:
....destination
....day of week
....row number (of flight)
....carry-on number
....premium flight options (y/n)

I certify that this code is mine, and mine alone,
in accordance with GVSU academic honesty policy.

-->GITHUB REPO:
https://github.com/nbiish/GVSU-spring2024/tree/main/project_1

COMPLETION DATE: 2/11/24
"""

#CALCULATES COSTS BY
  #DESTINATION
  #DAY
  #ROW
  #BAGGAGE
def fare_calculation(destination, day, row, number_of_bags, is_premium_plus):

  #MAIN FUNCTION VARIABLES
  fare = 0
  subtotal = 0
  tax = 0
  total = 0
  summary = ''

  #DETERMINE FIRST CLASS
  first_class_charge = 0
  first_class_yes_no = 'NO'
  is_first_class = False
  if 8>row>0:
    is_first_class = True
    first_class_yes_no = 'YES'
  first_class_summary = ''

  #DETERMINE ADDITIONAL CHARGES
  additional_charges = 0
  premium_seating_yes_no = 'NO'
  is_exit_row = False
  is_leg_room_row = False
  exit_row_charge = 49
  leg_room_charge = 35

  #PREMIUM PLUS DISCOUNT FOR PREMIUM SEATING
  if is_premium_plus:
    exit_row_charge = 0
    leg_room_charge = 0
  if 13<row<16:
    is_exit_row = True
    premium_seating_yes_no = 'YES'
  elif 7<row<14 or 15<row<21:
    is_leg_room_row = True
    premium_seating_yes_no = 'YES'
  premium_charge_summary = ''

  #DETERMINE BAGGAGE COSTS
  def baggage_pricing(number_of_bags):
    baggage_cost = 0
    if is_premium_plus:
        number_of_bags -= 1
    if number_of_bags == 1:
      baggage_cost = 35
    elif number_of_bags > 1:
      baggage_cost = ((number_of_bags-1) * 25)+35

    return baggage_cost
  baggage_summary = ''

  #DFW PRICING BY DAY
  def dfw_pricing(day):
    fare = 0
    if day == 'MON':
      fare = 213
    elif day == 'TUE':
      fare = 198
    elif day == 'WED':
      fare = 198
    elif day == 'THU':
      fare = 213
    elif day == 'FRI':
      fare = 399
    elif day == 'SAT':
      fare = 213
    elif day == 'SUN':
      fare = 198
    return fare

  #LAX PRICING BY DAY
  def lax_pricing(day):
    fare = 0
    if day == 'MON':
      fare = 334
    elif day == 'TUE':
      fare = 314
    elif day == 'WED':
      fare = 314
    elif day == 'THU':
      fare = 334
    elif day == 'FRI':
      fare = 429
    elif day == 'SAT':
      fare = 334
    elif day == 'SUN':
      fare = 314
    return fare

  #MIA PRICING BY DAY
  def mia_pricing(day):
    fare = 0
    if day == 'MON':
      fare = 279
    elif day == 'TUE':
      fare = 204
    elif day == 'WED':
      fare = 204
    elif day == 'THU':
      fare = 279
    elif day == 'FRI':
      fare = 370
    elif day == 'SAT':
      fare = 279
    elif day == 'SUN':
      fare = 204
    return fare

  #SEA PRICING BY DAY
  def sea_pricing(day):
    fare = 0
    if day == 'MON':
      fare = 315
    elif day == 'TUE':
      fare = 294
    elif day == 'WED':
      fare = 294
    elif day == 'THU':
      fare = 315
    elif day == 'FRI':
      fare = 430
    elif day == 'SAT':
      fare = 315
    elif day == 'SUN':
      fare = 294
    return fare

  #BOS PRICING BY DAY
  def bos_pricing(day):
    fare = 0
    if day == 'MON':
      fare = 241
    elif day == 'TUE':
      fare = 205
    elif day == 'WED':
      fare = 205
    elif day == 'THU':
      fare = 241
    elif day == 'FRI':
      fare = 298
    elif day == 'SAT':
      fare = 241
    elif day == 'SUN':
      fare = 205
    return fare

  #CHECK FOR DESTINATION & FIRST_CLASS & ROW CHARGES --> USES FUNCTIONS ABOVE <--
#START IF
  if destination == 'DFW':
    day_of_week_price = dfw_pricing(day) #<-- DFW FUNCTION
    #CHECK FIRST CLASS###############
    if is_first_class:
      first_class_charge = day_of_week_price * 0.75
      subtotal = day_of_week_price + first_class_charge
      first_class_summary = f"First Class Option: {first_class_yes_no}\n-adds ${first_class_charge:.2f}\n{'-'*27}\n"
    #ADD ROW LOGIC###################
    elif is_leg_room_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${leg_room_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + leg_room_charge
    elif is_exit_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${exit_row_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + exit_row_charge
    else:
      subtotal = day_of_week_price
    #BAGGAGE COSTS###################
    if baggage_pricing(number_of_bags) == 0:
      baggage_summary = ''
    elif baggage_pricing(number_of_bags) > 0:
      if is_premium_plus:
        baggage_summary = f"""Baggage costs: ${(baggage_pricing(number_of_bags)):.2f}\n"""
      else:
        baggage_summary = f"""Baggage costs: ${baggage_pricing(number_of_bags):.2f}\n"""
    #################################
    #TOTAL & PRINT##################
    if is_premium_plus:
      tax = (subtotal + 94) * 0.18
      total = (subtotal+94) + tax + baggage_pricing(number_of_bags)
    else:
      tax = subtotal * 0.18
      total = subtotal + tax + baggage_pricing(number_of_bags)
    summary = f"""\n{'*'*27}\nTICKET PRICE SUMMARY:\n\n{'-'*27}\nFare: ${day_of_week_price:.2f}\n{'-'*27}\n{first_class_summary}{premium_charge_summary}\n{'*'*18}\nSubtotal: ${subtotal:.2f}\nPremium: $94\nTaxes: ${tax:.2f}\n{baggage_summary}\nTOTAL: ${total:.2f}\n{'*'*27}"""

#SECOND IF
  elif destination == 'LAX':
    day_of_week_price = lax_pricing(day) #<-- LAX FUNCTION
    #CHECK FIRST CLASS###############
    if is_first_class:
      first_class_charge = day_of_week_price * 0.75
      subtotal = day_of_week_price + first_class_charge
      first_class_summary = f"First Class Option: {first_class_yes_no}\n-adds ${first_class_charge:.2f}\n{'-'*27}\n"
    #ADD ROW LOGIC###################
    elif is_leg_room_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${leg_room_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + leg_room_charge
    elif is_exit_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${exit_row_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + exit_row_charge
    else:
      subtotal = day_of_week_price
    #BAGGAGE COSTS###################
    if baggage_pricing(number_of_bags) == 0:
      baggage_summary = ''
    elif baggage_pricing(number_of_bags) > 0:
      if is_premium_plus:
        baggage_summary = f"""Baggage costs: ${(baggage_pricing(number_of_bags)):.2f}\n"""
      else:
        baggage_summary = f"""Baggage costs: ${baggage_pricing(number_of_bags):.2f}\n"""
    #################################
    #TOTAL & PRINT##################
    if is_premium_plus:
      tax = (subtotal + 94) * 0.18
      total = (subtotal+94) + tax + baggage_pricing(number_of_bags)
    else:
      tax = subtotal * 0.18
      total = subtotal + tax + baggage_pricing(number_of_bags)
    summary = f"""\n{'*'*27}\nTICKET PRICE SUMMARY:\n\n{'-'*27}\nFare: ${day_of_week_price:.2f}\n{'-'*27}\n{first_class_summary}{premium_charge_summary}\n{'*'*18}\nSubtotal: ${subtotal:.2f}\nPremium: $94\nTaxes: ${tax:.2f}\n{baggage_summary}\nTOTAL: ${total:.2f}\n{'*'*27}"""

#THIRD IF
  elif destination == 'MIA':
    day_of_week_price = mia_pricing(day) #<-- MIA FUNCTION
    #CHECK FIRST CLASS###############
    if is_first_class:
      first_class_charge = day_of_week_price * 0.75
      subtotal = day_of_week_price + first_class_charge
      first_class_summary = f"First Class Option: {first_class_yes_no}\n-adds ${first_class_charge:.2f}\n{'-'*27}\n"
    #ADD ROW LOGIC###################
    elif is_leg_room_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${leg_room_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + leg_room_charge
    elif is_exit_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${exit_row_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + exit_row_charge
    else:
      subtotal = day_of_week_price
    #BAGGAGE COSTS###################
    if baggage_pricing(number_of_bags) == 0:
      baggage_summary = ''
    elif baggage_pricing(number_of_bags) > 0:
      if is_premium_plus:
        baggage_summary = f"""Baggage costs: ${(baggage_pricing(number_of_bags)):.2f}\n"""
      else:
        baggage_summary = f"""Baggage costs: ${baggage_pricing(number_of_bags):.2f}\n"""
    #################################
    #TOTAL & PRINT##################
    if is_premium_plus:
      tax = (subtotal + 94) * 0.18
      total = (subtotal+94) + tax + baggage_pricing(number_of_bags)
    else:
      tax = subtotal * 0.18
      total = subtotal + tax + baggage_pricing(number_of_bags)
    summary = f"""\n{'*'*27}\nTICKET PRICE SUMMARY:\n\n{'-'*27}\nFare: ${day_of_week_price:.2f}\n{'-'*27}\n{first_class_summary}{premium_charge_summary}\n{'*'*18}\nSubtotal: ${subtotal:.2f}\nPremium: $94\nTaxes: ${tax:.2f}\n{baggage_summary}\nTOTAL: ${total:.2f}\n{'*'*27}"""

#FOURTH IF
  elif destination == 'SEA':
    day_of_week_price = sea_pricing(day) #<-- SEA FUNCTION
    #CHECK FIRST CLASS###############
    if is_first_class:
      first_class_charge = day_of_week_price * 0.75
      subtotal = day_of_week_price + first_class_charge
      first_class_summary = f"First Class Option: {first_class_yes_no}\n-adds ${first_class_charge:.2f}\n{'-'*27}\n"
    #ADD ROW LOGIC###################
    elif is_leg_room_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${leg_room_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + leg_room_charge
    elif is_exit_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${exit_row_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + exit_row_charge
    else:
      subtotal = day_of_week_price
    #BAGGAGE COSTS###################
    if baggage_pricing(number_of_bags) == 0:
      baggage_summary = ''
    elif baggage_pricing(number_of_bags) > 0:
      if is_premium_plus:
        baggage_summary = f"""Baggage costs: ${(baggage_pricing(number_of_bags)):.2f}\n"""
      else:
        baggage_summary = f"""Baggage costs: ${baggage_pricing(number_of_bags):.2f}\n"""
    #################################
    #TOTAL & PRINT##################
    if is_premium_plus:
      tax = (subtotal + 94) * 0.18
      total = (subtotal+94) + tax + baggage_pricing(number_of_bags)
    else:
      tax = subtotal * 0.18
      total = subtotal + tax + baggage_pricing(number_of_bags)
    summary = f"""\n{'*'*27}\nTICKET PRICE SUMMARY:\n\n{'-'*27}\nFare: ${day_of_week_price:.2f}\n{'-'*27}\n{first_class_summary}{premium_charge_summary}\n{'*'*18}\nSubtotal: ${subtotal:.2f}\nPremium: $94\nTaxes: ${tax:.2f}\n{baggage_summary}\nTOTAL: ${total:.2f}\n{'*'*27}"""

#FINAL ELIF
  elif destination == 'BOS':
    day_of_week_price = bos_pricing(day) #<-- BOS FUNCTION
    #CHECK FIRST CLASS###############
    if is_first_class:
      first_class_charge = day_of_week_price * 0.75
      subtotal = day_of_week_price + first_class_charge
      first_class_summary = f"First Class Option: {first_class_yes_no}\n-adds ${first_class_charge:.2f}\n{'-'*27}\n"
    #ADD ROW LOGIC###################
    elif is_leg_room_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${leg_room_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + leg_room_charge
    elif is_exit_row:
      if is_premium_plus:
        subtotal = day_of_week_price
        premium_charge_summary = ''
      else:
        premium_charge_summary = f"Premium Row Charges: {premium_seating_yes_no}\n-adds ${exit_row_charge:.2f}\n{'-'*27}\n"
        subtotal = day_of_week_price + exit_row_charge
    else:
      subtotal = day_of_week_price
    #BAGGAGE COSTS###################
    if baggage_pricing(number_of_bags) == 0:
      baggage_summary = ''
    elif baggage_pricing(number_of_bags) > 0:
      if is_premium_plus:
        baggage_summary = f"""Baggage costs: ${(baggage_pricing(number_of_bags)):.2f}\n"""
      else:
        baggage_summary = f"""Baggage costs: ${baggage_pricing(number_of_bags):.2f}\n"""
    #################################
    #TOTAL & PRINT##################
    if is_premium_plus:
      tax = (subtotal + 94) * 0.18
      total = (subtotal+94) + tax + baggage_pricing(number_of_bags)
    else:
      tax = subtotal * 0.18
      total = subtotal + tax + baggage_pricing(number_of_bags)
    summary = f"""\n{'*'*27}\nTICKET PRICE SUMMARY:\n\n{'-'*27}\nFare: ${day_of_week_price:.2f}\n{'-'*27}\n{first_class_summary}{premium_charge_summary}\n{'*'*18}\nSubtotal: ${subtotal:.2f}\nPremium: $94\nTaxes: ${tax:.2f}\n{baggage_summary}\nTOTAL: ${total:.2f}\n{'*'*27}"""

#END IF - NO ELSE
  return summary


#######################################################
print("---Enter Information---\n")
destination = input("Destination Options:\nDFW LAX MIA SEA BOS --> ").upper()
day = input("\nDay of week:\nMON TUE WED THU FRI SAT SUN --> ").upper()
if day not in ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']:
  day = 'MON'
row = input("\nDesired Row Number: ")
#PREMIUM PLUS##############
number_of_bags = input("\nBaggage:\n-First carry-on + $35(free for Premium Plus)\n-Additional carry-on + $25\n\nNumber of carry-on bags: ")
premium_plus_ticket = input("\nAdd Premium-Plus for $94:\n-no change fee\n-one free checked bag\n-FREE Premium seating\n\n(y/n): \n").upper()
is_premium_plus = False
premium_plus_intro = ''
is_not_premium_plus_cost = ' + $35'
if 'Y' in premium_plus_ticket:
  is_premium_plus = True
  is_not_premium_plus_cost = ''
  premium_plus_intro = f"\nPremium Plus members:\n"
###########################
print(f"\nDesired Seating:\n-First Class (Rows 1-7) + 75%\n-Exit Row (Rows 14-15) + $49\n-Premium Seating: (Rows 8-13, 16,20){is_not_premium_plus_cost}\n-No Charge: (Rows 21-35)")

if (destination not in ['DFW', 'LAX', 'MIA', 'SEA', 'BOS']):
  print("\n--> Oops! Destination must be DFW, LAX, SEA, MIA or BOS.")
elif (not row.isdigit()) or (not (0<int(row)<36)):
  print("\n--> Oops! Row must be 1 - 35.")
elif (day not in ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']) or (not number_of_bags.isdigit()) or (premium_plus_ticket not in ['Y', 'N']):
  print("\nERROR:\nWrong input type for one or multiple choices.")
else:
  number_of_bags = int(float(number_of_bags))
  row = int(float(row))
  print(fare_calculation(destination, day, row, number_of_bags, is_premium_plus))