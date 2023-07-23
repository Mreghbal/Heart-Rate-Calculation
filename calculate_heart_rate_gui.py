import tkinter as tk

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

# Define GUI functions
def calculate_button_clicked():
    age = int(age_entry.get())
    target_min, target_max = calculate_heart_rate(age)

    heart_rate = int(heart_rate_entry.get())
    user_condition = get_user_condition(heart_rate, target_min, target_max)

    target_range_label.config(text=f"Target Heart Rate Range: {target_min} - {target_max}")
    heart_rate_label.config(text=f"Your Heart Rate: {heart_rate}")
    condition_label.config(text=f"Condition: {user_condition}")

# Create the main window
window = tk.Tk()
window.title("Heart Rate Calculator")

# Create labels
age_label = tk.Label(window, text="Enter your age:")
age_label.pack()

# Create entry for age input
age_entry = tk.Entry(window)
age_entry.pack()

heart_rate_label = tk.Label(window, text="Enter your heart rate:")
heart_rate_label.pack()

# Create entry for heart rate input
heart_rate_entry = tk.Entry(window)
heart_rate_entry.pack()

# Create button to calculate heart rate
calculate_button = tk.Button(window, text="Calculate", command=calculate_button_clicked)
calculate_button.pack()

# Create labels to display results
target_range_label = tk.Label(window, text="")
target_range_label.pack()

heart_rate_label = tk.Label(window, text="")
heart_rate_label.pack()

condition_label = tk.Label(window, text="")
condition_label.pack()

# Run the GUI main loop
window.mainloop()
