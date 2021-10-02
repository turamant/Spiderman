import os

# Каждый веб-узел, обход которого является отдельным проектом
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project" + directory)
        os.makedirs(directory)

# Создание файлов очереди и обхода
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Создать новый файл
def write_file(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()


# Добавить данные в существующий файл
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass
# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results

# Iterate through a set, each item be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)




if __name__=='__main__':
    create_project_dir('keras')
    create_data_files('keras', 'https://keras.com/')