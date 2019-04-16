#!/usr/bin/python3

import hashlib,binascii,argparse


def md5(passwd):
    passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
    return passwd


def sha1(passwd):
    passwd = hashlib.sha1(passwd.encode('utf-8')).hexdigest()
    return passwd


def ripe160md(passwd):
    ripe = hashlib.new('ripemd160')
    ripe.update(passwd.encode('utf-8'))
    return ripe.hexdigest()


def sha256(passwd):    
    passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    return passwd


def sha512(passwd):
    passwd = hashlib.sha512(passwd.encode('utf-8')).hexdigest()
    return passwd


def NTLM(passwd):
    ntlm = binascii.hexlify(hashlib.new('md4', passwd.encode('utf-16le')).digest())
    return str(ntlm)[2:-1]





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--Type", dest="Type", help="The type of hash you would like.",
                        choices=["md5", "sha1", "ripe160md", "sha256", "sha512", "NTLM"], required=True)
    parser.add_argument("-d", "--Dict", dest="Dict", help="The word list you will be using.", required=True)
    parser.add_argument("-sp", "--Prefix", dest="Prefix", help="The salt prefix to prepend.", default='')
    parser.add_argument("-hv", "--Hash", dest="Hash", help="The hash value to crack.", required=True)
    parser.add_argument("-ss", "--Suffix", dest="Suffix", help="The salt suffix to append.", default='')
    args = parser.parse_args()

    f = open(args.Dict, 'r', encoding='utf-8')
    lines = f.read().splitlines()
    for line in lines:
        saltedString = str(args.Prefix) + line + str(args.Suffix)
        if args.Type=="md5":
            crackAttempt = md5(saltedString)
            if crackAttempt.lower() == args.Hash.lower():
                print("The password was: {}".format(line))
                exit(0)

        elif args.Type=="sha1":
            crackAttempt = sha1(saltedString)
            if crackAttempt.lower() == args.Hash.lower():
                print("The password was: {}".format(line))
                exit(0)
        elif args.Type=="ripe160md":
            crackAttempt = ripe160md(saltedString)
            if crackAttempt.lower() == args.Hash.lower():
                print("The password was: {}".format(line))
                exit(0)

        elif args.Type=="sha256":
            crackAttempt = sha256(saltedString)
            if crackAttempt.lower() == args.Hash.lower():
                print("The password was: {}".format(line))
                exit(0)
        elif args.Type=="sha512":
            crackAttempt = sha512(saltedString)
            if crackAttempt.lower() == args.Hash.lower():
                print("The password was: {}".format(line))
                exit(0)
        elif args.Type=="NTLM":
            crackAttempt = NTLM(saltedString)
            if crackAttempt.lower() == args.Hash.lower():
                print("The password was: {}".format(line))
                exit(0)


if __name__ =="__main__":
    main()
