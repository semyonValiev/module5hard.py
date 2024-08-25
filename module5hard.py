import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Имя: {self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __hash__(self):
        return hash(self.password)


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Видео: {self.title}'


class UrTube:

    def __init__(self, current_user=None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
            else:
                print('Такой пользователь не зарегистрирован')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        user = User(nickname, password, age)
        self.current_user = user
        self.users.append(user)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, control_word):
        result = []
        for i in self.videos:
            if control_word.lower() in i.title.lower():
                result.append(i.title)
        return result

    def watch_video(self, film_name):
        if self.current_user not in self.users:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return self
        for video in self.videos:
            if video.title == film_name:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return self
                for i in range(int(video.duration)):
                    print(f'{i + 1}', end=' ')
                    time.sleep(1)
                i += 1
                print('Конец видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    ur.add(v1, v2)

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    ur.watch_video('Лучший язык программирования 2024 года!')
