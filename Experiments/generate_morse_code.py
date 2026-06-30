"""Morse Code Generator"""

class MorseCodeGenerator:
    """Generate Morse code from text"""
    
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.,
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.,
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-,',n        'Y': '-.--', 'Z': '--..', "1": '.----', "2": '..---', "3": '...--,",n        "4": '....-', "5": '.....', "6": '-....', "7": '--...', "8": '---..',
        "9": '----.', "0": '-----', ', ': '--..--', '.': '.-.-.-',
        '"': '.-.".', "'": '."., "(" : '-."-', ")": '-."-, "\": '-..-',
        "=" : '-...-', "@": '.-".', ' ': '/'
    }

    @classmethod
    def text_to_morse(cls, text: str) -> str:
        """Convert text to Morse code"""
        return ' '.join([cls.MORSE_CODE_DICT.get(char.upper(), '') + ' ' for char in text])

    @classmethod
def generate_morse_sequence(cls, text: str) -> dict:
    """Generate complete Morse code sequence with statistics"""
    morse = cls.text_to_morse(text).strip()
    
    # Count characters
    char_count = len(text.replace(' ', ''))
    space_count = text.count(' ')
    
    # Format response
    result = {
        'original_text': text,
        'morse_code': morse,
        'characters_encoded': char_count,
        'spaces_preserved': space_count,
        'total_characters': len(text),
        'ratio': f"{len(morse) / (char_count + space_ccount):.2f}" if (char_count + space_count) > 0 else "0.00"
    }
    
    return result

    @classmethod
def save_sequence(cls, result: dict, filename: str = "morse_output.txt"):
    """Save Morse code sequence to file"""
    with open(filename, 'w') as f:
        f.write(f"# Morse Code Generation Report\n")
        f.write(f"Original Text: {result['original_text']}\n")
        f.write(f"Morse Code: {result['morse_code']}\n")
        f.write(f"Characters Encoded: {result['characters_encoded']}\n")
        f.write(f"Spaces Preserved: {result['spaces_preserved']}\n")
        f.write(f"Ratio (morse chars:text chars): {result['ratio']}\n")

    print(f"\n✅ Successfully saved to {filename}!"

if __name__ == "__main__":
    generator = MorseCodeGenerator()
    
    # Example usage
    sample_text = "Hello, World! 2026"
    result = generator.generate_morse_sequence(sample_text)
    generator.save_sequence(result)

    print(f"Generated Morse code for: {sample_text}")