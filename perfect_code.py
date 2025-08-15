class exit:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        raise Exception('Successful')


exit = exit()
