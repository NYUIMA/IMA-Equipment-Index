import requests

illegal_char_filename = [
    "\\",
    "/",
    ":",
    "+",
    "*",
    "?",
    '"',
    "<",
    ">",
    "|",
    "@",
    "(",
    ")",
    "[",
    "]",
    ",",
    ";",
    "=",
    "#",
    "!",
    "$",
    "&",
    "'",
    "®",
]

illegal_char_markdown = [
    "\\",
    "`",
    "*",
    "_",
    "{",
    "}",
    "[",
    "]",
    "<",
    ">",
    "(",
    ")",
    "#",
    "+",
    "-",
    ".",
    "!",
    "|",
]


class Item:
    def __init__(self, idx: int, category: str, data: tuple):
        def verify(val: str | None) -> str | None:
            if not val:
                return None
            return str(val).strip()

        def wrap_URL(url: str):
            if not url:
                return False
            if len(url) >= 55:
                return url[:55] + "..."
            else:
                return url

        def parse_url(url: str | None) -> str | None:
            if not url:
                return None
            url = url.split("\n")
            for i in range(len(url)):
                res = []
                for part in url[i].split(" "):
                    if part.startswith("http://") or part.startswith("https://"):
                        res.append(f"[{wrap_URL(part)}]({part})")
                    else:
                        res.append(sanitize_description(part))
                url[i] = " ".join(res)
            if len(url) > 1:
                return "\n\n" + "\n\n".join(url)
            return url[0]

        def sanitize_filename(filename: str) -> str:
            sanitized = []
            for char in filename.lower():
                if char in illegal_char_filename:
                    sanitized.append("-")
                elif char == " ":
                    sanitized.append("_")
                else:
                    sanitized.append(char)
            return "".join(sanitized)

        def sanitize_description(content: str) -> str:
            if type(content) != str or content == "#REF!":
                return ""
            sanitized = []
            for char in content:
                if char in illegal_char_markdown:
                    sanitized.append("\\" + char)
                elif char == "\n":
                    sanitized.append("\n\n")
                else:
                    sanitized.append(char)
            return "".join(sanitized)

        self.category: str = category
        self.idx: int = idx + 1
        self.name: str = data[1].value
        self.safe_name: str = sanitize_filename(self.name)
        self.imageRemoteURL: str = (
            str(data[2].value).split('"')[1] if data[2].value else None
        )
        self.imageURL: str = f"/img/{self.category.lower()}/{self.safe_name}.png"
        self.tag: str = data[3].value
        self.brand: str = verify(data[4].value)
        self.model: str = verify(data[5].value)
        self.description: str = sanitize_description(data[7].value)
        self.productURL: str = parse_url(data[8].value)
        self.docURL: str = parse_url(data[9].value)
        self.accessories: str = sanitize_description(data[10].value)

    def __str__(self):
        return f"{self.idx}: {self.name} ({self.safe_name})\nDescription:\n{self.description}"


def image_downloader(url: str, filedir: str) -> None:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(
            f"Error: {response.status_code} while fetching {url} to save as {filedir}"
        )
    with open(filedir, "wb") as file:
        file.write(response.content)


def header_parser(title: str) -> str:
    return f"""\
---
pagination_prev: null
pagination_next: null
---

# {title}

| Name | Image |
| :--- | :---: |
"""


def sheet_parser(ws) -> list[Item]:
    items = []
    category = ws.title
    for idx, row in enumerate(tuple(ws.rows)[1:]):
        if row[1].value:
            items.append(Item(idx, category, row))
    return items


def items_list_parser(item: Item) -> str:
    return f"""\
| [{item.name}](./{item.safe_name}) | ![{item.safe_name}]({item.imageURL}) |
"""


def information_parser(item: Item) -> str:
    info = []
    basic_info = ["## Basic information"]
    if item.brand:
        basic_info.append(f"**Brand**: {item.brand}")
    if item.model:
        basic_info.append(f"**Model**: {item.model}")
    if item.productURL:
        basic_info.append(f"**Product page**: {item.productURL}")
    if item.docURL:
        basic_info.append(f"**Documentation**: {item.docURL}")
    if len(basic_info) > 1:
        info.append("\n\n".join(basic_info))
    if item.accessories:
        info.append("## Accessories List")
        info.append(item.accessories)
    if item.description:
        info.append("## Description")
        info.append(item.description)
    if len(info):
        return "\n\n".join(info)
    return ""


def item_parser(item: Item) -> str:
    return f"""\
---
title: "{item.name}"
sidebar_position: {item.idx}
tags:
    - "{item.tag}"
image: "{item.imageURL}"
description: "Brand: {item.brand}, Model: {item.model}"
---
# {item.name}

![{item.safe_name}]({item.imageURL})

{information_parser(item)}

"""
