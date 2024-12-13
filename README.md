# Workout-Tracking Project

This is a Python-based project to track your workouts. It integrates with the Nutritionix API to analyze your exercises and logs the data into a Google Sheet via the Sheety API.

## Features
- Input your exercise details in natural language.
- Automatically calculate calories burned, exercise duration, and other metrics using the Nutritionix API.
- Log workout data (date, time, exercise, duration, calories) to a Google Sheet.

## Technologies Used
- **Python**
- **Nutritionix API**
- **Sheety API**

## Setup Instructions

### Prerequisites
1. Python 3.8 or above installed on your system.
2. Accounts and credentials for:
   - [Nutritionix API](https://www.nutritionix.com/)
   - [Sheety API](https://sheety.co/)

### Environment Variables
Set the following environment variables:
- `application_id` : Your Nutritionix Application ID.
- `application_keys` : Your Nutritionix Application Key.
- `sheety_username` : Your Sheety username.
- `sheety_password` : Your Sheety password.
- `sheety_url` : The endpoint URL of your Sheety project.

Export these variables in your terminal:
```bash
export application_id="your_application_id"
export application_keys="your_application_keys"
export sheety_username="your_username"
export sheety_password="your_password"
export sheety_url="your_sheety_url"
```

### Install Dependencies
Use `pip` to install required libraries:
```bash
pip install requests
```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/workout-tracking.git
   cd workout-tracking
   ```

2. Run the script:
   ```bash
   python workout_tracker.py
   ```

3. Enter your workout details when prompted, e.g., `I ran 5 km`.

4. Check your Google Sheet for the updated workout log.

## Example Workflow
1. Input:
   ```
   Tell me which exercise you did: I ran 3 miles and cycled for 30 minutes.
   ```

2. Logged Data in Google Sheet:  
   | Date&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Time&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Exercise| Duration | Calories |  
   |-----------------|--------------|-------------|--------------|------------|  
   | 12-12-2024 | 08:15 PM | Running | 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |  
   | 12-12-2024 | 08:15 PM | Cycling&nbsp;&nbsp; | 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;             | 250&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      |  

## Contribution
Feel free to contribute to this project by submitting a pull request or reporting issues.

## License
This project is licensed under the MIT License.
