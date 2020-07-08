# Resolve the problem!!
import re

def run():
    # Start coding here
    msg = ''

    with open('./encoded.txt',mode='r',encoding='utf-8') as f:
        msg=''.join(re.findall('[a-z]',f.read()))

    print('El mensaje oculto es: ',msg)


if __name__ == '__main__':
    run()
