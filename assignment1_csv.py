import csv

class CSV_Saver:
    # that offers a comprehensive set of methods for managing CSV data.
    # reading
    # writing
    # updating 
    # deleting in rows
    # static method to create a new CSV file with specified column headings 
    def __init__(self,file_name):
        self.file_name = file_name

    def reading(self):
        with open(self.file_name,'r') as file :
            print(file.readlines())

    def updating(self):
        with open(self.file_name,'a') as file :
            pass

    def deleting_data_rows(self):
        pass

    @staticmethod
    def create_CSV(file_name,heading):
        with open(file_name,"w") as file:
            csv_write = csv.writer(file)
            csv_write.writerows(heading)

class CSV_Operation(CSV_Saver):
    # This child class will provide a tailored interface for specific data manipulation tasks.
    def __init__(self)-> None:
        super().__init__()
        # initialize the CSV file nave and column headings
        pass
    # methods to Create , Update data rows, utilizing functionalities from parent class   
    pass

file_name = "test.csv"
headings = ["Name", "Age", "City"]

CSV_Saver.create_CSV(file_name,headings)
csv_saver = CSV_Saver(file_name)
csv_saver.reading()

