# Self-Improvement AI Script

## Overview

This script is a self-improving AI designed to enhance its own code. By utilizing OpenAI's capabilities, the script can request improvement suggestions and apply them iteratively.

## Requirements

- Python 3.7+
- OpenAI Python client (`openai` package)
- Environment variable `OPENAI_API_KEY` set with your OpenAI API key

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/MichaelEight/ai-improves-own-code
   cd <repository-directory>
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set the OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. The script will log activities and save the improved code to `improved_code.txt`. Replace manually to continue. This is done this way to allow user to review the changes and polish small imperfections like using ```python tag at the beginning of the file.

## Contribution

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the MIT License.
