
from gui.main_window import MainWindow
from message_pool.message_pool import MessagePool
from llm_interfaces.llm1_interface import LLM1Interface
from llm_interfaces.llm2_interface import LLM2Interface
from message_pool.learning_mechanism import LearningMechanism

def main():
    message_pool = MessagePool()
    llm1 = LLM1Interface(api_key="YOUR_API_KEY")
    llm2 = LLM2Interface(api_key="YOUR_API_KEY")
    llm_interfaces = [llm1, llm2]

    learning_mechanism = LearningMechanism(message_pool, llm_interfaces)
    
    app = MainWindow(message_pool, llm_interfaces)
    app.mainloop()

if __name__ == "__main__":
    main()
