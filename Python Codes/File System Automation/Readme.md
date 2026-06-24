# Books to Notes

A Python automation tool that watches a folder for PDF files, extracts annotations (highlights, comments, underlines, and other markup), and converts them into structured notes.

## Overview

When a PDF is added or updated inside the monitored folder, the system automatically:

1. Detects the PDF file.
2. Waits until the file is fully written and accessible.
3. Opens the PDF using PyMuPDF.
4. Extracts text and annotations.
5. Processes the extracted information.
6. (Planned) Generates Markdown notes automatically.

The long-term goal is to transform annotated PDFs into a searchable personal knowledge base.

---

## Features

### Current Features

* Folder monitoring using Watchdog
* Automatic PDF detection
* Handles file-locking during file copy operations
* Reads PDF content using PyMuPDF
* Detects PDF modifications
* Extracts annotation metadata
* Prints highlighted and annotated content to the terminal

### Planned Features

* Markdown note generation
* Annotation categorization
* Support for:

  * Highlights
  * Underlines
  * Comments
  * Sticky Notes
  * Rectangles and boxed regions
* Structured JSON exports
* AI-generated summaries
* Knowledge graph generation
* Local vector database integration
* Chat with annotated notes

---

## Workflow

```text
PDF Added / Modified
          ↓
Folder Watcher
          ↓
PDF Processing
          ↓
Annotation Extraction
          ↓
Structured Data
          ↓
Markdown Notes (Planned)
```

---

## Project Structure

```text
books_to_notes/

├── books/
│   └── PDFs monitored by the watcher
│
├── notes/
│   └── Generated markdown files (planned)
│
├── watcher.py
├── pdf_reader.py
├── annotation_extractor.py
├── markdown_writer.py
└── main.py
```

Current implementation is contained in a single script and will be refactored into modules as the project grows.

---

## Technologies Used

### Python

Core programming language.

### Watchdog

Used for monitoring filesystem events.

Responsibilities:

* Detect new PDFs
* Detect PDF updates
* Trigger processing automatically

### PyMuPDF

Used for PDF processing.

Responsibilities:

* Open PDF files
* Read page text
* Access annotations
* Extract highlighted content

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd books_to_notes
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install watchdog pymupdf
```

---

## Running the Project

Update the folder path inside the script:

```python
observer.schedule(
    event_handler,
    r"path_to_your_pdf_folder",
    recursive=False
)
```

Run:

```bash
python main.py
```

The watcher will continue running until manually stopped.

---

## Example Output

```text
Created paper.pdf

Pages: 12

Highlighted Text:
Transformer architecture uses self-attention

Highlighted Text:
Positional encoding preserves sequence information
```

---

## Future Vision

Books to Notes is intended to become more than a PDF annotation extractor.

The long-term objective is:

```text
PDF
 ↓
Annotations
 ↓
Structured Notes
 ↓
Knowledge Base
 ↓
Personal Learning Memory
```

Instead of manually rewriting highlights and comments, the system should automatically convert reading activity into reusable knowledge.

---

## Learning Goals Behind This Project

This project is also being used to learn:

* Event-driven programming
* Filesystem automation
* PDF internals
* Annotation extraction
* Data processing pipelines
* Software architecture
* Knowledge management systems
* AI-assisted learning workflows

---

## Status

Current Stage: MVP Prototype

Completed:

* PDF monitoring
* PDF opening
* Annotation detection

In Progress:

* Reliable annotation extraction

Next Milestone:

* Automatic Markdown generation from annotations
