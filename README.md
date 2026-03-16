# 🚗 AI-Based Smart Parking Automation System

## 📖 Overview

The **AI-Based Smart Parking Automation System** is a computer vision-based solution designed to detect and monitor parking space availability automatically.  
It analyzes parking lot video footage in real time and identifies whether parking spaces are **occupied or free**.

This system reduces the need for manual monitoring and helps improve **parking efficiency, traffic flow, and user convenience**.

---

# ✨ Features

- Real-time parking space detection from video feed
- Interactive parking space marking tool
- Color-coded visualization of parking spaces  
  - 🟢 **Green** → Available space  
  - 🔴 **Red** → Occupied space
- Displays **total available parking spots**
- Supports **multiple parking space configurations**
- Lightweight and efficient **image processing pipeline**

---

# 🛠️ Tech Stack

- **Python**
- **OpenCV** – Image processing and computer vision
- **NumPy** – Numerical computations
- **CVZone** – Computer vision utilities

---

# 📦 Dependencies

The project requires the following Python libraries:

```
opencv-python
numpy
cvzone
```

---

# ⚙️ Installation Strategy

## Prerequisites

- Python **3.7 or higher**
- **pip** (Python package installer)

---

## Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd AI-Based-Smart-Parking-Automation-System-main/Model
```

---

## Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv parking_env
```

### Activate the Environment

**Windows**

```bash
parking_env\Scripts\activate
```

**Mac / Linux**

```bash
source parking_env/bin/activate
```

---

## Step 3: Install Required Packages

```bash
pip install opencv-python numpy cvzone
```

### Alternatively Using `requirements.txt`

Create a `requirements.txt` file:

```
opencv-python==4.8.1.78
numpy==1.24.3
cvzone==1.6.1
```

Then install:

```bash
pip install -r requirements.txt
```

---

## Step 4: Verify Installation

```bash
python -c "import cv2, numpy, cvzone; print('All dependencies installed successfully')"
```

---

# 📂 Project Structure

```
Model/
│
├── main.py          # Main application for real-time parking detection
├── space.py         # Tool for marking parking spaces (fixed size)
├── test.py          # Alternative tool for marking parking spaces (dynamic size)
├── Positions        # Pickle file storing parking space positions
├── tp               # Alternative pickle file storing parking space positions
├── carPark.mp4      # Sample parking video
├── img.png          # Reference image for marking parking spaces
└── README.md        # Project documentation
```

---

# 🚀 Usage Guide

## Step 1: Mark Parking Spaces

Before running the detection system, you need to define the parking spaces in the area.

---

### Option A: Using `space.py` (Fixed Size Spaces)

Run:

```bash
python space.py
```

Instructions:

- **Left-click** → Add a parking space (107x48 pixels)
- **Left-click on existing rectangle** → Remove it
- Close the window when done

Parking spaces are automatically saved to the **Positions** file.

---

### Option B: Using `test.py` (Dynamic Size Spaces)

Run:

```bash
python test.py
```

Instructions:

- **Left-click and drag** → Draw parking space rectangle
- **Right-click** → Delete a rectangle
- Close the window when finished

Parking spaces are automatically saved to the **tp** file.

---

# ▶️ Step 2: Run Parking Detection

After defining parking spaces:

```bash
python main.py
```

A video window will open showing parking analysis.

---

## Visual Indicators

- 🟢 **Green Rectangle** → Free parking space
- 🔴 **Red Rectangle** → Occupied parking space

The system also displays:

```
Total Available Spots: X / Y
```

---

# 🧠 Detection Process

Each video frame goes through several image processing steps:

### 1️⃣ Frame Capture

Frames are captured from the video file:

```
carPark.mp4
```

---

### 2️⃣ Grayscale Conversion

The image is converted to grayscale to simplify processing.

---

### 3️⃣ Gaussian Blur

Noise is reduced using Gaussian smoothing.

---

### 4️⃣ Adaptive Thresholding

Separates foreground objects from the background.

---

### 5️⃣ Median Blur

Further removes noise from the binary image.

---

### 6️⃣ Dilation

Expands white regions to fill gaps.

---

### 7️⃣ Parking Space Analysis

For each parking space:

- Crop the processed image
- Count **non-zero (white) pixels**
- Apply the detection rule

```
Pixel Count < 900  → Space is FREE
Pixel Count ≥ 900 → Space is OCCUPIED
```

---

### 8️⃣ Visualization

Detection results are drawn on the original frame with colored rectangles and statistics.

---

# ⚙️ Configuration

## Parking Space Dimensions

Defined in `main.py` and `space.py`

```
107 x 48 pixels
```

---

## Detection Threshold

Defined in `main.py`

```
threshold = 900
```

You may adjust this value depending on lighting conditions.

---

## Video Source

Currently the system uses:

```
carPark.mp4
```

To use a **live webcam**, change:

```python
cap = cv2.VideoCapture(0)
```

---

# 🛠️ Troubleshooting

### Video Window Not Opening

Ensure **OpenCV is correctly installed** and video codecs are supported.

---

### Parking Positions Not Loading

Verify that the **Positions** or **tp** files exist and are not corrupted.

---

### Poor Detection Accuracy

Try:

- Adjusting the **threshold value**
- Improving lighting conditions
- Re-marking parking spaces

---

### Import Errors

Make sure all dependencies are installed inside the active Python environment.

---

# 🔮 Future Enhancements

- Machine learning-based vehicle detection
- Multi-camera parking monitoring
- Web dashboard for remote monitoring
- Integration with smart parking management systems
- Mobile application for user notifications
- Real-time parking reservation

---

# 👨‍💻 Contributors

- Abhiraj  
- Anshika
- Prashant  
- Utkarsh  

---

# 📜 License
This project is licensed under the **MIT License**.
