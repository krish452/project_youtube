# project_youtube

YouTube API Data Extraction and Storage

Description: This Python script demonstrates how to use the YouTube Data API, provided by Google Cloud Platform (GCP), to fetch information about videos based on a search query and store the data in a SQLite database. The script utilizes the requests library to make HTTP requests to the YouTube API, and the sqlite3 module to interact with the SQLite database.

Key Features:

API Key Integration: The script securely retrieves the YouTube Data API key from an environment variable using the dotenv library, ensuring the confidentiality of the API key.
Data Extraction: It extracts information about YouTube videos, including the video ID, channel ID, title, and channel name, from the API response.
Database Creation: The script creates a SQLite database named videos.db and defines a table named videos to store the extracted video data.
Data Insertion: It inserts the extracted video details into the SQLite database using parameterized SQL queries to prevent SQL injection attacks.
Data Viewing: The script provides a function to view the contents of the database, allowing easy verification of the stored data.
Usage Instructions: To use the script, users need to set up a YouTube Data API key through Google Cloud Platform and store it in a .env file. They can then specify the search query and maximum number of results to fetch. After executing the script, users can view the stored video data by running the viewing_db() function.

Technologies Used: Python, requests library, dotenv library, SQLite, SQL, Google Cloud Platform.

Potential Extensions: This script can be extended to include additional functionality, such as updating existing records, handling pagination for fetching multiple pages of search results, and implementing error handling for API requests.

Learning Objectives: This project demonstrates proficiency in working with web APIs, handling JSON data, database management using SQLite, integrating environment variables for security, and leveraging cloud services for data retrieval and integration into Python projects.
