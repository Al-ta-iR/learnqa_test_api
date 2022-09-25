import os  # в данном случае будет читать переменные окружения (ОС)


class Environment:
	DEV = 'dev'
	PROD = 'prod'

	URLS = {
		DEV: 'https://playground.learnqa.ru/api_dev',
		PROD: 'https://playground.learnqa.ru/api'
	}

	def __init__(self):  # функция считывает установленное окружение
		try:
			self.environment['ENV']  # попробуем считать установленное значение окружения и возьмём его в работу.
		except:  # Если же не выйдет, то по умолчанию ставим окружение DEV
			self.env = self.DEV

	def get_base_url(self):  # получаем url для api
		if self.env in self.URLS:
			return self.URLS[self.env]
		else:
			raise Exception(f"Unknown value of ENV variable {self.env}")

ENV_OBJECT = Environment()  #создаём объект, который мы можем импортировать снаружи
