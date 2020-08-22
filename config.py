import configparser

def write(config):

    filename=input("input filename:\n")
    while True:
        section=input("select section, press enter to exit\n")
        if  not section:
            break;
        else:
            if section not in config.keys():
                config[section]={}
            key=input("input key:\n")
            val=input("input value:\n")
            config[section].update({key:val})

    f=open("config/{}".format(filename),"w+")
    config.write(f)
    f.close()


orderbook={
    'exit':0,
    'write':write,
    'w':write
}



def main():
    config=configparser.ConfigParser()
    while True:
        order=input("input your order:\n")

        if order not in orderbook.keys():
            print("error order!")
            continue


        elif orderbook[order]==0:
            break

        else:
            orderbook[order](config)



if __name__=="__main__":
    main()