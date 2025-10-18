# 🚀 CSV MCP Server — Bring Your Data to Life in Claude

## Why This Matters

If you've ever tried to analyze CSV files in Claude.ai, you know the pain — it can't read your files directly. You end up:

- Copying and pasting CSV snippets (and hitting character limits)
- Uploading your data to other tools
- Manually describing what's inside your CSV

That's time-consuming and breaks your workflow.

## Enter the CSV MCP Server

This lightweight connector lets Claude directly access and analyze your local CSV files — privately, efficiently, and in real time.

With it, you can simply say:

**"Claude, show me all customers from New York with purchases over $1000,"**

and Claude will query your actual file.

## What This Server Does

Once connected, Claude can:

✅ List your local CSV files

✅ Preview structure and sample data

✅ Run queries using natural language or Pandas syntax

✅ Generate quick summaries (mean, median, count, etc.)

✅ Handle large datasets — all without sending data online

Everything runs locally — your files never leave your system.

## Why It's Different

- **Local-first & private**: your data stays on your device
- **Fast**: built using FastMCP
- **Extendable**: easily add Excel, TSV, or custom logic
- **Seamless**: Claude becomes your personal data assistant

## Quick Start

### Requirements

- Python 3.11 or higher
- Claude Desktop app
- [uv](https://docs.astral.sh/uv/) (recommended package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/Navneet1710/csv_mcp_server.git
cd csv_mcp_server
uv init .
```

### 2. Install Dependencies

Using uv, add the required packages:
```bash
uv add fastmcp
uv add pandas
```

### 3. Set Your CSV Directory

Open `main.py` and edit line 14 to match where your CSV files are stored:
```python
CSV_DIRECTORY = Path.home() / "Documents" / "csv_files"  # customize this if needed
```

### 4. Run the Server

Start the MCP server with:
```bash
uv run main.py
```

For development or inspection mode (to see tools, logs, and capabilities):
```bash
uv run fastmcp dev main.py
```

## Connecting to Claude Desktop

Open your Claude configuration file:

| OS | Path |
|---|---|
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

Add this MCP server entry:
```json
"csv-analyzer": {
      "command": uv,
      "args": [
        "--directory",
        "path\\to\\csv_mcp_server",
        "run",
        "main.py"
      ]
}
```

Save and restart Claude Desktop.

## Using It Inside Claude

Once connected, try commands like:

### List all CSVs
*"What CSV files are available?"*

### Preview a file
*"Show me the first few rows of sales_data.csv."*

### Run queries
*"From customer_data.csv, show all entries where purchase > 500."*

### Summarize data
*"Give me the average revenue in financial_report.csv."*

### Analyze relationships
*"Find the correlation between 'age' and 'satisfaction_score' in survey_results.csv."*

## Tools and Resources

| Type | Name | Description |
|---|---|---|
| Resource | `csv://list` | Lists all available CSV files |
| Resource | `csv://{filename}` | Preview a CSV (first 10 rows) |
| Tool | `read_csv(filename, rows)` | Read full or partial CSV data |
| Tool | `get_csv_info(filename)` | Get metadata and structure |
| Tool | `query_csv(filename, query)` | Filter data using Pandas query syntax |
| Tool | `get_csv_statistics(filename, column)` | Compute descriptive statistics |

## Default Folder Structure

By default, CSV files live in:

```
Documents/
└── csv_files/
    ├── sales_data.csv
    ├── customer_info.csv
    ├── inventory.csv
    └── financial_report.csv
```

## Customization

- **Change CSV directory** → edit `CSV_DIRECTORY` in `main.py`
- **Add support for Excel/TSV** → update the file-reading logic
- **Create your own tools** → add new `@mcp.tool()` functions for custom analysis

## Troubleshooting

### "Directory does not exist"
→ Make sure the path exists or create it:
```bash
mkdir -p ~/Documents/csv_files
```

### "File not found"
→ Check spelling and ensure the file is inside your configured directory.

### Claude doesn't detect the server
→ Restart Claude Desktop and confirm the config file path.

### Permission issues
→ Ensure Claude has read access to the directory (run as admin on Windows if needed).

### Debugging
Run directly:
```bash
uv run main.py
```

## Contributing

Got an idea or improvement? Contributions are welcome!

1. Fork this repo
2. Create a feature branch
3. Add your changes
4. Submit a pull request

## License

Open source — use, modify, and share freely.

## Built With

- [FastMCP](https://github.com/jlowin/fastmcp) — for fast, local MCP integration
- [pandas](https://pandas.pydata.org/) — for data manipulation and statistics
- [Anthropic's MCP](https://modelcontextprotocol.io/) — for connecting Claude to your environment

---

## Turn Claude Into Your Personal Data Analyst

Set this up once — and from then on, you can explore and analyze your CSVs right inside Claude.

**No uploads, no manual parsing, no limits.**

Run it locally. Keep your data private. Get instant insights.

**Make sure you don't forget to star the repo**

