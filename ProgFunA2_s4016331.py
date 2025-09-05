#Name: Priyanka Tiwari
#StudentID:S4016331
#Highest Level:HD (Displaying booking history)



#Custom Exception for InvalidCustomer, InvalidNameError, InvalidLocationError, InvalidRateType, InvalidDistanceError, InvalidPrice, InvalidDiscount_rate
#All custom exception are subclass of Exception main class
class InvalidCustomer(Exception):
    pass

class InvalidNameError(Exception):
    pass

class InvalidLocationError(Exception):
    pass

class InvalidRateType(Exception):
    pass

class InvalidDistanceError(Exception):
    pass
class InvalidPrice(Exception):
    pass

class InvalidDiscount_rate(Exception):
    pass

#defining the customer class
#Id,name are the attributes which are instance variables
#using property decorator to ID and name variables also setter is used
#get_discount and display_info are empty super methods
#Customer class is a Parent class of all customers

class Customer:
    def __init__(self, ID, name):
        self.__ID = int(ID)
        self.__name = name

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def get_discount(self):
        pass

    def display_info(self):
        pass

#BasicCustomer is subclass of Customer
#It extends the variables and methods from the super class customer
#ID and name are used from super class
#discount_rate is a instance varaible which is set to 0.1 by default
#display_info method is used to display the information of customer which is ID, name and discount_rate
#get_discount_rate is used to get the discount
#set_discount_rate is used to set the discount of all basic customers
class BasicCustomer(Customer):
    def __init__(self, ID, name, discount_rate=0.1):
        super().__init__(ID, name)
        self.__discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self.__discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate):
        self.__discount_rate = discount_rate

    def get_discount(self, distance_fee):
        return self.discount_rate * distance_fee

    def display_info(self):
        print(f"{self.ID}, {self.name}, {self.discount_rate:.2f}")

    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate

#Enterprise Customer is also a subclass of Customer
#it also extends ID and name from Customer class
#beside ID and name Enterprise customer has low_rate and threshold which are by default 0.15 and 100 respectively
#getter and setter of each instance variables are set
#high_rate is calculated from low_rate which is 5% more than low_rate
#get_threshold, set_threshold are the method to get the threshold and set a new value to the threshold
#get_discount is a method to get the discount_rate for the enterprise customer.
#if the distance_fee is lesser than threshold than low_discount rate is applied or else high discount rate is applied.
#display_info is a method to display the data
#set_discount_rate is used to change the discount_rate 
#if high_rate is not set then it can be calculated based on low_rate

class EnterpriseCustomer(Customer):
    def __init__(self, ID, name, low_rate=0.15, threshold=100):
        super().__init__(ID, name)
        self.low_rate = low_rate
        self.high_rate = low_rate + 0.05
        self.threshold = threshold

    @property
    def low_rate(self):
        return self.__low_rate

    @low_rate.setter
    def low_rate(self, low_rate):
        self.__low_rate = low_rate

    @property
    def high_rate(self):
        return self.__high_rate

    @high_rate.setter
    def high_rate(self, high_rate):
        self.__high_rate = high_rate

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_discount(self, distance_fee):
        if distance_fee < self.threshold:
            return self.low_rate * distance_fee
        else:
            return self.high_rate * distance_fee

    def display_info(self):
        print(f"{self.ID}, {self.name}, {self.low_rate:.2f}, {self.high_rate:.2f},{self.threshold}")

    def set_discount_rate(self, low_rate, high_rate=None):
        self.low_rate = low_rate
        if high_rate is None:
            high_rate = low_rate + 0.05
        self.high_rate = high_rate

#location class is having location_ID and name as  instance variables
#getter and setters are used for Location_ID and name
#display_info is a method for displaying Location_ID and name
class Location:
    def __init__(self, location_ID, name):
        self.location_ID = location_ID
        self.name = name

    @property
    def location_ID(self):
        return self.__location_ID

    @location_ID.setter
    def location_ID(self, location_ID):
        self.__location_ID = location_ID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def display_info(self):
        print(self.location_ID, self.name)
