# Pet Program

**A Secure Data-Entry Form using OOP Encapsulation** 

## Project Overview
This project acts as a secure database entry form for a veterinary clinic or pet registry. It perfectly demonstrates how an application takes raw user input and securely injects it into a protected Object using **Encapsulation**.

## Core OOP Features
* **Empty State Initialization:** The `Pet` class initializes with completely blank private fields (`__name`, `__animal_type`, `__age`), waiting securely for authorized data.
* **Data Injection (Setters):** The GUI captures user input from text boxes and securely passes it through setter methods to populate the object.
* **Data Retrieval (Getters):** Immediately after saving, the program uses getter methods to extract the protected data and generate a live digital receipt on the screen.

## How to Run the Program
1. Open the `pet_program` folder in your terminal or IDE.
2. Run the main execution driver:
   ```bash
   python pet_main_file.py
