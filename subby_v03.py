import countries_dict_v01 as countDict
import flagpy as fp


class Submarine:
    def __init__(self):
        ask_name = input("Vessel Name: ")
        ask_country = input("Country: ")
        id, country = countDict.get_country(ask_country)
        self.name = ask_name
        self.country = country
        self.id = id
        self.heading = 0
        self.depth = 50
    
def get_sub():
    return Submarine() # constructor Call

def get_flag(countryID):
    fp.display(countryID)

def get_status(sub):
    print(f"Submarine:{sub.name} Country:{sub.country} ID:{sub.id}")
    print(f"Heading: {sub.heading}")
    print(f"Depth at {sub.depth} meters")


def main():
    sub = get_sub()
    get_status(sub)
    get_flag(sub.country)
    allofthem = fp.get_country_list()
    print(allofthem)
    
    
if __name__ == "__main__":
    main()