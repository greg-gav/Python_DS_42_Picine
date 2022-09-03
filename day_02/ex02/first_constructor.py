import sys


class Research:
    def __init__(self, path):
        self._path = path

    def file_reader(self):
        expected_data = ('0', '1')
        try:
            with open(f'{self._path}', 'r') as file:
                lines = file.readlines()
                h1, h2 = lines[0].split(',')
                for line in lines[1:]:
                    v1, v2 = line.split(',')
                    if v1.strip() not in expected_data or v2.strip() not in expected_data:
                        raise ValueError(f"Unexpected data")
                    if v1.strip() == v2.strip():
                        raise ValueError(f"Unexpected data")
                file.seek(0)
                return file.read()
        except Exception as e:
            print(f"Error caught: {e}")
            sys.exit(1)
    
def run():
    if len(sys.argv) != 2:
        sys.exit(1)
    research = Research(sys.argv[1])
    data = research.file_reader()
    print(data)
    
if __name__ == "__main__":
    run()
