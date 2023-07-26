import sys
import os
import shutil
import time

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
        ".alac", ".amr", ".ape", ".au", ".dss",
        ".flac", ".flv", ".m4a", ".m4b", ".m4p",
        ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
        ".opus", ".qcp", ".tta", ".voc", ".wav",
        ".wma", ".wv"
    )

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
        ".mp4", ".m4p", ".m4v", ".mxf"
    )

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
    ".gif", ".webp", ".svg", ".apng", ".avif"
    )

curr_dir = os.getcwd()

def main():
    while True:
        sum = 0
        target_dir = input(" I'm ready. Which directory you want to organise? $")
        try:
            os.chdir(target_dir)
            print("|==============================================================================|\n")
            print(f" Moving from {curr_dir} to {target_dir}.\n")
            time.sleep(2)
            break
        except:
            print("|==============================================================================|\n")
            print(" Directory not found. Try again.")

    print("|==============================================================================|\n")
    print(" Scanning for files.....\n")
    time.sleep(2)

    for file in os.listdir():
        sum += 1

    if sum == 0:
        print("|==============================================================================|\n")
        print(" There are no files in this directory.\n")
        main()
    elif sum == 1: 
        print("|==============================================================================|\n")
        print(f" Found {sum} file.\n")
        time.sleep(2)
    else:
        print("|==============================================================================|\n")
        print(f" Found {sum} files.\n")
        time.sleep(2)


    print("|==============================================================================|\n")
    input(f" {sum} files will be organised by extension in their directories.\n This could take a while. Press enter to continue. $\n")

    print("|==============================================================================|\n")
    print(" Dividing files by extension...\n")

    for file in os.listdir():
        FILENAME = str(file.lower())
        def is_audio(file):
            return os.path.splitext(FILENAME)[1] in audio

        def is_video(file):
            return os.path.splitext(FILENAME)[1] in video

        def is_image(file):
            return os.path.splitext(FILENAME)[1] in img

    time.sleep(2)

    print("|==============================================================================|\n")
    print(" Creating directories...\n")
    if not os.path.exists("audio"):
        os.mkdir("audio")

    if not os.path.exists("images"):
        os.mkdir("images")

    if not os.path.exists("video"):
        os.mkdir("video")

    time.sleep(2)

    print("|==============================================================================|\n")
    print(" Moving files in their directories...\n")

    for file in os.listdir():
        FILENAME = str(file.lower())
        if is_audio(file):
            shutil.move(file, "audio")
        elif is_video(file):
            shutil.move(file, "video")
        elif is_image(file):
            shutil.move(file, "images")

    time.sleep(2)

    print("|==============================================================================|\n")
    print(f" All {sum} files are now organised.\n")
    print(" Exiting program. Goodbye ^^.\n")
    time.sleep(2)
    sys.exit()

if __name__ == '__main__':
    main()

    

    
        