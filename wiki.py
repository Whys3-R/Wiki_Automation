import wikipedia

# Basic or Suggestions search
def search_type():
    result = 0
    print("""Types of Searches:
    1. Basic Search
    2. Suggested Search""")
    search = input("Which type of search would you like to do: ")

    if (search == "1" or search.lower() == "basic search"):
        result = 1
    elif (search == "2" or search.lower() == "suggested search"):
        result = 2
    return result

def basic_search(search_in):
    return wikipedia.summary(search_in)

def detail_search(search_in):
    return wikipedia.search(search_in)

def requested_search():
    search_request = input("What would you like to search? ")
    return search_request

def more_info(search_in):
    print(wikipedia.WikipediaPage(search_in).content)
    

def main():
    specific = search_type()
    search_input = requested_search()
    if specific == 1:
        print(basic_search(search_input))
        cont = input("Would you like more information? (Y/N)")
        if cont.lower() == "y":
            more_info(search_input)
    elif specific == 2:
        query_count = 1
        queries = detail_search(search_input)
        print("Queries with \"{}\": ".format(search_input))
        for query in queries:
            print("{0}. {1}".format(query_count, query))
            query_count += 1
        print("{}. None of the following".format(query_count))
        desired_query = input("Which query do you want?")
        if str(query_count) == desired_query:
            main()

        # detail_search(search_input)
    else:
        print("Error")
def exit():
    input("""
    =============================================

    Press any key to Exit the Program..........""")

main()
exit()



# search_request = input("What would you like to search? ")
# print(wikipedia.summary(search_request))

# print(wikipedia.search(search_request))