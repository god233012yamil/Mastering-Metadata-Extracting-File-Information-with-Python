import ffmpeg

def get_video_metadata(video_path):
    probe = ffmpeg.probe(video_path)

    # Extracting format metadata
    format_info = probe['format']
    print("Format Metadata:")
    print(f"Filename: {format_info['filename']}")
    print(f"Format: {format_info['format_long_name']}")
    print(f"Duration: {format_info['duration']} seconds")
    print(f"Size: {format_info['size']} bytes")
    print(f"Bit rate: {format_info['bit_rate']} bps")

    # Extracting video stream metadata
    video_stream = next((stream for stream in probe['streams'] \
                         if stream['codec_type'] == 'video'), None)
    if video_stream:
        print("\nVideo Stream Metadata:")
        print(f"Codec: {video_stream['codec_name']}")
        print(f"Codec Description: {video_stream['codec_long_name']}")
        print(f"Width: {video_stream['width']} pixels")
        print(f"Height: {video_stream['height']} pixels")
        print(f"Frame Rate: {video_stream['r_frame_rate']}")
        print(f"Bit rate: {video_stream.get('bit_rate', 'N/A')} bps")
        print(f"Duration: {video_stream['duration']} seconds")

    # Extracting audio stream metadata
    audio_stream = next((stream for stream in probe['streams'] \
                         if stream['codec_type'] == 'audio'), None)
    if audio_stream:
        print("\nAudio Stream Metadata:")
        print(f"Codec: {audio_stream['codec_name']}")
        print(f"Codec Description: {audio_stream['codec_long_name']}")
        print(f"Sample Rate: {audio_stream['sample_rate']} Hz")
        print(f"Channels: {audio_stream['channels']}")
        print(f"Bit rate: {audio_stream.get('bit_rate', 'N/A')} bps")
        print(f"Duration: {audio_stream['duration']} seconds")

# Example usage
video_path = 'example.mp4'
get_video_metadata(video_path)
