# Simple PNG to JPEG Backup Script
 This script will create a jpeg backup of a folder containing pngs, while also maintaining the source’s folder structure. It is useful for creating a backup of a large number of png files in the jpeg format.

This script is tested with Windows 11 but should work in other operating systems.

This script requires [opencv-python](https://pypi.org/project/opencv-python/). 

To Run, simply run the following in a command line in the same directory as the python file.
```
{
  python convertfiles.py "png/source/directory" "jpeg/backup/directory"
}
```

Replace "png/source/directory" and "jpeg/backup/directory" with the png source directory and the jpeg backup directory, respectively.
