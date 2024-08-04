from service.CinemaSystem import CinemaTicketSystem


def main():
    cinema_ticket_system = CinemaTicketSystem()
    cinema_ticket_system.welcome_to_cts()
    while True:
        command = input().lower()
        print()
        if command == "/addUser".lower():
            name = input("Для регистрации введите имя пользователя: ")
            cinema_ticket_system.addUser(name)

        elif command == "/addMovie".lower():
            title = input("Для добавления фильма в базу данных введите его название: ")
            cinema_ticket_system.addMovie(title)

        elif command == "/showAllMovies".lower():
            cinema_ticket_system.showAllMovies()

        elif command == "/buyTicket".lower():
            print("Для покупки билета введите идентификатор пользователя и идентификатор фильма:")
            userID = input("UserID: ")
            movieID = input("MovieID: ")
            cinema_ticket_system.buyTicket(int(userID), int(movieID))

        elif command == "/cancelTicket".lower():
            print("Для отмены покупки билета, введите идентификатор билета: ")
            ticketID = input("TicketID: ")
            cinema_ticket_system.cancelTicket(int(ticketID))

        elif command == "/exit".lower():
            print("Всего хорошего! :)")
            break

        elif command == "/help".lower():
            cinema_ticket_system.all_commands()

        else:
            print("Такой команды нет, введите /help для просмотра доступных комманд")



if __name__ == "__main__":
    main()




