def panjang_file(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

def main():
  print("Number of lines in the file: ", panjang_file("quotes.txt"))
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

if __name__== "__main__":
  main()
