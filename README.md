# 🎨 Gesture Drawing

A real-time **hand gesture based drawing application** built using Python, OpenCV and MediaPipe.

The project allows users to draw on a virtual canvas using hand movements captured through a webcam. Different gestures can be used for drawing, erasing, clearing the canvas and selecting colors.

## ✨ Features

- 🖐️ Real-time hand tracking using MediaPipe
- ✏️ Draw on a virtual canvas using hand gestures
- 🧹 Erase parts of the drawing
- 🎨 Select different drawing colors
- 🗑️ Clear the complete canvas
- ↩️ Undo previous actions
- 💾 Save the drawing as an image
- 📷 Uses webcam for real-time interaction

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

## 📁 Project Structure

```text
Gesture-Drawing/
│
├── app.py
│
├── vision/
│   └── hand_detector.py
│
├── logic/
│   └── gesture_control.py
│
├── core/
│   └── draw_engine.py
│
├── requirements.txt
├── .gitignore
└── README.md
🎮 Controls
Action	Control
Draw	Hand gesture
Erase	Hand gesture
Clear Canvas	Hand gesture
Select Color	Hand gesture
Undo	U key
Save Drawing	S key
Exit	ESC key
🚀 Installation
1. Clone the repository
git clone https://github.com/sainaalam2007/Gesture-Drawing-.git
2. Navigate to the project
cd Gesture-Drawing-
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
📦 Requirements

Make sure Python is installed on your system.

The project uses:

OpenCV
MediaPipe
NumPy

See requirements.txt for the required package versions.

🖥️ Usage
Connect your webcam.
Run app.py.
Show your hand in front of the camera.
Use the supported gestures to interact with the canvas.
Press S to save your drawing.
Press U to undo.
Press ESC to exit.
🔮 Future Improvements
Add more gesture controls
Add more colors and brush sizes
Add shape drawing
Add text writing using gestures
Improve gesture recognition accuracy
Add a better UI and toolbar
Add multiple canvas/background options
👩‍💻 Author

Saina Alam

CSE × AI/ML Student

GitHub: @sainaalam2007

⭐ If you find this project interesting, feel free to explore the repository!


### Ek important thing 👀

README mein jo `requirements.txt` hai, **woh bhi bana dena**. Tumhare current working environment ke according usme ye daal sakti ho:

```txt
mediapipe==0.10.21
tensorflow==2.17.1
numpy==1.26.4
protobuf==4.25.9
opencv-python==4.11.0.86

Then:

git add .
git commit -m "Add README and project documentation"
git push
