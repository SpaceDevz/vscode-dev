import fileinput

class ConfigReader():
    def __read__(file, lines = float('inf')):
        if lines = float('inf'):
            for line in fileinput.input(file, inplace=1):
                print(line)
