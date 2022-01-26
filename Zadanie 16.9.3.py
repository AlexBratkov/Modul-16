class Client:
    def __init__(self, name, surname, prihod, rashod):
        self.name = name
        self.surname =surname
        self.prihod = sum(prihod)
        self.rashod = sum(rashod)
    def get_balanse(self):
        return self.prihod - self.rashod
    def __str__(self):
        return f'Клиент - {self.name} {self.surname}, ,баланс - {self.get_balanse()}'
clients = [
              {'name': 'Игорь', 'surname': 'Губарев', 'prihod': {55, 24, 98}, 'rashod': {26, 15}},
              {'name': 'Максим','surname': 'Ткач', 'prihod': {89, 20, 10}, 'rashod': {100, 10}},
              {'name': 'Александр','surname': 'Петров', 'prihod': {26, 87,}, 'rashod': {23, 14}}
          ]
for client in clients:
    obj_client = Client(client['name'], client['surname'], client['prihod'], client['rashod'])
    print(obj_client)