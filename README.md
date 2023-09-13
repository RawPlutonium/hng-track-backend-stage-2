# Person Management REST API

This is a REST API for managing persons built with Flask and MongoDB. It allows you to perform CRUD (Create, Read, Update, Delete) operations on person records.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This REST API is designed to provide basic CRUD operations for managing person records. It's built using Flask, a Python web framework, and uses MongoDB as the database. You can create, read, update, and delete person records through a set of well-defined API endpoints.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- MongoDB installed and running locally on the default port (27017).

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/rawplutonium/person-management-api.git
   ```

2. Navigate to the project directory:


    ```
    cd person-management-api
    ```
3. Install the required packages:


    ```
    pip install Flask Flask-RESTful pymongo flasgger
    ```
## Usage
1. Start the Flask application:
    ```
    python app.py
    ```
    Your API should now be running locally at ```http://localhost:5000```.

    You can use tools like Postman or curl to interact with the API. Here are some example API requests:

    ### a. Create a new person:


    ```POST http://localhost:5000/api```

    #### Request body:

        
        {
        "_id": "2",
        "name": "Jane Smith",
        "age": 25
        }
        
    ### b. Fetch details of a person:


    ```GET http://localhost:5000/api/2```

    ### c. Update details of an existing person:

    ```PUT http://localhost:5000/api/2```
    #### Request body:
    ```
    {
    "age": 26
    }
    ```
    ### d. Remove a person:

    ```DELETE http://localhost:5000/api/2```



    ## API Endpoints
    1. ```GET /api/<string:user_id>```:
     Retrieve details of a person by user_id.
    
    2. ```POST /api```: 
    Add a new person.

    3. ```PUT /api/<string:user_id>```: Update details of an existing person.

    4. ```DELETE /api/<string:user_id>```: Remove a person.


## Documentation
For detailed API documentation, including request and response formats, please refer to the Swagger documentation available at http://localhost:5000/swagger/

## Testing
You can test the API using tools like Postman or by running Python unit tests. We've provided a sample test script using the `unittest`` library in Python.

1. Ensure your API is running locally at `http://localhost:5000`. If it's not running, start it with:

    ```
    python app.py
    ```
2. Open a terminal and navigate to your project directory.
3. Run the provided test script:
    ```
    python test_api.py
    ```
    This script will run a series of tests to verify the functionality of your API. It includes tests for creating a new person, fetching person details, updating person details, and deleting a person.

    Note: Before running the tests, make sure to set up the necessary test data. The script adds a person with user_id 4 and then removes it during testing. You can customize this test data as needed.
4. The test script will display the results of each test   case, indicating whether they pass or fail.
## Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.