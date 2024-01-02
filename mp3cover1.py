from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import sys

filename_mp3 = sys.argv[1]

print(f"Reading file {filename_mp3}")
audio = MP3(filename_mp3, ID3=ID3)

print("ID3 tags details:")
print(audio.pprint())
