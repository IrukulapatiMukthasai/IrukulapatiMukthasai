import tkinter as tk
from datetime import datetime
import time
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch / Clock")

        # Clock label
        self.clock_label = tk.Label(root, text="", font=("Arial", 24))
        self.clock_label.pack(pady=10)

        # Stopwatch label
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 36), fg="blue")
        self.stopwatch_label.pack(pady=20)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start", command=self.start)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=5)

        # Stopwatch variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.update_clock()

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        while self.running:
            elapsed = time.time() - self.start_time + self.elapsed_time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))
            self.stopwatch_label.config(text=formatted_time)
            time.sleep(0.1)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            threading.Thread(target=self.update_stopwatch, daemon=True).start()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time += time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

# Run the application
root = tk.Tk()
app = StopwatchClockApp(root)
root.mainloop()

