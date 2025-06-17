#!/usr/bin/env python3
"""
Caesar Cipher Tool - Internship Project
======================================

A comprehensive implementation of the Caesar cipher encryption algorithm
with interactive CLI interface, file operations, and cryptanalysis features.

Author: Siddhant Mandal
Date: 17 June 2025
Project: Software Development Internship
"""

import os
import sys
from typing import Optional


class CaesarCipher:
    """
    A class to handle Caesar cipher encryption and decryption operations.
    
    The Caesar cipher is a substitution cipher that shifts each letter in the
    alphabet by a fixed number of positions.
    """
    
    def __init__(self):
        self.alphabet_size = 26
        self.min_shift = 1
        self.max_shift = 25
    
    def cipher(self, text: str, shift: int, decrypt: bool = False) -> str:
        """
        Encrypts or decrypts text using Caesar cipher algorithm.
        
        Args:
            text (str): The message to encrypt/decrypt
            shift (int): Number of positions to shift (1-25)
            decrypt (bool): If True, decrypts the message; if False, encrypts
        
        Returns:
            str: The encrypted/decrypted message
        
        Raises:
            ValueError: If shift value is not between 1 and 25
        """
        if not (self.min_shift <= shift <= self.max_shift):
            raise ValueError(f"Shift must be between {self.min_shift} and {self.max_shift}")
        
        if decrypt:
            shift = -shift
        
        result = ""
        
        for char in text:
            if char.isalpha():
                # Determine if uppercase or lowercase
                base = ord('A') if char.isupper() else ord('a')
                # Apply Caesar cipher formula with modular arithmetic
                shifted = (ord(char) - base + shift) % self.alphabet_size + base
                result += chr(shifted)
            else:
                # Keep non-alphabetic characters unchanged
                result += char
        
        return result
    
    def encrypt(self, text: str, shift: int) -> str:
        """Encrypt text with given shift value."""
        return self.cipher(text, shift, decrypt=False)
    
    def decrypt(self, text: str, shift: int) -> str:
        """Decrypt text with given shift value."""
        return self.cipher(text, shift, decrypt=True)
    
    def brute_force_decrypt(self, encrypted_text: str) -> dict:
        """
        Try all possible shift values to decrypt a message.
        Useful when the shift value is unknown.
        
        Args:
            encrypted_text (str): The encrypted message to decrypt
        
        Returns:
            dict: Dictionary with shift values as keys and decrypted text as values
        """
        results = {}
        for shift in range(self.min_shift, self.max_shift + 1):
            decrypted = self.decrypt(encrypted_text, shift)
            results[shift] = decrypted
        return results
    
    def encrypt_file(self, input_file: str, shift: int, output_file: Optional[str] = None) -> bool:
        """
        Encrypt the contents of a text file.
        
        Args:
            input_file (str): Path to input file
            shift (int): Shift value for encryption
            output_file (str, optional): Path to output file
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            encrypted_content = self.encrypt(content, shift)
            
            if output_file is None:
                name, ext = os.path.splitext(input_file)
                output_file = f"{name}_encrypted{ext}"
            
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(encrypted_content)
            
            return True
            
        except FileNotFoundError:
            print(f"❌ Error: File '{input_file}' not found.")
            return False
        except PermissionError:
            print(f"❌ Error: Permission denied accessing file.")
            return False
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
    
    def decrypt_file(self, input_file: str, shift: int, output_file: Optional[str] = None) -> bool:
        """
        Decrypt the contents of a text file.
        
        Args:
            input_file (str): Path to input file
            shift (int): Shift value for decryption
            output_file (str, optional): Path to output file
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            decrypted_content = self.decrypt(content, shift)
            
            if output_file is None:
                name, ext = os.path.splitext(input_file)
                output_file = f"{name}_decrypted{ext}"
            
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(decrypted_content)
            
            return True
            
        except FileNotFoundError:
            print(f"❌ Error: File '{input_file}' not found.")
            return False
        except PermissionError:
            print(f"❌ Error: Permission denied accessing file.")
            return False
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False


