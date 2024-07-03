
import json

operations = {}
with open( "operations.json", "r", encoding="utf-8" ) as json_plist:
    operations = json.load(json_plist)

#Условие для вывода операции
target_state = 'EXECUTED'
#Количество операций для вывода
max_len_result_list = 5

def out_result(in_dict: dict) -> str:
    '''
    Функция преобразования словаря в строку согласно условию в задании
    '''
    date_ = ".".join(reversed(in_dict.get("date")[:10].split("-")))
    description_ = in_dict.get("description")
    in_dict_ = in_dict.get("from","")
    if len(in_dict_):
        from_ = in_dict.get("from","").split(" ")
        from_number = ' ' + from_[-1][0:4] + ' ' + from_[-1][5:7] + "** **** " + from_[-1][:4] + " "
        
        if len(from_) > 2:
            from_type = " ".join(from_[0:2])
        else:
            from_type = from_[0]
    else:
        from_type, from_number = "", ""
    to_ = f'Счет **{in_dict.get("to")[-4:]}'
    return f'{date_} {description_}\
            \n{from_type}{from_number}-> {to_}\
            \n{in_dict.get("operationAmount", {}).get("amount", {})} {in_dict.get("operationAmount", {}).get("currency", {}).get("name", {})}' 

#Список для вывода резултата работы скрипта
result = []

#Обрабатываем каждую запись в обратном порядке, 
#так как по условию нас интересуют тольпо последние записи
for each in reversed(operations):
    if each.get('state') == target_state:
        if each.get('date'):
            result.append(each)
            if len(result) == max_len_result_list:
                break

#Сортиурем по дате
result = sorted(result, key=lambda d: d['date'], reverse=True)

for each in result:
    print(out_result(each),'\n')        