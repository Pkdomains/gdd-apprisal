import requests
from bs4 import BeautifulSoup

# Define the URL and form data for the appraisal page
url = 'https://in.godaddy.com/domain-value-appraisal'
data = {
    'area': 'in',
    'domain': ''
}

# Define the list of domains to appraise
domains = ['example.com', 'google.com', 'facebook.com', ...] # Up to 50 domains

# Initialize the results dictionary
results = {}

# Submit the form for each domain and extract the appraisal data
for domain in domains:
    # Set the domain in the form data
    data['domain'] = domain

    # Submit the form and get the HTML response
    response = requests.post(url, data=data)

    # Parse the HTML response and extract the appraisal data
    soup = BeautifulSoup(response.text, 'html.parser')
    appraisal = soup.select_one('.appraisal-result strong').text

    # Add the appraisal data to the results dictionary
    results[domain] = appraisal

# Display the results to the user
for domain, appraisal in results.items():
    print(f'{domain}: {appraisal}')
