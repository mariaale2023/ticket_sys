import random
# Develop a Help Desk ticketing system prototype. 


# Create a class Ticket to represent a INDIVIDUAL ticket
class Ticket:
  # Internal Tickets assignation numbers start from 2000. 
  ticket_start_number = 2000
  list_of_tickets = []

  # Tickets include as information:  
      # Staff ID = user_staff_id
      # Name of ticket creator = user_name
      # Contact email of ticket cretor =    user_email
      # Description of the issue = description
      # Ticket number 
      # Ticket status = open or close
      # Ticket comments 
      # Ticket response

  # function to open a ticket
  def __init__(self, user_name,user_staff_id, user_email, description ):
    self.user_name = user_name 
    self.user_staff_id = user_staff_id
    self.user_email = user_email
    self.description = description
    self.ticket_number = str(Ticket.ticket_start_number)
    self.status = "Open"
    self.comment = []
    self.response = "Not yet provided"
    
    # Additon 1 to "Open" counter ticket
    Ticket.ticket_start_number += 1

    # Append new ticket to the list of tickets
    Ticket.list_of_tickets.append(self)

  # create password new password
  def new_password(self):
     random_five_numbers = random.randint(1000000,9999999)
     password = f'{self.user_name}{random_five_numbers}'
     return password
  

  # function to respond ticket
  def resolve_ticket(self, comment):
     self.status = 'Close'
     self.response = 'Ticket Resolve'
     self.comment.append({comment})

  # function to reopen ticket

  
  # Show the ticket 
  def __str__(self):
      return f"  Caller Name: {self.user_name}\n" \
             f"  Ticket Number: {self.ticket_number}\n" \
             f"  Ticket Creator: {self.user_staff_id}\n" \
             f"  Caller Email: {self.user_email}\n" \
             f"  Description: {self.description}\n" \
             f"  Status: {self.status}\n" \
             f"  Response: {self.response}\n" \
             f"  Comments: {', '.join(self.comment)}\n"\
  
  


# Ability to respond to tickets, with the generation of new passwords for "Password Change" requests. 

# Keep track of ticket statistics, including the number of tickets submitted, resolved, and open. 

# Stakeholders: 



