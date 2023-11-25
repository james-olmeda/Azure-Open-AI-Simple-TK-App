import tkinter as tk
from tkinter.font import Font
import threading
from completion import Completion

class Chat:
    def __init__(self):
        # Initialize the main window
        self.main_window = tk.Tk()
        self.main_window.title("Chat")
        self.main_window.geometry("600x600")

        # Create a font for the chat messages
        self.chat_font = Font(family="Helvetica", size=16)

        # Create a chat window (Text widget) and configure text alignment
        self.chat_window = tk.Text(self.main_window, state=tk.DISABLED, wrap=tk.WORD, font=self.chat_font)
        self.chat_window.tag_configure('right', justify='right')
        self.chat_window.tag_configure('left', justify='left')
        self.chat_window.pack(padx=10, pady=10, expand=True, fill='both')

        # Create an entry field for user input
        self.entry = tk.Entry(self.main_window, width=30)
        self.entry.pack(padx=10, pady=10, fill='x', expand=True)
        self.entry.bind("<Return>", self.send_message)

        # Create a send button to trigger sending messages
        self.send_button = tk.Button(self.main_window, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10, side='right')

    def fetch_gpt_response(self, user_message):
        # Enable the chat window for editing
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, f"\n\nGPT: ", 'left')
        self.chat_window.config(state=tk.DISABLED)
        
        # Fetch and display partial responses from GPT in real-time
        for partial_response in Completion.gptResponse(user_message):
            self.main_window.after(0, self.update_chat_window, partial_response, True)

        # Add a newline for better separation
        self.main_window.after(0, self.update_chat_window, "\n\n", True)

    def update_chat_window(self, response, append=False):
        # Enable the chat window for editing
        self.chat_window.config(state=tk.NORMAL)

        # Append or display the response based on the 'append' parameter
        if append:
            self.chat_window.insert(tk.END, response)
        else:
            self.chat_window.insert(tk.END, f"\n\nGPT: {response}\n\n", 'left')
        
        # Disable the chat window to prevent further editing
        self.chat_window.config(state=tk.DISABLED)

    def send_message(self, event=None):
        user_message = self.entry.get()
        if user_message:
            # Enable the chat window for editing
            self.chat_window.config(state=tk.NORMAL)
            
            # Display the user message and format it as "User: message"
            self.chat_window.insert(tk.END, f"\n\nUser: {user_message}  \n\n", 'right')
            
            # Disable the chat window to prevent further editing
            self.chat_window.config(state=tk.DISABLED)
            
            # Clear the user input field
            self.entry.delete(0, tk.END)
            
            # Start a new thread to fetch GPT responses
            threading.Thread(target=self.fetch_gpt_response, args=(user_message,)).start()

    def run(self):
        # Start the main GUI event loop
        self.main_window.mainloop()


