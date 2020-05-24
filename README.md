# Udacity - Full Stack API Final Project

This is the final project of the Udacity Full Stack Developer Nano Degree. The goal of this project is to deploy a Flask application using Heroku and PostgreSQL and enable Role Based Authentication and roles-based access control git (RBAC) with Auth0 (third-party authentication systems).

## Full Stack Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.


### Roles and Permissions:

There are 3 different types of roles associated with this application. The details and permissions associated are given below:

1. Casting Assistant
    * get:actors
    * get:movies

2. Casting Director
    * delete:actors
    * get:actors
    * get:movies
    * patch:actors
    * patch:movies
    * post:actors

3. Executive Producer
    * delete:actors
    * delete:movies
    * get:actors
    * get:movies
    * patch:actors
    * patch:movies
    * post:actors
    * post:movies
    

## Getting Started

### Pre-Requisites

Create a postgre database for testing the app locally  before deploying to Heroku.
JWT tokens for each of the roles (Casting Assistant, Casting Director and Executive Producer) with appropriate permissions mapped to them (provided below with an expiry time of 24 hours)

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the project directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## About the Stack

### Backend

The project is hosted live via Heroku.
Role based authentication has been setup for 3 roles (Casting Assistant, Casting Director and Executive Producer) using AUTH0.

### API Endpoint for testing 

https://capstone-sainath.herokuapp.com/

### Unit Tests

1. To run the tests locally, make sure you have PostgreSQL installed, https://www.postgresql.org/
2. Create a test postgre database.
3. Setup the 2 environment variables as mentioned in config_settings.env file locally by running below commands. 

    * DATABASE_URL - Update the datatabase name, user name, password, port #

        ```bash
        export DATABASE_URL=<Refer to the config_settings.env file and update your database parameters>
        ```

    * TOKEN_TEST - Copy the value from config_settings.env file. This is the Bearer token generated from AUTH0 for the role - Executive Producer which is allowed to run all endpoints.

        ```bash
        export TOKEN_TEST=<Copy/Paste from config_settings.env file as it is>
        ```

4. After setting up environment variables, run the below command. Make sure you are in the folder where test_app.py file is present.

    ```bash
        python test_app.py
    ```

#### Note:
Run the test only after setting up the environment variables correctly so that all tests will be successful in first attempt. Else, you may have to update the ID field of tables accordingly for delete endpoints. 

### Test using Postman

1. Authorization token for all roles has been updated in postman collection file - Capstone.postman_collection
2. Import this postman collection file in POSTMAN app and run all cases


## API Reference

### Getting Started

1. Base URL : Backend app is hosted on https://capstone-sainath.herokuapp.com
2. Authentication : Role based authentication using AUTH0

####Below JWTs are available with an expiration time of 24 hours for each of the roles:
Casting Assistant
-----------------
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpFcTdCSUhnaURSXzliZUNJS3JoayJ9.eyJpc3MiOiJodHRwczovL3NhaW5hdGgtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5ZDVmOGZkZTQzMWEwYzhkNjhhYzFlIiwiYXVkIjoiQ2Fwc3RvbmVBUEkiLCJpYXQiOjE1OTAzMjAwNjIsImV4cCI6MTU5MDQwNjQ2MiwiYXpwIjoiYm1teWtTMHdRNzJwMkZUNXloZlZTQVRyYnRTaXVONDgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.3tnZDFkwl3cL7rRumBD7BTpRNd_dGwK-9ufdpxPpKNMy7kCvh5ntatzkXx9VuxZFPNWVPtigm2w2CjDbJPfFvNCQgsMmq7gp2rtD4LGK7Unu9WDdJ5BN0GnpDCno3EUZ3jmZ1fSggxs7Nwb032chGTHPKP2EiKYNkkBt-vLthuqwjW-5PLWRAwSCPDMk0AzFHLI5c515kEMqP5o0DlXia73BNlvEZFNLu2RypNZXUPFqxkX2huuJoZLwwpEGhQJGNCTlp2u_kOcdAmT-bORTHiVUtriEMjXMIq9Wqz0W05dIRDUSBqFg9JVEhByYI5PK4-7lfsfKe3ij-vztiN_HlA

Casting Director
----------------
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpFcTdCSUhnaURSXzliZUNJS3JoayJ9.eyJpc3MiOiJodHRwczovL3NhaW5hdGgtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5ZDVmZTlkZTQzMWEwYzhkNjhhY2YyIiwiYXVkIjoiQ2Fwc3RvbmVBUEkiLCJpYXQiOjE1OTAzMjA0NDcsImV4cCI6MTU5MDQwNjg0NywiYXpwIjoiYm1teWtTMHdRNzJwMkZUNXloZlZTQVRyYnRTaXVONDgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.rhReP9maR7uRwT3Wb75ro7KiRJl6vUe-R5omccdm2Fr4NOeVA6L1BFFYS25mNyC_g5CE9eDumIVkY199dcS6b65rmuxJ8wXP-m2UB_KN9Ec7u12lMUL_8IL4z21LmFGobryrniWgmqvqpwMD0pgh1LEnjNUoi4-DCjMGnb6TFgm-XY3Y_G-l_vMmMWYQy8kqaWTRFxPDHdvC2FhAgyUK-zDvQSPisuTcg-d-lTmcFzS3L1fgCNOsnk-HIjOZgMXmKR4P7m_H1XtpXUiQAVXyDYRFU0WY4XGbcSLBupSrjGK5mX6lMYkjYIAwFT6UpcJ8SN5dE7m4N5_wbqduj-Czvw

