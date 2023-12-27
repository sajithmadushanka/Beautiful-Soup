import requests
from bs4 import BeautifulSoup
url = "https://www.aliexpress.us/item/3256802937815138.html?spm=a2g0o.cart.0.0.2cb838davp0Wr2&mp=1&gatewayAdapt=glo2usa"

response = requests.get(url)
if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
  
   
    
    title_text = soup.find_all('h1')
    if title_text:
             print(title_text)  # Extract the text content
    else:
            print("H1 element not found within the specified div.")


else:
    print(response.status_code)