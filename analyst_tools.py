from smolagents import tool

@tool
def table_metadata_loader(table_name: str) -> str:
    """
    Load metadata for a given table from a schema file.
    This function reads the schema from a file and returns the metadata for the specified table.

    Args:
        table_name (str): The name of the table to load metadata for.
    """
    with open("data/schema.txt", "r") as file:
        metadata = file.read()
    return f"Metadata for {table_name} {metadata}"