class Research:
    def file_reader():
        with open('data.csv', 'r') as file:
            return file.read()

def run():
    print(Research.file_reader())
    
if __name__ == "__main__":
    run()
