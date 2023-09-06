# Write the solution for "Split the files".
import os


def getFileSize(file: os.DirEntry[str]):
    """Returns the size of a file in bytes."""
    return file.stat().st_size


def splitFile(file):
    """Partitions file into subfiles of 499 bytes or less."""
    os.makedirs("outputs/split", exist_ok=True)
    os.system(f"split -d -C 499 inputs/split/{file.name} outputs/split/{file.name}-")
    os.system(f"rm -f outputs/split/{file.name}-00")


# iterate through the files in the inputs directory
for file in os.scandir("inputs/split"):
    if getFileSize(file) >= 500:
        splitFile(file)
