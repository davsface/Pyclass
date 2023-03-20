# Create a program that consists of 4 functions that do the following
# 	get_input asks the user to input a list of places they would like to visit
# 	normalize strips unnecessary spaces and capitalizes the inputs
# 	sort sorts the list
#   print prints the items in the list

def get_input():
    input_places = []

    print("input some places you would like to visit, press q to stop")
    location = input()
    while location != 'q':
        input_places.append(location)
        location = input()
    return input_places

def normalize(places):
    for i in range(len(places)):

        places[i] = places[i].strip()
        places[i] = places[i].capitalize()

    return places

def sort(places):
    places.sort()
    return places

def print_places(places):
    for i in places:
        print(i)
    return

if __name__ == "__main__":
    #places = []
    places = get_input()
    places = normalize(places)
    places = sort(places)
    print_places(places)

# def get_input():
#     places = []
#     city = input("Enter a list of places you would like to visit\n")
#     while city != "":
#         places.append(city)
#         city = input()
#
#     return places
#
# def normalize(places):
#     return [place.strip().capitalize() for place in places]
#
# def sort(places):
#     return sorted(places)
#
# def print_list(places):
#     for place in places:
#         print(place)
#
# # Main program
# places = get_input()
# normalized_places = normalize(places)
# sorted_places = sort(normalized_places)
# print_list(sorted_places)
