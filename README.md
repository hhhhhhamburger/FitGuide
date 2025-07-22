# FitGuide

FitGuide is a command-line Python application designed to help users manage their health and fitness goals. It provides tools for calculating daily energy expenditure, body mass index, exercise calorie burn, daily weight loss targets, and offers healthy meal suggestions. The program is designed with safety in mind, encouraging gradual and sustainable weight loss.

## Features

- **TDEE Calculator**: Calculates your Total Daily Energy Expenditure based on your gender, height, weight, age, and weekly exercise frequency.
- **BMI Calculator**: Computes your Body Mass Index and provides health advice based on your BMI category.
- **Exercise Calorie Calculator**: Estimates calories burned for various exercises, including running, walking, pull-ups, jumping rope, and sit-ups.
- **Daily Weight Loss Planner**: Helps you track your daily calorie intake and expenditure to achieve a safe weight loss of 1-2 kilograms per week.
- **Meal Suggestions**: Recommends healthy meal options for breakfast, lunch, and dinner, tailored to your preferences and dietary needs.

## Usage

1. Run the program:
   ```bash
   python main.py
   ```
2. Follow the on-screen prompts to select a function:
   - 1: TDEE Calculator
   - 2: BMI Calculator
   - 3: Exercise Calorie Calculator
   - 4: Daily Weight Loss Planner
   - 5: Meal Suggestions
   - 6: Exit

## File Overview

- `main.py`: The main entry point. Handles user interaction and menu navigation.
- `tdee_calculator.py`: Contains the TDEE calculation logic.
- `bmi_calculator.py`: Contains the BMI calculation and advice logic.
- `exercise_calculator.py`: Calculates calories burned for different exercises.
- `lose_weight.py`: Helps users plan daily calorie intake and expenditure for weight loss.
- `food_suggestion.py`: Provides meal suggestions based on user preferences.

## Safety Notice

This program is designed to promote safe weight loss (1-2 kg per week). Rapid weight loss can cause health issues such as headaches, fatigue, irritability, and hair loss. Always consult a healthcare professional before starting any weight loss program.

## Requirements

- Python 3.x

No external libraries are required. 
