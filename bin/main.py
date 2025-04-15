from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
from os import makedirs
from parsers import (
    item_parser,
    sheet_parser,
    items_list_parser,
    header_parser,
    image_downloader,
)

# Load the Excel workbook
wb = load_workbook(filename="source.xlsx")
print("Workbook loaded\n" + "-" * 30)

# Iterate through each worksheet in the workbook
for ws in wb:
    print("Processing", ws.title, end="... ", flush=True)

    # Parse the worksheet to extract items
    items = sheet_parser(ws)

    # Initialize the image loader for the worksheet
    image_loader = SheetImageLoader(ws)

    # Create directories for storing images and documentation
    makedirs(f"static/img/{ws.title.lower()}", exist_ok=True)
    makedirs(f"docs/{ws.title}", exist_ok=True)

    # Create and write the header for the documentation index file
    with open(f"docs/{ws.title}/index.md", "w") as file:
        file.write(header_parser(ws.title))

    # Process each item in the worksheet
    for item in items:
        # Append item details to the documentation index file
        with open(f"docs/{ws.title}/index.md", "a") as file:
            file.write(items_list_parser(item))

        try:
            # Download or save the item's image
            if item.imageRemoteURL:
                image_downloader(
                    item.imageRemoteURL,
                    f"static/img/{ws.title.lower()}/{item.safe_name}.png",
                )
            else:
                image_loader.get(f"C{item.idx + 1}").save(
                    f"static/img/{ws.title.lower()}/{item.safe_name}.png"
                )

            # Generate and save the item's detailed documentation
            md = item_parser(item)
            with open(f"docs/{ws.title}/{item.safe_name}.md", "w") as file:
                file.write(md)

        # Handle errors during processing
        except Exception as e:
            print(
                f"Error: item No. {item.idx} in worksheet {item.category} has a problem:\n{e}"
            )

    print("Finished")

print("-" * 30 + "\nAll done!")
