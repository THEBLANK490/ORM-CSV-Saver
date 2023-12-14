import csv
import os 

class CSV_Saver:
    id = 0
    
    #constructor for the CSV_Saver class 
    def __init__(self,file_name):
        self.file_name = file_name
        self.data =[]

    # a method to read the data from csv file
    def reading(self):
        with open(self.file_name,'r',newline='') as file :
            csv_reader = csv.DictReader(file)
            self.data = list(csv_reader)
            return self.data

    #a method for creating new data in csv file
    def create_data(self,new_data):
        with open(self.file_name,'a',newline='') as file :
            fieldnames = ["id","Name","Age","City"]
            csv_write = csv.DictWriter(file, fieldnames=fieldnames)
            
            if not os.path.isfile(self.file_name):
                csv_write.writeheader()
            csv_write.writerow(new_data)

    # a method for updating the rows in the csv file 
    def updating(self, id, updated_data):
        found = False
        #read the CSV file 
        rows = self.reading()
        #iterate through the rows and select the specified ID to update and set the flag(found) to True
        for i, row in enumerate(rows):
            if row["id"] == str(id):
                rows[i] = updated_data
                found = True
                break

        #if found then update the value else say row doesnot exists
        if found:
            with open(self.file_name, 'w', newline='') as file:
                fieldnames = ["id","Name","Age","City"]
                csv_writer = csv.DictWriter(file,fieldnames=fieldnames) #csv writer dict object
                csv_writer.writeheader()
                csv_writer.writerows(rows) # write the updated rows back to csv_file
            print(f"Row with ID {id} updated successfully.")
        else:
            print(f"Row with ID {id} does not exist.")
        

    #a method for deleting the rows in the csv file
    def deleting_data_rows(self, id_to_delete):
        found = False
        # Read the CSV file
        rows = self.reading()
        # Check if the row with the specified ID exists
        for i, row in enumerate(rows):
            if row["id"] == str(id_to_delete):
                found = True
                del rows[i]  # Remove the row if found
                break

        if found:
            with open(self.file_name, 'w', newline='') as file:
                fieldnames = ["id","Name","Age","City"]
                csv_writer = csv.DictWriter(file,fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(rows)
            print(f"Row with ID {id_to_delete} deleted successfully.")
        else:
            print(f"Row with ID {id_to_delete} does not exist.")

    #a static method to crete the heading row in the csv file
    @staticmethod
    def create_CSV(file_name,heading):
        with open(file_name,"w", newline='') as file:
            csv_write = csv.writer(file)
            csv_write.writerow(heading)
        print("File Created.\n") 

    #a method to read the input from the user and returns them in a dict to update the data
    @classmethod
    def get_new_data_for_update(cls):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter the city name: ")
        return {"id": cls.id, "Name": name, "Age": age, "City": city}
    
    #a method to read the input from the user and returns them in a dict to write the data
    @classmethod
    def get_new_data(cls):
        cls.id += 1
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter the city name: ")
        return {"id": cls.id, "Name": name, "Age": age, "City": city}

class CSV_Operation(CSV_Saver):
    # This child class will provide a tailored interface for specific data manipulation tasks.
    def __init__(self,file_name):
        super().__init__(file_name)

    def create(self):
        new_data = self.get_new_data()
        self.create_data(new_data)

    def update(self,id,updated_data):
        self.updating(id,updated_data)

file_name = "test.csv"

#create an object of the parent class CSV_Saver
csv_saver = CSV_Saver(file_name)

while True:
    print("""Select from the below table:
        1. Press 1 to create the table with the heading.
        2. Press 2 to write the data into the table.
        3. Press 3 to read the data from the table. 
        4. Press 4 to update the data.
        5. Press 5 to delete the data.
        6. Press 6 to write the data into the table from child class. 
        7. Press 7 to update the data into the table from child class.\n
        8. Press 8 to exit.""")
        
    
    choice = input("Enter YOur Choice: ")
    if choice == '1':
        if not os.path.isfile(file_name):
            heading = ["id","Name", "Age", "City"]
            # calling the static method to create the heading 
            CSV_Saver.create_CSV(file_name,heading)
        else:
            print("File already exists.\n")

    elif choice == '2':
        if os.path.isfile(file_name):
            #ask the user for input by accessing the method in the csv_saver class
            new_data =  csv_saver.get_new_data()
            #to create the data accessing the create_data method 
            csv_saver.create_data(new_data)
        else:
            print("Please create a table by pressing 1. \n")

    elif choice == '3':
        if os.path.isfile(file_name):
            #access the method reading in the CSV_saver class
            result = csv_saver.reading()
            print(result)
        else:
            print("Please create a table by pressing 1. \n")

    elif choice == '4':
        if os.path.isfile(file_name):
            index_to_update = int(input("Enter the Id to update: "))
            updated_data = csv_saver.get_new_data_for_update()
            csv_saver.updating(index_to_update, updated_data)
        else:
            print("Please create a table by pressing 1. \n")

    
    elif choice == '5':
        if os.path.isfile(file_name):
            id_to_delete = input("Enter the ID to delete: ")
            csv_saver.deleting_data_rows(id_to_delete)
        else:
            print("Please create a table by pressing 1. \n")

    elif choice == '6':
        if os.path.isfile(file_name):
            csv_operation = CSV_Operation(file_name)
            csv_operation.create()
        else:
            print("Please create a table by pressing 1. \n")
    
    elif choice == '7':
        if os.path.isfile(file_name):
            index_to_update = int(input("Enter the Id to update: "))
            updated_data = csv_saver.get_new_data_for_update()
            csv_operation = CSV_Operation(file_name)
            csv_operation.update(index_to_update, updated_data)
        else:
            print("Please create a table by pressing 1. \n")
    
    elif choice == '8':
        break

    else:
        print("Invalid choice. Please enter a valid option.")