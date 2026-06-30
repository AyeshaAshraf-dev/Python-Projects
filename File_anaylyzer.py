import time
import functools
class CorruptLogError(Exception):
    pass


def time_it(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time = time.perf_counter()
        total = end_time - start_time
        print(f"Excution time for {func.__name__}: {total:.4f} seconds")
        return result
    return wrapper
    
def log_generator(filepath):
    with open(filepath,'r') as file:
        for line in file:
            yield line

@time_it
def procces_logs(file_path):
    with open("rejected.txt", "a") as rejected_file:
        for line in  log_generator(file_path):
            try:
                clean_line = line.strip()
                if "INFO" not in clean_line and "WARNING" not in clean_line and "ERROR" not in clean_line:
                    raise CorruptLogError(f"INVALID log format: {clean_line}")
                print(f"Proccessing valid line: {clean_line}")
            except CorruptLogError as e:
                rejected_file.write(f"REJECTED: {clean_line}\n")
        return "DONE"

result1=procces_logs("new.txt")
print(result1)