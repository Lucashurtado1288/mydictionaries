"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json

#opening the JSON file
file = open('school_data.json', 'r')

# Converting the JSON data into a python list of dictionaries
schools = json.load(file)


# Looping through schools listed in conferences: ACC, Big 12, Big Ten and SEC.
# Filter that will only include schools with the conference requirements listed above. 
filtered_schools = []

for school in schools: 
    # Creating variable to avoid writing out lengthy keys (two keys "NCAA" and "NCAA/NAIA conference number football (IC2020)")
    # Two keys are nested in the school_data.josn, the reason for listed them both as shown below. 
    conf = school['NCAA']["NAIA conference number football (IC2020)"]

    # Further filtering within conf variable that will append school dictionary to only include specific conferences.
    if conf in [372, 108, 107, 130]:
        filtered_schools.append(school)
    


# (a) Graduation report
# Looping through every school in the list, school represents one dictionary at a time
# All schools with key "Graduation rate  women (DRVGR2020)" that is greater than 75%
    # Format to SchoolReport1

for school in filtered_schools: 
    grad_rate = school["Graduation rate  women (DRVGR2020)"]
    if grad_rate != None and grad_rate > 75:
        # Printing university name
        print ("University: " + school["instnm"])
        # Convert grad_rate to str and add % symbol to match format
        print("Graduation Rate for Women: " + str(grad_rate) + "%")
        print()




# (b) Cost report
# Loop through all schools again with key "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
# whose costs are 60,000 and above
    # format according to SchoolReport2

for school in filtered_schools:
    # Total price for in-state students living off campus
    cost = school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]
    if cost != None and cost > 60000:
        # Print school name
        print("University: " + school["instnm"])
        print("Total price for in-state students living off campus: $" + format(cost, ",.2f"))
        print()


