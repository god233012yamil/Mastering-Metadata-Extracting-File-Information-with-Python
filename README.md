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




