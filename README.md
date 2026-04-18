# PDF Merger

A Python CLI tool that recursively searches for PDF files in a directory structure and intelligently merges them based on filename patterns.

## Features

- **Recursive directory traversal** - Scans through all subdirectories looking for PDF files
- **Smart merging** - Groups PDFs by base filename (ignoring numeric suffixes) and merges them in order
- **Preserves structure** - Maintains the original directory hierarchy in the output
- **Filename pattern matching** - Automatically handles files with patterns like `document-1.pdf`, `document-2.pdf`, etc.

## Requirements

- Python 3.10 or higher
- PyPDF2 (for PDF manipulation)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pdf_merger
```

2. Install dependencies using Pipenv:
```bash
pipenv install
```

Or install PyPDF2 directly:
```bash
pip install pypdf2
```

## Usage

### Basic Usage

Run the CLI from the project root directory:

```bash
python main.py
```

The tool will:
1. Scan the `./in` directory recursively for all PDF files
2. Group PDFs by their base filename (e.g., `document-1.pdf` and `document-2.pdf` become `document.pdf`)
3. Merge grouped PDFs in numerical order
4. Write merged results to the `./out` directory, preserving the original directory structure

### Directory Structure

Expected input structure:
```
./in/
├── subfolder1/
│   ├── report-1.pdf
│   ├── report-2.pdf
│   └── guide-1.pdf
└── subfolder2/
    ├── manual-1.pdf
    ├── manual-2.pdf
    └── manual-3.pdf
```

Output structure:
```
./out/
├── subfolder1/
│   ├── report.pdf (merged from report-1.pdf and report-2.pdf)
│   └── guide.pdf
└── subfolder2/
    └── manual.pdf (merged from manual-1.pdf, manual-2.pdf, and manual-3.pdf)
```

## How It Works

1. **File Discovery** - The `Searcher` class recursively scans the input directory for all `.pdf` files, organizing them by their containing directory
2. **Filename Parsing** - File paths are parsed to extract the base filename, removing numeric suffixes (e.g., `-1`, `-2`)
3. **Grouping** - PDFs are grouped by their base filename within each directory
4. **Merging** - PDFs in each group are merged together using PyPDF2
5. **Output** - Merged PDFs are written to the output directory with the same structure as the input

### Filename Pattern

The tool recognizes and handles filenames with the pattern `{name}-{number}.pdf`:

- `document-1.pdf` + `document-2.pdf` → `document.pdf`
- `report-1.pdf` → `report.pdf` (single file, no merge needed but renamed)

## Architecture

The project follows a modular architecture:

- **`main.py`** - Entry point that initializes dependencies and starts the merge process
- **`merger/`** - Core merging logic and contracts/interfaces
- **`dir/`** - Directory searching and file discovery
- **`infrastructure/`** - External dependencies (file I/O, PDF merging)

## Error Handling

The CLI includes comprehensive error handling:
- If an error occurs during merging, it will be caught and displayed
- The program will wait for user input before exiting (press any key to continue)
- Errors include context about which operation failed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Example

```bash
$ python main.py
Merging process started, please wait...
press any key to exit...
```

After execution, check the `./out` directory for merged PDFs organized in the same structure as your input.
