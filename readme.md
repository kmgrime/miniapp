# Mini Web App README

This is a minimal web application built with Flask and SQLite for storing and viewing contact information.

## Files and Components

### `app.py`

`app.py` is the main Python script that defines the Flask application and its routes. Here's a breakdown of its functionality:

- The main route (`/`) displays a contact form that allows users to submit Name, Address, and Phone Number.

- Upon submitting the form, the data is stored in a SQLite database (`mydatabase.db`).

- The "View Form" button on the main page navigates users to the `/view` route.

- The `/view` route queries the SQLite database and displays the stored contact information in a table format.

### `templates/view.html`

`view.html` is an HTML template used to render the contact information stored in the database. It displays a table with columns for ID, Name, Address, and Phone Number.

- Users can navigate back to the main form by clicking the "Back to Form" link.

### Shell Script (`prepare_venv.sh`)

`prepare_venv.sh` is a shell script for setting up a virtual environment (venv) and installing project dependencies from a `requirements.txt` file.

- The script creates a venv in the project folder and activates it.

- It then installs the required Python packages listed in `requirements.txt`.

- After successful installation, the script echoes "Successfully installed."

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kmgrime/miniapp.git

2. Navigate to the project folder:

    ```bash
    cd mini-web-app

3. Run the shell script to set up the virtual environment and install dependencies:

    ```bash
    ./prepare_venv.sh

4. Start the Flask application:

    ```bash
    python app.py

5. Access the web application in your browser by visiting <http://localhost:5000>.

6. Fill out the contact form, submit data, and use the "View Form" button to see the stored contact information.

### Dependencies

- Flask (Python web framework)
- SQLite3 (Database engine)
- Jinja2 (Template engine)