# Improved-HashCracker-WL
Supports md5, sha1, ripe160md, sha256, sha512, NTLM, known salts, command line argument parsing.


# Syntax 


### Required arguments:

-t TYPE, --Type TYPE    {md5,sha1,ripe160md,sha256,sha512,NTLM}
                        The type of hash you would like.

-d DICT, --Dict DICT  The word list you will be using.

-hv HASH, --Hash HASH
                        The hash value to crack.

### Optional arguments:
  -h, --help            show this help message and exit
  
  
  -sp PREFIX, --Prefix PREFIX
                        The salt prefix to prepend.
 
  -ss SUFFIX, --Suffix SUFFIX
                        The salt suffix to append.

# Examples


$./HashCracker.py -t md5 -d /usr/share/wordlists/fasttrack.txt -hv d2bc2f8d09990ebe87c809684fd78c66 -sp 123
The password was: password
$

$ ./HashCracker.py -t sha512 -d /usr/share/wordlists/rockyou.txt -hv 545cc9419a5f6018a79582812f135353100d9a8d442a3224f87f7bdd99e2d51db278bb04ff7bea0565bb5cc69d8640b796af4ae170e19b07baeffbdc7a5f60d9 -sp foo -ss bar
The password was: Password1
$ 

Made by James Hayes
