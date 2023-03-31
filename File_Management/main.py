import os

# This code allows user to remove any type of files
#User should only removes jpg images.
#WHich is not secure
def wrongCode(filename):
    os.remove(filename)
    print("File removed")


def correctCode(filename):
    #Check to if user removes the images
    if filename.endswith('.jpg'):
        os.remove(filename)
        print("File removed")
    else:
        print("Only .jpg files are allowed to be removed.")


if __name__ == "__main__":
    filename = input("Enter file name: ")
    wrongCode(filename)
    correctCode(filename)