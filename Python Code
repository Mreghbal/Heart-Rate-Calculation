def calculate_heart_rate(age):
    max_heart_rate = 220 - age
    target_min = 0.5 * max_heart_rate
    target_max = 0.85 * max_heart_rate
    return target_min, target_max

def get_user_condition(heart_rate, target_min, target_max):
    if heart_rate < target_min:
        return "Below target range"
    elif heart_rate >= target_min and heart_rate <= target_max:
        return "Within target range"
    else:
        return "Above target range"

# Get user input for age
age = int(input("Enter your age: "))

# Calculate heart rate
target_min, target_max = calculate_heart_rate(age)

# Get user input for heart rate
heart_rate = int(input("Enter your heart rate: "))

# Determine the user's condition
user_condition = get_user_condition(heart_rate, target_min, target_max)

# Print the results
print(f"Target Heart Rate Range: {target_min} - {target_max}")
print(f"Your Heart Rate: {heart_rate}")
print(f"Condition: {user_condition}")
