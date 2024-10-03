# Quizzler - Python Quiz App
![Screenshot 2024-10-03 224156](https://github.com/user-attachments/assets/09bf9f37-e9d5-4020-a8cc-4d67106f918f)

This is a Python-based quiz application that retrieves questions from the Open Trivia Database API and allows users to answer True/False questions through a graphical user interface (GUI) built using `tkinter`. The application demonstrates how to interact with external APIs to retrieve data dynamically, parse the data, and use it to drive the logic and user experience of the application.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Acknowledgments](#acknowledgments)

## Features

- **API Integration**: Fetches quiz questions dynamically from the [Open Trivia Database API](https://opentdb.com/), demonstrating the ability to request, retrieve, and parse JSON data from a remote server.
- Displays questions in a graphical user interface (GUI) using `tkinter`.
- Allows users to answer True/False questions and provides real-time feedback.
- Keeps track of the user's score and shows the final score at the end of the quiz.
- Highlights correct answers in green and incorrect answers in red.

## Installation

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- Internet connection (for fetching questions)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/galgrinfeld/Quizzler.git
    ```

2. **Install required Python libraries:**

    Navigate to the project directory and install the necessary dependencies (if any). For this project, you'll need the `requests` library for making HTTP requests to the Open Trivia Database API.

    ```bash
    pip install requests
    ```

3. **Run the Application:**

    After installing dependencies, you can run the application by executing the main Python file:

    ```bash
    python main.py
    ```

## Usage

This project leverages API integration to dynamically fetch questions for the quiz. The questions are not hardcoded but are retrieved in real-time from the [Open Trivia Database API](https://opentdb.com/) using the following process:

1. **API Request**:
    - When the quiz starts, the application sends a GET request to the Open Trivia Database API to retrieve 10 True/False type questions in JSON format.
    - The data is parsed, and the questions are dynamically loaded into the app.

2. **Answering Questions**:
    - The quiz will begin by displaying questions one by one in the `tkinter` GUI.
    - Select either **True** or **False** using the corresponding buttons.
    - The background will flash **green** for a correct answer and **red** for an incorrect answer.
    - After 10 questions, the quiz will display the final score.

## Project Structure

The project consists of the following files:

- `main.py`: The main file that initializes and runs the quiz.
- `question_model.py`: Contains the `Question` class that represents a quiz question.
- `quiz_brain.py`: Contains the `QuizBrain` class, which manages the quiz logic and handles the interaction with the API data.
- `ui.py`: Contains the `QuizeInterFace` class, which handles the GUI using `tkinter`.
- `data.py`: Retrieves question data from the Open Trivia Database API using the `requests` library.
- `/images`: Contains the `true.png` and `false.png` images for the GUI buttons.

## Requirements

- Python 3.x
- Libraries:
  - `requests`: Used to fetch quiz questions from the Open Trivia Database.
  - `tkinter`: For building the graphical user interface (this is included with Python).

## Acknowledgments

- The quiz questions are fetched from the [Open Trivia Database](https://opentdb.com/).
- This project is inspired by Dr. Angela Yu's Python Bootcamp on Udemy.
