# 💻 Motivational Quotes Console App 🌟
This is a Python console-based application that fetches random motivational quotes from the ZenQuotes API and displays them with their authors. The app refreshes every 10 seconds to deliver continuous inspiration!

# ✨ Features
Dynamic Quotes: Fetches new motivational quotes from the ZenQuotes API.
Author Attribution: Displays the name of the quote's author.
Automatic Refresh: Prints a new quote every 10 seconds.
Error Handling: Handles exceptions gracefully with error messages.
# 🚀 How to Run
Clone this repository:
bash

# git clone https://github.com/your-username/motivational-quotes-console.git
Navigate to the project directory:
bash

cd motivational-quotes-console
Install required dependencies:
bash
Copy code
pip install requests
Run the script:
bash
Copy code
python motivational_quotes.py
🖼️ Example
Output:
markdown

"The best way to predict the future is to create it."  
- Peter Drucker  
**************************************************
(fetches new quotes every 10 seconds)
⚠️ Error Handling
If there is an issue connecting to the API, the app will display:


issue <error details>


