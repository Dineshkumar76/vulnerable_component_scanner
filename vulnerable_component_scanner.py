
import requests
import json
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VulnerableComponentScanner:
    def __init__(self, package_file):
        self.package_file = package_file
        self.api_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    
    def load_packages(self):
        logging.info("Loading packages from the file...")
        with open(self.package_file, 'r') as file:
            self.packages = [line.strip() for line in file.readlines()]
        logging.info(f"Found {len(self.packages)} packages.")
    
    def scan_for_vulnerabilities(self):
        logging.info("Scanning for vulnerabilities...")
        results = []
        for package in self.packages:
            logging.info(f"Checking {package} for known vulnerabilities...")
            params = {"keyword": package}
            try:
                response = requests.get(self.api_url, params=params)
                response_data = response.json()
                if "result" in response_data and response_data['result']['CVE_Items']:
                    logging.info(f"Vulnerabilities found for {package}")
                    results.append((package, response_data['result']['CVE_Items']))
                else:
                    logging.info(f"No vulnerabilities found for {package}")
            except Exception as e:
                logging.error(f"Error scanning {package}: {e}")
        
        return results

    def generate_report(self, vulnerabilities):
        if vulnerabilities:
            logging.info("Generating report...")
            with open("vulnerability_report.json", "w") as report_file:
                json.dump(vulnerabilities, report_file, indent=4)
            logging.info("Report saved as vulnerability_report.json")
        else:
            logging.info("No vulnerabilities found. No report generated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vulnerable Component Scanner Tool")
    parser.add_argument("package_file", help="File containing a list of components or packages")
    
    args = parser.parse_args()
    
    scanner = VulnerableComponentScanner(args.package_file)
    scanner.load_packages()
    vulnerabilities = scanner.scan_for_vulnerabilities()
    scanner.generate_report(vulnerabilities)
