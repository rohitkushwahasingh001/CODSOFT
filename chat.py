import requests
from bs4 import BeautifulSoup

# Function to search Google based on user queries
def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('h3')  # Extracting search result titles
    
    results = []
    for result in search_results:
        results.append(result.get_text())

    return results

# Simple chatbot with predefined queries and responses
def chatbot_response(user_input):
    if user_input.lower() == "hello":
        return "Hello! How can I assist you?"
    elif user_input.lower() == "bye":
        return "Goodbye! Have a great day!"
    else:
        # Search Google based on the user's input
        search_results = search_google(user_input)
        if search_results:
            return "Search Results:\n" + "\n".join(search_results)
        else:
            return "No search results found for the query."

# Main function to run the chatbot
def main():
    print("Chatbot: Hello! How can I assist you?")
    while True:
        user_input = input("User: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
