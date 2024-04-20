class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__allocate_seats(id)
    
    def __allocate_seats(self, id):
        seats_matrix = [[0] * self.__cols for _ in range(self.__rows)]
        self.__seats[id] = seats_matrix

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print("Invalid Show ID !")
            return
        
        seats_matrix = self.__seats[id]

        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Invalid seat ({row}, {col}) !")
                continue

            if seats_matrix[row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked !")

            else:
                seats_matrix[row][col] = 1
                print(f"Seat ({row}, {col}) booked for show {id}.")

    def view_show_list(self):
        print("\n----------------------")
        for show in self.__show_list:
            print(f"Movie Name: {show[1]}\tShow ID: {show[0]}\tTime: {show[2]}")
        print("----------------------")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid show ID.")
            return

        print("True for available seat otherwise seat is Booked already !\n")

        seats_matrix = self.__seats[id]

        print("\nAvailable seats for show", id)

        for i in range(self.__rows):
            for j in range(self.__cols):
                if seats_matrix[i][j] == 0:
                    print(f"Seat ({i}, {j})")

        print("\nUpdated Seats Matrix for Hall", self.__hall_no, ":\n")

        for row in seats_matrix:
            print(row)

hall = Hall(7, 7, 1)
hall.entry_show("111", "Jawan Maji(111)", "25/10/2024 11:00 AM")
hall.entry_show("333", "Sujon Maji(333)", "25/10/2024 2:00 PM")

while True:
    print("\n1. View all shows today")
    print("2. View available seats")
    print("3. Book Ticket")
    print("4. Exit")
    option = input("Enter option: ")

    if option == "1":
        hall.view_show_list()

    elif option == "2":
        id = input("Enter show ID: ")
        hall.view_available_seats(id)

    elif option == "3":
        id = input("Show ID: ")
        number_tickets = int(input("Number of tickets?: "))
        seat_list = []

        for _ in range(number_tickets):
            row = int(input("Enter seat row: "))
            col = int(input("Enter seat col: "))
            seat_list.append((row, col))
            hall.book_seats(id, seat_list)

    elif option == "4":
        break

    else:
        print("\nInvalid option. Please try again....!")
