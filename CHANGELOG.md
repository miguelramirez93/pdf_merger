# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-18

### Added
- Comprehensive README.md documentation with usage instructions
- Test case for multi-digit filename handling in PDF merger
- Support for PDF files with multi-digit numeric suffixes (e.g., `document-10.pdf`, `document-123.pdf`)
- Project documentation covering features, installation, and architecture

### Fixed
- Fixed regex pattern in `_get_file_index` method to correctly match filenames with multi-digit numeric suffixes
- Changed regex from `r"-([0-9]).pdf"` to `r"-([0-9]+)\.pdf"` to support files like `document-10.pdf`, `document-123.pdf`

### Changed
- Improved project structure with better code organization and test coverage

## Unreleased

### Planned Features
- Command-line arguments for custom input/output directories
- Support for batch processing multiple directory trees
- Progress indicators during merge operations
