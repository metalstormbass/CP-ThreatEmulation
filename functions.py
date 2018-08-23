import hashlib

def md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def file_name(file_path):
    filename_split = file_path.split("/")
    filename = str(filename_split[-1])
    return filename