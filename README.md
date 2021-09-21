# Dub's Doubles Server

## Learning Goals

- Expand understanding of ORM, SQL, React & full-stack development
- Set up the models and ViewSets to allow users to upload images
- Implement full CRUD functionality
- Implement authentication using Django

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

## Features

The server utilizes unmapped properties to send useful information along with the objects stored in the database, and custom actions to either send very specific data to the client, or manipulate object properties. These features allow the client to request more precise data from the server, thereby minimizing the amount of extraneous data sent back to the client and reducing &mdash; if not eliminating &mdash; the need for client side data filtering.

## Set Up

1. Clone this repo

    ```
    git clone git@github.com:thejmdw/dubs-doubles-server.git
    cd dubs-doubles-server
    ```

2. Activate virtual environment

    ```
    pipenv shell
    ```

3. Install dependencies

    ```
    pipenv install
    ```

4. [Install Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

5. Load the database

    ```
    ./seed_data.sh
    ```

5. Run the server

    ```
    python manage.py runserver
    ```

6. Finish installation by following the instructions found here:
<a href="https://www.github.com/thejmdw/dubs-doubles-client" target="_blank"><img src="https://img.shields.io/badge/client_repo%20-%2375120e.svg?&style=for-the-badge&&logoColor=white" alt="Dub's Doubles Client Repo" style="height: auto !important; width: auto !important;" /></a>

## Created by Jonathan Watson

<a href="https://www.github.com/thejmdw/" target="_blank"><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white" alt="Jonathan Watson GitHub" style="height: auto !important;width: auto !important;" /></a> <a href="https://www.linkedin.com/in/thejmdw/" target="_blank"><img src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" alt="Jonathan Watson LinkedIn" style="height: auto !important;width: auto !important;" /></a>