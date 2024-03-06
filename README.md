# DTH CRM System

This project is a Customer Relationship Management (CRM) system developed specifically for a DTH service provider. The system is designed to streamline various aspects of customer management, lead tracking, and telecaller operations.

## Features

- **User Authentication**: Users including administrators and telecallers can authenticate themselves securely.
  
- **Admin Dashboard**: Administrators have access to a comprehensive dashboard providing an overview of key metrics and functionalities.

- **Lead Management**: The system allows administrators to manage leads efficiently, including importing leads from Excel files, adding new leads manually, and updating existing leads.

- **Telecaller Interface**: Telecallers have their own dashboard where they can view assigned leads and update lead statuses.

- **Lead Assignment**: Administrators can assign leads to telecallers based on various criteria, streamlining the lead distribution process.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MushrafMuhammed/DTH-CRM-System.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure database settings in `settings.py` according to your environment.

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://127.0.0.1:8000/` in your web browser.

## Technologies Used

- **Django**: The project is built using the Django web framework, providing a robust foundation for web application development.
  
- **JavaScript/jQuery**: Client-side scripting is implemented using JavaScript and jQuery for dynamic user interactions.

- **HTML/CSS**: The user interface is designed using HTML for structure and CSS for styling.

- **Openpyxl**: Excel file handling is facilitated by the Openpyxl library, allowing seamless import of leads.
