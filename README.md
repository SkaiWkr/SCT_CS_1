# SCT_CS_1
🔐 Caesar Cipher Tool
A comprehensive Python implementation of the Caesar cipher encryption algorithm with an interactive command-line interface and advanced features.

✨ Features
🔒 Encrypt and Decrypt: Transform messages using customizable shift values (1-25)
🎯 Smart Text Handling: Preserves case sensitivity and keeps punctuation intact
🔍 Brute Force Decryption: Automatically try all possible shifts when the key is unknown
📁 File Operations: Encrypt entire text files with ease
🎮 Interactive Interface: User-friendly menu system with input validation
📚 Educational: Includes demonstrations and examples for learning purposes

🚀 Quick Start
[in bash]
# Clone the repository
git clone https://github.com/yourusername/caesar-cipher-tool.git
cd caesar-cipher-tool

# Run the program
python caesar_cipher.py

💡 Usage Examples
[in python]
# Basic encryption/decryption
encrypted = caesar_cipher("Hello World!", 3)  # → "Khoor Zruog!"
decrypted = caesar_cipher("Khoor Zruog!", 3, decrypt=True)  # → "Hello World!"

# Brute force attack (when shift is unknown)
brute_force_decrypt("Khoor Zruog!")  # Shows all 25 possible decryptions

# File encryption
encrypt_file("secret.txt", 7, "encrypted_secret.txt")

🎯 Use Cases
Educational: Learn cryptography fundamentals and algorithm implementation
Security Testing: Practice basic cryptanalysis with brute force attacks
Text Processing: Simple encryption for personal notes and messages
Programming Practice: Clean, well-documented code for learning Python

🛠️ Technical Details
Language: Python 3.x
Dependencies: None (uses only standard library)
Algorithm: Classic Caesar cipher with modular arithmetic
Input: Supports all ASCII text with proper case and punctuation handling

📖 How It Works
The Caesar cipher shifts each letter in the alphabet by a fixed number of positions. For example:

With shift 3: A → D, B → E, C → F
The algorithm wraps around: X → A, Y → B, Z → C

🤝 Contributing
Contributions are welcome! Feel free to:

Report bugs or suggest features; 
Improve documentation; 
Add new cipher algorithms; 
Enhance the user interface.

📚 Internship Project
This project was developed as part of my software development internship to demonstrate:

Algorithm implementation and cryptography fundamentals
Clean code practices with comprehensive documentation
Interactive user interface design and input validation
Problem-solving approach to text processing and security
File handling and advanced feature development

📝 License
This project is open source and available under the MIT License.

🔗 Connect
If you found this project helpful, please ⭐ star the repository and share it with others interested in cryptography and Python programming!

Built with ❤️ as part of my software development internship journey
