"""
FastMCP-based CSV File Connector for Claude
Allows Claude to access and analyze CSV files from your local filesystem
"""

from fastmcp import FastMCP
import pandas as pd
from pathlib import Path
import json
from typing import Optional

# Initialize FastMCP server
mcp = FastMCP("CSV File Analyzer")

# Configure your CSV directory
CSV_DIRECTORY = Path.home() / "Documents" / "csv_files"  # Change this to your preferred directory


@mcp.resource("csv://list")
def list_csv_files() -> str:
    """List all available CSV files in the configured directory"""
    if not CSV_DIRECTORY.exists():
        return json.dumps({"error": f"Directory {CSV_DIRECTORY} does not exist"})
    
    csv_files = list(CSV_DIRECTORY.glob("*.csv"))
    files_info = [
        {
            "name": f.name,
            "path": str(f),
            "size_kb": f.stat().st_size / 1024
        }
        for f in csv_files
    ]
    
    return json.dumps(files_info, indent=2)


@mcp.resource("csv://{filename}")
def get_csv_preview(filename: str) -> str:
    """Get a preview of a CSV file (first 10 rows)"""
    file_path = CSV_DIRECTORY / filename
    
    if not file_path.exists():
        return json.dumps({"error": f"File {filename} not found"})
    
    try:
        df = pd.read_csv(file_path)
        preview = {
            "filename": filename,
            "rows": len(df),
            "columns": list(df.columns),
            "preview": df.head(10).to_dict(orient='records'),
            "dtypes": df.dtypes.astype(str).to_dict()
        }
        return json.dumps(preview, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def read_csv(filename: str, rows: Optional[int] = None) -> str:
    """
    Read a CSV file and return its contents
    
    Args:
        filename: Name of the CSV file to read
        rows: Optional number of rows to return (returns all if not specified)
    """
    file_path = CSV_DIRECTORY / filename
    
    if not file_path.exists():
        return json.dumps({"error": f"File {filename} not found"})
    
    try:
        df = pd.read_csv(file_path)
        
        if rows:
            df = df.head(rows)
        
        result = {
            "filename": filename,
            "total_rows": len(df),
            "columns": list(df.columns),
            "data": df.to_dict(orient='records')
        }
        return json.dumps(result, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def get_csv_info(filename: str) -> str:
    """
    Get detailed information about a CSV file
    
    Args:
        filename: Name of the CSV file
    """
    file_path = CSV_DIRECTORY / filename
    
    if not file_path.exists():
        return json.dumps({"error": f"File {filename} not found"})
    
    try:
        df = pd.read_csv(file_path)
        
        info = {
            "filename": filename,
            "shape": {"rows": len(df), "columns": len(df.columns)},
            "columns": list(df.columns),
            "dtypes": df.dtypes.astype(str).to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "memory_usage_mb": df.memory_usage(deep=True).sum() / (1024 * 1024),
            "numeric_columns": list(df.select_dtypes(include=['number']).columns),
            "categorical_columns": list(df.select_dtypes(include=['object']).columns)
        }
        return json.dumps(info, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def query_csv(filename: str, query: str) -> str:
    """
    Query a CSV file using pandas query syntax
    
    Args:
        filename: Name of the CSV file
        query: Pandas query string (e.g., "age > 30 and city == 'NYC'")
    """
    file_path = CSV_DIRECTORY / filename
    
    if not file_path.exists():
        return json.dumps({"error": f"File {filename} not found"})
    
    try:
        df = pd.read_csv(file_path)
        filtered_df = df.query(query)
        
        result = {
            "filename": filename,
            "query": query,
            "matched_rows": len(filtered_df),
            "data": filtered_df.to_dict(orient='records')
        }
        return json.dumps(result, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": f"Query error: {str(e)}"})


@mcp.tool()
def get_csv_statistics(filename: str, column: Optional[str] = None) -> str:
    """
    Get statistical summary of a CSV file or specific column
    
    Args:
        filename: Name of the CSV file
        column: Optional specific column name to analyze
    """
    file_path = CSV_DIRECTORY / filename
    
    if not file_path.exists():
        return json.dumps({"error": f"File {filename} not found"})
    
    try:
        df = pd.read_csv(file_path)
        
        if column:
            if column not in df.columns:
                return json.dumps({"error": f"Column {column} not found"})
            stats = df[column].describe().to_dict()
            result = {
                "filename": filename,
                "column": column,
                "statistics": stats
            }
        else:
            stats = df.describe(include='all').to_dict()
            result = {
                "filename": filename,
                "statistics": stats
            }
        
        return json.dumps(result, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


if __name__ == "__main__":
    # Create the CSV directory if it doesn't exist
    CSV_DIRECTORY.mkdir(parents=True, exist_ok=True)
    
    # Run the MCP server
    mcp.run()