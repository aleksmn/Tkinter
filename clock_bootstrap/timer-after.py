import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")

        self.time_left = 10  # Set the timer for 10 seconds
        self.label = tk.Label(root, text=f"Time left: {self.time_left}", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Timer", command=self.reset_timer)
        self.reset_button.pack(pady=10)

    def start_timer(self):
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)  # Call this function again after 1000 ms (1 second)
        else:
            self.label.config(text="Time's up!")

    def reset_timer(self):
        self.time_left = 10  # Reset to 10 seconds
        self.label.config(text=f"Time left: {self.time_left}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()