#Rate class is having rate_ID, name and price as instance variables
#getter and setters are used for rate_ID, name and price
#display_info is a method for displaying rate_ID, name and price
class Rate:
    def __init__(self, rate_ID, name, price):
        self.rate_ID = rate_ID
        self.name = name
        self.price = price

    @property
    def rate_ID(self):
        return self.__rate_ID

    @rate_ID.setter
    def rate_ID(self, rate_ID):
        self.__rate_ID = rate_ID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def display_info(self):
        print(self.rate_ID, self.name, self.price)

#Service class has three variables service_id, service_name and price
#getter and setter of each variables are set
#display_info() is a method to display the service_id, service_name and price
class Service:
    def __init__(self, service_id, service_name, price):
        self.__service_id = service_id
        self.__service_name = service_name
        self.__price = price
    @property
    def service_id(self):
        return self.__service_id
    @property
    def service_name(self):
        return self.__service_name
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price

    def display_info(self):
        print(f"Service ID: {self.service_id}, Name: {self.service_name}, Price: {self.price} AUD")



#Package is a subclass of Service and has 3 variables 
#package_id, name and service which is a list of services
#since service is super class getter and setter for package_id and name are inherited from Service class
#calculate_price is a method to sum up of the service prices of individual services and give 20% discount on the total_price
#same like services displaying the information of packages with their id, name of package plus the list of services name and prices associated with them.
class Package(Service):
    def __init__(self, package_id, name, *service):
        super().__init__(package_id, name, price=0)
        self.service = list(service)

    @property
    def service(self):
        return self.__service
    
    service.setter
    def service(self, service):
        self.__service = service

    def calculate_price(self):
        total_price = sum(service.price for service in self.service)
        price = 0.8 * total_price
        return price
    

    def display_info(self):
        print(f"\nPackage ID: {self.service_id}, Name: {self.service_name}")
        print("Services:")
        for service in self.service:
            print(f"Name: {service.service_name},Price: {service.price} AUD")
        
#class Booking take 6 instance variables in which service is a list.
#getter and setter are used to get and set the variables
#compute_cost() is a method of calculating the total_cost 
#it takes one parameter which is selected_services by default it is set as None
#the basic_fee is set as 4.2 for all the customer
#discount is set as 0 initially
#since distance is treated as a string at first we are converting it into float.
#distance_fee is calculated by using distance and rate_price of the selected rate
#Now if a customer is an instance of Customer class which can be basic or enterprise customer then discount is given to them
#get_discount is used to return the discount of a particular type of customer
#if a customer has services selected then only service_fee is calculated.
#now service_fee can be decided based on whether the cutomer has chosen service or package
#if it is an instance of package then calculate function of package is called or else price of a service is directly set.
#total_cost is addition of distance_fee, basic_fee and discount is given only on distance_fee
#service_fee is also added to total_cost.
#the function return distance_fee, basic_fee,discount, service_fee and total_cost.

class Booking:
    def __init__(self, customer, departure, destination, distance, rate, service=[]):
        self.customer = customer
        self.departure = departure
        self.destination = destination
        self.distance = distance
        self.rate = rate
        self.service = service

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, departure):
        self.__departure = departure

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        self.__destination = destination

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance):
        self.__distance = distance

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        self.__rate = rate
    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, service):
        self.__service = service

    def compute_cost(self,selected_service=None):
        basic_fee = 4.2
        discount = 0
        distance = float(self.distance)

        distance_fee = distance * self.rate.price
        if isinstance(self.customer, Customer):
            discount = self.customer.get_discount(distance_fee)
        if selected_service:
            service_fee = selected_service.calculate_price() if isinstance(selected_service,Package) else selected_service.price
        else:
            service_fee = 0

        total_cost = distance_fee + basic_fee - discount+service_fee
        return distance_fee, basic_fee, discount,service_fee,total_cost
    