Executive Producer
------------------
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpFcTdCSUhnaURSXzliZUNJS3JoayJ9.eyJpc3MiOiJodHRwczovL3NhaW5hdGgtZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjYTQwNzdmNzkwOGMwYzY4YTQ5ZmZjIiwiYXVkIjoiQ2Fwc3RvbmVBUEkiLCJpYXQiOjE1OTAzMzI2NzIsImV4cCI6MTU5MDQxOTA3MiwiYXpwIjoiYm1teWtTMHdRNzJwMkZUNXloZlZTQVRyYnRTaXVONDgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.G8Am8znoDShIu5jGNmPwWwuYPSTeOZtpYNYHux9-azdW1SHE81kJaYgrT1ecnFtZQ1KfQBNFpV7Fw2BwN1Os5j6hFrEDomK-e_rR2Trl5swgT9tnZrKovSoyGO8-IY8hp9IxrgW1qIjuZUvETFInFQ1rDbBPTUvfvc8UeP9QrQs1-UMvBNr8z1DRrB03ZJPS9g2A1Hxxg2KHw0ZzpBSuF0yaOgyL1ExyBBU1wN0pBFfH_PN_vpSPggw0c-KxUQYnE-HYLWyPHjNpitTi41xnErcy9vqijVCO6ThOzqVWcpLZSFSAKJQD7lzm-nnOU6BGHW8ks5JuZ9w4OabIckKeyQ

### Error Handling

Errors are returned as JSON objects in the following format:

```json
{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}
```

The API will return these error types when requests fail:
* 400: bad request
* 404: Resource not found
* 422: unprocessable
* 500: Internal Server Error

If the route requires authentification and the request fails, it will return:
* 401: "authorization_header_missing"
* 400: "invalid_claims"
* 403: "unauthorized"

### Roles and Permissions

#### Casting Assistant 
    • Can view actors and movies

#### Casting Director 
    • All permissions a Casting Assistant has 
    • Add or delete an actor from the database 
    • Modify actors or movies

#### Executive Producer
    • All permissions a Casting Director has 
    • Add or delete a movie from the database

### Endpoints

#### GET /

No authentication required. This is to check if the APP is up and running. 

```json
{
    "Message": "Welcome to the Casting Agency Application",
    "success": true
}
```

#### GET /actors (Auth required)

Returns details of all actors.

Sample output:

```json
{
    "actors": [
        {
            "age": 25,
            "gender": "Female",
            "id": 1,
            "name": "Jennifer"
        },
        {
            "age": 26,
            "gender": "Male",
            "id": 2,
            "name": "Brad"
        }
    ],
    "success": true
}
```

#### GET /actors/<actor_id> (Auth required)

Returns actor details for the given id.

Sample output:

```json
{
    "actors": {
        "age": 25,
        "gender": "Female",
        "id": 1,
        "name": "Jennifer"
    },
    "success": true
}
```

#### GET /movies (Auth required)

Returns details of all movies.

Sample output: 

```json
{
    "movies": [
        {
            "id": 1,
            "releasedate": "23-04-2019",
            "title": "Once upon a time in hollywood"
        },
        {
            "id": 2,
            "releasedate": "16-03-2013",
            "title": "Gravity"
        }
    ],
    "success": true
}
```

#### GET /movies/<movie_id> (Auth required)

Returns movies details for the given id. 

Sample output: 

```json
{
    "movies": {
            "id": 1,
            "releasedate": "23-04-2019",
            "title": "Once upon a time in hollywood"
    },
    "success": true
}
```

#### POST /actors (Auth required)

Add a new actor.

Sample input:

```json
{
	"name": "John",
	"age": "26",
	"gender": "Male"
}
```

#### POST /movies (Auth required)

Add a new movie.

Sample input:

```json
{
	"title": "Jumanji",
	"releasedate": "20-12-2019"
}
```

#### PATCH /actors/<actor_id> (Auth required)

Update an existing actor. 

Sample input:

```json
{
	"name": "Dany",
	"age": "25"
}
```

#### PATCH /movies/<movie_id> (Auth required)

Update an existing movie. 

Sample Input:

```json
{
	"title": "Inception"
}
```

#### DELETE /actors/<actor_id> (Auth required)

Delete an existing actor.

Sample Output:

```json
{
    "deleted_actor_id": 2,
    "message": "Actor details successfully deleted",
    "success": true
}
```

#### DELETE /movies/<movie_id> (Auth required)

Delete an existing movie.

Sample Output:

```json
{
    "deleted_movie_id": 3,
    "message": "Movie details successfully deleted",
    "success": true
}
```

### AUTHORS

Sainath Meduri

## Acknowledgements

I would like to thank Udacity for providing the opportunity and the framework and guidelines for completing this final project.

