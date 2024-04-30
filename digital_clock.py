""" Digital Clock by Kevin Leon Smith 8.23.23 """

import datetime
import tkinter as tk

def interpolate_color(start_color, end_color, percentage):
    """Interpolate between two RGB colors."""
    return tuple(int(start_color[i] + (end_color[i] - start_color[i]) * percentage) for i in range(3))

def update_background():
    """Update the background color based on the current time."""
    now = datetime.datetime.now()
    hour = now.hour + now.minute / 60
    
    # Define transition start and end times (18:00 to 6:00)
    start = 18  # Start transition at 18:00 (6 PM)
    end = 6     # End transition at 6:00 (6 AM)
    
    if start <= hour or hour <= end:
        # Normalize hour to fit the transition timeline
        if hour > start:
            normalized_hour = hour - start
        else:
            normalized_hour = hour + 24 - start
        
        # Calculate percentage of the transition completed
        max_hours = 12  # Number of hours from 6 PM to 6 AM
        percentage = normalized_hour / max_hours
        
        # Define start and end colors (black to light blue)
        start_color = (0, 0, 0)      # Black
        end_color = (173, 216, 230)  # Light blue
        
        # Interpolate color
        interp_color = interpolate_color(start_color, end_color, percentage)
        
        # Convert RGB to hexadecimal
        hex_color = '#{:02x}{:02x}{:02x}'.format(*interp_color)
        
        # Update the background color
        clock.config(bg=hex_color)
    else:
        # If it's not within the transition period, set to end color if AM or start color if PM
        if hour > end:
            clock.config(bg="#000000")  # Black
        else:
            clock.config(bg="#add8e6")  # Light blue
    
    # Schedule this function to run again after 60 seconds
    clock.after(60000, update_background)

# Create the main window
window = tk.Tk()
window.title('Clock with Changing Background Color')
window.geometry('300x300')

# Create a label for displaying the time
clock = tk.Label(window, font=('Arial', 24), bg="#000000", fg="#FFFFFF")
clock.pack(expand=True)

# Start the background update process
update_background()

# Update the clock every second
def update_clock():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_clock)

update_clock()

# Run the GUI
window.mainloop()
