# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''


# There is only one key in the datastore dictionary, which is "medical". 
# The value associated with this key is a list of dictionaries. 
# Each dictionary in the list represents a room in the doctor's office and contains key-value pairs for the room number, use, square footage, and price. 

datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}


outfile = open('retail_space.csv', 'w')
outfile.write('room-number,use,sq-ft,price\n')

# Below is the code that will loop through the list of dictionaries in the "medical" key of the 
# datastore dictionary and write the details of each room to the 'retail_space.csv' file in the specified format.
'''
list_of_offices = datastore["medical"]

for office in list_of_offices:
    # print(type(office))
    # print(office)
    roomno = office["room-number"]
    use = office["use"]
    sq_ft = office["sq-ft"]
    price = office["price"]

    outfile.write(str(roomno)+','+ use + ',' + str(sq_ft) + ',' + str(price)+ '\n')

outfile.close()

'''
# The above code can be simplified by directly looping through the list of dictionaries
# in the "medical" key of the datastore dictionary without assigning it to a separate variable.
# MUCH MORE EFFICIENT WAY TO WRITE THE CODE BELOW:

for office in datastore["medical"]:
    
    outfile.write(str(office["room-number"])+','+ office["use"] + ',' + str(office["sq-ft"]) + ',' + str(office["price"])+ '\n')

outfile.close() 


# The code below will use the pickle module to save the datastore dictionary to a file called "datastore.dat".
# The pickle module is used to serialize and deserialize Python objects, 
# allowing you to save complex data structures like dictionaries to a file and load them back into memory later.
import pickle


pickle_file = open("datastore.dat","wb" )
pickle.dump(datastore, pickle_file)
pickle_file.close()


