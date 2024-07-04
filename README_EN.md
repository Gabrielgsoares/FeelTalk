
# FeelTalk Project

[Click here](README_PT.md) for the Portuguese version of this README.

## Introduction

FeelTalk was created to assist individuals with physical limitations and speech disabilities. This project aims to enable effective communication with friends, family, and colleagues, combating social isolation and promoting interaction.

## Project Code Overview

### Main Components
- **main.py**: The main entry point of the application.
- **guiHome.py**: Manages the home screen interface.
- **guiExpressions.py**: Handles the interface for selecting and displaying expressions.
- **tracking.py**: Contains functionalities related to tracking and interpreting user inputs.

### Libraries Used
- **tkinter**: For creating the graphical user interface.
- **opencv-python**: Used for image processing and tracking functionalities.
- **numpy**: For numerical operations required in image processing.
- **pillow**: For handling image files within the application.

### File Structure
```
ProjetoFeelTalk/
├── src/
│   ├── projeto_FeelTalk/
│   │   ├── assets/
│   │   │   ├── frame0/
│   │   │   ├── frame1/
│   │   │   ├── frame2/
│   │   ├── guiExpressions.py
│   │   ├── guiHome.py
│   │   ├── main.py
│   │   ├── tracking.py
|   |   ├── run_both.py
├── README_PT.md
├── README_EN.md
└── requirements.txt
```

## How to Run

To execute the code, follow these steps:

1. Ensure you have Python installed on your machine.
2. Install the required libraries using the command:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script to start the application:
   ```bash
   python src/projeto_FeelTalk/run_both.py
   ```

---
