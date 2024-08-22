import time


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and password == i.password:
                self.current_user = i

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == i.nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_outs()
            self.log_in(user.nickname, user.password)

    def log_outs(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)

    def get_videos(self, word):
        play_list = []
        for i in self.videos:
            if word.upper() in i.title.upper():
                play_list.append(i.title)
        return play_list

    def watch_video(self, video):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print('Вам нет 18 лет! Пожалуйста, покиньте страницу!')
        else:
            for i in self.videos:
                if video in i.title:
                    for j in range(1, i.duration + 1):
                        print(j, end=' ')
                        time.sleep(1)
                    print('Конец видео')

    def __str__(self):
        return self.videos


class Video:
    def __init__(self, title, duration, time_now=0, adult_mod=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mod = adult_mod

    def __str__(self):
        return self.title


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return hash(self.password)

    def __eq__(self, other):
        return self.nickname == other.nickname


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mod=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')