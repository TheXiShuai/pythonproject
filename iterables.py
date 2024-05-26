# class my_range:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current
    
# or using GENERATOR as follows:

# def my_range(start,end):
#     current = start
#     while True:
#         yield current
#         current += 1

        
# nums = my_range( )

# for num in nums:
#     print(num)
    
    
    
# class Sentence:
    
   
    
#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration
#         index = self.index
#         self.index += 1
#         return self.words[index]
        
            

# my_sentence = Sentence('This is a test')

# for _ in my_sentence:
#     print(next(_))

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))


        
            
       
# def paperwork(n, m):
#     if n or m < 0:
#         return 0
#     else:
#         return n * m

# print(paperwork(5,-3))


        