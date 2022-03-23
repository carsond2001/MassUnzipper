import os
import shutil

def fast_scandir(dirname, fileList):
    for root, directories, files in os.walk(dirname, topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            fileList.append(os.path.join(root, name))

def unzipper(path_to_zip_file, directory_to_extract_to):
    import zipfile
    import patoolib
    try:
        try:
            patoolib.extract_archive(path_to_zip_file, outdir=directory_to_extract_to)
        except:
            with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to)
    except:
        return

if __name__ == "__main__":
    fileList = []
    fast_scandir("D:\presets\In", fileList)
    print(fileList)
    for path in fileList:
        unzipper(path, "D:\presets\In")
    fast_scandir("D:\presets\In", fileList)
    print(fileList)
    for path in fileList:
        print("e")
        try:
            if path[-1] == "v":
                shutil.move(path, "D:\presets\Out")
        except:
            continue

