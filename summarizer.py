import click
import requests

@click.command()
@click.option('-t', '--text-file', type=click.Path(exists=True), help='Path to the text file to summarize.')
@click.argument('text', required=False)
def get_text(text_file, text):
    try:
        if text_file:
            with open(text_file, 'r') as file:
                text = file.read()
            save_to_file = True
        elif text:
            save_to_file = False
        else:
            click.echo('Please provide either a text file with -t or direct text as an argument.')
            return
        
        summary = summarize_text(text)
        click.echo(f'Summary:\n{summary}')
        
        if save_to_file:
            output_file = 'summary.txt'
            with open(output_file, 'w') as file:
                file.write(summary)
            click.echo(f'Summary has been written to {output_file}')
        
    except Exception as e:
        click.echo(f"An error occurred: {e}")

def summarize_text(text):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'qwen2:0.5b',
        'prompt': f'Summarize the following text in a concise and informative manner: {text}',
        'stream': False
    }

    response = requests.post('http://localhost:11434/api/generate', headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get('response', '')
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == '__main__':
    get_text()
