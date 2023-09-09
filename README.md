# FastAPI-SQLAlchemy-Asyncio-Firestore

Project Overview
This project is a web application built with FastAPI, integrating both SQLAlchemy and Firestore to provide flexibility in managing data. The application focuses on creating, reading, and listing items in both Firestore (NoSQL) and an SQL database simultaneously. It demonstrates how to use two different types of databases in a single application.
<br>
Components and Technologies<br>
FastAPI: The web framework used to create API endpoints and manage HTTP requests and responses.<br>
SQLAlchemy: The ORM (Object-Relational Mapping) library for working with SQL databases. It enables the definition and interaction with database tables <br>using Python classes.<br>
Firestore: A NoSQL database provided by Google Cloud. It offers schema-less storage and real-time synchronization.<br>
Firebase Admin SDK: The Firebase Admin SDK is used to initialize Firestore.<br>
uvicorn: Uvicorn serves as the lightweight ASGI server to run the FastAPI application.<br>
Project Structure<br>
main.py: The main Python script containing the FastAPI application, SQLAlchemy database models, and Firestore integration.<br>
your_firestore_credentials.json: Replace this file with your Firestore credentials JSON.<br>
test.db: The SQLite database used in this project (you can replace it with your preferred SQL database).<br>
Features<br>
Create Item: This POST endpoint (/items/) allows you to create a new item. It accepts a JSON payload containing the item's name and description. The item <br>is simultaneously stored in both Firestore and the SQL database.
Read Item by ID: This GET endpoint (/items/{item_id}) retrieves item information by its ID. It returns a JSON response with details from both Firestore and <br>the SQL database.
Read All Items: This GET endpoint (/items/) lists all items stored in both Firestore and the SQL database.<br>
Usage<br>
Replace "your_firestore_credentials.json" with the actual path to your Firestore credentials JSON file.<br>
Configure the database URL in the DATABASE_URL variable according to your preferred SQL database.<br>
Run the application by executing the script.<br>
The application starts an ASGI server (uvicorn) and listens on port 8000 by default.<br>
Use HTTP clients like curl, httpie, or a web browser to interact with the API endpoints.<br>
Error Handling<br>
The application includes basic error handling and responds with appropriate error codes and messages when issues arise, such as when an item is not found.<br>
<br>
Potential Improvements<br>
Consider enhancing the project by adding more API endpoints and expanding the functionality to include features related to item management in both <br>Firestore and SQL databases.
