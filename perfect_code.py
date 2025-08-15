class exit:
    def __new__(cls):
        return super().__new__(cls)()
    def __call__(self):
        raise Exception('Successful')
exit()
