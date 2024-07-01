
import tkinter as tk
from message_pool_view import MessagePoolView
from llm_interaction_view import LLMInteractionView

class MainWindow(tk.Tk):
    def __init__(self, message_pool, llm_interfaces):
        super().__init__()
        self.title("Message Pool System")

        self.message_pool_view = MessagePoolView(self, message_pool)
        self.llm_interaction_view = LLMInteractionView(self, llm_interfaces)

        self.message_pool_view.pack(side="left", fill="both", expand=True)
        self.llm_interaction_view.pack(side="right", fill="both", expand=True)
