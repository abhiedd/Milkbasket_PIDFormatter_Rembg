# Hero Code Plus

A robust Streamlit app for flexible campaign PID/asset formatting and product image management, built for Milkbasket’s campaign workflow.

## Features

- Campaign-wise PID/asset export from CSV or Google Sheets
- Bulk “All_PIDs” tab with image URLs and missing-image highlights
- ZIP download of all product images in All_PIDs tab
- Auto-fill of image links for PID1/PID2 using a product dump
- Supports both local files and Google Sheet links
- **NEW:** Optional button for bulk background removal with download as ZIP (uses rembg)
- **Filenames preserved:** Downloaded images retain their original `image_src` filenames from the product dump, always as `.png`
- **All images resized to 650x650px**

## Quick Start

1. Clone the repo:
   ```
   git clone https://github.com/YOUR_USERNAME/hero-code-plus.git
   cd hero-code-plus
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Launch the app:
   ```
   streamlit run hero_code_plus.py
   ```

## Files

- hero_code_plus.py — main Streamlit app
- requirements.txt — required Python packages
- .gitignore — recommended for a clean repo

## Usage

Just upload your campaign file and, optionally, your product dump to auto-fill images and assets!

For background removal, go to the "All_PIDs" tab and use the "Remove background and download images as ZIP" button.

---

For more, see the comments inside hero_code_plus.py.
