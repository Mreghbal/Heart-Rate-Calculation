# Heart Rate Calculation

This repository contains a Python script that calculates the target heart rate range based on age and determines the user's condition based on their heart rate. This README provides a complete explanation of the subject, step-by-step instructions to run and use the code, and additional information for GitHub followers.

## Table of Contents
- [Introduction](#introduction)
- [Explanation](#explanation)
- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Running the Code](#running-the-code)
- [Follow Me](#follow-me)

## Introduction
Heart rate is an important indicator of cardiovascular health and fitness. It represents the number of times the heart beats per minute (bpm). The maximum heart rate varies with age, and it can be estimated using the formula: `220 - age`. The target heart rate range is often used during exercise to ensure that the intensity level is appropriate for achieving specific fitness goals.

This Python script calculates the target heart rate range based on the user's age and determines whether their current heart rate falls within, below, or above the target range. It provides valuable information for individuals who want to monitor their heart rate during physical activities and maintain a healthy lifestyle.

## Explanation
The script consists of two main functions:

1. `calculate_heart_rate(age)`: This function takes the user's age as input and calculates the target heart rate range. It uses the formula `220 - age` to determine the maximum heart rate and then calculates the target minimum and maximum values multiplying the maximum heart rate by 0.5 and 0.85, respectively.

2. `get_user_condition(heart_rate, target_min, target_max)`: This function takes the user's heart rate, target minimum, and target maximum as inputs and determines the user's condition based on their heart rate. If the heart rate is below the target minimum, it returns "Below target range". If the heart rate is within the target range, it returns "Within target range". Otherwise, it returnsAbove target range".

The script prompts the user to enter their age and heart rate. It then calls the `calculate_heart_rate` function calculate the target heart rate range based on the entered age. Next, it calls the `get_user_condition` function to determine the user's condition based on the entered heart rate and the calculated target range. Finally, it prints the target heart rate range, the user's heart rate, and their condition.

## Usage

###erequisites
To run this code, you need to have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/).

### Running the Code
Follow these steps to run and use the code:

1. Clone the repository to your local machine or download the `heart_rate_calculation.py` file.

2. Open a terminal or command prompt and navigate to the directory where the `heart_rate_calculation.py` file is located.

3. Run the following command to execute the script:
   ```
   python heart_rate_calculation
   ```

4. Enter your age when prompted and press Enter.

5. Enter your heart rate when prompted and press Enter.

6. The script will calculate the target heart rate range and determine your condition based on the entered values. The results will be displayed in the terminal.

Example output:
```
Enter your age: 30
Enter your heart rate: 150

Target Heart Rate Range: 95.0 - 161.5
Your Heart Rate: 150
Condition: Within target range
```

Congratulations! You have successfully run the heart rate calculation script.

## Follow Me
If you find this project helpful interesting, feel free to follow me on LinkedIn and Twitter for more updates and similar projects.

LinkedIn: [Reza Eghbal](https://www.linkedin.com/in/mreghbal)

Twitter: [Reza Eghbal](https://twitter.com/mreghbal)

Thank you for your support!
