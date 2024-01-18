# web-scraping-test

This script automates a sequence of actions on a specific webpage using Selenium, a tool for
automating web browsers. This script essentially automates a specific web browsing task,
which is to find all pages related to 'Campylobacter' on the "https://www.bfr.bund.de
/de/start.html" website, and collects the body text from those pages.Here's a step-by-step
summary:
1. A new browser window is opened using the Chrome WebDriver.
2. The script navigates to "https://www.bfr.bund.de/de/start.html".
3. It then waits for 0.5 seconds to ensure the page is fully loaded.
4. It finds a search field on the page by its ID, "autocomplete-search", and enters the term
'Campylobacter'. After simulating an Enter key press to submit the search, it waits
another 0.5 seconds.
5. The script then finds a dropdown menu with the ID "search_rows" and selects "50 Treffer
pro Seite" (which translates to "50 hits per page" in English) from it, waiting another 0.5
seconds afterwards.
6. It proceeds to find all the links on the page that contain the word 'Campylobacter'.
7. For each link found, the script:
• Refinds the links on the page to avoid stale references.
• Scrolls the page such that the link in question is in view.
• Attempts to click the link, ignoring any StaleElementReferenceException errors that
may arise.
• If the click is successful, it retrieves the entire text from the body of the new page
and appends it to a list called text_list.
• The script then navigates back to the previous page.
8. After iterating through all the links, it quits the browser. Finally, the script prints out the
list text_list, which holds the text content from the body of each page it successfully
visited.
