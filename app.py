from controllers.scraper import TestSet


def main(): 

    print("Aperte 1 para começar a execução do programa:")
    option = input()

    while option == 1:
        TestSet.parse()

    

main()




