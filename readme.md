# mp3cover.py

`mp3cover.py` appends cover image to mp3 file.

* Script removes multiple covers
* Script stores single cover
* Add empty ID3 tag if no tags
* Script overwrites mp3 file

Install `mutagen` module before using.

```bat
pip install -U mutagen
```

## Using

```bat
mp3cover.py music.mp3 cover.jpg
```
