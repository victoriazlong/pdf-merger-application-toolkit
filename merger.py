import os
from pypdf import PdfWriter


def merge_pdfs(input_files: list[str], output_filename: str = "Combined_Application.pdf") -> None:
    """Combines multiple PDF files into a single output document.

    Args:
        input_files (list[str]): List of file paths to combine.
        output_filename (str): Name of the generated merged PDF.
    """
    merger = PdfWriter()
    missing_files = []

    for file_path in input_files:
        if os.path.exists(file_path):
            merger.append(file_path)
            print(f"Added: {file_path}")
        else:
            missing_files.append(file_path)

    if missing_files:
        print(f"\nWarning: The following files were not found and skipped: {missing_files}")

    if len(merger.pages) > 0:
        merger.write(output_filename)
        merger.close()
        print(f"\nSuccess! Final merged file saved as: {output_filename}")
    else:
        print("\nError: No valid PDF files were provided to merge.")


if __name__ == "__main__":
    # Specify the target PDF files to merge in order
    files_to_combine = [
        "sample_files/sample_resume.pdf",
        "sample_files/sample_cover_letter.pdf",
        "sample_files/sample_transcript.pdf",
    ]

    merge_pdfs(input_files=files_to_combine, output_filename="Complete_Application.pdf")