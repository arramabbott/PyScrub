from PIL import Image
from PIL.ExifTags import TAGS
def get_exif(fn):
	ret = {}
	i = Image.open(fn)
	info = i._getexif()
	print info

get_exif('/home/ghost/Downloads/downloads.jpg')