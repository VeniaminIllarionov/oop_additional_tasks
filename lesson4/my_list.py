class My_List(list):
    def __init__(self, *args, **kwargs):
        print("Работает магический метод")
        super().__init__(*args, **kwargs)

    def __add__(self, other):
        print("Работает магический метод")
        return super().__add__(other)

    def __len__(self):
        print("Работает магический метод")
        return super().__len__()

    def __str__(self):
        print("Работает магический метод")
        return super().__str__()


lst = My_List(['Jone', 'Snow', 'Java'])

lst1 = My_List(['Kate', 'Yuo', 'John'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

lst + lst1
print(lst)
print(len(lst))
