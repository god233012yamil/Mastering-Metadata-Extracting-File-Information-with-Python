# Mastering Metadata: Extracting File Information with Python

Welcome to the "Mastering Metadata: Extracting File Information with Python" repository! This repository provides a comprehensive guide and sample codes for extracting metadata from various file types using Python.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Extracting Metadata](#extracting-metadata)
  - [File System Metadata](#file-system-metadata)
  - [Image Metadata](#image-metadata)
  - [PDF Metadata](#pdf-metadata)
  - [DOCX Metadata](#docx-metadata)
  - [Excel Metadata](#excel-metadata)
  - [Audio Metadata](#audio-metadata)
  - [Video Metadata](#video-metadata)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Metadata is essentially data about data, providing essential details about files without looking into their actual content. Extracting and utilizing metadata can enhance applications, from organizing large datasets to automating workflows. This repository aims to equip Python developers with the knowledge and tools to extract metadata from various file types.

## Getting Started

To get started with extracting metadata from different file types using Python, you will need to install some libraries. Below are the required libraries for each file type:

- **File System Metadata:** `os`, `pwd`, `grp`, `time` (Unix-like systems)
- **Image Metadata:** `Pillow`
- **PDF Metadata:** `PyPDF2`
- **DOCX Metadata:** `python-docx`, `python-docx-custom-properties`
- **Excel Metadata:** `openpyxl`
- **Audio Metadata:** `mutagen`
- **Video Metadata:** `ffmpeg-python`

You can install these libraries using pip:

```bash
pip install Pillow PyPDF2 python-docx python-docx-custom-properties openpyxl mutagen ffmpeg-python
```

## Extracting Metadata
### File System Metadata
Extract metadata from the file system including size, permissions, ownership, and timestamps.

![image](https://github.com/user-attachments/assets/9dfc1741-2503-43a1-a84c-5c505fd1e520)

### Image Metadata
Extract metadata from image files such as camera model, exposure settings, and GPS location.

![image](https://github.com/user-attachments/assets/43464607-b4ea-4bdf-8865-2f842fb3c985)

### PDF Metadata
Extract metadata from PDF files such as author, title, subject, and creation date.

![image](https://github.com/user-attachments/assets/e40433cc-53b8-4ed4-9ccb-194031b8845b)

### DOCX Metadata
Extract metadata from DOCX files including core properties, custom properties, and hyperlinks.

![image](https://github.com/user-attachments/assets/9b2ff173-2429-419c-90ae-56f4d05555b4)

### Excel Metadata
Extract metadata from Excel files including core properties, custom properties, and sheet information.

![image](https://github.com/user-attachments/assets/6ade2671-ef52-48dd-b4ca-7bc30b9b0e12)

### Audio Metadata
Extract metadata from audio files such as artist, album, genre, and more.

![image](https://github.com/user-attachments/assets/3cde2617-129d-44eb-92ae-a5207c497f9c)

### Video Metadata
Extract metadata from video files including codec, resolution, frame rate, and duration.

![image](https://github.com/user-attachments/assets/c0be7fef-d186-4875-b3fa-cef15a9328a8)

### Additional Resources
For more detailed information and further learning, refer to these resources:

[Introduction](#introduction)

* [Pillow Documentation](#https://pillow.readthedocs.io/en/stable/)
* [PyPDF2 Documentation](#https://pypdf2.readthedocs.io/en/latest/)
* [python-docx Documentation](#https://python-docx.readthedocs.io/en/latest/)
* [openpyxl Documentation](#https://openpyxl.readthedocs.io/en/stable/)
* [Mutagen Documentation](#https://mutagen.readthedocs.io/en/latest/)
* [ffmpeg-python Documentation](#https://github.com/kkroening/ffmpeg-python)

### Contributing
Contributions are welcome! If you have any improvements or additions to the code, feel free to submit a pull request. Please ensure your code follows the project's style guidelines and includes appropriate tests.



