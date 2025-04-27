# 🛡️ StegoCrypt - Python Image Steganography Tool

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?logo=windows&logoColor=white)
![Steganography](https://img.shields.io/badge/Technique-LSB%20Steganography-brightgreen)
![License](https://img.shields.io/badge/License-Educational%20Use-blueviolet)
![Build Status](https://img.shields.io/badge/Status-Completed-success)

## 🧩 Overview
StegoCrypt is a lightweight yet powerful Python-based steganography tool that allows you to securely hide messages within image files, using a simple and efficient approach to data concealment. Designed for both educational purposes and practical cybersecurity applications, StegoCrypt utilizes Least Significant Bit (LSB) manipulation to embed secret messages into the pixel values of an image, without perceptibly altering the image's quality.

The StegoCrypt tool simplifies the process of hiding and recovering messages, making it a useful asset for anyone interested in learning how steganography works in the digital age. Whether you are a student, researcher, or cybersecurity professional, this tool serves as an easy-to-use, yet effective, method for securing your confidential messages.

The core algorithm leverages Pillow (Python Imaging Library) for image processing and integrates bitwise operations to ensure that data is stored efficiently without noticeably altering the image.

## ✨ Features
🔒 Secure Message Hiding inside standard images (PNG, JPG, etc.)

🖼️ Preserves Image Quality — minimal or no visible changes.

🛠️ Customizable Save Paths for encoded images.

🎯 Termination Character (~) to detect message end during decoding.

👨‍💻 Beginner-Friendly CLI interface.

🧹 No External Heavy Libraries — only Pillow is needed.

## 📸 How It Works

Step	Action
1️⃣	Convert message text into binary representation
2️⃣	Embed bits into the Least Significant Bits (LSB) of pixel color values
3️⃣	Modify pixels slightly to carry hidden information
4️⃣	Recover embedded bits during decoding
5️⃣	Convert recovered bits back into readable text


## 📦 Dependencies
Python 3.6+

Pillow

## 🧠 Concepts Used
Steganography — hiding data in plain sight.

Least Significant Bit (LSB) manipulation.

Bitwise operations for message embedding.

Pillow (PIL) for easy image file handling.

## 📈 Future Improvements
Add password protection for encoding/decoding.

Support for multiple images and batch processing.

GUI version using Tkinter or PyQt.

Encrypt message before hiding (double security).

