from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import sys


def print_using_and_exit():
    print("Add cover image to mp3 file")
    print("Using: mp3cover.py music.mp3 cover.jpg")
    sys.exit(1)


# check command line arguments mp3cover.py mp3 jpeg
if len(sys.argv) < 3:
    print_using_and_exit()

filename_mp3 = sys.argv[1]
filename_cover = sys.argv[2]

if not filename_mp3.upper().endswith(".MP3"):
    print("Invalid first argument (not a mp3 file)")
    print_using_and_exit()

if not filename_cover.upper().endswith(".JPG"):
    print("Invalid second argument (not a jpg file)")
    print_using_and_exit()

print(f"Reading file {filename_mp3}")
audio = MP3(filename_mp3, ID3=ID3)

print("ID3 tags details:")
print(audio.pprint())

print("Adding tags")

if audio.tags is None:
    print("File has no any tags. Adding empty...")
    audio.add_tags()
else:
    print("Updating tags...")

print("Erasing all covers...")
audio.tags.setall("APIC", [])

print(f"Adding a new cover from {filename_cover}")
audio.tags.add(
    APIC(
        encoding=1,
        mime='image/jpg',
        type=3,
        desc=u'Cover',
        data=open(filename_cover, "rb").read()
    )
)
audio.save()
