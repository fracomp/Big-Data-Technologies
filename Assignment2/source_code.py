#import necessary library
import time
from rtree import index

#function's definition
def sequential(points,queries,filename):
    '''This function reads the 2D data points and the queries ranges
       and write a file with the number of points
       retrieved by each query'''
    outputFile=open(filename,'w')
    for q in queries:
         count=0
         for p in points:
             if  (int(q[0]) <= int(p[1]) <= int(q[1])) and (int(q[2]) <= int(p[2]) <= int(q[3])):
                 count+=1
         print(count,file=outputFile)
    outputFile.close()

def read_file(filename,val=0):
    '''This function reads the 2D dataset from a file and return a more manageable list'''
    inputfile=open(filename,'r')
    inList=[]
    for line in inputfile:
        inList.append(line.split())
    inputfile.close()
    if (val==0):
        del inList[0]  #we do not want the number of records in our list
    return inList

def insert_record(index,points):
    '''This function inserts record into the index'''
    for line in points:
        ind=int(line[0])
        x=int(line[1])
        y=int(line[2])
        idx.insert(ind, (x, y, x, y))

def number_points(queries,filename):
    '''This function reads the list of queries and write the number of points
       retrieved by each query into a file'''
    outputFile=open(filename,'w')
    for line in queries:
        x_1=int(line[0])
        x_2=int(line[1])
        y_1=int(line[2])
        y_2=int(line[3])
        print(len(list(idx.intersection((x_1, y_1, x_2, y_2)))),file=outputFile)
    outputFile.close()

#main program
'''Let us first read the data points and the range query'''
points=read_file("data.txt")
queries=read_file("query.txt",1)

'''Sequential method and timing'''
ts = time.process_time()
sequential(points,queries,"Output_file_Sequential.txt")
elapsed_times = time.process_time() - ts
print("The total time for sequential query is ",elapsed_times,"seconds")
print("The average time for sequential query is ",elapsed_times/100,"seconds")

'''R-tree method and timing'''
idx = index.Index()
insert_record(idx,points)
t = time.process_time()
number_points(queries,"Output_file_Rtree.txt")
elapsed_time = time.process_time() - t
print("The total time for R-tree query is ",elapsed_time,"seconds")
print("The average time for R-tree query is ",elapsed_time/100,"seconds")

'''Comparison between R-tree answering query' time and sequential answering query' time'''
rate=round(elapsed_times/elapsed_time,3)
print('R-tree is',rate,'times faster than sequential query')
