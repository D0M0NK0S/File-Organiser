import os
import shutil

#directory = input("Give the main directory for file organisation: ")
directory = "/Users/domonkoskenesi/Downloads"
os.chdir(directory)

#Import non hidden files
files = []
def listdir_nohidden(path, files):
    for f in os.listdir(path):
        if not f.startswith('.'):
            files.append(f)
listdir_nohidden(directory, files)
types = set()

#Describe different file types of categories
audio = ("3ga", "aac", "ac3", "aif", "aiff",
         "alac", "amr", "ape", "au", "dss",
         "flac", "flv", "m4a", "m4b", "m4p",
         "mp3", "mpga", "ogg", "oga", "mogg",
         "opus", "qcp", "tta", "voc", "wav",
         "wma", "wv")

video = ("webm", "MTS", "M2TS", "TS", "mov",
         "mp4", "m4p", "m4v", "mxf", "avi")

img = ("jpg", "jpeg", "jfif", "pjpeg", "pjp", "png",
       "gif", "webp", "svg", "apng", "avif", "tiff", "bmp")

#Move files into sepearte folders
def move_files(files):
  already_moved = set()
  #Create the folders
  for elem in files:
    print(elem)
    if os.path.isfile(elem):
      if not os.path.isdir(directory + f"/{elem.split('.').pop()}"):
        os.mkdir(elem.split(".").pop())
        types.add(elem.split(".").pop())
  #Move the files
  for elem in files:
    if os.path.isfile(elem): 
      if not os.path.isfile(directory + f"/{elem.split('.').pop()}" + f"/{elem}"):
        shutil.move(elem, directory + f"/{elem.split('.').pop()}")
      else:
        already_moved.add(elem)

  #Make the main directories
  def is_audio(file):
      return file in audio

  def is_video(file):
      return file in video

  def is_image(file):
      return file in img

  files = os.listdir(".")

  #Move type_folders into MAIN folders
  for elem in files:
    if is_audio(elem):
      if not os.path.isdir(directory + "/audio"):
        os.mkdir("audio")
      if not os.path.isdir(directory + f"/{elem}"):
       shutil.move(elem, directory + "/audio")
      else:
        for i in os.listdir(directory + f"/{elem}"):
          if not os.path.isfile(directory + "/audio" + f"/{elem}" + f"/{i}"):
            shutil.move(directory + f"/{elem}" + f"/{i}", directory + "/audio" + f"/{elem}")
          else:
           already_moved.add(elem)
    
    elif is_video(elem):
      if not os.path.isdir(directory + "/videos"):
        os.mkdir("videos")
      if not os.path.isdir(directory + "/videos" + f"/{elem}"):
        shutil.move(elem, directory + "/videos")
      else:
        for i in os.listdir(directory + f"/{elem}"):
          if not os.path.isfile(directory + "/videos" + f"/{elem}" + f"/{i}"):
            shutil.move(directory + f"/{elem}" + f"/{i}", directory + "/videos" + f"/{elem}")
          else:
           already_moved.add(elem)
    
    elif is_image(elem):
      if not os.path.isdir(directory + "/images"):
        os.mkdir("images")
      if not os.path.isdir(directory + "/images" + f"/{elem}"):
        shutil.move(elem, directory + "/images")
      else:
        for i in os.listdir(directory + f"/{elem}"):
          if not os.path.isfile(directory + "/images" + f"/{elem}" + f"/{i}"):
            shutil.move(directory + f"/{elem}" + f"/{i}", directory + "/images" + f"/{elem}")
          else:
           already_moved.add(elem)

#Remove moved folders and duplicates
  if already_moved != []:
    if input("Do you wish to remove already moved elements and copies? Y/N::   ") == "Y":
      for elem in already_moved:
        if os.path.isfile(elem):
          os.remove(elem)
        elif os.path.isdir(elem):
          shutil.rmtree(elem)


move_files(files)