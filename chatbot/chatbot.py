import tkinter as tk
from tkinter import scrolledtext
from main import get_response  # Import the chatbot logic from chatbot.py

# GUI setup using Tkinter
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rule-Based Chatbot")
        
        # Set up the chat window
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, state='disabled', font=("Arial", 12))
        self.chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Entry box for user input
        self.entry_box = tk.Entry(root, width=60, font=("Arial", 12))
        self.entry_box.grid(row=1, column=0, padx=10, pady=10)
        self.entry_box.bind("<Return>", self.send_message)
        
        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, width=12, font=("Arial", 12))
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

    def send_message(self, event=None):
        user_input = self.entry_box.get().strip()
        if user_input:
            self.display_message(f"You: {user_input}")
            response = get_response(user_input)  # Call the get_response function from chatbot.py
            self.display_message(f"Chatbot: {response}")
        self.entry_box.delete(0, tk.END)
    
    def display_message(self, message):
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, message + "\n\n")
        self.chat_window.config(state='disabled')
        self.chat_window.yview(tk.END)

# Run the chatbot GUI
if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
