def main():
    outfile = open('data.txt', 'w')

    name = input("Please enter first name: ")
    age = input("Please enter your age: ")


    outfile.write('your name is: ' + name + '\n')
    outfile.write('your age is: ' + age + '\n')

    outfile.close()


main()
