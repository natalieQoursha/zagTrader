import subprocess
import requests

def run_ollama(prompt):
    try:
        result = subprocess.run(
            ['ollama', 'run', 'gemma2:latest', prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return result.stdout

    except Exception as e:
        return f"Error: {str(e)}"
   
def read_code_from_github(raw_url):
    try:
        response = requests.get(raw_url)
        response.raise_for_status()  
        return response.text  

    except requests.exceptions.RequestException as e:
        return f"Error fetching file from GitHub: {str(e)}"

if __name__ == "__main__":
    github_url= "https://raw.githubusercontent.com/natalieQoursha/zagTrader/refs/heads/main/example.js"
    code_to_review = read_code_from_github(github_url)
        
    prompt = f"""Analyze this code for vulnerabilities, performance bottlenecks, and potential errors. 
    Return the results as a structured JSON object with the following format:

    {{
        "Vulnerabilities": {{
            "line_number": {{
                "code": "Exact line of code",
                "problem": "Description of the issue",
                "solution": "Suggested alternative code"
            }}
        }},
        "Performance Bottlenecks": {{
            "line_number": {{
                "code": "Exact line of code",
                "problem": "Description of the issue",
                "solution": "Suggested alternative code"
            }}
        }},
        "Potential Errors": {{
            "line_number": {{
                "code": "Exact line of code",
                "problem": "Description of the issue",
                "solution": "Suggested alternative code"
            }}
        }}
    }}

    Code to analyze:
    {code_to_review}"""

    result = run_ollama(prompt)
        
    print("Analysis Result:\n", result)