class CaesarCipherCLI:
    """
    Command-line interface for the Caesar Cipher tool.
    Provides interactive menu and user input handling.
    """
    
    def __init__(self):
        self.cipher = CaesarCipher()
        self.running = True
    
    def print_header(self):
        """Print the application header."""
        print("\n" + "="*60)
        print("🔐 CAESAR CIPHER TOOL - INTERNSHIP PROJECT 🔐")
        print("="*60)
        print("Developed as part of software development internship")
        print("Demonstrating algorithm implementation and UI design")
        print("="*60)
    
    def print_menu(self):
        """Print the main menu options."""
        print("\n📋 MAIN MENU:")
        print("1. 🔒 Encrypt a message")
        print("2. 🔓 Decrypt a message")
        print("3. 🔍 Brute force decrypt (try all shifts)")
        print("4. 📁 Encrypt a file")
        print("5. 📂 Decrypt a file")
        print("6. 📚 View examples")
        print("7. ❓ Help & Information")
        print("8. 🚪 Exit")
    
    def get_valid_shift(self, prompt: str = "Enter shift value (1-25): ") -> int:
        """Get a valid shift value from user input."""
        while True:
            try:
                shift = int(input(prompt))
                if self.cipher.min_shift <= shift <= self.cipher.max_shift:
                    return shift
                else:
                    print(f"❌ Please enter a number between {self.cipher.min_shift} and {self.cipher.max_shift}.")
            except ValueError:
                print("❌ Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
    
    def get_user_input(self, prompt: str) -> str:
        """Get user input with keyboard interrupt handling."""
        try:
            return input(prompt).strip()
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
    
    def encrypt_message(self):
        """Handle message encryption."""
        print("\n" + "="*40)
        print("🔒 ENCRYPT MESSAGE")
        print("="*40)
        
        message = self.get_user_input("Enter message to encrypt: ")
        if not message:
            print("❌ Message cannot be empty.")
            return
        
        shift = self.get_valid_shift()
        
        try:
            encrypted = self.cipher.encrypt(message, shift)
            print(f"\n✅ Encryption successful!")
            print(f"📝 Original:  '{message}'")
            print(f"🔒 Encrypted: '{encrypted}'")
            print(f"🔑 Shift used: {shift}")
            print(f"💡 Tip: Use shift value {shift} to decrypt this message")
        except Exception as e:
            print(f"❌ Encryption failed: {str(e)}")
    
    def decrypt_message(self):
        """Handle message decryption."""
        print("\n" + "="*40)
        print("🔓 DECRYPT MESSAGE")
        print("="*40)
        
        message = self.get_user_input("Enter message to decrypt: ")
        if not message:
            print("❌ Message cannot be empty.")
            return
        
        shift = self.get_valid_shift()
        
        try:
            decrypted = self.cipher.decrypt(message, shift)
            print(f"\n✅ Decryption successful!")
            print(f"🔒 Encrypted: '{message}'")
            print(f"📝 Decrypted: '{decrypted}'")
            print(f"🔑 Shift used: {shift}")
        except Exception as e:
            print(f"❌ Decryption failed: {str(e)}")
    
    def brute_force_decrypt(self):
        """Handle brute force decryption."""
        print("\n" + "="*40)
        print("🔍 BRUTE FORCE DECRYPT")
        print("="*40)
        print("This will try all possible shift values (1-25)")
        
        message = self.get_user_input("Enter encrypted message: ")
        if not message:
            print("❌ Message cannot be empty.")
            return
        
        print(f"\n🔍 Trying all shifts for: '{message}'")
        print("-" * 60)
        
        results = self.cipher.brute_force_decrypt(message)
        
        for shift, decrypted in results.items():
            print(f"Shift {shift:2d}: {decrypted}")
        
        print("\n💡 Look for the result that makes the most sense!")
    
    def encrypt_file_menu(self):
        """Handle file encryption."""
        print("\n" + "="*40)
        print("📁 ENCRYPT FILE")
        print("="*40)
        
        input_file = self.get_user_input("Enter input file path: ")
        if not input_file:
            print("❌ File path cannot be empty.")
            return
        
        shift = self.get_valid_shift()
        
        output_file = self.get_user_input("Enter output file path (or press Enter for auto-naming): ")
        if not output_file:
            output_file = None
        
        print(f"\n🔄 Encrypting file...")
        success = self.cipher.encrypt_file(input_file, shift, output_file)
        
        if success:
            final_output = output_file if output_file else f"{os.path.splitext(input_file)[0]}_encrypted{os.path.splitext(input_file)[1]}"
            print(f"✅ File encrypted successfully!")
            print(f"📁 Output saved to: {final_output}")
            print(f"🔑 Shift used: {shift}")
    
    def decrypt_file_menu(self):
        """Handle file decryption."""
        print("\n" + "="*40)
        print("📂 DECRYPT FILE")
        print("="*40)
        
        input_file = self.get_user_input("Enter input file path: ")
        if not input_file:
            print("❌ File path cannot be empty.")
            return
        
        shift = self.get_valid_shift()
        
        output_file = self.get_user_input("Enter output file path (or press Enter for auto-naming): ")
        if not output_file:
            output_file = None
        
        print(f"\n🔄 Decrypting file...")
        success = self.cipher.decrypt_file(input_file, shift, output_file)
        
        if success:
            final_output = output_file if output_file else f"{os.path.splitext(input_file)[0]}_decrypted{os.path.splitext(input_file)[1]}"
            print(f"✅ File decrypted successfully!")
            print(f"📁 Output saved to: {final_output}")
            print(f"🔑 Shift used: {shift}")
    
    def show_examples(self):
        """Display examples of Caesar cipher usage."""
        print("\n" + "="*50)
        print("📚 CAESAR CIPHER EXAMPLES")
        print("="*50)
        
        examples = [
            ("Hello World!", 3),
            ("Python Programming", 13),
            ("Attack at dawn!", 5),
            ("INTERNSHIP PROJECT", 7),
            ("Cryptography is fun!", 12)
        ]
        
        for i, (message, shift) in enumerate(examples, 1):
            encrypted = self.cipher.encrypt(message, shift)
            decrypted = self.cipher.decrypt(encrypted, shift)
            
            print(f"\nExample {i}:")
            print(f"  Original:  '{message}'")
            print(f"  Shift:     {shift}")
            print(f"  Encrypted: '{encrypted}'")
            print(f"  Decrypted: '{decrypted}'")
        
        print(f"\n💡 Notice how:")
        print(f"   • Case is preserved (A→D, a→d)")
        print(f"   • Punctuation stays the same")
        print(f"   • Numbers and spaces are unchanged")
        print(f"   • Alphabet wraps around (Z→C with shift 3)")
    
    def show_help(self):
        """Display help information."""
        print("\n" + "="*50)
        print("❓ HELP & INFORMATION")
        print("="*50)
        
        print("\n🔐 What is Caesar Cipher?")
        print("The Caesar cipher is one of the simplest encryption techniques.")
        print("It shifts each letter in the alphabet by a fixed number of positions.")
        
        print("\n📝 How it works:")
        print("• Choose a shift value (1-25)")
        print("• Each letter moves that many positions in the alphabet")
        print("• A with shift 3 becomes D, B becomes E, etc.")
        print("• When you reach Z, it wraps around to A")
        
        print("\n🔑 Example with shift 3:")
        print("  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
        print("  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")
        print("  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C")
        
        print("\n🛡️ Security Note:")
        print("Caesar cipher is not secure for real-world use!")
        print("It's easily broken with frequency analysis or brute force.")
        print("This tool is for educational purposes and learning cryptography basics.")
        
        print("\n🎯 Internship Project Goals:")
        print("• Demonstrate algorithm implementation skills")
        print("• Show clean code practices and documentation")
        print("• Practice user interface design")
        print("• Learn file handling and error management")
        
        print("\n📋 Features implemented:")
        print("• Interactive command-line interface")
        print("• Input validation and error handling")
        print("• File encryption/decryption capabilities")
        print("• Brute force cryptanalysis")
        print("• Comprehensive documentation")
        print("• Object-oriented design patterns")
    
    def run(self):
        """Main application loop."""
        self.print_header()
        
        while self.running:
            self.print_menu()
            
            choice = self.get_user_input("\nEnter your choice (1-8): ")
            
            if choice == '1':
                self.encrypt_message()
            elif choice == '2':
                self.decrypt_message()
            elif choice == '3':
                self.brute_force_decrypt()
            elif choice == '4':
                self.encrypt_file_menu()
            elif choice == '5':
                self.decrypt_file_menu()
            elif choice == '6':
                self.show_examples()
            elif choice == '7':
                self.show_help()
            elif choice == '8':
                print("\n" + "="*40)
                print("👋 Thank you for using Caesar Cipher Tool!")
                print("💼 Internship project completed successfully")
                print("🎓 Great job learning cryptography basics!")
                print("="*40)
                self.running = False
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 8.")
            
            if self.running and choice in ['1', '2', '3', '4', '5', '6', '7']:
                continue_choice = self.get_user_input("\nPress Enter to continue or 'q' to quit: ")
                if continue_choice.lower() == 'q':
                    print("\n👋 Goodbye!")
                    self.running = False


def main():
    """Main function to run the Caesar Cipher CLI application."""
    try:
        app = CaesarCipherCLI()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}")
        sys.exit(1)


# Direct usage examples for testing
def run_examples():
    """Run some examples for testing purposes."""
    cipher = CaesarCipher()
    
    print("🧪 TESTING CAESAR CIPHER FUNCTIONS")
    print("="*40)
    
    # Test basic encryption/decryption
    message = "Hello, World!"
    shift = 3
    encrypted = cipher.encrypt(message, shift)
    decrypted = cipher.decrypt(encrypted, shift)
    
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Match: {message == decrypted}")
    
    # Test brute force
    print(f"\nBrute force results for '{encrypted}':")
    results = cipher.brute_force_decrypt(encrypted)
    for s, text in list(results.items())[:5]:  # Show first 5
        print(f"  Shift {s}: {text}")


if __name__ == "__main__":
    # Uncomment the line below to run examples instead of the full CLI
    # run_examples()
    
    # Run the main CLI application
    main()
