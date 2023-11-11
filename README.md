# Help Desk Ticketing System

## Overview

This is a simple prototype of a Help Desk Ticketing System. The system allows users to submit, view, resolve, and reopen tickets. Each ticket is associated with a unique ticket number and contains information such as the creator's name, staff ID, email, description, status, and response.

## Features

- **Open Ticket:** Users can submit a new ticket by providing details about the issue.
- **View Tickets:** View a list of all submitted tickets.
- **Resolve Ticket:** Resolve an open ticket, providing a comment. Closed tickets cannot be resolved again.
- **Reopen Ticket:** Reopen a closed ticket, providing a comment.
- **Display Statistics:** View statistics, including the number of submitted, resolved, and open tickets.

## Technology Used

- Python 3

## Installation

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:mariaale2023/ticket_sys.git
   ```
2. **Navigate to the Project Directory:**
   `cd help-desk-ticketing-system`

3. **Run the Program:**
   `/usr/bin/python3 dashboard.py`

## Project Structure

- dashboard.py: Main program file.
- ticket.py: Ticket class definition.
- README.md: Project documentation.

## Note

- Ticket numbers start from 2000 internally.
- Password reset tickets generate a new password for the user.

Feel free to explore and test the different functionalities of the Help Desk Ticketing System.
