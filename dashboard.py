from ticket import Ticket

print("\n\nWelcome to Service Desk")




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
        '\n\nSELECT OPTION:\n' 
        '1: Open ticket.\n'
        '2: Show all tickets.\n' 
        '3: Reopen resolve ticket.\n' 
        '4: Resolve ticket by number.\n'
        '5: Display ticket statistics\n')
  
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
  
  elif user_action == "2":
     print("--------------------------------\n"
              '\n List of Tickets.\n')
     for i in Ticket.list_of_tickets:
        print(i)
     print("--------END LIST TICKETS---------\n")
     
    
    
     
 

    


  # new_ticket = Ticket(operator_name, callerID, caller_email, description)
