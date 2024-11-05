import logging

logging.basicConfig(filename ='myfile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start the program')

def prime_or_not(n):

    logging.debug('Start the prime number checking of %s' % n)

    for i in range(2,int(n**0.5)+1):
        logging.debug('i is %s' % i)

        if n%i == 0:
            return 'Not Prime'
    return "Prime"

print(prime_or_not(49))

logging.debug('End of the program')
