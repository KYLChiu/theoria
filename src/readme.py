from pathlib import Path

codeowners_file = Path(".github/CODEOWNERS")
output_file = Path("README.md")

if not codeowners_file.exists():
    print("No CODEOWNERS file found!")
    exit(1)

lines = codeowners_file.read_text().splitlines()

entries = []
for line in lines:
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split()
    pattern = parts[0]
    owners = ", ".join(parts[1:])
    entries.append(f"- `{pattern}` → {owners}")

content = "# Code Owners\n\nThis file lists which files or directories each person/team is responsible for.\n\n"
content += "\n".join(entries)

output_file.write_text(content)
print(f"Generated {output_file}")
