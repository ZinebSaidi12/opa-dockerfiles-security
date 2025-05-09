import json
from dockerfile_parse import DockerfileParser

# Initialize parser for current directory
dfp = DockerfileParser(path='.')

# Start parsed structure
parsed = {
    "FromImage": dfp.baseimage or "",
    "User": None,
    "Instructions": []
}

# Loop through Dockerfile instructions
for inst in dfp.structure:
    instruction = inst["instruction"].upper()
    value = inst["value"]

    # Capture USER if defined
    if instruction == "USER":
        parsed["User"] = value

    # Collect all instructions
    parsed["Instructions"].append({
        "instruction": instruction,
        "value": value
    })

# Output JSON to stdout
print(json.dumps(parsed))
