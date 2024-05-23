# name: str = input("Enter your name: ")
# print(f'WITAJ {name}')
data_off_users: list = [
    {"name": "Julia", "surname": "Szklarzewska", "posts": 5, "location": "Hajnówka"},
    {"name": "Norbert", "surname": "Szeliga", "posts": 15, "location": "Rzeszów"},
    {"name": "Kacper", "surname": "Wójcik", "posts": 8, "location": "Legnica"},
    {"name": "Sebastian", "surname": "Wątroba", "posts": 12, "location": "Siedlce"},
]
print(f'Witaj {data_off_users[0]["name"]}')
def read(users:list)->None:
    """
    This is a function to show users from a list
    :param users: a list of users
    :return: None
    """

    for user in data_off_users[1:]:
        print(f'twój znajomy {user["name"]}, opublikował: {user["posts"]}')

read(data_off_users)