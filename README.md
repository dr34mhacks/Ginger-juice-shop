
## Ginger Juice Shop - Vulnerable SSTI Lab

Welcome to the Ginger Juice Shop, where you can explore and learn about Server-Side Template Injection (SSTI) vulnerabilities in a safe and controlled environment. This application provides two scenarios for practicing SSTI exploitation: a basic example and a more advanced challenge with input restrictions.

![image](https://github.com/user-attachments/assets/d3ddc15b-5037-4a3c-8082-c6ef54241aa0)


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
python app.py
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

## Security Disclaimer

This application is intended for educational purposes only. Do not use these techniques on systems without explicit permission. Always practice ethical hacking and responsible disclosure.

## Contributing

Feel free to submit issues or pull requests for enhancements or bug fixes. Contributions are welcome!

## Blog 

- https://<url>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy pentesting! 🛡️🔍
