class CinemaTicketSystem:
    def __init__(self):
        self.users = []
        self.user_id = 1

        self.movies = []
        self.movie_id = 1

        self.tickets = []
        self.tickets_ids = []
        self.ticket_id = 0

    def welcome_to_cts(self):
        print("""
Здравствуйте, сэр! У вас есть следующие доступные функции:

1. Для регистрации пользователя введите '/addUser';
2. Для добавления фильма введите '/addMovie';
3. Для вывода списка всех доступных фильмов введите '/showAllMovies';
4. Для покупки билета на фильм введите '/buyTicket';
5. Для отмены покупки билета введите '/cancelTicket';
6. Для выхода из программы введите '/exit';
""")

    def all_commands(self):
        print("""
Список всех доступных комманд:
1. Для регистрации пользователя введите '/addUser';
2. Для добавления фильма введите '/addMovie';
3. Для вывода списка всех доступных фильмов введите '/showAllMovies';
4. Для покупки билета на фильм введите '/buyTicket';
5. Для отмены покупки билета введите '/cancelTicket';
6. Для выхода из программы введите '/exit'.
        """)

    def addUser(self, name):
        user_id = self.user_id
        self.users.append({'id': user_id, 'name': name})
        self.user_id += 1
        print(f"Пользователь {name} был зарегистрирован.")
        return user_id

    def addMovie(self, movie):
        print()
        movie_id = self.movie_id
        self.movies.append({'id': movie_id, 'title': movie})
        self.movie_id += 1
        print(f"Фильм '{movie}' был добавлен.")
        return movie_id

    def showAllMovies(self):
        print()
        print("Список доступных фильмов:")
        i = 1
        for movie in self.movies:
            print(f"{i}: {movie['title']}")
            i += 1


    def buyTicket(self, user_id, movie_id):
        print()
        user_exist = False
        for user in self.users:
            if user['id'] == user_id:
                user_exist = True
                break

        movie_exist = False
        for movie in self.movies:
            if movie['id'] == movie_id:
                movie_exist = True
                break


        if user_exist and movie_exist:
            self.ticket_id += 1
            ticket_id = self.ticket_id
            self.tickets.append({'id': ticket_id, 'userId': user_id})
            self.tickets_ids.append(ticket_id)

            user_name = ""
            movie_title = ""

            for user in self.users:
                if user['id'] == user_id:
                    user_name = user['name']
            for movie in self.movies:
                if movie['id'] == movie_id:
                    movie_title = movie['title']
            print(f"{user_name} покупает билет на фильм '{movie_title}'")
            return self.ticket_id
        else:
            print("Пользователя или фильма нету в базе")



    def cancelTicket(self, ticket_id):
        if ticket_id in self.tickets_ids:
            self.tickets_ids.remove(ticket_id)
            for ids in self.tickets:
                self.tickets.remove(ids)
            print("Билет отменен")
            return True
        else:
            print("Билет с таким идентификатором не найден")
            return False


