from pathlib import Path

class CodeLoader:

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def get_python_files(self):
        files = list(self.project_path.rglob("*.py"))
        return files

    def print_files(self):
        files = self.get_python_files()

        print("\nPython Files Found:\n")

        for file in files:
            print(file)