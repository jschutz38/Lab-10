#authors' names are Julia Schutz, Julia Bub, and Christina Shadid
dict = {"blue":1, "purple":3, "red":2, "green":4}
def my_get_method(key, default, dict):
    if key in dict:
        print(dict[key])
    else:
        print(default)

my_get_method("green", 0, dict)
