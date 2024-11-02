

# Cursor Movement Through Head and Click Through Eye Blink

This project enables hands-free computer control by using head movement to control cursor position and eye blinks for mouse clicks. It leverages computer vision and machine learning to detect and track facial features for accurate control.

## Features

- **Cursor Movement**: Control the cursor by moving your head.
- **Click Through Blink**: Perform clicks by blinking your eyes.
- **Hands-Free**: Designed for individuals needing alternative input methods, such as those with limited hand mobility.

## Requirements

- Python 3.7 or higher
- OpenCV
- Dlib
- Mediapipe (for facial landmark detection)
- PyAutoGUI (for simulating mouse clicks)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cursor-movement-through-head-and-click-through-eye-blink.git
   cd cursor-movement-through-head-and-click-through-eye-blink
   ```

2. **Create a Virtual Environment**:

   It’s recommended to create a virtual environment to manage dependencies for this project.

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   
   With the virtual environment activated, install the required packages using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: Ensure that you have a compatible version of `dlib` and `mediapipe` as they may require specific installation commands depending on your system.

5. **Download Required Model Files** (if needed):

   Some packages (like `dlib`) require pre-trained model files for facial landmark detection. You may need to download these manually if they aren't bundled with the package.

6. **Run the Application**:

   After all dependencies are installed, you can start the application:

   ```bash
   python main.py
   ```

## Usage

- Move your head in front of the camera to control the cursor.
- Blink your eyes to simulate a click.
- Customize sensitivity in the settings to adjust for different head movement ranges.

## Contributing

Feel free to fork this project and make improvements. If you’d like to contribute, submit a pull request, and please follow the code style used throughout the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

