import requests

def search_pypi(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    return response.status_code, response.json() if response.status_code == 200 else None

# Check for 'web_search_client'
status_code, package_info = search_pypi("web_search_client")
if status_code == 200:
    print(f"Package found: {package_info['info']['name']}")
else:
    print("Package not found on PyPI.")
