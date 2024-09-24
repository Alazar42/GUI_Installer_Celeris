import os
import shutil
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk  # Import ttk from ttkbootstrap
from threading import Thread
import subprocess
import requests

class CelerisInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("Celeris Installer")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.header = ttk.Label(root, text="Celeris Framework Installer", font=("Helvetica", 16, "bold"))
        self.header.pack(pady=15)

        # Install button
        self.install_button = ttk.Button(root, text="Download and Install Celeris", command=self.install_celeris)
        self.install_button.pack(pady=20)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)
        self.progress_label = ttk.Label(root, text="")
        self.progress_label.pack()

    def install_celeris(self):
        self.install_button.config(state=tk.DISABLED)  # Disable the button during installation

        # Start the installation in a separate thread to avoid freezing the GUI
        installation_thread = Thread(target=self.perform_installation)
        installation_thread.start()

    def perform_installation(self):
        try:
            # Check for internet connection
            self.check_internet_connection()

            # Clone the Celeris repository
            celeris_repo_url = "https://github.com/Alazar42/Celeris.git"
            clone_dir = os.path.join(os.getcwd(), 'Celeris')

            if os.path.exists(clone_dir):
                self.delete_existing_directories(clone_dir)

            # Use subprocess to clone the repository
            self.run_command(["git", "clone", celeris_repo_url, clone_dir])

            # Paths for Celeris files
            include_src = os.path.join(clone_dir, 'include')
            lib_src = os.path.join(clone_dir, 'lib')

            # Destination paths (default for Unix-like systems)
            include_dst = '/usr/local/include/celeris'
            lib_dst = '/usr/local/lib/celeris'

            # Delete existing directories if they exist
            self.delete_existing_directories(include_dst)
            self.delete_existing_directories(lib_dst)

            # Create destination directories
            os.makedirs(include_dst, exist_ok=True)
            os.makedirs(lib_dst, exist_ok=True)

            # List all files to copy (both include and lib folders)
            include_files = [(os.path.join(root, f), os.path.relpath(os.path.join(root, f), include_src))
                             for root, _, files in os.walk(include_src) for f in files]
            lib_files = [(os.path.join(root, f), os.path.relpath(os.path.join(root, f), lib_src))
                          for root, _, files in os.walk(lib_src) for f in files]

            all_files = include_files + lib_files
            total_files = len(all_files)

            # Copy files with progress update
            for i, (src, rel_path) in enumerate(all_files):
                dst_dir = include_dst if src.startswith(include_src) else lib_dst
                dst_file = os.path.join(dst_dir, rel_path)
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                shutil.copy2(src, dst_file)

                # Update progress bar
                self.progress["value"] = (i + 1) / total_files * 100
                self.progress_label.config(text=f"Installing... {int(self.progress['value'])}%")
                self.root.update_idletasks()

            # Show success message and reset UI
            self.reset_ui(success=True)

        except Exception as e:
            # Handle errors and reset UI
            self.reset_ui(success=False, error_message=str(e))

    def check_internet_connection(self):
        """Check if the internet connection is available."""
        try:
            requests.get("http://www.google.com", timeout=5)
        except requests.ConnectionError:
            raise Exception("No internet connection. Please check your network settings.")

    def run_command(self, command):
        """Run a shell command and wait for it to finish."""
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Command failed: {result.stderr}")

    def delete_existing_directories(self, path):
        """Delete directory and its contents if it exists."""
        if os.path.exists(path):
            shutil.rmtree(path)

    def reset_ui(self, success=True, error_message=""):
        if success:
            messagebox.showinfo("Success", "Celeris has been successfully installed!")
        else:
            messagebox.showerror("Error", f"Installation failed: {error_message}")

        # Reset UI elements
        self.progress["value"] = 0
        self.progress_label.config(text="")
        self.install_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    # Initialize Tkinter
    root = tk.Tk()

    # Create the installer app
    app = CelerisInstaller(root)

    # Run the GUI loop
    root.mainloop()
