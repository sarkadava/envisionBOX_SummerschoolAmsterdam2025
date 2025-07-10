# Introduction

In this course, we will try to balance the conceptual with the technical. This means we will have time for discussion, have some old-school type lecture sessions, but then we will also be running python code for the technical part.

The technical session is always difficult to get all people installed in the right way. We therefore ask you to prepare beforehand the below installation procedure before the first day of the course (if you dont manage, dont worry too much, you can catch up later). Below are the installation details that we would like you to follow. We also made a video with you for a window installation example, where we go through the whole routine.

Of course, you will sometimes get stuck somewhere, and after some googling you still might not have figured it out. Perhaps your machine is set in a particular way with little user rights. That's ok, then you troubleshoot with us, or you work with your neighbor.

## Day-to-day structure

Each daily session (2 hours) follows this template:
* Opening discussion & error checks (5-15 min)
* Core concept introduction (30-60 min)
* Hands-on practice (30-45 min)
* Group work & discussion (30 min)

## What are our technical steps that we will go through

1. We learn to automatically classify gestures from video
2. We learn to mask and track videos
3. We become familiar with data wrangling to calculate gesture-speech coupling
4. We become conceptually familiar with creating gesture similarity analyses

On the last day, we brainstorm what we can do on a large scale with what we have learned.

## Installation Procedure

We work with the following repository for this LOT Winterschool. This has all the materials you need for this winter school:
https://github.com/WimPouw/WinterLOTschool_MultimodalComputational

Clone URL: https://github.com/WimPouw/WinterLOTschool_MultimodalComputational.git

### Step 1: GitHub Setup
Sign up at GitHub (https://github.com) and save your username and password (you need it later to log in)

### Step 2: Installing Anaconda for Python
- Windows: Follow this tutorial to install Anaconda here: https://www.anaconda.com/download
  > ⚠️ Important: After installation, you'll have a new terminal program called 'Anaconda Prompt' - use this for the conda commands below

- macOS/Linux: Follow the installation instructions here: https://www.anaconda.com/download
  > ⚠️ Important: After installation, the regular terminal will recognize conda commands

### Step 3: Visual Studio Code
Install from: https://code.visualstudio.com/download
Also check out Accessibility settings to increase readability when color blind: [link](
Also https://code.visualstudio.com/docs/editor/accessibility#:~:text=Color%20vision%20accessibility,-You%20can%20search&text=Use%20the%20Extensions%20view%20Ctrl,Ctrl%2BK%20Ctrl%2BT)

### Step 4: GitHub Desktop
Download and install from: https://desktop.github.com/download/

### Step 5: Cloning the Repository
1. Open GitHub Desktop
2. Sign in with your GitHub credentials
3. Click "Add" → "Clone repository" 
4. Enter URL: https://github.com/WimPouw/WinterLOTschool_MultimodalComputational.git
5. Choose where to save the repository on your computer

### Step 6: Install ELAN (if you want to look at gesture detection output)
Download link: https://archive.mpi.nl/tla/elan/download

### Step 7: Python Dependencies
Open Anaconda Prompt (Windows) or Terminal (macOS/Linux):

```bash
# Navigate to repository folder
cd [your_folder_structure/WinterLOTschool_MultimodalComputational]
 > ⚠️ If your changing drive to a different partition (e.g., d:) then first enter in "d:" and then cd to your location d:/your_folder_structure/WinterLOTschool_MultimodalComputational

# Create conda environment
conda create -n envision python=3.9

# Activate environment
conda activate envision

# Install pip
conda install pip

# Install dependencies
pip install -r requirements.txt
```
## Alternative Installation for macOS Users

If you encounter a tensorflow-cpu installation error on macOS, follow these alternative steps:

### Step 6 (Alternative): Python Dependencies for macOS
Open Terminal and run:

```bash
# Navigate to repository folder
cd [your_folder_structure/WinterLOTschool_MultimodalComputational]

# Create conda environment
conda create -n envision python=3.9

# Activate environment
conda activate envision

# Install pip
conda install pip

# Install tensorflow-cpu first (without version constraints)
pip install tensorflow

# Install envisionhgdetector without dependencies
pip install envisionhgdetector==0.0.4.8 --no-deps

# Install remaining dependencies
pip install -r requirementsbackupOS.txt
```

### Final Setup: Opening Your First Notebook

1. Open Visual Studio Code
2. Open the notebook: UsingEnvisionHGdetector_package.ipynb in /UsingEnvisionHGdetector_package/
3. Set Python Environment:
   - Click kernel selector in top-right corner
   - Select "Python Environments"
   - Choose "envision"
   > ⚠️ If you don't see "envision", ensure you followed Step 6 correctly

## Common Issues
- If conda commands aren't recognized: Restart your terminal/Anaconda Prompt
- If pip install fails: Make sure you're in the right folder with requirements.txt
- If kernel doesn't show up: Ensure you activated the envision environment

### Installing FFmpeg
FFmpeg is required and needs to be installed at the system level (separate from your conda environment):

Windows and mac users:
1. In Anaconda Prompt (with envision environment activated):
   ```bash
   conda install -c conda-forge ffmpeg
   ```
Alternative manual method for Windows:
- Download from https://www.gyan.dev/ffmpeg/builds/ (get "ffmpeg-release-essentials.zip")
- Extract the zip file
- Add the bin folder to your System PATH

## Collab links
Day 1: https://colab.research.google.com/drive/12aC6Qd40jCHIramJE3VmQXEspJZDAvt7?usp=sharing

# OTHER MATERIALS
## Assignments
* Course Manual: https://github.com/WimPouw/WinterLOTschool_MultimodalComputational/blob/main/OtherMaterials/PouwOwoyele_LOT_course%20description_RM1course.pdf

## Drive folder for videos and setup
https://drive.google.com/drive/folders/1IevjiF2K49u9BjEixiTl7fOIhmoVevhW

## Slides
* Day 1 (intro): https://github.com/WimPouw/WinterLOTschool_MultimodalComputational/blob/main/OtherMaterials/day1_lot_coreplan.pdf
* Day 1 (technical): https://docs.google.com/presentation/d/1_MDUQq3kUk6UdzcilmhjHcGwl7yd6l8a/edit?usp=drive_link&ouid=117988542648841827008&rtpof=true&sd=true
* Day 2 (intro & technical): https://docs.google.com/presentation/d/1rba1dqR6tdsmi45X2fvxUxXbavuhXQNgc9fNR-akh_U/edit#slide=id.g32561259a70_0_1135
* Day 2 (conceptual: https://github.com/WimPouw/WinterLOTschool_MultimodalComputational/blob/main/OtherMaterials/day2_lot_conceptual.pdf
* Day 3 (intro & technical): https://docs.google.com/presentation/d/1aGlpodfO5QZthprS-iWt7gDAdV8MUUIz/edit?usp=drive_link&ouid=117988542648841827008&rtpof=true&sd=true
* Day 4 (intro & technical):  https://docs.google.com/presentation/d/1DzevNy8-rI2xUI5djLRCBwJ7bHju3p2B/edit?usp=drive_link&ouid=117988542648841827008&rtpof=true&sd=true
* Day 5: https://drive.google.com/file/d/1kreaDBXNUdP95AZdQCw0AHCAeEqyy0f0/view