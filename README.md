# 3D STL Model Viewer

This is a simple desktop application for viewing 3D models from `.stl` files. The application is built using Python, with PySide6 for the graphical user interface and VTK for 3D rendering.

## Features

*   **File Upload:** Allows users to upload one or more `.stl` files through a file dialog.
*   **File List:** Displays the paths of the selected files.
*   **3D Visualization:** Opens a separate window for each selected file to visualize the 3D model.
*   **VTK Integration:** Uses the Visualization Toolkit (VTK) to render the 3D models, allowing for interaction with the model (rotating, panning, zooming).

## Dependencies

The application requires the following Python libraries:

*   `PySide6`: For the graphical user interface.
*   `VTK`: For 3D rendering and visualization.

All required dependencies are listed in the `requirements.txt` file.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/3D-desktop-app.git
    cd 3D-desktop-app
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app/app.py
    ```

## Project Structure

*   `app/app.py`: The main entry point of the application.
*   `app/core/main_window.py`: Defines the main window of the application, including the file upload and view buttons.
*   `app/core/stl_viewer.py`: Implements the 3D viewer widget using VTK.
*   `requirements.txt`: A list of all the Python dependencies for the project.
