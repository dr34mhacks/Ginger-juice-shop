
## Ginger Juice Shop - Vulnerable SSTI Lab

Welcome to the Ginger Juice Shop, where you can explore and learn about Server-Side Template Injection (SSTI) vulnerabilities in a safe and controlled environment. This application provides two scenarios for practicing SSTI exploitation: a basic example and a more advanced challenge with input restrictions.

### Homepage UI
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/c54e3415-1d91-4316-a99c-349ebf72fe0d">

### /hard endpoint UI
<img width="1512" alt="image" src="https://github.com/user-attachments/assets/76b8cc39-4862-49e9-a266-446bf05429a4">



## Prerequisites 

Before setting up the application, make sure you have the following installed on your machine:

- **Python 3.7 or later**: [Download Python](https://www.python.org/downloads/)
- **Flask:** Usually comes by default in many newer debian distro if not just install it by using
- 
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

- https://<url>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy pentesting! 🛡️🔍
