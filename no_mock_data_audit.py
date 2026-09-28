import os
import re

def audit_directory(directory):
    prohibited_keywords = ['fake', 'faker', 'random.choice', 'np.random', 'mock', 'synthetic']
    allowed_files = ['no_mock_data_audit.py', 'test', 'tests']
    
    issues_found = 0
    
    for root, dirs, files in os.walk(directory):
        # Skip virtual env and allowed test folders
        if 'venv' in root or 'migrations' in root or any(x in root for x in allowed_files):
            continue
            
        for file in files:
            if file.endswith('.py') and file not in allowed_files:
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    for keyword in prohibited_keywords:
                        # Allow np.random in specific AI training files for initialization, but flag others
                        if keyword == 'np.random' and 'train.py' in file:
                            continue
                            
                        if re.search(r'\b' + re.escape(keyword) + r'\b', content, re.IGNORECASE):
                            # Ensure it's not just a comment
                            lines = content.split('\n')
                            for i, line in enumerate(lines):
                                if keyword.lower() in line.lower() and not line.strip().startswith('#'):
                                    print(f"WARNING: Prohibited mock/random data keyword '{keyword}' found in {filepath} at line {i+1}")
                                    print(f"  -> {line.strip()}")
                                    issues_found += 1
                                    
    if issues_found == 0:
        print("AUDIT PASSED: No prohibited mock data generation keywords found in source files.")
    else:
        print(f"AUDIT FAILED: Found {issues_found} potential instances of mock data generation.")
        
if __name__ == "__main__":
    audit_directory('.')
