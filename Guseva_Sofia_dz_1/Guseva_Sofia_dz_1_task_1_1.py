# coding : utf-8

# Задача-1: Реализовать вывод информации о промежутке
# времени в зависимости от его продолжительности
# duration в секундах.

def convert_time(duration: int):                                                     # def convert_time(duration: int) -> str:
    if (duration >= 60):
        minutes = duration // 60                                                     # days = 0
        seconds = duration % 60                                                      # hours = 0
        if (minutes >= 60):
            hours = minutes // 60
            minutes = minutes % 60
            if (hours >= 24):
                days = hours // 24
                hours = hours % 24
                return print(days, "d", hours, "h", minutes, "min", seconds, "sec")
            else:
                return print(hours, "h", minutes, "min", seconds, "sec")            # pass
        else:
            return print(minutes, "min", seconds, "sec")                            # pass
    else:
        return print(duration, "sec")                                               # pass
                                                                                    # return seconds, minutes, hours, days
duration = 53
result = convert_time(duration)

duration = 153
result = convert_time(duration)

duration = 4153
result = convert_time(duration)

duration = 400153
result = convert_time(duration)
                                                                                    # print(result)