#class Records is used to read, find, display the existing customer, location, rates and services 
#each file is read by using with open function in a read mode
#each character is separated using comma and read.
#customer_dictionary is used to store the customer_ID and name of the customer
#since there are two type of customer Basic and enterprise the number of character will be different after the type of customer so reading accordingly.
# finally appending customer to existing_customers list   
#similarly reading location, rate and services files and storing them in lists separately.
#read_booking is used to read the data from the booking.txt file. here each booking is stored in the bookings list.
#using positive and negative indexing and slicing too.
#add_booking is a method to add new booking to the bookings list.
#get_booking is a method to extract the booking based on customer_name in the bookings list.
#find_customer, find_location, find_rate and find_service are methods to check it a particular data i.e id or name (customer, location, rate or service) is existing or no
#generate_new_location_id is used to generate a new location id based on the last existing location id or else by deafult it is set as L1.
#add_location is used to add new locations to the exisiting location list. it checks if the location is already present in existing_location_list or not
#if it is present it won't add that location else it will update the location-list and add the new location.
#list_customer, list_location, list_rate, list_service and list_booking are used to display customer, location, rate, services and booking which are existing.
#add_update_rate is used to add a new rate type and it's price rate_id is generated based on previous rate_ID and add them to the existing rate_type list
#if a rate_type already exists then it will just update the price of the particular rate_type 
#get_most_valuable_customer is a method for getting the customer who has max total_cost value
#here price is also checked for errors
#displaying the valuable_customer based on it's total_cost which is stored in the bookings.
#booking_history is used to display the booking of a particular customer.

