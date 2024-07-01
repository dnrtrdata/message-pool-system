
# Message Pool System

## Overview

The Message Pool System is a framework designed to facilitate interactions between multiple Large Language Models (LLMs) and Unreal Engine 5.4. It allows LLMs to exchange messages, share knowledge, and learn from each other's contributions through a central message pool. This project includes a graphical user interface (GUI) for monitoring and managing these interactions, making it easier to oversee and control the process.

## Purpose

The primary goal of this system is to create a collaborative environment where different LLMs can:
- **Communicate**: Exchange messages through a central pool.
- **Learn**: Update their knowledge based on the messages received from other LLMs and Unreal Engine 5.4 interactions.
- **Collaborate**: Work together to provide more comprehensive and enriched responses for Unreal Engine 5.4 projects.

## Components

### 1. Message Pool
The message pool is a central repository where all messages exchanged between LLMs and Unreal Engine 5.4 are stored. It manages the addition and retrieval of messages to ensure seamless communication.

**Key Files**:
- `message_pool/message_pool.py`

### 2. LLM Interfaces
These interfaces facilitate communication with various LLM APIs and Unreal Engine 5.4. Each LLM and Unreal Engine have their own interface to handle sending and receiving messages.

**Key Files**:
- `llm_interfaces/ue5_interface.py`

### 3. Learning Mechanism
This component processes the messages in the pool and updates the LLMs and Unreal Engine based on the interactions. It ensures that the LLMs learn from each other and improve over time.

**Key Files**:
- `message_pool/learning_mechanism.py`

### 4. GUI
The graphical user interface provides a user-friendly way to monitor and manage the message exchanges between LLMs and Unreal Engine. It displays the message pool and allows interaction with the LLMs.

**Key Files**:
- `gui/main_window.py`

### 5. Main Script
The main script initializes and runs the entire system, tying together all the components and starting the GUI.

**Key Files**:
- `main.py`

## Getting Started

### Prerequisites
- Python 3.x
- Required Python packages (listed in `requirements.txt`)
- Unreal Engine 5.4

### Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/message-pool-system.git
   cd message-pool-system
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set up Unreal Engine 5.4**:
   - Ensure Unreal Engine 5.4 is installed and configured on your system.
   - Set the project path in `ue5_interface.py`.

### Running the System

To start the Message Pool System, run the main script:
```
python main.py
```
This will launch the GUI, and you can begin monitoring and managing the interactions between the LLMs and Unreal Engine 5.4.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).

---

Thank you for checking out the Message Pool System. We hope it facilitates your projects and enhances your LLM and Unreal Engine interactions!
