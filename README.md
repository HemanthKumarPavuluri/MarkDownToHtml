# MarkDownToHtml
📌 Project Overview
This project is a static site generator that converts Markdown (.md) files into HTML using a custom parsing and templating system. It processes Markdown files, extracts their structure, and generates styled HTML pages dynamically.

🚀 Features
✔️ Converts Markdown (.md) files into HTML
✔️ Supports recursive page generation for nested content
✔️ Custom templating system with {{ Title }} and {{ Content }} placeholders
✔️ Fully WCAG-compliant output
✔️ Supports static asset copying (CSS, images, etc.)
✔️ Includes a built-in Python HTTP server


🛠️ Installation & Setup
1. Clone the Repository
git clone https://github.com/HemanthKumarPavuluri/MarkDownToHtml.git
cd MarkDownToHtml

2. Ensure Python 3 is Installed
   python3 --version
   
4. Run the Static Site Generator
  ./main.sh

📂 Project Structure
MarkdownToHtml/
│── content/                # Markdown files to be converted
│   ├── index.md            # Main homepage content
│   ├── majesty/            # Subdirectory with additional content
│   │   ├── index.md
│── public/                 # Generated HTML output (ignored in Git)
│── static/                 # Static assets (CSS, images)
│   ├── index.css
│   ├── images/
│── template.html           # HTML template with placeholders
│── src/
│   ├── main.py             # Main script to process Markdown
│   ├── markdown_blocks.py  # Markdown parsing functions
│── main.sh                 # Bash script to automate the process
│── README.md               # Project documentation (this file)
│── .gitignore              # Ignore generated public/ directory


🖥️ Usage
To generate pages for all Markdown files:
python3 src/main.py

To start a simple web server:
cd public && python3 -m http.server 8888


🌟 Contributing
Fork the repository
Create a feature branch (git checkout -b feature-name)
Commit your changes (git commit -m "Added a new feature")
Push to GitHub (git push origin feature-name)
Submit a Pull Request
