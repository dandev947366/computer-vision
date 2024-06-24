import os
from PIL import Image

def load_image(image_path):
    """
        Read img path
        Args: image_path
        Returns: img
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print('Error when reading image: ', image_path, ' ', e)
        return None
        
# check image validation        
def is_image_file(file_path):
    """
        return: True - if is image
                False - if not image
    """
    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    return file_path.lower().endswith(image_extensions)

def get_image_list(folder_path):
    image_list = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)
        for filename in filenames:
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and is_image_file(file_path):
                img = load_image(file_path)
                if img is not None:
                    image_list.append(img)
    return image_list