# FindIt - جِدها
Find It (جِدها) is a platform designed to connect people who have lost items with those who have found them. 
Our goal is to make it easy for people in Egypt to reunite with their lost belongings.

## Features:
* **User Registration:** Users can create accounts and log in using their phone numbers.
* **Lost/Found Item Reporting:** Users can submit detailed reports of lost or found items.
* **Intelligent Matching:** The system uses a combination of tags and location to find potential matches.
### Upcomming Features:
* **Real-time Chat:** Users can communicate through a secure chat portal to coordinate returns.
* **Admin Panel:** Administrators can manage users, items, and reports.
* **SMS Notifications:** Users receive SMS messages when a potential match is found.
* **Arabic and English Support:** The platform is available in both Arabic and English.

## Getting Started:

### Prerequisites:

* PostgreSQL
* Python 3.x
* pip

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Ziad-kh99/FindIt.git
    cd find-it
    ```

2.  Create a virtual environment:

    ```bash
    python3 -m venv .venv
    source venv/bin/activate      # On Linux and MacOS
    venv\Scripts\activate         # On Windows
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5.  Run database migrations:

    ```bash
    python manage.py migrate
    ```

6.  Start the development server:

    ```bash
    python manage.py runserver
    ```

