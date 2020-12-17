MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input(f"ENTER MOVIE NAME: ")
    title = title.lower()
    hero = input(f"ENTER LEAD HERO NAME: ")
    hero = hero.lower()
    heroine = input(f"ENTER LEAD HEROINE NAME: ")
    heroine = heroine.lower()

    movies.append({
        'title': title,
        'hero': hero,
        'heroine': heroine
    })


def list_movie(lists):
    title = lists['title']
    hero = lists['hero']
    heroine = lists['heroine']
    print(f"{title.title()} have {hero.title()} & {heroine.title()} as lead actors.")


def find_movie():
    search = input(f"WHAT YOU WANT TO SEARCH? [movie]/[hero]/[heroine]  ")
    search = search.lower()
    if search == 'movie':
        title = input("ENTER MOVIE NAME:  ")
        for films in movies:
            if title == films['title']:
                title = films['title']
                hero = films['hero']
                heroine = films['heroine']
                print(f"{title.title()} have {hero.title()} & {heroine.title()} as lead actors.")
                break
        else:
            print("\nMOVIE TITLE YOU ARE SEARCHING IS NOT FOUND! Try Again Later...")

    elif search == 'hero':
        hero = input("ENTER HERO NAME:  ")
        a = 0
        for actor in movies:
            if hero == actor['hero']:
                title = actor['title']
                hero = actor['hero']
                heroine = actor['heroine']
                print(f"\n{title.title()} have {hero.title()} & {heroine.title()} as lead actors.")
                a = a + 1
                continue
        if a == 0:
            print("\nACTOR YOU ARE SEARCHING IS NOT FOUND! Try Again Later...")

    elif search == 'heroine':
        heroine = input("ENTER HEROINE NAME:  ")
        a = 0
        for actor in movies:
            if heroine == actor['heroine']:
                title = actor['title']
                hero = actor['hero']
                heroine = actor['heroine']
                print(f"\n{title.title()} have {hero.title()} & {heroine.title()} as lead actors.")
                a = a + 1
                continue
        if a == 0:
            print("\nACTOR YOU ARE SEARCHING IS NOT FOUND! Try Again Later...")


selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie()
    elif selection == "l":
        for film in movies:
            list_movie(film)
    elif selection == "f":
        find_movie()
    else:
        print('Unknown command. Please try again.\n')
    selection = input(MENU_PROMPT)
