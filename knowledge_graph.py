# KNOWLEDGE GRAPH IMPLEMENTATION

# Knowledge stored as triples

kg_data = [
    ("Charminar", "located_in", "Hyderabad"),
    ("Golconda Fort", "located_in", "Hyderabad"),
    ("Hyderabad", "famous_for", "Biryani"),
    ("Charminar", "type", "Historical"),
    ("Hussain Sagar", "type", "Nature"),
    ("Laad Bazaar", "type", "Shopping"),
    ("Paradise Restaurant", "serves", "Biryani")
]

# DISPLAY KNOWLEDGE GRAPH

print("KNOWLEDGE GRAPH TRIPLES")
print("----------------------------------")

for item in kg_data:
    print(item)

# SEARCH FUNCTION

def find_place(name):

    print("\nSearching Information for:", name)

    exists = False

    for subject, relation, obj in kg_data:

        if subject.lower() == name.lower():

            print(f"{subject} --> {relation} --> {obj}")

            exists = True

    if exists is False:
        print("No information found")

# USER INPUT

location = input("\nEnter place name to search: ")

find_place(location)
