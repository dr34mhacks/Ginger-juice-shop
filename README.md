
## Ginger Juice Shop - Vulnerable SSTI Lab

Welcome to the Ginger Juice Shop, where you can explore and learn about Server-Side Template Injection (SSTI) vulnerabilities in a safe and controlled environment. This application provides two scenarios for practicing SSTI exploitation: a basic example and a more advanced challenge with input restrictions. I hosted this live as well in case if you are sloth bear like me, Use the live link here at:

[Live Lab](https://ssti.pythonanywhere.com/)

### Homepage UI
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/e4caf1ae-d9d5-4089-a3c4-c522a6b83932">

### Hard Section
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/8135990a-1b2f-421e-972f-6dc6978b3e5f">


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

## Security Disclaimer

This application is intended for educational purposes only. Do not use these techniques on systems without explicit permission. Always practice ethical hacking and responsible disclosure.

## Contributing

Feel free to submit issues or pull requests for enhancements or bug fixes. Contributions are welcome!

## Blog 

- [https://dr34mhacks.github.io/posts/how-to-exploit-ssti/](https://dr34mhacks.github.io/posts/how-to-exploit-ssti/)

## License

This project is licensed under the MIT License

Happy Hunting! 🛡️🔍
