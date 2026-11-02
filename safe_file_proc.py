
import traceback

# Custom exception classes
class FileProcessingError(Exception):
    pass


class InvalidFileFormatError(FileProcessingError):
    pass


class EmptyFileError(FileProcessingError):
    pass


def process_file(filename):
    file = None

    try:
        file = open(filename, "r", encoding="utf-8")
        content = file.read()

        if not content.strip():
            raise EmptyFileError("The file is empty.")

        if not content.lstrip().startswith("DFm:"):
            raise InvalidFileFormatError(
                "Invalid file format. File must start with 'DATA:'."
            )

        data = content.strip().split("DFm:", 1)

    except FileNotFoundError:
        print("Error: File not found.")

    except (InvalidFileFormatError, EmptyFileError) as e:
        print("Processing Error:", e)
        print("Traceback information:")
        traceback.print_exc()

    except PermissionError:
        print("Error: Permission denied.")

    except OSError as e:
        print("File system error:", e)

    else:
        print("File processed successfully!")
        print("Extracted Data:", data)

    finally:
        if file is not None:
            file.close()

        print("File closed safely.")
        print("File processing completed.")


# Main program
filename = input("Enter file name: ")
process_file(filename)
