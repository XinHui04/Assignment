import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import datetime

# Define the list of valid tour guide’s names
name = ["Alie", "Bella", "Catherine","alie", "bella", "catherine"]

# Create the main window
root = tk.Tk()
root.title("ABC Zoo Ticket")
root.configure(bg='lightblue')  # Set background color for the main window

# Display greeting to the user
welcome_label = tk.Label(root, text="Welcome to ABC Zoo !", font=("Times", 22, 'bold'), fg='white', bg='lightblue')
welcome_label.pack(padx=50, pady=20)

# Get trip ID from the user
trip_id_label = tk.Label(root, text='Trip ID:',font=( "Calibri",12 ), bg='lightblue')
trip_id_label.pack(padx=1, pady=1)
trip_id_entry = tk.Entry(root, bg='white')
trip_id_entry.pack(padx=10, pady=10)

# Get tour guide’s name from the user
tour_guide_label = tk.Label(root, text="Tour Guide's Name (Alie , Bella , Catherine) :", font=( "Calibri",12 ), bg='lightblue')
tour_guide_label.pack(padx=1, pady=1)
tour_guide_entry = tk.Entry(root, bg='white')
tour_guide_entry.pack(padx=11, pady=11)

# Create submit button
def submit_button():
    trip_id = trip_id_entry.get()  # Get trip ID value
    tour_guide = tour_guide_entry.get()  # Get tour guide’s name value
    # Reject invalid trip ID and tour guide’s name
    if trip_id == "":
        # Error Message
        messagebox.showerror(title="Error", message="Invalid Trip ID")
   
    elif tour_guide == "" or tour_guide not in name:
        # Error Message
        messagebox.showerror(title="Error", message="Invalid tour guide’s name")
    else:
        # Hide the main window
        root.withdraw()
   
        # Prompt for guest’s age
        age = []
        toddler, children, senior, adult = 0, 0, 0, 0

        # While loop for guests’ age
        while age != "":
            age = simpledialog.askstring (title="Guest age", prompt="Please enter guest’s age (Press enter if no more guests):\n\n*Enter alphabet(s) or special character(s) to re-enter the age.\n ")

            # exit the page when clicking cancel or the x button
            if age is None:
                break
   
            # Reject Invalid data
            if not age.isdigit() and age != "":
                # Error Message
                messagebox.showerror(title="Error", message="Invalid age. Please enter again with digits.")
                previous = simpledialog.askstring(title="Previous", prompt="Do you want to RESET all the previous data ? (Y for yes, other keys for no): ")
   
                # Reset all the data of ages
                if previous.lower() == "y":
                    toddler, children, senior, adult = 0, 0, 0, 0
                    continue
                else:
                    continue
           
            # Calculate the number of each group of guest
            if age != "":
                age = int(age)

                if age <= 2:
                    toddler += 1
                   
                elif 3 <= age <= 12:
                    children += 1

                elif age >= 65:
                    senior += 1

                else:
                    adult += 1
   
        # Calculate total costs
        total_cost = toddler * 0 + children * 14 + adult * 23 + senior * 18

        # insert date and time
        current_datetime = datetime.datetime.now()  

        receipt = tk.Toplevel(root)
        receipt.title("Receipt")
        receipt.configure(bg = 'lightblue')  # Set background color for receipt window

        # Header
        receipt_label = tk.Label(receipt, text="ABC Zoo Ticket", font=("Times", 22, 'bold'),fg='white', bg='lightblue')  
        receipt_label.pack(pady=5)

        receipt_text1 = f"Trip ID: {trip_id}"  
        receipt_text2 = f"Tour Guide: {tour_guide}"  
        receipt_text3 = f"Date/Time: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}"
        receipt_label1 = tk.Label(receipt, text=receipt_text1, font=("Courier", 10), bg='lightblue')
        receipt_label2 = tk.Label(receipt, text=receipt_text2, font=("Courier", 10), bg='lightblue')
        receipt_label3 = tk.Label(receipt, text=receipt_text3, font=("Courier", 10), bg='lightblue')
        receipt_label1.pack(padx=20, pady=(10, 2))
        receipt_label2.pack(padx=20, pady=(2, 10))  
        receipt_label3.pack(padx=20, pady=(2, 5))  

        #   Table
        table_frame = tk.Frame(receipt, bg='lightblue')
        table_frame.pack()

        #   Define data for the table
        table_data = [
            ("Group of guests", "Price", "Qty", "Amount"),
            ("Toddler (0-2)", "$0.00", toddler, f"${toddler * 0:.2f}"),
            ("Children (3-12)", "$14.00", children, f"${children * 14:.2f}"),
            ("Adult (13-64)", "$23.00", adult, f"${adult * 23:.2f}"),
            ("Senior (65+)", "$18.00", senior, f"${senior * 18:.2f}"),
            ("Total", "----", toddler + children + senior + adult, f"${total_cost:.2f}")
        ]

        for row_index, row_data in enumerate(table_data) :
            for col_index, cell_data in enumerate(row_data) :
                label = tk.Label(table_frame, text = cell_data, font = ("Courier", 12), bg='lightblue')
                label.grid(row=row_index, column = col_index, padx = 10, pady = 5, sticky = "w")

        receipt_text = "Thank you for visiting ABC Zoo! \nPlease come again."
        receipt_label = tk.Label(receipt, text=receipt_text, font = ("Times", 14),fg='darkblue', bg='lightblue')
        receipt_label.pack(padx = 20, pady = 20)

        receipt.mainloop()

# Create the submit button
submit_button = tk.Button(root, text = 'Submit', command = submit_button, bg='green', fg='white', font = ("Calibri",12))
submit_button.pack(padx = 3, pady = 30)

# Start the GUI event loop
root.mainloop()
