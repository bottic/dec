from datetime import datetime
import re
def _logger(old_foo):
    def new_foo(*args, **kwargs):
        result = old_foo(*args, **kwargs)
        with open('logs.txt', 'a') as file_logs:
            file_logs.write(f'{datetime.now()}--{old_foo.__name__}\nargs: {args}--kwargs: {kwargs}\n result: {result}\n')
        return result
    return new_foo

def logger(file_path):

    def _logger(old_foo):
        def new_foo(*args, **kwargs):
            result = old_foo(*args, **kwargs)
            with open(f'{file_path}/logs.txt', 'a') as file_logs:
                file_logs.write(
                    f'{datetime.now()}--{old_foo.__name__}\nargs: {args}--kwargs: {kwargs}\n result: {result}\n')
            return result

        return new_foo

    return _logger

