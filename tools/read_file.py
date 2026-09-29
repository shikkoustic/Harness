SCHEMA = {
  "type": "function",
  "function": {
    "name": "read_file",
    "description": "Read the contents of a text file given it's path",
    "parameters": {
      "type": "object",
      "properties": {
        "path": {
          "type": "string",
          "description": "The file path to read, e.g. Agent.py"
        }
      },
      "required": ["path"]
    },
  },
}

def run(path: str) -> str:
  try:
    with open(path, "r") as f:
      return f.read()
  except Exception as e:
    return f"Error reading file: {e}"