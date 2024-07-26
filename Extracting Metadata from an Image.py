from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_image_metadata(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    if exif_data is not None:
        # Dictionary to store metadata
        metadata = {}

        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            metadata[tag_name] = value

        # Print general metadata
        print("General Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")

        # Print GPS metadata if available
        if 'GPSInfo' in metadata:
            gps_info = metadata['GPSInfo']
            gps_data = {}
            for gps_tag, gps_value in gps_info.items():
                gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                gps_data[gps_tag_name] = gps_value

            print("\nGPS Metadata:")
            for key, value in gps_data.items():
                print(f"{key}: {value}")
    else:
        print("No EXIF metadata found")

# Example usage
image_path = 'example.jpg'
get_image_metadata(image_path)
