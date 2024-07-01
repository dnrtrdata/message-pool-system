import subprocess
import sys

def install_dependencies():
    dependencies = [
        "openai",
        "numpy",
        "pandas",
        "dash",
        "dash-bootstrap-components",
        "dash-core-components",
        "dash-html-components",
        "plotly"
    ]
    
    for dependency in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])
            print(f"Successfully installed {dependency}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {dependency}: {e}")

if __name__ == "__main__":
    install_dependencies()
