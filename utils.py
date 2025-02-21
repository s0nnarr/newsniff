
def extract_urls(filename):
    with open(filename, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')] # Read lines, remove spaces
    
    return urls

