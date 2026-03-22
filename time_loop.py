#basic stucture of what time loop should look like

import time
import threading

titles = ["Harry Potter", "Pride and Prejudice"]
pages = [250, 430]
first_name = ["J.K", "Jane"]
last_name = ["Rowling", "Austen"]
location = ["UK", "UK"]


def build_book_dict(titles, pages, first_name, last_name, locations):
    # Create the zip object
    inputs = zip(titles, pages, first_name, last_name, locations)
    d = {} 
    
    # Iterate and build the nested structure
    for t, p, f, l, loc in inputs:
        d.update({
            t: {
                'Pages': p,
                'Author': {'First': f, 'Last': l},
                'Publisher': {'Location': loc}
            }
        })
    
    # Requirement: delay the execution of your function by three seconds.
    time.sleep(3)
    return d

print("Building dictionary...")
print(build_book_dict(titles, pages, first_name, last_name, location))

timer = threading.Timer(5.0, build_book_dict(titles, pages, first_name, last_name, location))
timer.cancel()
print("Timer Cancelled.")
