from ticket import Ticket

print("\n\nWelcome to Service Desk")

# Instance to
ticket1 = Ticket("MAria", "123",  "maria@maria.cl", "Printer")
ticket2 = Ticket("Ale", "234",  "ale@ale.cl", "Windows")
ticket3 = Ticket("Jorge", "234",  "jorge@Jorge.cl", "Office365")
ticket4_close = Ticket("George", "234",  "George@George.cl", "Router Internet")
ticket4_close.status = "Close"
ticket4_close.response = "Test response to close ticket"
ticket4_close.comment= ['Test comment to close ticket']


# def submit_ticket():
#     creator_name = input("Enter your name: ")
#     staff_id = input("Enter your staff ID: ")
#     contact_email = input("Enter your contact email: ")
#     description = input("Describe the issue: ")

#     ticket = Ticket(creator_name, staff_id, contact_email, description)
#     ticket.submit()

#     print("Ticket submitted successfully!")

while True:
  user_action = input(
        '--------------------------------\n'
        'SELECT OPTION:\n' 
        '1: Open ticket.\n'
        '2: Show all tickets.\n' 
        '3: Resolve ticket by number.\n'
        '4: Reopen resolve ticket.\n' 
        '5: Display ticket statistics\n'
        '--------------------------------\n')
   
  
  if user_action == "1":
     operator_name = input('Enter your name: ')
     callerID = input('Enter your UserID: ')
     caller_email = input('Enter your email: ')
     description = input('Do you need to "Reset Password")?? (y / n)')
     
     # if Issue is reset password incorporate the new password in the new ticket
     # using the class TICKET
     if description == 'y':
        ticket = Ticket(operator_name, callerID,  caller_email, "Password Reset")
        new_password = ticket.new_password()
        print("--------------------------------\n"
                  '\n New password generated.\n'
                  f'   Your new password is {new_password} \n'
                  '    Your ticket has been resolved and close')
    
     
     
     else:
        description = input('Describe your issue: ')
        ticket = Ticket(operator_name, callerID, caller_email, description)
        print("--------------------------------\n"
              "Ticket submitted successfully!\n"
              "The details of your ticket are:\n"
              f'{ticket}')
        
     

   # Show the list of Tickets
  elif user_action == "2":
     print("--------------------------------\n"
              '\n List of Tickets.\n')
     for i in Ticket.list_of_tickets:
        print(i)
     print("--------END LIST TICKETS---------\n")
     
   # Resolve ticket by number
  elif user_action == "3":
     print("--------------------------------\n")
     input_number_ticket = input("Insert the number of ticket?\n")
     input_number_ticket = int(input_number_ticket)

     # Check if the ticket number is within the valid range. 
     # remember the list of ticket start from 2000
     if 0 <= input_number_ticket - 2000 < len(Ticket.list_of_tickets):
        solve_coment = input("Insert your coment about your resolution\n")
        Ticket.list_of_tickets[input_number_ticket - 2000 ].resolve_ticket(solve_coment) 
        print(f"\nTicket {input_number_ticket} resolved successfully.\n")
        print("\n--------------------------------\n")
     else:
        print(f"\nInvalid ticket number: {input_number_ticket}\n")
        print("\n--------------------------------\n")
  
  #Reopen a close ticket
  elif user_action == "4":
     print("--------------------------------\n")
     input_number_ticket = input("Insert the number of ticket that you want to open?\n")
     input_number_ticket = int(input_number_ticket)
    
     if 0 <= input_number_ticket - 2000 < len(Ticket.list_of_tickets) and Ticket.list_of_tickets[input_number_ticket- 2000].status == "Close":
        reopen_coment = input("Insert your coment about Why is reopen this ticket\n")
        Ticket.list_of_tickets[input_number_ticket - 2000 ].reopen_ticket(reopen_coment) 
        print(f"\nTicket {input_number_ticket} REOPEN successfully.\n")
        print("\n--------------------------------\n")
     else:
        print(f"\nInvalid ticket number: {input_number_ticket}\n")
        print("\n--------------------------------\n")
         
     




     

     
    
     
 

    


  # new_ticket = Ticket(operator_name, callerID, caller_email, description)
