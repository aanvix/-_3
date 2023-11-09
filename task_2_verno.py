participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group_1,group_2, sep=","):
    participants_1 = group_1.split(sep)
    participants_2 = group_2.split(sep)
    common_participants = list(set(participants_1).intersection(participants_2))
    return common_participants
common_participants = find_common_participants(participants_first_group, participants_second_group)

print("Общие участники:", common_participants)









