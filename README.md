# Eros

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install eros.

```bash
pip install eros
```

## Usage

```python
from eros import Client, Instagram, TikTok, Pinterest, Threads, Twitter, YouTube

client = Client(api_key="your api key")
Instagram = Instagram(client)
return await Instagram.get_user("therock")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)