import os
from PIL import Image
import pyheif

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'heic'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_heic_to_jpeg(input_path):
    """
    Converts a HEIC file to JPEG. Deletes the original HEIC.
    Returns the path to the JPEG file (or original path if not HEIC).
    """
    if input_path.lower().endswith('.heic'):
        heif_file = pyheif.read(input_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        output_path = os.path.splitext(input_path)[0] + ".jpeg"
        image.save(output_path, format="JPEG")
        os.remove(input_path)  # delete original HEIC
        return output_path
    return input_path
