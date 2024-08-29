import tkinter as tk
from tkinter import scrolledtext
from main import main
import sys

# Color Scheme
BACKGROUND_COLOR = "#2C3E50"
TEXT_COLOR = "#ECF0F1"
BUTTON_COLOR = "#FFFFFF"  # White button background
BUTTON_TEXT_COLOR = "#000000"  # Black text color
BUTTON_HOVER_COLOR = "#BDC3C7"  # Light gray for hover effect
TEXT_AREA_COLOR = "#34495E"
FONT = ("Helvetica", 12)
BUTTON_RADIUS = 10  # Radius for rounded corners
BUTTON_WIDTH = 20

class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.config(state='normal')
        self.widget.insert(tk.END, str)
        self.widget.config(state='disabled')
        self.widget.see(tk.END)  # Scroll to the end

    def flush(self):
        pass  # Required for file-like object

class RoundedButton(tk.Button):
    def __init__(self, parent, text, command=None, **kwargs):
        super().__init__(parent, text=text, command=command, **kwargs)
        self.config(bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=FONT, relief=tk.FLAT, borderwidth=0)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        self.config(width=BUTTON_WIDTH, height=2)

    def on_hover(self, event):
        self.config(bg=BUTTON_HOVER_COLOR)

    def on_leave(self, event):
        self.config(bg=BUTTON_COLOR)

class TradingBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Brokers Trading Bot")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Title Label
        title_label = tk.Label(root, text="Interactive Brokers Trading Bot", font=("Helvetica", 18, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        title_label.pack(pady=10)

        # Frame for Buttons
        button_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=10)

        # Start Button
        self.start_button = RoundedButton(button_frame, text="Start Trading Bot", command=self.start_bot)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        # Statistics Button
        self.stats_button = RoundedButton(button_frame, text="Show Statistics", command=self.show_statistics)
        self.stats_button.grid(row=0, column=1, padx=5, pady=5)

        # Logs Area
        self.log_area = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled', bg=TEXT_AREA_COLOR, fg=TEXT_COLOR, font=FONT, wrap=tk.WORD)
        self.log_area.pack(padx=10, pady=10)

        # Redirect stdout to log_area
        sys.stdout = TextRedirector(self.log_area)

        # Status Bar
        self.status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=FONT)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def start_bot(self):
        self.status.config(text="Bot Running...")
        print("Starting Trading Bot...\n")
        self.root.after(100, main)
        self.status.config(text="Bot Finished Execution")

    def show_statistics(self):
        from trading_statistics import TradingStatistics
        stats = TradingStatistics()
        stats_output = stats.get_stats()
        print(f"Statistics: {stats_output}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = TradingBotGUI(root)
    root.mainloop()
