#// Name: Marcus Bracken
#// Course: CIS261-Object-Oriented Computer Programming I
#// Lab: Country


def display_menu():
    print("\n----- Country Management System -----")
    print("1. View all countries")
    print("2. Add a new country")
    print("3. Delete a country")
    print("4. Exit")
    print("-------------------------------------")


def initialize_countries():
    return {"US": "United States", "CA": "Canada", "JP": "Japan"}


def view_countries(countries):
    print("\nAvailable countries:")
    for key in countries:
        print(f"Code: {key}")
    
    country_code = input("\nEnter the country code to view the country: ").upper()
    if country_code in countries:
        print(f"The country for code {country_code} is {countries[country_code]}")
    else:
        print("Invalid country code entered.")


def add_country(countries):
    country_code = input("\nEnter a new country code: ").upper()
    if country_code in countries:
        print("This country code already exists.")
    else:
        country_name = input("Enter the name of the country: ")
        countries[country_code] = country_name
        print(f"{country_name} has been added with the code {country_code}.")


def delete_country(countries):
    country_code = input("\nEnter the country code to delete: ").upper()
    if country_code in countries:
        deleted_country = countries.pop(country_code)
        print(f"{deleted_country} has been deleted.")
    else:
        print("Invalid country code entered.")


def main():
    countries = initialize_countries()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_countries(countries)
        elif choice == "2":
            add_country(countries)
        elif choice == "3":
            delete_country(countries)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please choose a valid option.")

if __name__ == "__main__":
    main()
