def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()



test_function() #рабочая
inner_function()

# Вызов функции inner_function приводит к такой ошибке:

# Traceback (most recent call last):
#   File "C:\Users\Виталий\PycharmProjects\string\Module_4\module_4_2.py", line 9, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

