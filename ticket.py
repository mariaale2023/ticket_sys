# Develop a Help Desk ticketing system prototype. 


# Create a class Ticket to represent a INDIVIDUAL ticket
class Ticket:
  # Internal Tickets assignation numbers start from 2000. 
  ticket_start_number = 2000

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
  def __init__(self, user_staff_id, user_name, user_email, description ):
    self.user_staff_id = user_staff_id
    self.user_name = user_name 
    self.user_email = user_email
    self.description = description
    self.ticket_number = str(Ticket.ticket_start_number)
    self.status = "Open"
    self.comment = []
    self.response = "Not yet provided"

    Ticket.ticket_start_number += 1
  
  # function to respond ticket

  # function to reopen ticket

  

  def __str__(self):
      return f"Ticket Number: {self.ticket_number}\n" \
             f"Ticket Creator: {self.user_staff_id}\n" \
             f"Caller Name: {self.user_name}\n" \
             f"Caller Email: {self._email}\n" \
             f"Description: {self.description}\n" \
             f"Comments: {', '.join(self.comments)}\n"\
            #  f"Status: {self.status}\n" \
  
  


  




  

    

    







# Ability to respond to tickets, with the generation of new passwords for "Password Change" requests. 

# Keep track of ticket statistics, including the number of tickets submitted, resolved, and open. 

# Stakeholders: 



