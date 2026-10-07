import zipfile

def extract_archive(archivepath, deet_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(deet_dir)



if __name__ == "__main__":
    extract_archive("compressed.zip", "dest")