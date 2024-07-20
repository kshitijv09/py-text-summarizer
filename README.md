# Text Summarizer CLI Tool

This is a Python command-line tool for summarizing text using the Qwen2 0.5B model via the Ollama API. The tool can handle both text files and direct text input.

## Prerequisites

1. **Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. **Ollama**: Download Ollama. You can download it from [ollama.com](https://ollama.com/).

## Steps to Set Up and Run the Tool

### Step 1: Download and Run Ollama

1. **Download Ollama**:
    - Visit the [Ollama website](https://ollama.com) and download the appropriate version for your operating system.

2. **Run the Qwen2 0.5B Model**:
    - Open a terminal and run the following command to start the Qwen2 0.5B model:
      ```bash
      ollama run qwen2:0.5b
      ```

### Step 2: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/kshitijv09/py-text-summarizer.git
cd py-text-summarizer
```

### Step 3: Install dependencied

```bash
pip install -r requirements.txt
```
### Step 4: Run the tool

By providing a text file. In this case summary will be saved in a file summary.txt

```bash
python summarizer.py -t path/to/textfile.txt
```
Directly passing text as argument

```bash
python summarizer.py "Your direct text here"
```



