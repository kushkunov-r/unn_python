Dict_interface = {"FastEthernet0/1":"switchport mode access",
                  "FastEthernet0/2":"switchport mode access",
                  "FastEthernet0/11":"switchport mode access",
                  "GigabitEthernet0/3":"switchport mode trunk",
                  "GigabitEthernet0/4":"switchport mode trunk",
                  "GigabitEthernet0/9":"switchport mode trunk",}

List_trunk=["GigabitEthernet0/3", "GigabitEthernet0/5", "FastEthernet0/2"]
List_access=["FastEthernet0/1", "FastEthernet0/3", "GigabitEthernet0/4", "GigabitEthernet0/7"]

for i in Dict_interface:
    if i in List_trunk:
        if "trunk" in Dict_interface[i]:
            print("Интерфейс", i, "настроен корректно")
        else:
            print("Интерфейс", i, "настроен не корректно")
    elif i in List_access:
        if "access" in Dict_interface[i]:
            print("Интерфейс", i, "настроен корректно")
        else:
            print("Интерфейс", i, "настроен не корректно")
    else:
        print("Для интерфейса", i, "проверка не выполнена")
