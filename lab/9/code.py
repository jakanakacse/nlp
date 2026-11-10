from gtts import gTTS

text = "Jatiya Kabi Kazi Nazrul Islam University (JKKNIU) is a premier public university in Trishal, Mymensingh, established in 2006."
output_file = "output.mp3"

print("Input Text:")
print(text)

try:
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"\nText successfully converted to audio and saved to: {output_file}")
except Exception as e:
    print(f"\nTTS conversion note (requires internet for gTTS): {e}")

