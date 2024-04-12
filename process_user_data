import csv

def calculate_average_age(data):
  """Calculates the average age from the provided user data."""
  total_age = 0
  for row in data:
    total_age += int(row[1])  
  return total_age / len(data) if data else 0.0  

def find_users_by_city(data, city_to_find):
  """Finds users by city from the provided user data."""
  matching_users = []
  for row in data:
    if row[2].lower() == city_to_find.lower():  
      matching_users.append(row)
  return matching_users

def sort_users_by_name(data):
  """Sorts users by name from the provided user data."""
  return sorted(data, key=lambda row: row[0])  

def print_users(data):
  """Prints user data in a formatted table."""
  if not data:
    print("No users found in the data file.")
    return
  print("{:20s} {:10s} {:20s}".format("Name", "Age", "City"))
  print("-" * 50)
  for row in data:
    print("{:20s} {:10d} {:20s}".format(row[0], int(row[1]), row[2]))

def load_user_data():
  """Loads user data from the CSV file."""
  data = []
  try:
    with open("user_data.csv", 'r', newline='') as csvfile:
      reader = csv.reader(csvfile)
      next(reader)  
      for row in reader:
        data.append(row)
  except FileNotFoundError:
    print("user_data.csv file not found.")
  return data

def get_all_cities(data):
  """Extracts all unique cities from the user data."""
  cities = set()
  for row in data:
    cities.add(row[2])
  return list(cities)  

def main():
  user_data = load_user_data()

  while True:
    print("\nMenu:")
    print("1. Print all users")
    print("2. Print average users age")
    print("3. Find users by city")
    print("4. Sort users by name")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      print_users(user_data)
    elif choice == '2':
      average_age = calculate_average_age(user_data)
      print(f"Average user age: {average_age:.2f}")
    elif choice == '3':
      all_cities = get_all_cities(user_data)
      if not all_cities:
        print("No city data found in the file.")
      else:
        print("\nAvailable cities:")
        for city in all_cities:
          print(city)
      city_to_find = input("\nEnter city to find users (or leave blank to cancel): ")
      if city_to_find:
        matching_users = find_users_by_city(user_data, city_to_find)
        print_users(matching_users)
    elif choice == '4':
      sorted_data = sort_users_by_name(user_data)
      print_users(sorted_data)
    elif choice == '5':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  main()