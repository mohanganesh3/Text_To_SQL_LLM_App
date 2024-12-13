# Text-to-SQL LLM App: The Future of Database Queries

Welcome to Text-to-SQL LLM App – a revolutionary web application that transforms plain English questions into SQL queries, leveraging the power of Google’s Gemini model. Forget the days of manually writing SQL queries; simply ask questions, and let the AI do the work!

This project is the perfect example of how Generative AI can seamlessly integrate with databases, enabling anyone to interact with data without needing to know SQL. Whether you’re a beginner or a seasoned developer, this app makes querying databases as simple as asking a question.

## 🎬 Demo 
   1.Launch the app by running streamlit run app.py in the terminal and open it in your browser.
 
  <img width="673" alt="Screenshot 2024-12-13 at 8 17 35 AM" src="https://github.com/user-attachments/assets/855c59cf-0ed5-4c4d-bd58-509497dc1cee" />
  
   2.Ask a question in natural language, like “How many students are in Data Science class?”.
   
   3.Show the generated SQL query and the response fetched from the database directly on the app interface.
 
 <img width="698" alt="Screenshot 2024-12-13 at 8 19 07 AM" src="https://github.com/user-attachments/assets/df4b970f-61ae-4bc5-9b5d-544edb2ee760" />



## 🚀 Features
	•	Ask Anything, Get SQL: Ask natural language questions like “How many students are in the Data Science class?” and get SQL queries instantly.
	•	AI-Powered: Powered by Google Gemini, a cutting-edge Generative AI model that understands your questions and generates SQL queries.
	•	User-Friendly Interface: Built with Streamlit, offering an intuitive and clean interface for smooth interaction.
	•	SQLite Backend: All data is stored in an SQLite database, ensuring fast, reliable query results.
	•	Adaptable to Any Database: Customize the database schema for any use case and seamlessly interact with it via plain English.

## 🛠️ Tech Stack
	•	Frontend: Built with Streamlit for an interactive web interface.
	•	Backend: Python with SQLite to handle database operations.
	•	Generative AI: Powered by Google Gemini for intelligent query generation.
	•	Environment Management: Manage dependencies with virtualenv and pip.
	•	Version Control: Managed with Git and hosted on GitHub.

## 📦 Installation

    Ready to bring the magic to your local machine? Here’s how you can set up the project in no time:

    1. Clone the repository:

    git clone https://github.com/mohanganesh3/Text_To_SQL_LLM_App.git
    cd Text_To_SQL_LLM_App

    2. Set up your virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

    3. Install the dependencies:

    pip install -r requirements.txt

    4. Set up the environment variables:

    Create a .env file in the root directory and add your Google API Key:

    GOOGLE_API_KEY=your_google_api_key_here

    5. Run the app:

    streamlit run app.py

    Boom! The app is live and ready for you to interact with.

## 🤖 How It Works
	1.	Natural Language Processing (NLP): You type in any SQL-related question, and the app uses Google Gemini to understand the intent.
	2.	SQL Query Generation: Based on your question, the app generates an appropriate SQL query, such as SELECT, INSERT, UPDATE, etc.
	3.	Database Interaction: The query is executed on an SQLite database, and the results are displayed back to you instantly.

    For example, you could ask:
	    •	“How many students are in the Data Science class?” – The app will generate SELECT COUNT(*) FROM STUDENT WHERE CLASS='Data Science';
	    •	“List all students in section A” – The app will generate SELECT * FROM STUDENT WHERE SECTION='A';

## 💡 Example Use Cases

    Here are a few things you can do with this app:
	    •	Database Exploration: Ask questions about the contents of the database, like “Who scored more than 80 marks?” or “What is the average marks of students in Data Science?”
	    •	Data Insertion: Ask the app to add new records, like “Insert a student named John into the Data Science class with 75 marks.”
	    •	Data Analysis: Ask more complex questions, such as “Which class has the highest average marks?”

## 📂 Project Structure

    Here’s how the project is organized:

    Text_To_SQL_LLM_App/
    │
    ├── app.py                # Main Streamlit app file
    ├── requirements.txt      # Project dependencies
    ├── .env                  # Environment variables (e.g., Google API key)
    ├── README.md             # Project documentation
    └── database/
        └── student.db        # SQLite database file with sample data

## 🎯 Contributing

    We’d love for you to contribute to this project! Whether it’s a bug fix, feature request, or documentation improvement, your help is always welcome.

    To contribute:
	    1.	Fork the repository.
	    2.	Create a new branch (git checkout -b feature-name).
	    3.	Make your changes.
	    4.	Commit your changes (git commit -m 'Add new feature').
	    5.	Push your branch (git push origin feature-name).
	    6.	Open a Pull Request.


## 💬 Final Thoughts

    This project is a great showcase of how Generative AI can simplify database interactions. Whether you’re a beginner exploring AI, a developer looking to integrate AI into your          workflow, or an interviewer looking for innovative solutions, this app demonstrates the potential of AI-powered query generation in real-world applications.

    So, go ahead, ask your question, and let the app handle the SQL for you!
