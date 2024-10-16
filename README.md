
# Vulnerable Component Scanner

This tool scans for known vulnerabilities in software components by querying the National Vulnerability Database (NVD). It helps identify outdated or vulnerable packages in your projects.

## Features
- Scans components listed in a file for known vulnerabilities.
- Queries the National Vulnerability Database (NVD) for vulnerabilities.
- Generates a detailed report in JSON format.

## Requirements
- `requests`
- `argparse`
- `logging`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vulnerable_component_scanner.git
   cd vulnerable_component_scanner
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare a file with a list of components (e.g., `components.txt`):
   ```
   component1
   component2
   ```

4. Run the scanner:
   ```bash
   python vulnerable_component_scanner.py components.txt
   ```

## Output
- The tool generates a report `vulnerability_report.json` that contains any vulnerabilities found for the specified components.

## License
This project is licensed under the MIT License.
