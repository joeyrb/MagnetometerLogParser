import os

def getLogFilenamesFrom(cdir):
    log_files = []
    for f in os.listdir(cdir):
        if f[-4:] == '.csv' or f[-4:] == '.log':
            log_files.append(cdir + f)
    log_files.sort()
    return log_files

def getLogFilenames():
    cdir = os.getcwd()
    return getLogFilenamesFrom(cdir)
    


def main():
    # fn_list = getLogFilenames()
    fn_list = getLogFilenamesFrom(os.getcwd() + '/devkit_xmas/')    
    print(fn_list)

if __name__ == '__main__':
    main()