import logging

def wrongCode(filename):
    #Reading a file
    """
    1.If the file does not exist,
        the code will raise a FileNotFoundError exception,
        but it does not handle the exception or provide any useful information
        to the user about what went wrong.
    2.If the file is not readable due to permissions or other issues,
        the code will raise an IOError exception,
        but it does not handle the exception or provide any useful information to
        the user about what went wrong.
    3.The code does not log any information about errors or exceptions that occur,
        which makes it difficult to diagnose issues and identify potential security vulnerabilities.
    """
    f = open(filename, "r")
    contents = f.read()
    print(contents)
    f.close()


def correctCode(filename):
    try:
        f = open(filename, "r")
        contents = f.read()
        print(contents)
        f.close()
    except FileNotFoundError as e:
        logging.error(f"Error: File '{filename}' not found")
    except IOError as e:
        logging.error(f"Error: Could not read file '{filename}'")


if __name__ == "__main__":
    filename = input("Enter filename: ")
    #wrongCode(filename)
    correctCode(filename)