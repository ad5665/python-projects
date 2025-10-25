# python-projects


Heck yeah, that sounds rad! 🤘 You’re already set up perfectly — your Bash/PowerShell chops will give you a huge edge since Python automations often feel like shell scripts on steroids.

Here’s how we can roll: I’ll give you a few project ideas (beginner → intermediate → advanced), all scoped so you can build, test with pytest, and iterate. Then you send me your code — I’ll review it like a code mentor would: suggest cleaner patterns, better structure, and how to write sharper pytest tests.


## 🟢 Beginner Projects — "Get rolling"
### 1. File Organizer

Goal: Sort files in a directory by extension (like photos → /images, .txt → /docs).
Why it’s good: Practice with os, shutil, and command-line args (argparse).
Tests: Use pytest’s tmp_path fixture to verify the files get moved to the right spot.

### 2. Log Parser

Goal: Parse a log file, extract errors, and summarize counts by type.
Why: Regex and file I/O — real-world debugging tools.
Tests: Mock logs, assert the summary dict matches expectations.

### 3. Simple CLI Calculator

Goal: Add, subtract, multiply, divide from CLI.
Why: Learn argument parsing and functions.
Tests: Parametrize with pytest.mark.parametrize to test multiple inputs cleanly.


## 🟡 Intermediate Projects — "Hit the singletrack"
### 4. Weather CLI App

Goal: Call a weather API (e.g. OpenWeatherMap), display current temp and forecast.
Why: Learn requests, error handling, and environment variables for API keys.
Tests: Use pytest-mock to mock API responses.

### 5. Task Tracker (CLI or TUI)

Goal: Manage tasks (add, list, done) with a JSON or SQLite backend.
Why: Teaches persistence, data models, and command design.
Tests: Validate CRUD operations using a temp DB file or fixture.

### 6. Mini Config Manager

Goal: Read/write .ini or .yaml configs for apps or scripts.
Why: Introduces configparser or pyyaml, and schema validation.
Tests: Use fixtures for config files and assert key parsing logic.


## 🔴 Advanced Projects — "Send it!"
### 7. Mini REST API (with FastAPI or Flask)

Goal: Build an API with CRUD endpoints for a resource (e.g. bikes, books, etc.).
Why: Get comfy with REST principles, models, and dependency injection.
Tests: Use pytest + httpx to test endpoints.

### 8. Parallel Command Runner

Goal: Run shell commands concurrently and collect outputs.
Why: Teaches asyncio or concurrent.futures.
Tests: Mock subprocess calls to verify concurrency logic.

### 9. DNS/Network Utility

Goal: Write a script that queries DNS records or pings multiple hosts.
Why: Great bridge between scripting and network automation.
Tests: Mock network calls and validate output parsing.

## 🧪 How we’ll roll together

You pick a project (or I can suggest based on your goals — e.g. DevOps tools, data automation, etc.).

You share your code — I’ll:

Review structure, readability, and test strategy.

Suggest refactors or better patterns (like context managers, pathlib, f-strings, etc.).

Add pytest improvements (fixtures, parametrization, mocking, coverage).

We iterate until it’s clean and pro-level. 🚀