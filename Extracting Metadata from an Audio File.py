from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC

def get_audio_metadata(audio_path):
    if audio_path.endswith('.mp3'):
        audio = MP3(audio_path, ID3=EasyID3)
    elif audio_path.endswith('.mp4') or audio_path.endswith('.m4a'):
        audio = MP4(audio_path)
    elif audio_path.endswith('.flac'):
        audio = FLAC(audio_path)
    else:
        raise ValueError("Unsupported file format")

    print("Audio Metadata:")
    for tag, value in audio.items():
        print(f"{tag}: {value}")

    print("\nAdditional Metadata:")
    if isinstance(audio, MP3):
        print(f"Bitrate: {audio.info.bitrate} bps")
        print(f"Length: {audio.info.length} seconds")
        print(f"Sample Rate: {audio.info.sample_rate} Hz")
    elif isinstance(audio, MP4):
        print(f"Length: {audio.info.length} seconds")
        print(f"Sample Rate: {audio.info.sample_rate} Hz")
        print(f"Channels: {audio.info.channels}")
    elif isinstance(audio, FLAC):
        print(f"Sample Rate: {audio.info.sample_rate} Hz")
        print(f"Channels: {audio.info.channels}")
        print(f"Bits per Sample: {audio.info.bits_per_sample}")

# Example usage
audio_path = 'example.mp3'
get_audio_metadata(audio_path)
