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


def observed_items():
    observations = []

    for _ in range(7):
        item = input("Please enter an observation:\n")
        observations.append(item)

        return observations
    return None


def run_task2():

    print("Counting observations...")
    data = observed_items()
    results = set()
    for item in data:
        cont = data.count(item)
        results.add((item, cont))

    for item, cont in results:
        print(f"{item} observed: {cont} times")


run_task2()
