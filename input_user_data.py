import csv


file_name = "user_data.csv"


def get_valid_int(prompt):
  while True:
    try:
      value = int(input(prompt))
      if value > 0:
        return value
      else:
        print("Age must be a positive integer. Please try again.")
    except ValueError:
      print("Invalid input. Please enter an integer.")

def main():
  
  try:
    with open(file_name, 'x', newline='') as csvfile:  
      writer = csv.writer(csvfile)
      writer.writerow(["Name", "Age", "City"])
      print(f"File '{file_name}' created.")
  except FileExistsError:  
    print(f"File '{file_name}' already exists. Using it for data input.")

  
  with open(file_name, 'a', newline='') as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(csvfile)  

    while True:
      
      user_choice = input("Enter new user data [y/n]? ").lower()
      if user_choice not in ("y", "n"):
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

      if user_choice == 'n':
        break

      
      name = input("Enter user name: ")
      age = get_valid_int("Enter user age: ")
      city = input("Enter user city: ")
      writer.writerow([name, age, city])

      print(f"Data for {name} written to {file_name}")

if __name__ == "__main__":
  main()