print("sinh vien : le hoai nam ")
print(" ma so sv : 235752021610066")


def file_read_from_head(fname, nlines):
      from itertools import islice
      with open(fname) as f:
             for line in islice(f, nlines):
                      print(line)
file_read_from_head('test.txt', 2)
