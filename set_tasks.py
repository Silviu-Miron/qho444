# def observed():
#     observations = {"Car", "Sky", "Sky Scraper", "Bike", "House", "House"}
#     return observations
#
#
# def run_task1():
#     print(observed())
#
#
# run_task1()


# Task 2


# def observed_items():
#     observations = []
#
#     for _ in range(7):
#         item = input("Please enter an observation:\n")
#         observations.append(item)
#
#     return observations
#
#
# def run_task2():
#
#     print("Counting observations...")
#     data = observed_items()
#     results = set()
#     for item in data:
#         cont = data.count(item)
#         results.add((item, cont))
#
#     for item, cont in results:
#         print(f"{item} observed: {cont} times")
#
#
# run_task2()


# Activity 3


def observed_items():
    observations = []

    for _ in range(5):
        item = input("Please enter an observation:\n")
        observations.append(item)

    return observations


def remove_observations(obs_list):
    while True:
        choice = (
            input("\nDo you wish to remove an observation (yes/no) ").strip().lower()
        )
        if choice != "yes":
            break

        to_remove = input("\n What observation do you wish to remove?\n")
        if to_remove in obs_list:
            obs_list.remove(to_remove)
            print("Done")

        else:
            print("That observation does not exist")


def run_task3():
    data = observed_items()
    remove_observations(data)

    print("\n Observations:")
    sorted_items = sorted(set(data))
    for item in sorted_items:
        count = data.count(item)
        print(f"{item} observed: {count} times")


run_task3()
