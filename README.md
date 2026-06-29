# PDF to Audio
Small Python project that allows the user to extract the text from a PDF file and listen to it using the user's computer speech engine.

# Objective of the project
The aim fo this project was to dive into PDF reading and text extracting. My objective was to learn more about those areas using Python and becoming familiar with said technologies.

This small project can also solve a problem I sometimes have: I need to read a long text but don't have the time. Using this small project I can convert the text into speech and listen to it while I do other things.

# Technologies used
- Python 3.11
- PyPDF2
- pyttsx3
- Tkinter

# How to run the project
1. Clone the repository
2. Create a virtual Python environment
    python3.11 -m venv .venv
    source .venv/bin/activate
3. Install dependencies in requirements.txt file
    pip install -r requirements.txt
4. Run the project
    python main.py

# Limitations
- This project cannot read text from images, even if they are in a PDF   format.
- It has not been tested with scanned PDFs so its performance on that regard is unknown.

# Key takeaways
The development of this project has allowed me to discover how to extract text from a PDF and convert it to audio while discovering there are libraries and methods in Python for those specific tasks.

I have also acquired more confidence when it comes to interpreting command-line exceptions and error messages since I was missing many packages I had to install so many errors were printed in the terminal.
After a few I was able to read them on my own and act upon them.

# Note
This project was developed following a tutorial. However some changes were added due to the original code not working properly and some methods being deprecated.
Here is the link to the tutorial followed: https://www.youtube.com/watch?v=Flm2YHEFd5A
