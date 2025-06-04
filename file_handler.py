import os
import time

class FileHandler:
    def __init__(self, file_path=None):
        self.file_path = file_path or 'data.txt'
        self.file_last_position = 0

        # Ensure the directory exists
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Create the file if it does not exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as _:  # Create an empty file
                pass

        # Open and seek to end to track last position
        with open(self.file_path, 'r') as file:
            file.seek(0, os.SEEK_END)
            self.file_last_position = file.tell()

    def append_to_file(self, data):
        try:
            with open(self.file_path, 'a') as file:
                file.write(data + "\n")
                file.flush()
            print(f"Data appended successfully to {self.file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_data(self):
        while not os.path.exists(self.file_path):
            time.sleep(0.5)

        with open(self.file_path, 'r') as file:
            file.seek(self.file_last_position)
            for line in file:
                yield line.strip()
            self.file_last_position = file.tell()

    def get_last_line(self):
        latest_line = None
        for new_data in self.get_data():
            latest_line = new_data
        return latest_line

    def get_file_name(self):
        return os.path.basename(self.file_path)

    def switch_to_new_file(self, new_file_path):
        self.file_path = new_file_path
        self.file_last_position = 0

        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Wait until the new file exists or create it
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as _:
                pass
