dict_alp = []
dict_alp_capital = []
dict_numbers = []
dict_chars = []

for i in range(ord('a'), ord('z') + 1):
    dict_alp.append(chr(i))

for i in range(ord('A'), ord('Z') + 1):
    dict_alp_capital.append(chr(i))

for i in range(ord('0'), ord('9') + 1):
    dict_numbers.append(chr(i))

for i in range(ord(' '), ord('~') + 1):
    if chr(i) in dict_alp:
        continue
    elif chr(i) in dict_alp_capital:
        continue
    elif chr(i) in dict_numbers:
        continue
    dict_chars.append(chr(i))


def power_password_space(alp_power, pass_len):
    return alp_power ** pass_len


def brute_force_time(power, speed_per_sec, count_attempts, pause_time):
    count_attempts_total = power // count_attempts
    if (power / count_attempts) % 2 == 0:
        count_attempts_total -= 1
    time_await = count_attempts_total *  pause_time
    time = power / speed_per_sec + time_await
    return printing(time)


def check_password(password):
    def check_password_in(password):
        contains_number = any(char in dict_numbers for char in password)
        contains_lower = any(char in dict_alp for char in password)
        contains_upper = any(char in dict_alp_capital for char in password)
        contains_special = any(char in dict_chars for char in password)
        return contains_lower, contains_upper, contains_number, contains_special

    answer = check_password_in(password)
    alp_power = [26, 36, 52, 95, 10]

    if answer[3]:
        return alp_power[3]
    elif answer[0] and answer[1]:
        return alp_power[2]
    elif answer[2] and (answer[0] or answer[1]):
        return alp_power[1]
    elif answer[2]:
        return alp_power[4]
    else:
        return alp_power[0]


def printing(time):
    year = 60 * 60 * 24 * 365
    year_total = int(time / year)
    if year_total > 0:
        time -= year * year_total

    month = 60 * 60 * 24 * 30
    month_total = int(time / month)
    if month_total > 0:
        time -= month * month_total

    day = 60 * 60 * 24
    day_total = int(time / day)
    if day_total > 0:
        time -= day * day_total

    hour = 60 * 60
    hour_total = int(time / hour)
    if hour_total > 0:
        time -= hour * hour_total

    mins = 60
    mins_total = int(time / mins)
    if mins_total > 0:
        time -= mins * mins_total

    time = format(time, '.16f')
    sec_total = time

    print(f"years: {year_total}\n"
          f"months: {month_total}\n"
          f"days: {day_total}\n"
          f"hours: {hour_total}\n"
          f"mins: {mins_total}\n"
          f"seconds: {sec_total}")


if __name__ == "__main__":
    password = str(input("введите пароль: "))
    length = len(password)
    pass_len = len(password)
    power_password = check_password(password)
    power_password_space = power_password_space(power_password, length)

    print("Мощность алфавита: ", power_password)
    print("Кол-во комбинаций: ", power_password_space)

    s = float(input("Скорость перебора паролей в секунду: "))
    m = int(input("Кол-во неправильных попыток: "))
    v = float(input("пауза в v секунд: "))

    brute_force_time(power_password_space, s, m, v)
