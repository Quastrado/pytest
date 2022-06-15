def file_worker(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

print(file_worker('base.txt'))