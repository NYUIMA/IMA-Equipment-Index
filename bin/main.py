from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
from os import makedirs
from shutil import rmtree
import json
import os
import sys
from parsers import (
    item_parser,
    sheet_parser,
    items_list_parser,
    header_parser,
    image_downloader,
)

FAILED = False

# Load the Excel workbook
wb = load_workbook(filename="source.xlsx")
print("Workbook loaded\n" + "-" * 30)

if os.path.exists("links_map.json"):
    with open("links_map.json", "r") as f:
        try:
            links_map = json.load(f)
        except json.JSONDecodeError:
            links_map = {}
else:
    links_map = {}

# Iterate through each worksheet in the workbook
for ws in wb:
    print("Processing", ws.title, end="... ", flush=True)

    if ws.title not in links_map:
        links_map[ws.title] = {}

    # Parse the worksheet to extract items
    items = sheet_parser(ws)

    # Initialize the image loader for the worksheet
    image_loader = SheetImageLoader(ws)

    # Delete existing data folders
    # rmtree(f"static/img/{ws.title.lower()}")
    rmtree(f"docs/{ws.title}")

    # Create directories for storing images and documentation
    makedirs(f"static/img/{ws.title.lower()}", exist_ok=True)
    makedirs(f"docs/{ws.title}")

    # Create and write the header for the documentation index file
    with open(f"docs/{ws.title}/index.md", "w") as file:
        file.write(header_parser(ws.title))

    # Process each item in the worksheet
    for item in items:
        # Append item details to the documentation index file
        with open(f"docs/{ws.title}/index.md", "a") as file:
            file.write(items_list_parser(item))
        if item.safe_name not in links_map[ws.title]:
            links_map[ws.title][item.safe_name] = item.imageRemoteURL

        if item.imageRemoteURL:
            if links_map[ws.title][item.safe_name] != item.imageRemoteURL:
                links_map[ws.title][item.safe_name] = item.imageRemoteURL
                downloaded = image_downloader(
                    item.imageRemoteURL,
                    f"static/img/{ws.title.lower()}/{item.safe_name}.png",
                )
                if not downloaded:
                    print(
                        f"Error: item No. {item.idx} in worksheet {item.category} has the above problem.\n"
                    )
                    FAILED = True
        else:
            image_loader.get(f"C{item.idx + 1}").save(
                f"static/img/{ws.title.lower()}/{item.safe_name}.png"
            )

        # Generate and save the item's detailed documentation
        md = item_parser(item)
        with open(f"docs/{ws.title}/{item.safe_name}.md", "w") as file:
            file.write(md)

    print("Finished")

# At the end of processing, write back the updated links_map
with open("links_map.json", "w") as links_map_file:
    json.dump(links_map, links_map_file, indent=2)
print("-" * 30 + "\nAll done!")
sys.exit(FAILED)
