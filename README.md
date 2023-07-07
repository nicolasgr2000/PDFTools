# PDF Tools

PDF Tools is a Python application that provides various functionalities for manipulating PDF files. It allows you to perform the following operations:

- Unlock PDF: Remove password protection from one or more PDF files.
- Lock PDF: Apply password protection to one or more PDF files.
- Split PDF: Divide a PDF file into multiple smaller files based on page ranges.
- Merge PDF: Combine multiple PDF files into a single file.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the `pdf_tools.py` script.

The application will launch with a graphical user interface (GUI) consisting of four sections:

1. **Unlock PDF**: Drag and drop or select PDF files to remove password protection.
2. **Lock PDF**: Drag and drop or select PDF files to apply password protection.
3. **Split PDF**: Drag and drop or select PDF files to specify page ranges for splitting.
4. **Merge PDF**: Drag and drop or select multiple PDF files to combine them into a single file.

Each section has an area for drag and drop functionality and a button to manually select files. Once you perform the desired operation, a confirmation message will be displayed.

## Requirements

- Python 3.11
- PyPDF2 library

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute and suggest improvements!


