users = ['Admin', 'Guest', 'User', 'Bot']

#изменяем элементы по индексу
users[2] = 'Moderator'        #меняем 'User' на 'Moderator'
users[-1] = 'SuperAdmin'      #меняем последний элемент

#новый пользователь
users.append('Newbie')

print(f"Обновленный список пользователей: {users}")