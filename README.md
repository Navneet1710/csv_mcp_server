# 🚀 CSV MCP Server — Bring Your Data to Life in Claude

## Why This Matters

If you've ever tried to analyze CSV data in Claude.ai, you've probably hit a wall.
You couldn't just hand it a file — instead, you had to:

- Copy and paste CSV snippets (often hitting text limits)
- Upload files elsewhere to summarize or filter
- Explain what's inside the file manually

That's inefficient, error-prone, and breaks your workflow.

## Enter the CSV MCP Server

This tool connects Claude directly to your local CSV files, so it can explore, query, and summarize your data — all from within the chat.

With it, you can say things like:

**"Claude, show me all customers from New York with purchases over $1000,"**

and it just works.

## What This Server Does

Once connected, Claude can:

✅ See and list the CSV files in your local directory

✅ Understand their structure (columns, datatypes, preview rows)

✅ Run queries using natural language or Pandas syntax

✅ Generate summaries (mean, median, counts, etc.) for any column

✅ Handle large files efficiently — all without sending your data online

Your data stays on your machine. Claude just talks to this local server through the Model Context Protocol (MCP).

## Why It's Different

Unlike cloud-based CSV tools, this one is:

- **Local-first & private** — nothing leaves your system
- **Fast** — built with FastMCP
- **Flexible** — you can extend it to support Excel, TSV, or other formats
- **Seamlessly integrated** — Claude becomes your data analyst

## Quick Start

### Requirements

- Python 3.11+
- Claude Desktop app
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### 1. Install

Clone and enter the repo:
```bash
git clone <repository-url>
cd csv_mcp_server
```

Install dependencies:

Using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

### 2. Set Your CSV Directory

In `main.py`, edit line 14:
```python
CSV_DIRECTORY = Path.home() / "Documents" / "csv_files"
```

You can point this to any folder where you keep your CSV files.

### 3. Run the Server
```bash
python main.py
```

## Connecting to Claude

Open your Claude Desktop configuration file:

| OS | Path |
|---|---|
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Linux | `~/.config/Claude/claude_desktop_config.json` |

Add the MCP server entry:
```json
{
  "mcpServers": {
    "csv-analyzer": {
      "command": "python",
      "args": ["C:\\path\\to\\csv_mcp_server\\main.py"],
      "env": {}
    }
  }
}
```

Save and restart Claude Desktop.

## How to Use It

Once running, try these prompts inside Claude:

### List available files
*"What CSV files can you see?"*

### Preview data structure
*"Show me the structure of sales_data.csv."*

### Run filters
*"From customer_data.csv, list all customers in California with orders above $500."*

### Get stats
*"Summarize the 'revenue' column in quarterly_report.csv."*

### Do analysis
*"Find the correlation between age and satisfaction in survey_results.csv."*

## Tools and Resources

| Type | Name | Description |
|---|---|---|
| Resource | `csv://list` | Lists all available CSV files |
| Resource | `csv://{filename}` | Preview a CSV (first 10 rows) |
| Tool | `read_csv(filename, rows)` | Read full or partial CSV data |
| Tool | `get_csv_info(filename)` | Get metadata and structure |
| Tool | `query_csv(filename, query)` | Filter data using Pandas query syntax |
| Tool | `get_csv_statistics(filename, column)` | Compute descriptive statistics |

## Directory Layout

By default, your files go in:

```
Documents/
└── csv_files/
    ├── sales_data.csv
    ├── customer_info.csv
    ├── inventory.csv
    └── financial_report.csv
```

## Customization

### Change folder:
Edit `CSV_DIRECTORY` in `main.py`.

### Add formats:
Extend file-reading functions to handle Excel, TSV, etc.

### Create new tools:
Add more `@mcp.tool()` functions for custom queries or analysis.

## Troubleshooting

### "Directory does not exist"
→ Make sure the path exists or create it:
```bash
mkdir -p ~/Documents/csv_files
```

### "File not found"
→ Check filename and ensure it's in the correct directory.

### Claude doesn't detect the server
→ Restart Claude Desktop, confirm config path and Python installation.

### Permission issues
→ Verify Claude can access your folder (or run as admin on Windows).

### Debugging
Run directly:
```bash
python main.py
```

## Contributing

Want to improve this?

1. Fork the repo
2. Create a new branch
3. Add your changes
4. Open a pull request

Feedback and ideas are welcome!

## License

Open-source and free to use, modify, or share.

## Built With

- [FastMCP](https://github.com/jlowin/fastmcp) — for efficient MCP server performance
- [pandas](https://pandas.pydata.org/) — for data analysis
- [Anthropic MCP](https://modelcontextprotocol.io/) — for integrating Claude with local data

---

## Ready to Make Claude Your Personal Data Analyst?

Set it up once — and from then on, you can chat with your CSVs just like you talk to Claude.

**No uploads, no manual parsing, no limits.**

Run it locally. Keep your data private. Get instant insights.