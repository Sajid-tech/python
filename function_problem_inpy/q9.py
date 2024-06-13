#  Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    # li = []
    # for i in range(2, limit+1, 2):
    #     li.append(i)
    # return li
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(10):
    print(num)


