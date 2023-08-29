import codecs
import sys


def main(filename):
    output_file = open("output_file.txt", "w")
    with open(filename) as f:
        for line in f:
            output_file.write(codecs.decode(line, "rot_13"))
            output_file.close()
            if __name__ == "__main__":
                _filename = sys.argv[1]
                main(_filename)


           