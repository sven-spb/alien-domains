# Async Domain Checker

This project is a Python script that performs asynchronous DNS queries to check for specific conditions on domain records. It gets domain names from a list, checks their `NS` and `A` records, and identifies domains whose `A` records fall within a specified subnet and do not have specific `NS` records.

## Features

- **Asynchronous DNS Queries**: Perform non-blocking DNS lookups with `aiodns`.
- **Subnet Filtering**: Validate `A` records against a target subnet.
- **Selective NS Filtering**: Skip domains with specific `NS` records.

## Prerequisites

- Python 3.13+
- Valid `.env` file with configuration settings

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sven-spb/alien-domains.git
   cd alien-domains
   ```

2. **Install dependencies**:

    With a miracle of the [uv](https://github.com/astral-sh/uv):

    ```bash
    uv sync
    ```

    Alternatively with the `pip`:

    ```bash
    pip install -r requirements.txt
    ```
   
3. **Set up the .env file: Create a .env file from [.env_example](.env_example) in the project root with the following keys:**:
   ```bash
    SUBNET=192.168.0.0/23
    TARGET_NS=ns1.domain.tld,ns2.domain.tld
   ```

## Usage
Simplest way to run the script is through the `uv`:
```bash
uv run app.py
```
Or, if you are in virtual environment:
```bash
python app.py
```
You should provide list with domain names you need to check. Either with `domains` in [alien_domains.py](alien_domains.py) or you could import `check_domain_records_async()` from outside and pass the list as a parameter.

## How it Works

### NS Record Check:
- Skips domains if any `NS` record matches `TARGET_NS` values.

### A Record Check:
- Prints domain names and their `A` records if the IP address falls within the specified `SUBNET`.

## Contributing
Feel free to fork the repository and submit pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT> file for details.

Enjoy! 🎉
