
from gui.main_window import MainWindow
from message_pool.message_pool import MessagePool
from llm_interfaces.ue5_interface import UE5Interface
from message_pool.learning_mechanism import LearningMechanism

def main():
    message_pool = MessagePool()
    ue5 = UE5Interface(project_path="path/to/your/ue5/project")
    llm_interfaces = [ue5]

    learning_mechanism = LearningMechanism(message_pool, llm_interfaces)
    
    app = MainWindow(message_pool, llm_interfaces)
    app.mainloop()

if __name__ == "__main__":
    main()
