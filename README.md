# Celeris Installer

## Overview

The **Celeris Installer** is a user-friendly graphical interface application designed for easy installation of the Celeris framework on Linux systems. With this installer, users can quickly download, install, and set up the necessary files to start using the Celeris framework without the hassle of complex configurations.

## Features

- Simple and intuitive GUI for a seamless installation experience.
- Downloads the latest version of the Celeris framework directly from the GitHub repository.
- Automatically handles the extraction of files and installation of header and library files.
- Progress bar to monitor the download and installation process.
- Prompts for permission before deleting existing files to prevent accidental data loss.
- Error handling and user notifications to inform about the installation status.

## Requirements

- Python 3.x
- Required libraries:
  - `ttkbootstrap`
  - `requests`
  

## Installation

1. **Clone or Download the Repository:**

   You can clone this repository using Git:

   ```bash
   git clone https://github.com/Alazar42/GUI_Installer_Celeris.git
   ```

   Or download the ZIP file from the repository and extract it.

2. **Navigate to the Project Directory:**

   ```bash
   cd GUI_Installer_Celeris
   ```
And You can install the required libraries using pip:

  ```bash
  pip install -r requirements.txt
  ```
  
3. **Run the Installer:**

   Use the following command to run the installer:

   ```bash
   python3 main.py
   ```

   Make sure to run it in an environment where you have permissions to install the Celeris framework.

## Usage

1. Launch the Celeris Installer.
2. Click the "Download and Install Celeris" button to start the installation process.
3. Monitor the progress bar as the installer downloads and sets up the framework.
4. Upon completion, you'll receive a notification about the installation status.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgements

- [Celeris Backend Framework](https://github.com/Alazar42/Celeris) for providing a powerful backend API framework.
- Libraries used for GUI and networking.
