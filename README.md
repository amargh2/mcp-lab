# System & Network MCP Lab

A lightweight, hands-on [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server built with Python and `FastMCP`.

---

### 🧭 About This Project

This is a personal learning lab built to explore the nuts and bolts of the **Model Context Protocol (MCP)** and understand how it bridges language models to real-world systems. 

Rather than just treating AI like a conversational chatbot, this project dives into what's happening underneath: Natural Language Interfaces (NLI), the Context Plane, and how tools, resources, and prompts actually function across the wire. 

I built this in tandem with Gemini—pair-programming through the concepts, mechanics, and code step-by-step—to understand firsthand how MCP acts as an adapter and translation layer between reasoning agents and deterministic operating system/networking tools.

Very excited by the protocol, what it can do, and what it makes possible for more people.

---

## 🛠️ Included Tools

| Tool | Parameters | Description |
| :--- | :--- | :--- |
| **`resolve_dns`** | `domain: str` | Resolves a domain name (e.g. `google.com`) to its IPv4 address using native sockets. |
| **`get_hostname`** | *(none)* | Retrieves the hostname of the current operating system/machine. |
| **`calculate_subnet`** | `network: str` | Calculates a full subnet profile for an IPv4 CIDR block (e.g. `192.168.0.0/16`), including netmask, wildcard mask, usable host count, and range in $O(1)$ time with zero memory bloat. Handles `/31` (RFC 3021) and `/32` edge cases. |

---

## 🧠 How It Works Under the Hood

1. **Simple local communication (`stdio`):** The AI app runs `server.py` in the background and talks to it over standard input/output using basic JSON messages.
2. **Letting Python do what it's good at:** Language models are great with words and inference but mechanical, deterministic operations make more sense to offload to a function. Offloading subnet calculations and network queries to Python means the answers are fast, mathematically accurate, and don't waste model tokens.
3. **Clean Python type hints:** FastMCP uses standard Python type hints (`domain: str`) and docstrings to automatically tell the model what each tool expects, with no complicated schemas to write by hand.

---

## 🚀 Quickstart

### 1. Prerequisites
* Python 3.10+

### 2. Setup Virtual Environment
```bash
git clone <your-repo-url>
cd MCP
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Testing with the MCP Inspector
Run the visual debugger to inspect tool schemas and test executions:
```bash
mcp dev server.py
```

---

## 🔌 Connecting to an AI Client

Add this server to your AI application's `mcp_config.json` (Claude Desktop, Cursor, Antigravity, etc.):

```json
{
  "mcpServers": {
    "sysadmin-tools": {
      "command": "/absolute/path/to/MCP/.venv/bin/python",
      "args": [
        "/absolute/path/to/MCP/server.py"
      ]
    }
  }
}
```

Once loaded, the AI agent will automatically detect these tools and call them conversationally whenever your prompt requires networking or system inspection.