class Records:

    def __init__(self):
        self.existing_customers = []
        self.existing_locations = []
        self.existing_rate_types = []
        self.services = []
        self.customer_dictionary = {}
        

    def read_customers(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    fields_from_line = line.strip().split(",")
                    customer_ID = fields_from_line[0].strip()
                    customer_name = fields_from_line[1].strip()
                    customer_type = fields_from_line[2].strip()
                    customer_dictionary={int(customer_ID):customer_name}
                    if customer_type == "B":
                        discount_rate = float(fields_from_line[3].strip())
                        customer = BasicCustomer(customer_ID, customer_name, discount_rate)
                    elif customer_type == "E":
                        discount_rate = float(fields_from_line[3].strip())
                        threshold = float(fields_from_line[4].strip())
                        customer = EnterpriseCustomer(customer_ID, customer_name, discount_rate, threshold)
                    self.existing_customers.append(customer)
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")

    def read_locations(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    fields_from_line = line.strip().split(",")
                    location_ID = fields_from_line[0].strip()
                    name = fields_from_line[1].strip()
                    location = Location(location_ID, name)
                    self.existing_locations.append(location)
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")

    def read_rates(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    fields_from_line = line.strip().split(",")
                    rate_ID = fields_from_line[0].strip()
                    name = fields_from_line[1].strip()
                    price = float(fields_from_line[2].strip())
                    rate = Rate(rate_ID, name, price)
                    self.existing_rate_types.append(rate)
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
    
    def read_services(self, file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    field_from_line = line.strip().split(',')
                    if field_from_line[0].startswith("S"):
                        name= field_from_line[1].strip()
                        price =float(field_from_line[2])
                        service = Service(field_from_line[0],name,price)
                        self.services.append(service)
                    elif field_from_line[0].startswith("P"):
                        service_ids = field_from_line[2:]
                        service_ids_strip=[]
                        for s in service_ids:
                            s=s.strip()
                            service_ids_strip.append(s)
                        component_services = [s for s in self.services if s.service_id in service_ids_strip]
                        package = Package(field_from_line[0], field_from_line[1], *component_services)
                        self.services.append(package)
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
    
    def read_booking(self, file_name):
        self.bookings=[]
        try:
            with open(file_name,"r") as file:
                for line in file:
                    field_from_line =line.strip().split(",")

                    booking ={
                    "customer_name": field_from_line[0].strip(),
                    "departure" : field_from_line[1].strip(),
                    "destination":field_from_line[2:-7:2],
                    "distance":field_from_line[3:-6:2],
                    "rate_type":field_from_line[-6].strip(),
                    "service":field_from_line[-5].strip(),
                    "basic_fee":field_from_line[-4].strip(),
                    "distance_fee":field_from_line[-3].strip(),
                    "discount" :field_from_line[-2].strip(),
                    "total_cost":field_from_line[-1].strip(),
                    }
                    self.bookings.append(booking)


        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
            return []


    def add_booking(self, booking):
        self.bookings.append(booking)

    def get_bookings(self):
        booking_history={}
        for booking in self.bookings:
            if 'customer_name' in booking:
                customer_name=booking['customer_name']
                if customer_name in booking_history:
                    booking_history[customer_name].append(booking)
                else:
                    booking_history[customer_name]=[booking]
            else:
                print("Missing Customer name:")
        return booking_history
   
    def find_customer(self, search_value):
        for customer in self.existing_customers:
            if str(search_value) == str(customer.ID) or search_value == customer.name:
                return customer
        return None

    def find_location(self, search_value):
        for location in self.existing_locations:
            if str(search_value) == str(location.location_ID) or search_value == location.name:
                return location
        return None
    
    def find_rate(self, search_value):
        for rate in self.existing_rate_types:
            if str(search_value) == str(rate.rate_ID) or search_value == rate.name:
                return rate
        return None
    
    def find_service(self, search_value):
        for service in self.services:
            if str(search_value)==str(service.service_id) or search_value==service.service_name:
                return service
        return None
    
    def generate_new_location_id(self):
        existing_numbers = [int(location.location_ID[1:]) for location in self.existing_locations if location.location_ID.startswith('L')]
    
        if existing_numbers:
            new_location_id = f"L{max(existing_numbers) + 1}"
        else:
            new_location_id = "L1"
    
        return new_location_id

    def add_location(self, location_names):
        for location_name in location_names:
            location_name = location_name.strip()
            if self.find_location(location_name):
                continue
        
            location_id = self.generate_new_location_id()
            location = Location(location_id, location_name)
            self.existing_locations.append(location)
            print(f"Added location: {location_id}, {location_name}")

   
    def list_customers(self):
        for customer in self.existing_customers:
            customer.display_info()

    def list_locations(self):
        for location in self.existing_locations:
            location.display_info()

    def list_rates(self):
        for rate in self.existing_rate_types:
            rate.display_info()
    
    def list_services(self):
         for service in self.services:
             service.display_info()

    def list_booking(self):
        for booking in self.bookings:
            print(booking)

    def add_update_rate(self, name, price):
        try:
            if not name.isalpha():
                raise InvalidRateType("Name of rate type can contain only alphabets.")
            price = float(price)
            if price<=0:
                raise InvalidPrice("Price can not be negative.")
        except ValueError:
            raise InvalidPrice("Invalid input given for the price.")
        rate =self.find_rate(name)
        if not rate:
            new_rate_ID = f"R{len(self.existing_rate_types)+1}"
            new_rate = Rate(new_rate_ID, name, price)
            self.existing_rate_types.append(new_rate)
        else:
            rate.price=price

    def get_most_valuable_customer(self, booking_history):
        customers_total_spent = {
            customer: sum(booking['total_cost'] for booking in bookings)
            for customer, bookings in booking_history.items()
        }

        if customers_total_spent:
            most_valuable_customer = max(customers_total_spent, key=customers_total_spent.get)
            max_spent = customers_total_spent[most_valuable_customer]
            return most_valuable_customer, max_spent
        else:
            return None, 0
        
    def valuable_customer(self):
        booking_history = self.get_bookings()
        most_valuable_customer, max_spent = self.get_most_valuable_customer(booking_history)
        if most_valuable_customer:
            print(f"Customer Name: {most_valuable_customer}")
            print(f"Total Cost: {max_spent:.2f}(AUD)")
        else:
            print("No bookings found.")




    def booking_history(self, customer_name):
        customer_history = [booking for booking in self.bookings if booking['customer_name'] == customer_name]

        if not customer_history:
            print("No booking history found for customer:", customer_name)
        else:
            print(f"Booking History for {customer_name}:\n")
            for i,booking in enumerate(customer_history, start=1):
                print(f"Booking {i}")
                print("{:<20}".format("Departure:"), booking['departure'])
                print("{:<20}".format("Destination:"), ', '.join(booking['destination']))
                print("{:<20}".format("Service:"), booking['service'])
                print("{:<20}".format("Total Cost:"), booking['total_cost'])

#class operations has records as an instance variable.
#now the files are loaded
#display_menu has 13 options based on this the user can enter their choice.
#1.Book a trip2. Existing Customers3. Existing Locations4. Existing Rate Types5. Existing Services and Packages6. Add new locations7. Adjust the discount rate for Basic customer
#8. Adjust the discount rate for Enterprise Customer 9. Add/Update rate types and prices
#10. Display all booking 11. Most Popluar customer 12. Booking history of Customer 13. Exit
#for each option their respestive functions are called here.
#adjust_discount_rate_basic_customer and adjust_discount_rate_enterprise_custome is used to set a new discount rate for the basic customer or enterprise customer
#exception are handled here for discount type and customer_type.
#add_or_update_rate_type is for taking input from the user for rate_name and rate_price
#exceptions for invalidratetypes and invalidprice are handled.
#book_trip is a method for booking a trip
# here the the inputs from the customer are taken handled for exceptions for each input and given them chances to enter again
#if a customer exists in the existing_customer list then printing the customer type
#else generating the customer id
#be default all the new customer are  Basic customers
#there are given 0 discount on first booking and after wards are given discount rate of basic customer
#adding them to the existing_csutomer list.
#once the all inputs are received from the user the receipt gets printed.
#after that all the data is stored in the bookings list 
#objects of both records and operation are created and object records is passed into operations
#displaying the main_menu
#for command_line sys module is imported
#the length of the arguments is checked if it is less than 4 the program exits
#else argv are set respectively
#if the len is more than 5 then bookings file is also set.
#similarly loading of the data files is done and displaying the menu on the shell.

class Operations:
    def __init__(self, records):
        self.records = records
        self.load_data()

    def load_data(self):
        self.records.read_customers("customers.txt")
        self.records.read_locations("locations.txt")
        self.records.read_rates("rates.txt")
        self.records.read_services("services.txt")
        self.records.read_booking("bookings.txt")

    def display_menu(self):
        while True:
            print("1. Book a trip\n2. Existing Customers\n3. Existing Locations\n4. Existing Rate Types\n5. Existing Services and Packages\n6. Add new locations\n7. Adjust the discount rate for Basic customer")
            print("8. Adjust the discount rate for Enterprise Customer\n9. Add/Update rate types and prices\n10. Display all booking\n11. Most Popluar customer\n12. Booking history of Customer\n13. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.book_trip()

            elif choice == "2":
                print("-" * 50)
                print("The following are existing Customers")
                self.records.list_customers()
                print("-" * 50)

            elif choice == "3":
                print("-" * 50)
                print("The following are the existing locations")
                self.records.list_locations()
                print("-" * 50)

            elif choice == "4":
                print("-" * 50)
                print("The following are existing rate types")
                self.records.list_rates()
                print("-" * 50)

            elif choice == "5":
                print("-" * 50)
                print("The following are existing services and packages available")
                self.records.list_services()
                print("-" * 50)

            elif choice == "6":
                print("-" * 50)
                new_location = input("Please enter the new locations separated by commas:")
                new_location = [l.strip() for l in new_location.split(",")]
                print("New locations added successfully")
                self.records.add_location(new_location)
                print("-" * 50)

            elif choice == "7":
                print("-" * 50)
                print("Adjust the discount rate of Basic discount rate of customer")
                self.adjust_discount_rate_basic_customer()
                print("-" * 50)

            elif choice == "8":
                print("-" * 50)
                print("Adjust the discount rate of Enterprise customer")
                self.adjust_discount_rate_enterprise_customer()
                print("-" * 50)

            elif choice == "9":
                print("-" * 50)
                print("Add update rate types and prices")
                self.add_or_update_rate_type()
                print("-" * 50)

            elif choice == "10":
                print("-" * 50)
                print("Displaying all the booking")
                self.records.list_booking()
                print("-" * 50)

            elif choice == "11":
                print("-" * 50)
                print("Displaying most valuable customer")
                self.records.valuable_customer()
                print("-" * 50)

            elif choice == "12":
                customer_name=input("Enter customer name:")
                print("-" * 50)
                print("Display a customer booking history")
                self.records.booking_history(customer_name)
                print("-" * 50)
            elif choice == "13":
                print("-" * 50)
                print("Exiting the Taxi Menu")
                break

            else:
                print("Invalid choice. Please select a valid option.")
    
    #new discount_rate for basic customer
    def adjust_discount_rate_basic_customer(self):
        while True:
            try:
                new_rate = float(input("Please enter the new discount rate for Basic customers: "))
                if new_rate < 0:
                    raise InvalidDiscount_rate("Discount rate must be a positive number.")
                new_rate /= 100
                break
            except ValueError:
                print("Invalid input. Please enter a valid discount rate.")

        for customer in self.records.existing_customers:
            if isinstance(customer, BasicCustomer):
                customer.set_discount_rate(new_rate)
                self.records.customer_dictionary[customer.ID] = customer.name
                customer.display_info()
                print(f"Discount rate is updated for Basic customer to: {new_rate * 100:.1f}")

    #new discount rate for enterprise customer
    def adjust_discount_rate_enterprise_customer(self):
        while True:
            customer_id_name = input("Please enter the ID or name of the Enterprise customer: ")
            customer = self.records.find_customer(customer_id_name)

            if customer and isinstance(customer, EnterpriseCustomer):
                break
            else:
                print("Invalid customer. Please enter a valid customer ID or name.")

        while True:
            try:
                new_low_rate = float(input("Enter the new low discount rate for the Enterprise customer: "))
                if new_low_rate < 0:
                    raise InvalidDiscount_rate("Discount rate must be a positive number.")
                new_low_rate /= 100 
                break
            except ValueError:
                print("Invalid input. Please enter a valid discount rate.")

        customer.set_discount_rate(new_low_rate)
        self.records.customer_dictionary[customer.ID] = customer.name
        customer.display_info()  
        print(f"Discount rates are updated for Enterprise customer Low Rate: {new_low_rate * 100:.1f}")
        
   #add/update rate type
    def add_or_update_rate_type(self):
        try:
            rate_name= input("Enter the rate typename:")
            price = input("Enter the price:")

            self.records.add_update_rate(rate_name, price)
            print(rate_name, price)
        except InvalidRateType:
            print("Error!Invalid rate type")
        except InvalidPrice:
            print("Error! Invalid Price")



    def book_trip(self):
        while True:
           
            while True:
                print("Do you want to add extra services or packages")
                try:
                    service_option =input("Enter 'Y' for yes, 'N' for no:").strip()
                    if service_option == "Y":
                        print("The following are the services and packages offered.")
                        self.records.list_services()
                        service_name = input("Enter the ID of the service/package you want to order: ")
                        selected_service = self.records.find_service(service_name)
                        if selected_service is None:
                            print("Error service not available.Please Try again")
                            return
                        break
                    elif service_option == "N":
                        selected_service =None
                        break
                    else:
                        print("Error! Please enter a correct option(Y/N)")
                        
                except ValueError:
                    print("Invalid input given!")
                    continue

            customer_id_name = input("Enter customer id or name:") 
            while True:
                if customer_id_name.isalpha() or customer_id_name.isnumeric(): 
                    if customer_id_name.isnumeric():
                        customer_id_name = int(customer_id_name)               
                    customer= self.records.find_customer(customer_id_name)
                    break
                elif customer_id_name.isalnum()==True:
                    customer_id_name = input("Enter customer id or name.Please enter again:").strip().lower()
                    if customer_id_name.isalpha() or customer_id_name.isnumeric():                
                        customer= self.records.find_customer(customer_id_name)
                elif customer_id_name.isalnum()==True:
                    customer_id_name = input("Enter customer id or name:Please enter again:").strip()
                    continue
            while True:
                departureid_or_name = input("Enter departure location ID or name: ")
                departure_location = self.records.find_location(departureid_or_name)
                if departure_location is None:
                    print("Error Location not found.Please enter a valid location ID or Location name.")
                    continue
                break

            while True:
                destinationid_or_name = input("Enter destination location name or ID: ")
                destination_location = self.records.find_location(destinationid_or_name)

                if destination_location is None or destination_location == departure_location:
                    print("Error Destination Location not found or destination location is as same as departure.Please enter a valid location ID or Location name.") 
                    continue 
                break
            while True: 
                distance = input("Enter distance (in km): ")
                try:
                    if float(distance) <=0:
                        print("Distance should be a positive number.Please try again.")
                        continue
                except ValueError:
                    print("Error: Invalid input for distance. Must be an numeric value.")
                    continue
                break
            while True:
                rateid_or_name = input("Enter rate type name or ID: ")
                rate = self.records.find_rate(rateid_or_name)
                if rate is None:
                    print("Error Rate type not found.Please enter a valid rate type ID or name.")
                    continue
                break

            new_des=[destination_location]
            dis_list=[distance]
            while True:
                multi_des=input("Do you want to Add new destination[y/n]?").lower()
                if multi_des =="y":
                    multi_des_loc_id_name=input("Enter the new destination location id or name:").strip()
                    multi_des_loc = self.records.find_location(multi_des_loc_id_name)
                    if  multi_des_loc is None:
                        print("Error Destination entered doesn't exists.")
                    elif multi_des_loc in new_des or multi_des_loc==departure_location:
                        print("Please enter a different destination")
                    else:
                        new_des.append(multi_des_loc)
                        print(new_des)
                        distance_mul = float(input("Enter the distance:"))
                        if distance_mul<=0:
                            print("Error Distance should be positive number")
                        dis_list.append(distance_mul)

                elif multi_des=="n":
                    break
            distance=sum(float(d) for d in dis_list)

            customer = self.records.find_customer(customer_id_name)
            if isinstance(customer, BasicCustomer):
                customer_type = "Basic"
                print(f"Existing customer is: {customer_type} customer") 
                booking = Booking(customer, departure_location, destination_location, distance, rate,selected_service)
                distance_fee, basic_fee, discount,service_fee, total_cost = booking.compute_cost(selected_service)
            elif isinstance(customer, EnterpriseCustomer):
                customer_type = "Enterprise"
                print(f"Existing customer is: {customer_type} customer") 
                booking = Booking(customer, departure_location, destination_location, distance, rate,selected_service)
                distance_fee, basic_fee, discount, service_fee,total_cost = booking.compute_cost(selected_service)
            else:
                print("New Customer Found!")
                new_customer_id = str(max([c.ID for c in self.records.existing_customers]) + 1)
                name = customer_id_name
                customer_type = "New Customer"
                new_customer = BasicCustomer(new_customer_id, name, discount_rate=0.0)
                booking = Booking(customer, departure_location, destination_location, distance, rate, selected_service)
                distance_fee, basic_fee, discount,service_fee, total_cost = booking.compute_cost(selected_service)
                new_customer.set_discount_rate(0.1)
                self.records.existing_customers.append(new_customer)
            booking = Booking(customer, departure_location, destination_location, distance, rate,selected_service)
            distance_fee, basic_fee, discount, service_fee,total_cost = booking.compute_cost(selected_service)

            # Display the receipt
            print("-" * 50)
            print("Taxi Receipt".center(40))
            print("-" * 50)
            print("Name:".ljust(25) + customer.name if hasattr(customer, 'name') else "New Customer")
            print("Departure:".ljust(25) + departure_location.name)
            for i in range(len(new_des)):
                print("Destination: ".ljust(25)+new_des[i].name)
                print("Distance:".ljust(25)+f"{float(dis_list[i]):.2f}(km)")
            print("Rate_type:".ljust(25)+f"{rate.name}")
            print("Rate:".ljust(25) + f"{rate.price} (AUD per km)")
            if selected_service:
                print("Service/Package:".ljust(24)+f"{selected_service.service_name}")
                print("Price:".ljust(25)+f"{service_fee:.2f}(AUD)")
            print("-" * 50)
            print("Basic fee:".ljust(25) + f"{basic_fee:.2f} (AUD)")
            print("Distance fee:".ljust(25) + f"{distance_fee:.2f} (AUD)")
            print("Discount:".ljust(25) + f"{discount:.2f} (AUD)")
            print("Total cost:".ljust(25) + f"{total_cost:.2f} (AUD)")
            print("-" * 50)


            selected_service =None
            destination_name=[location.name for location in new_des]
            booking={
                "customer_name":customer.name if hasattr(customer, 'name') else customer_id_name,
                "departure":departure_location.name,
                "destination":destination_name,
                "distance":dis_list,
                "rate_type":rate.name,
                "service":selected_service.service_name if hasattr(selected_service,'service_name')else " ",
                "basic_fee":basic_fee,
                "distance_fee":distance_fee,
                "discount":discount,
                "total_cost":total_cost
            }
            self.records.add_booking(booking)

            break

if __name__ == "__main__":
    records = Records()
    operations = Operations(records)

    operations.display_menu()
  
#command_line 
import sys

def main():
    if len(sys.argv) < 4:
        print("Example: python your_program.py <customer_file> <location_file> <rate_file> <service_file> [<booking_file>]")
        sys.exit(1)
    customer_file = sys.argv[1]
    location_file = sys.argv[2]
    rate_file = sys.argv[3]
    service_file = sys.argv[4]
    if len(sys.argv) > 5:
        booking_file = sys.argv[5]
    else:
        booking_file = "bookings.txt" 
    records = Records()
    operations = Operations(records)
    records.read_customers(customer_file)
    records.read_locations(location_file)
    records.read_rates(rate_file)
    records.read_services(service_file)
    records.read_booking(booking_file)
    operations.display_menu()

if __name__ == "__main__":
    main()

#by using object oriented programming the code can be reused.
#using the concept of inheritance, class, objects i have implement the program for taxi management system
#if-else statements are used to choose from the menu option and checking the conditions 
#for loop is used here for iterating throughout the list or characters, etc
#while loop is used to run continuously until the condition is false
#try-except for handling exceptions and errors, validation
#the flow of my program
#the menu options are displayed, user can choose from those options.
#to book a trip user need to select 1. 
#after selecting 1, user is given option to add extra services or packages only one is allowed.
#if users selects Y then existing services and packages are displayed
#the user needs to enter the ID of service or package
#if N then break out of loop
#Customers to enter either their id or name it checks for exception in name or id and gives them another chance until valid input is received it also checks for existing customer
#next user should enter departure id or name if departure location is not in existing location then error 
#user need to enter the destination location id or name if present and not same as departure location then accepted
#distance is enter checked of negative or 0 and also for value error
#similarly or rate_type either id or rate_name is entered. exceptions are handled and user is given chance to enter again.
#the user is then asked for multiple location if y then users need to enter location id or name , it should not be same as departure location or previous destination location and must exist in location list
#if y then enter the distance which should be positive and numeric
#finally printing the receipt with name, departure, destinations, distances, rate_type, rate_price,
#service/package selected, price of service/package, basic_fee, distance_fee, discount and total_cost
#option 2 from the menu display the existing customer
#option 3 displays the existing locations
#option 4 display the existing rate types
#option 5 disaply the existing services and packages
#option 6 is used add new locations which are separated by comma and displays the new added location
#option 7 is used to update the discount_rate of the basic customer user is asked for new discount rate and now the discount gets updated for all basic customers
#option 8 is used to update the discount_rate for a particular enterprise customer 
#they are asked for their id or name to check whether there are enterprise customer else error
#if they enter correct option then given a chance to update the low_discount rate
#high_rate is automatically calculated
#option 9 is for add/update rate_type which taked rate type name as a input handles all the errors
#next it takes the rate price input for the entered name updates if existing else new is created
#option 10 is used to display in booking of all the customers
#option 11 is used to display most popular customer
#option 12 is used get the booking history of a particular customer
#option 13 is for exiting the program. comes out of loop
#else display invalid input and display the menu again.

#Note
#refered my assignment_1 file for exceptions and most_popular customer, booking_history

#References#
#[1]https://rmit.instructure.com/courses/107646/pages/4-dot-4-activity-formatting-outputs?module_item_id=5391396
#[2]https://rmit.instructure.com/courses/107646/pages/5-dot-1-3-reading-from-files?module_item_id=5391410
#[3]https://rmit.instructure.com/courses/107646/pages/6-dot-3-3-adding-methods-and-object-attributes-to-the-expense-manager-program?module_item_id=5391440
#[4]https://rmit.instructure.com/courses/107646/pages/8-dot-1-activity-static-and-instance-members?module_item_id=5391460
#[5]https://rmit.instructure.com/courses/107646/pages/10-dot-1-1-using-custom-exceptions-in-the-finance-manager?module_item_id=5391496
#[6]https://rmit.instructure.com/courses/107646/pages/9-dot-2-2-accessor-slash-getter-methods?module_item_id=5391481
#[7]https://docs.python.org/3.12/search.html?q=hasattr

            
            







                